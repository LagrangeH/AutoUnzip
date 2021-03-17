# RUN THIS FILE BY ADMINISTRATOR
# TODO: add scan archives using VirusTotal API
import sys, os
import time

from zipfile import ZipFile
from rarfile import RarFile
from loguru import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


path = 'C:\\Users\\Lagrange\\Downloads\\'
available_extensions = ('rar', 'zip')


def archiver(archive_extension, archive_path):
    if archive_extension == 'zip':
        return ZipFile(archive_path)
    elif archive_extension == 'rar':
        return RarFile(archive_path)
    else:
        logger.error('Расширение добавлено в список доступных, '
                     'но не добавлено в обработчик архивов такого расширения, '
                     'или какая-либо непредвиденная ошибка')


class ZipHandler(FileSystemEventHandler):
    def on_created(self, event):
        super().on_created(event)
        archive_extension = event.src_path.rpartition('.')[-1]
        if archive_extension in available_extensions:
            archive = archiver(archive_extension, event.src_path)
            archive.extractall(path=event.src_path.rpartition('.')[0])
            archive.close()
            os.remove(event.src_path)
        # elif archive_extension == 'rar':
        #     logger.debug('Unrarring file')
        #     archive = RarFile(event.src_path)
        #     archive.extractall(path=path)
        #     archive.close()


zip_handler = ZipHandler()

observer = Observer()
observer.schedule(zip_handler, path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

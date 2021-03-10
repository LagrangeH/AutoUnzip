import sys
import time

import zipfile
from loguru import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


path = 'C:\\Users\\Lagrange\\Downloads\\'


class ZipHandler(FileSystemEventHandler):
    def on_created(self, event):
        super().on_created(event)

        file_extension = event.src_path.rpartition('.')[-1]

        if file_extension == 'zip':
            zfile = zipfile.ZipFile(file=event.src_path)
            zfile.extractall(f'{path}unzipped')
            logger.debug('unzipped')


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

asdf = input()

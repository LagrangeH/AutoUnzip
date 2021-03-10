import sys
import time

from loguru import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ZipHandler(FileSystemEventHandler):
    def on_created(self, event):
        super().on_created(event)

        file_extension = event.src_path.rpartition('.')[-1]


path = 'C:\\Users\\Lagrange\\Downloads'

zip_handler = ZipHandler()

observer = Observer()
observer.schedule(zip_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

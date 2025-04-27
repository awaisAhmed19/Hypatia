import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import importlib
import hypatia  # Assuming your bot code is in bot.py


class BotReloader(FileSystemEventHandler):
    def __init__(self):
        self.last_modified_time = time.time()

    def on_modified(self, event):
        # If the file has been modified, reload the bot
        if event.src_path.endswith(".py") and time.time() - self.last_modified_time > 1:
            print(f"File changed: {event.src_path}. Reloading hypatia...")
            importlib.reload(hypatia)  # Reloads the bot.py module
            self.last_modified_time = time.time()


if __name__ == "__main__":
    path = "."  # Current directory
    event_handler = BotReloader()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

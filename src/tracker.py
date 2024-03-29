from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .utils import file_hash
import time
import os

class FileChangeTracker:
    """
    Tracks modifications to specified files and logs changes.

    Attributes:
        files_to_track (dict): A dictionary mapping file paths to their last known hash.
        observer (Observer): A watchdog observer for monitoring file system events.
    """

    def __init__(self):
        """Initializes the FileChangeTracker with an empty set of files and a watchdog observer."""
        self.files_to_track = {}
        self.observer = Observer()

    def track(self, filenames):
        """
        Starts tracking the specified files for changes.

        Args:
            filenames (list or str): A list of file paths or a single file path as a string.
        """
        if isinstance(filenames, str):
            filenames = [filenames]

        for filename in filenames:
            self.files_to_track[filename] = file_hash(filename)
            self.observer.schedule(FileChangeHandler(self.files_to_track), path=os.path.dirname(filename), recursive=False)

        if not self.observer.is_alive():
            self.observer.start()

class FileChangeHandler(FileSystemEventHandler):
    """
    Handles file system events and logs changes for the tracked files.

    Attributes:
        files_to_track (dict): A reference to the dictionary of tracked files and their hashes.
    """

    def __init__(self, files_to_track):
        """
        Initializes the FileChangeHandler with the dictionary of files to track.

        Args:
            files_to_track (dict): A dictionary mapping file paths to their last known hash.
        """
        self.files_to_track = files_to_track

    def on_modified(self, event):
        """
        Handles the modified event for tracked files.

        Args:
            event (FileSystemEvent): The event object representing the file system event.
        """
        if event.src_path in self.files_to_track:
            new_hash = file_hash(event.src_path)
            if new_hash != self.files_to_track[event.src_path]:
                self.log_change(event.src_path)
                self.files_to_track[event.src_path] = new_hash

    def log_change(self, filepath):
        """
        Logs the change for the modified file.

        Args:
            filepath (str): The path to the file that was modified.
        """
        timestamp = time.strftime("%Y%m%d")
        log_filename = f"{os.path.basename(filepath)}_{timestamp}.log"
        with open(log_filename, 'a') as log_file:
            log_file.write(f"File {filepath} was modified at {time.ctime()}
")
        
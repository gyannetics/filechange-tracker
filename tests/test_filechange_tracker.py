import time
import logging
from filechange_tracker.tracker import FileChangeTracker

# Function to simulate file modification
def modify_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

# Main function to test filechange_tracker
def test_filechange_tracker():
    logging.basicConfig(level=logging.INFO)

    # Initialize FileChangeTracker
    tracker = FileChangeTracker()

    # File to track
    file_to_track = 'sample_file.txt'

    # Start tracking the file
    tracker.track(file_to_track)
    logging.info(f"Started tracking {file_to_track}")

    # Simulate a file modification
    logging.info("Modifying the file...")
    modify_file(file_to_track, "New line added.\n")

    # Wait for a short period to ensure the tracker picks up the change
    time.sleep(5)

    # Check the status (this will log if changes are detected)
    tracker.status()

if __name__ == "__main__":
    test_filechange_tracker()

import hashlib

def file_hash(filepath):
    """
    Computes and returns the MD5 hash of a file's contents.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The MD5 hash of the file's contents.
    """
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()
        
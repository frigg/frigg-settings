import os


class FileSystemWrapper(object):
    """
    This is a wrapper around the os library in the stdlib.
    It was created to fit the interface of docker-wrapper-py.
    """

    def list_files(self, path):
        try:
            return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        except OSError:
            return []

    def read_file(self, path):
        with open(path) as f:
            return f.read()

    def file_exist(self, path):
        return os.path.isfile(path)

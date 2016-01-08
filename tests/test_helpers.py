import os

from frigg_settings.helpers import FileSystemWrapper


def path(*args):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), *args)


def test_filesystemwrapper_list_files():
    wrapper = FileSystemWrapper()
    files = wrapper.list_files(path())

    # This check cannot check the exact files because of
    # generated coverage files.
    assert '.frigg.yml' in files
    assert '.gitignore' in files
    assert 'frigg_settings' not in files
    assert 'tests' not in files


def test_filesystemwrapper_read_file():
    wrapper = FileSystemWrapper()
    assert(
        wrapper.read_file(path('MANIFEST.in'))
        ==
        'include setup.py README.md MANIFEST.in LICENSE\n'
    )


def test_filesystemwrapper_file_exist():
    wrapper = FileSystemWrapper()
    assert wrapper.file_exist(path('setup.py'))
    assert not wrapper.file_exist(path('non-exsting'))
    assert not wrapper.file_exist(path('tests'))

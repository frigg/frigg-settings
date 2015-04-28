import os
import unittest

from frigg_settings.helpers import FileSystemWrapper


class FileSystemWrapperTests(unittest.TestCase):
    def setUp(self):
        self.wrapper = FileSystemWrapper()

    def path(self, *args):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), *args)

    def test_list_files(self):
        files = self.wrapper.list_files(self.path())

        # This check cannot check the exact files because of
        # generated coverage files.
        self.assertIn('.frigg.yml', files)
        self.assertIn('.gitignore', files)
        self.assertNotIn('frigg_settings', files)
        self.assertNotIn('tests', files)

    def test_read_file(self):
        self.assertEqual(
            self.wrapper.read_file(self.path('MANIFEST.in')),
            'include setup.py README.md MANIFEST.in LICENSE\n'
        )

    def test_file_exist(self):
        self.assertTrue(self.wrapper.file_exist(self.path('setup.py')))
        self.assertFalse(self.wrapper.file_exist(self.path('non-exsting')))
        self.assertFalse(self.wrapper.file_exist(self.path('tests')))

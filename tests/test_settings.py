import os
import unittest
from unittest import mock

from frigg_settings import build_settings, build_tasks, load_settings_file
from frigg_settings.helpers import FileSystemWrapper

SETTINGS_FILE = ('tasks:\n - tox -e py34\n - tox -e flake8\n - tox -e isort\n - coverage report -m '
                 '&& coverage xml\n\ncoverage:\n  path: coverage.xml\n  parser: python\n')
SETTINGS_DICT = {'tasks': ['tox'], 'coverage': None}


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.runner = FileSystemWrapper()

    @mock.patch('frigg_settings.helpers.FileSystemWrapper.list_files')
    def test_build_tasks(self, mock_list_dir):
        build_tasks('path', self.runner)
        mock_list_dir.assert_called_once_with('path')

    @mock.patch('frigg_settings.helpers.FileSystemWrapper.read_file', side_effect=SETTINGS_FILE)
    def test_load_settings_file(self, mock_read_file):
        load_settings_file('.frigg.yml', self.runner)
        mock_read_file.assert_called_once_with('.frigg.yml')

    @mock.patch('frigg_settings.settings.load_settings_file', return_value=SETTINGS_DICT)
    def test_build_settings(self, mock_load_settings_file):
        build_settings(os.path.dirname(os.path.dirname(__file__)), self.runner)
        mock_load_settings_file.assert_called_once()
        self.assertTrue(mock_load_settings_file.call_args_list[0]
                                               .endswith('frigg/frigg-settings/.frigg.yml'))

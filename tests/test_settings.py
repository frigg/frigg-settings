import os
import pytest

from frigg_settings import build_settings, build_tasks, load_settings_file
from frigg_settings.helpers import FileSystemWrapper


@pytest.fixture
def settings_file():
    return ('tasks:\n - tox -e py34\n - tox -e flake8\n - tox -e isort\n - coverage report -m '
            '&& coverage xml\n\ncoverage:\n  path: coverage.xml\n  parser: python\n')


@pytest.fixture
def settings_dict():
    return {'tasks': ['tox'], 'coverage': None}


@pytest.fixture
def runner():
    return FileSystemWrapper()


def test_build_tasks(mocker, runner):
    mock_list_dir = mocker.patch('frigg_settings.helpers.FileSystemWrapper.list_files')
    build_tasks('path', runner)
    mock_list_dir.assert_called_once_with('path')


def test_load_settings_file(mocker, runner, settings_file):
    mock_read_file = mocker.patch('frigg_settings.helpers.FileSystemWrapper.read_file',
                                  side_effect=settings_file)
    load_settings_file('.frigg.yml', runner)
    mock_read_file.assert_called_once_with('.frigg.yml')


def test_build_settings(mocker, runner, settings_dict):
    mocker.patch('frigg_settings.settings.detect_tox_environments',
                 return_value=['tests', 'flake8'])
    mock_load_settings_file = mocker.patch('frigg_settings.settings.load_settings_file',
                                           return_value=settings_dict)
    build_settings(os.path.dirname(os.path.dirname(__file__)), runner)

    assert mock_load_settings_file.call_args_list[0].endswith('frigg/frigg-settings/.frigg.yml')


def test_build_settings_should_load_tox_tasks(mocker, runner, settings_dict):
    mocker.patch('frigg_settings.settings.detect_tox_environments',
                 return_value=['tests', 'flake8'])
    mocker.patch('frigg_settings.settings.load_settings_file', return_value=settings_dict)
    settings = build_settings(os.path.dirname(os.path.dirname(__file__)), runner)

    assert 'tox -e tests' in settings['tasks']
    assert 'tox -e flake8' in settings['tasks']
    assert 'tox' not in settings['tasks']

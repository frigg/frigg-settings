from os.path import join

import yaml
from frigg_test_discovery import detect_test_tasks, detect_tox_environments

from .model import FriggSettings


def build_tasks(directory, runner):
    return detect_test_tasks(runner.list_files(directory))


def load_settings_file(path, runner):
    if path is None:
        return {}

    content = yaml.load(runner.read_file(path))

    return content


def get_path_of_settings_file(directory, runner):
    if runner.file_exist(join(directory, '.frigg.yml')):
        return join(directory, '.frigg.yml')
    elif runner.file_exist(join(directory, '.frigg.yaml')):
        return join(directory, '.frigg.yaml')


def build_settings(directory, runner):
    path = get_path_of_settings_file(directory, runner)
    settings = FriggSettings(load_settings_file(path, runner))

    if not settings.has_tests_tasks:
        settings.tasks['tests'] = build_tasks(directory, runner)

    if runner and directory and 'tox' in settings.tasks['tests']:
        settings.tasks['tests'].remove('tox')
        for task in detect_tox_environments(runner, directory):
            settings.tasks['tests'].append('tox -e ' + task)

    if not settings.has_tests_tasks:
        raise RuntimeError('No tasks found')

    return settings

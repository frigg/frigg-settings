from os.path import join

import yaml
from frigg_test_discovery import detect_test_tasks, detect_tox_environments


def build_tasks(directory, runner):
    return detect_test_tasks(runner.list_files(directory))


def load_settings_file(path, runner):
    return yaml.load(runner.read_file(path))


def get_path_of_settings_file(directory, runner):
    if runner.file_exist(join(directory, '.frigg.yml')):
        return join(directory, '.frigg.yml')
    elif runner.file_exist(join(directory, '.frigg.yaml')):
        return join(directory, '.frigg.yaml')


def build_settings(directory, runner):
    path = get_path_of_settings_file(directory, runner)

    settings = {
        'setup_tasks': [],
        'tasks': [],
        'webhooks': [],
        'services': []
    }

    if path is not None:
        settings.update(load_settings_file(path, runner))
    else:
        settings['tasks'] = build_tasks(directory, runner)

    if 'tox' in settings['tasks']:
        settings['tasks'].remove('tox')
        for task in detect_tox_environments(runner, directory):
            settings['tasks'].append('tox -e ' + task)

    if len(settings['tasks']) == 0:
        raise RuntimeError('No tasks found')

    return settings

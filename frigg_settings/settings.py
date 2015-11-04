from os.path import join

import yaml
from frigg_test_discovery import detect_test_tasks, detect_tox_environments


def build_tasks(directory, runner):
    return detect_test_tasks(runner.list_files(directory))


def convert_v1_to_v2(content):
    tasks = {'setup': [], 'tests': [], 'verbose': []}

    if 'setup_tasks' in content:
        tasks['setup'] = content['setup_tasks']

    if 'tasks' in content:
        tasks['tests'] = content['tasks']

    if 'verbose_tasks' in content:
        tasks['verbose'] = content['verbose_tasks']

    content.update({'tasks': tasks})
    return content


def load_settings_file(path, runner):
    content = yaml.load(runner.read_file(path))

    if isinstance(content['tasks'], list):
        content = convert_v1_to_v2(content)

    return content


def get_path_of_settings_file(directory, runner):
    if runner.file_exist(join(directory, '.frigg.yml')):
        return join(directory, '.frigg.yml')
    elif runner.file_exist(join(directory, '.frigg.yaml')):
        return join(directory, '.frigg.yaml')


def build_settings(directory, runner):
    path = get_path_of_settings_file(directory, runner)

    settings = {
        'tasks': {
            'setup': [],
            'tests': [],
            'verbose': [],
            'after_success': [],
            'after_failure': [],
        },
        'webhooks': [],
        'services': []
    }

    if path is not None:
        settings.update(load_settings_file(path, runner))
    else:
        settings['tasks']['tests'] = build_tasks(directory, runner)

    if 'tox' in settings['tasks']['tests']:
        settings['tasks']['tests'].remove('tox')
        for task in detect_tox_environments(runner, directory):
            settings['tasks']['tests'].append('tox -e ' + task)

    if len(settings['tasks']['tests']) == 0:
        raise RuntimeError('No tasks found')

    return settings

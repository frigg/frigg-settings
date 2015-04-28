import os

from frigg_settings.helpers import FileSystemWrapper
from frigg_settings import build_tasks, load_settings_file, build_settings


path = os.getcwd()
runner = FileSystemWrapper()

print('tasks: {}'.format(build_tasks(path, runner)))
print('settings-file: {}'.format(load_settings_file('{}/.frigg.yml'.format(path), runner)))
print('build-settings: {}'.format(build_settings(path, runner)))

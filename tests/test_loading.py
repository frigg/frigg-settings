import os
import pytest
import yaml

from frigg_settings.helpers import FileSystemWrapper
from frigg_settings.settings import build_settings


def load_fixture(filename):
    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        filename
    )
    with open(path) as f:
        return yaml.load(f.read())


@pytest.fixture
def v1():
    return load_fixture('v1.yaml')


@pytest.fixture
def v2():
    return load_fixture('v2.yaml')


def test_should_load_v1(mocker, v1):
    mocker.patch('frigg_settings.settings.load_settings_file', return_value=v1)
    mocker.patch('frigg_settings.settings.get_path_of_settings_file')
    settings = build_settings('.', FileSystemWrapper())

    assert settings['setup_tasks'] is not None
    assert len(settings['setup_tasks']) == 1

    assert settings['tasks'] is not None
    assert len(settings['tasks']) == 3

    assert settings['verbose_tasks'] is not None
    assert len(settings['verbose_tasks']) == 1

    assert settings['coverage']['path'] == 'c.xml'
    assert settings['coverage']['parser'] == 'cobertura'

    assert settings['preview']['tasks'] is not None
    assert len(settings['preview']['tasks']) == 4

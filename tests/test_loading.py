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
    mocker.patch('frigg_settings.settings.yaml.load', return_value=v1)
    mocker.patch('frigg_settings.settings.get_path_of_settings_file')
    settings = build_settings('.', FileSystemWrapper())

    assert settings['tasks'] is not None
    assert settings['tasks']['setup'] is not None
    assert settings['tasks']['tests'] is not None
    assert settings['tasks']['verbose'] is not None

    assert len(settings['tasks']['setup']) == 1
    assert len(settings['tasks']['tests']) == 3
    assert len(settings['tasks']['verbose']) == 1

    assert settings['coverage']['path'] == 'c.xml'
    assert settings['coverage']['parser'] == 'cobertura'

    assert settings['preview']['tasks'] is not None
    assert len(settings['preview']['tasks']) == 4


def test_should_load_v2(mocker, v2):
    mocker.patch('frigg_settings.settings.yaml.load', return_value=v2)
    mocker.patch('frigg_settings.settings.get_path_of_settings_file')
    settings = build_settings('.', FileSystemWrapper())

    assert settings['tasks'] is not None
    assert settings['tasks']['setup'] is not None
    assert settings['tasks']['tests'] is not None
    assert settings['tasks']['verbose'] is not None

    assert len(settings['tasks']['setup']) == 1
    assert len(settings['tasks']['tests']) == 3
    assert len(settings['tasks']['verbose']) == 1

    assert settings['coverage']['path'] == 'c.xml'
    assert settings['coverage']['parser'] == 'cobertura'

    assert settings['preview']['tasks'] is not None
    assert len(settings['preview']['tasks']) == 4

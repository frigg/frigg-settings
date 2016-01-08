from frigg_settings import FriggSettings


def test_settings_should_have_defaults():
    settings = FriggSettings()
    assert settings.tasks is not None
    assert settings.services is not None
    assert settings.preview is not None


def test_update_should_update_dict():
    settings = FriggSettings()
    settings.update({'tasks': {'tests': ['tox']}})
    assert settings.tasks['tests'] == ['tox']


def test_update_should_keep_defaults_of_untouched_fields():
    settings = FriggSettings()
    settings.update({'tasks': {'tests': ['tox']}})
    assert settings.tasks['tests'] == ['tox']
    assert settings.tasks['setup'] == []
    assert settings.tasks['verbose'] == []
    assert settings.tasks['after_success'] == []
    assert settings.tasks['after_failure'] == []


def test_has_test_tasks_should_return_correct_value():
    assert FriggSettings({'tasks': {'tests': ['tox']}}).has_tests_tasks
    assert not FriggSettings({'tasks': {'tests': []}}).has_tests_tasks


def test_has_after_tasks_should_return_correct_value_for_successful_builds():
    assert FriggSettings({'tasks': {'after_success': ['tox']}}).has_after_tasks(True)
    assert not FriggSettings({'tasks': {'after_success': []}}).has_after_tasks(True)


def test_has_after_tasks_should_return_correct_value_for_unsuccessful_builds():
    assert FriggSettings({'tasks': {'after_failure': ['tox']}}).has_after_tasks(False)
    assert not FriggSettings({'tasks': {'after_failure': []}}).has_after_tasks(False)


def test_model_should_create_new_objects():
    FriggSettings({'tasks': {'tests': ['tox']}})
    assert FriggSettings({'tasks': {'setup': ['tox']}}).tasks['tests'] != ['tox']

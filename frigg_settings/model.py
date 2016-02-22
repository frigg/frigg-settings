
class FriggSettings(object):

    def __init__(self, obj=None):
        self.tasks = {
            'setup': [],
            'tests': [],
            'verbose': [],
            'after_success': [],
            'after_failure': [],
        }
        self.webhooks = []
        self.services = []
        self.preview = {}
        self.coverage = None

        if obj is None:
            return

        if 'tasks' in obj and isinstance(obj['tasks'], list):
            obj = self.convert_v1_to_v2(obj)

        self.update(obj)

    def update(self, obj):
        tasks = self.tasks
        self.__dict__.update(obj)
        if 'tasks' in obj:
            tasks.update(obj['tasks'])

        self.tasks = tasks

    def validate(self):
        return True

    @staticmethod
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

    @property
    def has_tests_tasks(self):
        return len(self.tasks['tests']) > 0

    def has_after_tasks(self, status):
        if status:
            return len(self.tasks['after_success']) > 0
        return len(self.tasks['after_failure']) > 0

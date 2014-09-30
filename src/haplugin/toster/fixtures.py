fixtures = {}


class Fixtures(object):

    def __init__(self, db):
        self.db = db
        self.fixtures = fixtures

    def _create(self, cls, **kwargs):
        obj = cls.get_or_create(self.db, **kwargs)
        data = self.fixtures.get(cls.__name__, {})
        data[kwargs['name']] = obj
        self.fixtures[cls.__name__] = data
        return obj

    def _create_nameless(self, cls, **kwargs):
        obj = cls.get_or_create(self.db, **kwargs)
        data = self.fixtures.get(cls.__name__, [])
        data.append(obj)
        self.fixtures[cls.__name__] = data
        return obj

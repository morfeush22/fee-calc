import ZODB
import ZODB.FileStorage


class NakedObject(object):
    pass


db = NakedObject()


def setup_db(config):
    global db
    storage = ZODB.FileStorage.FileStorage(config['db_path'])
    engine = ZODB.DB(storage)
    setattr(db, 'engine', engine)

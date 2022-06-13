
MAJOR = 0
MINOR = 1
REVISION = 0

VERSION = '{}.{}.{}'.format(MAJOR, MINOR, REVISION)


def read_version():
    app_version = {
        'app_name': 'Interactions REST API',
        'app_version': VERSION,
        'major': MAJOR,
        'minor': MINOR,
        'revision': REVISION
    }

    return app_version


if __name__ == '__main__':
    print(VERSION)
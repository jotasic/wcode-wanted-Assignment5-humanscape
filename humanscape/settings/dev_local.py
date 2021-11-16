import pathlib

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secrect_key')

OPEN_API_AUTH_KEY = os.environ.get('OPEN_API_AUTH_KEY', 'auth_key')

OPEN_API_SERVICE_KEY = os.environ.get('OPEN_API_SERVICE_KEY', 'service_key')

LOGGING_BATCH_PATH = os.path.join(BASE_DIR, 'log/batch/batch.log')
LOGGING_COMMON_PATH = os.path.join(BASE_DIR, 'log/common/batch.log')

SERVER_EMAIL = "notification@assignment5.com"

CRONJOBS = [
        ('*/1 * * * *', 'research.crontab.start_batch', ),
]

CRONTAB_DJANGO_SETTINGS_MODULE = 'humanscape.settings.dev_local'

pathlib.Path(os.path.dirname(LOGGING_BATCH_PATH)).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.dirname(LOGGING_COMMON_PATH)).mkdir(parents=True, exist_ok=True)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'format': {
            'format': '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },

    'handlers': {
        'batchfile': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'W0',
            'filename': LOGGING_BATCH_PATH,
            'formatter': 'format',
        },

         'commonfile': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when' : 'D',
            'filename': LOGGING_COMMON_PATH,
            'formatter': 'format',
        },

    },

    'loggers': {
        'batch': {
            'handlers': ['batchfile'],
            'level': 'INFO',
        },
         'research': {
            'handlers': ['commonfile'],
            'level': 'INFO',
        },
    },

}

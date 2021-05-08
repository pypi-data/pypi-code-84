"""Initialize from the environment"""
import logging
import logging.config
import os
import os.path

_cwd = os.getcwd()
_bootenv = os.environ.copy()

class _EnvMeta(type):
    def __init__(cls, *args, **kwargs):
        type.__init__(cls, *args, **kwargs)
        cls._instance = None

    @property
    def current(cls):
        if not cls._instance:
            cls._instance = Env()

        return cls._instance

    def reset(cls, env=None):
        cls._instance = Env(env)


class Env(metaclass=_EnvMeta):
    def __init__(self, env=None):
        # root_dir and root_dir_len are going to be used when
        # instrumenting every function, so preprocess them as
        # much as possible.
        self._cwd = _cwd
        self._env = _bootenv.copy()
        if env:
            self._env.update(env)

        self._root_dir = str(os.path.join(self._cwd) + '/')
        self._root_dir_len = len(self._root_dir)

        output_dir = self.get("APPMAP_OUTPUT_DIR",
                               os.path.join('tmp', 'appmap'))
        self._output_dir = os.path.abspath(output_dir)

        self._configure_logging()


    def set(self, name, value):
        self._env[name] = value

    def get(self, name, default=None):
        return self._env.get(name, default)

    def delete(self, name):
        del self._env[name]

    @property
    def root_dir(self):
        return self._root_dir

    @property
    def root_dir_len(self):
        return self._root_dir_len

    @property
    def output_dir(self):
        return self._output_dir

    @property
    def enabled(self):
        return self.get("APPMAP", "false").lower() == "true"

    @property
    def display_params(self):
        return self.get("APPMAP_DISPLAY_PARAMS", "true").lower() == "true"

    def _configure_logging(self):
        log_level = self.get("APPMAP_LOG_LEVEL", "warning").upper()

        log_config = self.get("APPMAP_LOG_CONFIG")
        log_stream = self.get("APPMAP_LOG_STREAM", "stderr")
        log_stream = 'ext://sys.%s' % (log_stream)
        config_dict = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'style': '{',
                    'format': '[{asctime}] {levelname} {name}: {message}'
                }
            },
            'handlers': {
                'default': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'default'
                }
            },
            'loggers': {
                'appmap': {
                    'level': log_level,
                    'handlers': ['default'],
                    'propagate': False
                }
            }
        }
        if log_config is not None:
            name, level = log_config.split('=', 2)
            config_dict['loggers'].update({
                name: {
                    'level': level.upper(),
                    'handlers': ['default'],
                    'propagate': False
                }
            })
        logging.config.dictConfig(config_dict)


def initialize(env=None):
    Env.reset(env)
    logging.info('appmap enabled: %s', Env.current.enabled)

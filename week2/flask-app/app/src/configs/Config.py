import os
import yaml


class Config(object):
    """
    project config wrapper
    """

    __cfg = {}

    def get_cfg(self) -> object:
        with open(
            os.path.dirname(os.path.realpath(__file__)) + '/config.yml', 'r'
        ) as yml_file:
            type(self).__cfg = yaml.safe_load(yml_file)

        return type(self).__cfg

    cfg = property(get_cfg)

    def get_env(self, environment) -> object:
        return self.cfg[environment]


if __name__ == '__main__':
    print(Config().cfg)
    print(Config().get_env('prod'))

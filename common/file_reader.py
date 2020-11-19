# -- coding: utf-8 --
import yaml
import os
class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data

# if __name__ == '__main__':
#     BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#     CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
#     y = YamlReader(CONFIG_FILE)
#     print(y.data)

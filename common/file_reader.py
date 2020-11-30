# -- coding: utf-8 --
import yaml
import os
class YamlReader:
    def __init__(self,yamlf):
        # 判断配置文件是否存在
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            # 配置文件不存在时抛出异常
            raise FileNotFoundError('文件不存在')

        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data

# -- coding: utf-8 --
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from auto_test.common.config import LOG_PATH

class Logger(object):
    def __init__(self,logger_name='framework'):
        self.logger = logging.getLogger(logger_name)

        logging.root.setLevel(logging.NOTSET)
        # 日志名称
        self.log_file_name = 'test.log'
        self.backup_count = 5
        # 日志输出等级
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                    when="D",# when='D' 代表以天为间隔 S：秒 D：天  H：小时
                                                    interval=1,# interval=1 代表间隔多少个“when”进行一次日志分割
                                                    backupCount=self.backup_count, # backupCount：允许存储的文件个数，如果大于这个数系统会删除最早的日志文件
                                                    delay=True,
                                                    encoding="utf-8")
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

# 外部调用此实例化对象
logger = Logger().get_logger()
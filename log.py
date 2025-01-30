import logging
import data

log=None

class create_log:

    def __init__(self):

        log_format='%(levelname)s %(asctime)s : %(message)s'
        date_format='%Y%m%d %H:%M:%S %p'
        self.level=logging.INFO
        self.filename='test.log' if data.test else 'run.log'

        logging.basicConfig(filename=self.filename,level=self.level,format=log_format,datefmt=date_format)

    def record(self,text,level=logging.INFO):

        logging.log(level,eval(text))

    def close(self):

        with open(self.filename,'a+') as file:
            file.write('\n')
        logging.shutdown()


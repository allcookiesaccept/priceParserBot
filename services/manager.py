from config.logger import logger
from services.parsers import (
    ti_one_vek
)
import os
from settings import BASE_DIR

FILES_FOLDER = os.path.join(BASE_DIR, 'files')

class Manager(object):

    def __init__(self, task_name):
        logger.info("Initializing Manager")
        self.task_name = task_name


    def __call__(self):

        parser = ti_one_vek.Vek21Parser()
        df = parser(self.task_name)
        file_name = f"{self.task_name.replace(' ', '_')}.xlsx"
        file_path = os.path.join(FILES_FOLDER, file_name)
        df.to_excel(file_path, index=False)
        return file_path

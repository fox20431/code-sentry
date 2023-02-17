import yaml
import os
from typing import *
from glob import glob

class CSTask:
    """Code Sentry Task Class"""
    def __init__(self, filename=""):
        
        # set the config file to load
        # both "cstask.yaml" and "cstask.yml" are available
        config_paths = ("./cs_task.yaml", "./cs_task.yml")
        if filename == "": 
            for config_path in config_paths:
                filename = config_path if os.path.exists(config_path) else None
        
        with open(filename, 'r') as f:
            json_data: Dict = yaml.load(f.read(), Loader=yaml.FullLoader)
            # get all items of dict and set them in current class
            for key, value in json_data.items():
                for attr in ("name", "script", "scope"):
                    # # TODO
                    # self.name = 
                    # pass 
                    setattr(self, key, value)
    
    def get_file_paths_watched(self):
        scopes: List[str] = self.scopes
        # use set to make sure the element is unique
        files = set()
        for scope in scopes:
            files.update(glob(scope))
        return files
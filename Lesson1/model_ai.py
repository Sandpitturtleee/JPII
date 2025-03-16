import json
import os
class ModelAI:
    model_count = 0

    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version
        self.new_model()

    def new_model(self):
        ModelAI.model_count += 1

    def models_amount(cls):
        return cls.model_count

    @classmethod
    def import_model_json(cls,file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/" + file_name, 'r') as file:
            data = json.load(file)
            model_name=data.get('name')
            version = data.get('version')
        return cls(model_name=model_name, version=version)


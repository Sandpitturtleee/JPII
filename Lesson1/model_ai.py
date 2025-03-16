import json
class ModelAI:
    model_count = 0

    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version

    def new_model(self):
        ModelAI.model_count += 1

    def models_amount(cls):
        return cls.model_count

    def import_model_json(self,file_name):

        with open(file_name, 'r') as file:
            data = json.load(file)
        print(data)

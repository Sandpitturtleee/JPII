from Lesson1.model_ai import ModelAI

if __name__ == '__main__':
    #Zad1
    model1 = ModelAI.import_model_json(file_name="model.json")
    print(f"{model1.model_count} {model1.model_name} {model1.version}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

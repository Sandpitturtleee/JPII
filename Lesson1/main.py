from Lesson1.model_ai import ModelAI

if __name__ == '__main__':
    #Zad1
    model1 = ModelAI.import_model_json(file_name="model.json")
    print(model1.model_count)
    print(model1.model_name)
    print(model1.version)
    #end


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

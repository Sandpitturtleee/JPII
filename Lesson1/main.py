from Lesson1.matrix import Matrix1
from Lesson1.model_ai import ModelAI


if __name__ == '__main__':
    # Zad1
    model1 = ModelAI.import_model_json(file_name="model.json")
    print(f"{model1.model_count} {model1.model_name} {model1.version}")

    # Zad2
    m1 = Matrix1(a=1, b=2, c=3, d=4)
    m2 = Matrix1(a=2, b=0, c=1, d=2)
    m3 = m1 + m2
    m4 = m1 * m2
    print(m3)
    print(repr(m4))



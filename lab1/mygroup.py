import math

groupmates = [{'name': 'Михаил',
  'surname': 'Любимцев',
  'group': 'БСТ2353',
  'exams': ['ПИС', 'БД', 'ОС'],
  'marks': [5, 4, 5]},
 {'name': 'Андрей',
  'surname': 'Резник',
  'group': 'БСТ2353',
  'exams': ['ПИС', 'БД', 'ОС'],
  'marks': [4, 4, 4]},
 {'name': 'Иван',
  'surname': 'Еремеев',
  'group': 'БСТ2353',
  'exams': ['ПИС', 'БД', 'ОС'],
  'marks': [5, 5, 5]},
 {'name': 'Фазаил',
  'surname': 'Аскеров',
  'group': 'БСТ2353',
  'exams': ['ПИС', 'БД', 'ОС'],
  'marks': [3, 4, 4]},
 {'name': 'Анна',
  'surname': 'Орлова',
  'group': 'БСТ2354',
  'exams': ['ПИС', 'БД', 'ОС'],
  'marks': [4, 5, 5]},
 {'name': 'Олег',
  'surname': 'Соколов',
  'group': 'БСТ2354',
  'exams': ['ПИС', 'БД', 'ОС'],
  'marks': [3, 3, 4]}]


def average(student):
    marks = student['marks']
    return sum(marks) / len(marks) if marks else 0.0

def filter_students(students, threshold):
    return [s for s in students if s['marks'] and average(s) > threshold]

def print_students(students):
    print(f"{'Имя':<10} {'Фамилия':<12} {'Экзамены':<15} {'Оценки':<10} Средний")
    for s in students:
        exams = ', '.join(s['exams'])
        marks = ', '.join(map(str, s['marks']))
        print(f"{s['name']:<10} {s['surname']:<12} {exams:<15} {marks:<10} {average(s):.2f}")
    if not students:
        print('Нет студентов, удовлетворяющих условию.')

def read_threshold():
    while True:
        try:
            value = float(input('Введите средний балл (2–5): ').replace(',', '.'))
            if not math.isfinite(value) or not 2 <= value <= 5:
                raise ValueError
            return value
        except ValueError:
            print('Ошибка: введите число от 2 до 5.')

if __name__ == '__main__':
    print_students(filter_students(groupmates, read_threshold()))

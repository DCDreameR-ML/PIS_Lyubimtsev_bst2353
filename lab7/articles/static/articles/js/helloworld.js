const groupmates = [
  {
    "name": "Михаил",
    "surname": "Любимцев",
    "group": "БСТ2353",
    "exams": [
      "ПИС",
      "БД",
      "ОС"
    ],
    "marks": [
      5,
      4,
      5
    ]
  },
  {
    "name": "Андрей",
    "surname": "Резник",
    "group": "БСТ2353",
    "exams": [
      "ПИС",
      "БД",
      "ОС"
    ],
    "marks": [
      4,
      4,
      4
    ]
  },
  {
    "name": "Иван",
    "surname": "Еремеев",
    "group": "БСТ2353",
    "exams": [
      "ПИС",
      "БД",
      "ОС"
    ],
    "marks": [
      5,
      5,
      5
    ]
  },
  {
    "name": "Фазаил",
    "surname": "Аскеров",
    "group": "БСТ2353",
    "exams": [
      "ПИС",
      "БД",
      "ОС"
    ],
    "marks": [
      3,
      4,
      4
    ]
  },
  {
    "name": "Анна",
    "surname": "Орлова",
    "group": "БСТ2354",
    "exams": [
      "ПИС",
      "БД",
      "ОС"
    ],
    "marks": [
      4,
      5,
      5
    ]
  },
  {
    "name": "Олег",
    "surname": "Соколов",
    "group": "БСТ2354",
    "exams": [
      "ПИС",
      "БД",
      "ОС"
    ],
    "marks": [
      3,
      3,
      4
    ]
  }
];

function average(student) {
    return student.marks.length
        ? student.marks.reduce((sum, mark) => sum + mark, 0) / student.marks.length : 0;
}
function filterByGroup(students, group) {
    const key = group.trim().toLocaleUpperCase('ru');
    return students.filter(s => s.group.toLocaleUpperCase('ru') === key);
}
function filterByAverage(students, threshold) {
    return students.filter(s => s.marks.length && average(s) > threshold);
}
function printStudents(students) {
    console.table(students.map(s => ({
        Имя: s.name, Фамилия: s.surname, Группа: s.group,
        Оценки: s.marks.join(', '), Средний: average(s).toFixed(2)
    })));
    const body = document.getElementById('student-rows');
    body.replaceChildren();
    for (const s of students) {
        const row = document.createElement('tr');
        for (const value of [s.name, s.surname, s.group,
                             s.marks.join(', '), average(s).toFixed(2)]) {
            const cell = document.createElement('td');
            cell.textContent = value;
            row.append(cell);
        }
        body.append(row);
    }
    document.getElementById('student-message').textContent =
        students.length ? `Найдено: ${students.length}` : 'Студенты не найдены';
}
document.getElementById('student-filter').addEventListener('submit', event => {
    event.preventDefault();
    const group = document.getElementById('group-filter').value;
    const mark = document.getElementById('mark-filter').value;
    const threshold = Number(mark);
    if (!mark.trim() || !Number.isFinite(threshold) || threshold < 2 || threshold > 5) {
        document.getElementById('student-message').textContent = 'Введите балл от 2 до 5';
        return;
    }
    let students = group.trim() ? filterByGroup(groupmates, group) : groupmates;
    printStudents(filterByAverage(students, threshold));
});
document.getElementById('reset-filter').addEventListener('click', () => {
    document.getElementById('student-filter').reset();
    printStudents(groupmates);
});
printStudents(groupmates);

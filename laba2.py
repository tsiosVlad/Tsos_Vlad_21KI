# База даних: логін -> пароль та список оцінок
users = {
    "vlad": {"pass": "1234", "grades": [10, 11, 8, 4, 12, 3, 9]},
    "admin": {"pass": "admin", "grades": [12, 11, 10, 12, 11]},
    "student1": {"pass": "pass1", "grades": [2, 3, 5, 4, 6, 1]},
    "student2": {"pass": "pass2", "grades": [7, 8, 9, 6, 10, 5]}
}

# Введення даних
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка авторизації
if login in users and users[login]["pass"] == password:
    print("\nУспішний вхід!")

    grades = users[login]["grades"]
    print("Ваші оцінки:", grades)

    # Лічильники
    good_grades = 0  # від 5 до 12
    bad_grades = 0  # від 1 до 4

    # Підрахунок через простий цикл
    for grade in grades:
        if 5 <= grade <= 12:
            good_grades += 1
        elif 1 <= grade <= 4:
            bad_grades += 1

    # Вивід результатів
    print("\n--- Статистика ---")
    print("Задовільних оцінок (5-12):", good_grades)
    print("Незадовільних оцінок (1-4):", bad_grades)

else:
    print("\nНеправильний логін або пароль!")
import sqlite3

#Шаг1 Создание базы данных

with sqlite3.connect('visits.db') as db:
    cursor = db.cursor()
    query = ''' 
        CREATE TABLE visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        clinic_name VARCHAR(20),
        doctor_name VARCHAR(20),
        doctor_speciality VARCHAR(20),
        visits_count INTEGER
        );
        '''
    cursor.execute(query)

#Шаг2 Заполнение базы данных
with sqlite3.connect('visits.db') as db:
    cursor = db.cursor()
    query_10 = ''' 
        INSERT INTO visits (id, clinic_name, doctor_name, doctor_speciality, visits_count)
        VALUES
            (1, 'Областная', 'Иванова В.А.', 'Терапевт', 1),
            (2, 'Городская', 'Петров С.И.', 'Хирург', 2),
            (3, 'Районная', 'Сидорова О.П.', 'Кардиолог', 3),
            (4, 'Детская', 'Васильев А.В.', 'Педиатр', 4),
            (5, 'Частная', 'Кузнецова М.Н.', 'Невролог', 5),
            (6, 'Клиника №6', 'Федоров К.Е.', 'Ортопед', 6),
            (7, 'Поликлиника №7', 'Николаева Л.Д.', 'Офтальмолог', 7),
            (8, 'Медцентр', 'Сергеев Р.О.', 'Уролог', 8),
            (9, 'Диагностический центр', 'Павлова Е.С.', 'Эндокринолог', 9),
            (10, 'Центр здоровья', 'Миронов Ю.Л.', 'Психотерапевт', 10);
        '''
    cursor.execute(query_10)


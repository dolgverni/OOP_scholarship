from scholarship_data import DATA


def bachelor(full_name, group_number, mid_score):
    return mid_score, 'bachelor'

def postgraduate(full_name, group_number, mid_score):
    return mid_score, 'postgraduate'


def get_scholarship_for_student(student_information): # student_information - результаты работ двух предыдущих функций
    mid_score = student_information[0]
    degree = student_information[1]
    if degree == 'bachelor': # рассчёт стипендии для бакалавра
        for item in DATA:
            if mid_score == item['max_mark']: # оценка 5 
                return item['scholarship_bachelor']
            if item['min_mark'] < mid_score < item['max_mark']: # оценка в пределах (4 ; 5) 
                return item['scholarship_bachelor']
            if item['min_mark'] < mid_score <= item['max_mark']: # оценка в пределах (3 ; 4]
                return item['scholarship_bachelor']
    
    else: # рассчёт стипендии для аспиранта
        for item in DATA:
            if mid_score == item['max_mark']: 
                return item['scholarship_postgraduate']
            if item['min_mark'] < mid_score < item['max_mark']: 
                return item['scholarship_postgraduate']
            if item['min_mark'] < mid_score <= item['max_mark']: 
                return item['scholarship_postgraduate']
    return 'студент без стипендии:(' # программа предполагает наличие стипендии у студентов, оценки которых в диапазоне (3;5]


# # для теста раскомментить
# student_a = bachelor('Иванов Иван Иванович', 1011, 5) # средний балл студента бакалавра 
# student_b = postgraduate('Демидов Демид Демидович',2011, 3) # средний балл студента аспиранта
# print(get_scholarship_for_student(student_a)) 
# print(get_scholarship_for_student(student_b))
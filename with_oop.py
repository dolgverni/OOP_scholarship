from scholarship_data import DATA


class Bachelor:

    def __init__(self, full_name, group_number, mid_score):
        self.full_name = full_name
        self.group_number = group_number
        self.mid_score = mid_score
        self.DATA = DATA

    def get_scholarship_for_bachelor(self):
        for item in self.DATA: 
            self.min_mark = item['min_mark']
            self.max_mark = item['max_mark']
            if self.mid_score == self.max_mark: # оценка 5 
                return item['scholarship_bachelor']
            if self.min_mark < self.mid_score < self.max_mark: # оценка в пределах (4 ; 5) 
                return item['scholarship_bachelor']
            if self.min_mark < self.mid_score <= self.max_mark: # оценка в пределах (3 ; 4]
                return item['scholarship_bachelor']
        return 'студент без стипендии:('


class Postgraduate(Bachelor):

    def get_scholarship_for_postgraduate(self):
        for item in self.DATA: 
            self.min_mark = item['min_mark']
            self.max_mark = item['max_mark']
            if self.mid_score == self.max_mark: 
                return item['scholarship_postgraduate']
            if self.min_mark < self.mid_score < self.max_mark: 
                return item['scholarship_postgraduate']
            if self.min_mark < self.mid_score <= self.max_mark: 
                return item['scholarship_postgraduate']
        return 'студент без стипендии:('


# # для теста раскомментить
# a = Bachelor('Иванов Иван Иванович', 1011, 3) # средний балл студента бакалавра 
# b = Postgraduate('Демидов Демид Демидович',2011, 4.22) # средний балл студента аспиранта
# print(a.get_scholarship_for_bachelor()) 
# print(b.get_scholarship_for_postgraduate())
import collections
import copy
from enum import Enum


class Gender(Enum):
    NONE_SPECIFIED = "none-specified"
    M = "male"
    F = "female"
    pass


class Department(Enum):
    NONE_SPECIFIED = "none-specified"
    HR_M = "Human-Resource-Management"
    C_M = "Company-Management"
    P = "Production"
    pass


class Company:
    def __init__(self, workers: list = None, group_leaders: list = None):
        self.workers = workers
        self.group_leaders = group_leaders
        pass

    def amount_of_worker(self):
        return self.workers is not None if len(
            self.workers) else 0  # if self.worker is not None => False => return len(self.worker) ?

    def amount_of_group_leader(self):
        return self.group_leaders is not None if len(
            self.group_leaders) else 0  # if self.group_leader is not None => False => return len(self.group_leader) ?

    def amount_of_departments(self):
        return len(self.find_departments())

    def find_departments(self):
        return self.sub_find_departments(self.workers) + self.sub_find_departments(self.group_leaders)

    def sub_find_departments(self, people):
        departments: list = []
        if people is not None:
            for person in people:
                is_in_list = False
                if len(departments) != 0:
                    for d in departments:
                        if person.department is d:
                            is_in_list = True
                            break
                if is_in_list is False:
                    departments.append(person.department)
        return collections.Counter(departments)

    def find_amount_of_participates_per_departments(self):
        temp_worker = self.group_leaders + self.workers;
        temp_dict: dict = {}
        for d in self.find_departments():
            temp_dict[d] = 0
        for worker in temp_worker:
            temp_dict[worker.department] = temp_dict[worker.department] + 1
        return temp_dict

    def find_biggest_department(self):
        dict = copy.deepcopy(self.find_amount_of_participates_per_departments())
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        new_dict = {}
        for d in sorted_dict:
            if len(new_dict) == 0:
                new_dict[d[0]] = d[1]
            else:
                if new_dict[list(new_dict)[-1]] == d[1]:
                    new_dict[d[0]] = d[1]
                else:
                    break

        return new_dict

    def gender_spread(self):
        people = self.workers + self.group_leaders
        spreading = {}
        for g in Gender:
            spreading[g] = 0
        for p in people:
            spreading[p.gender] = spreading[p.gender] + 1
        return spreading

    pass


class Person:
    def __init__(self, lastname: str = "", firstname: str = "", age: int = 0, gender: Gender = Gender.NONE_SPECIFIED):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.gender = gender
        pass

    def to_string(self):
        return "name: " + self.lastname + " " + self.firstname + "\nage\t: " + str(
            self.age) + "\ngender\t: " + self.gender.value

    pass


class Worker(Person):
    def __init__(self, lastname: str = "", firstname: str = "", age: int = 0, gender: Gender = Gender.NONE_SPECIFIED,
                 department: Department = Department.NONE_SPECIFIED):
        super(Worker, self).__init__(lastname, firstname, age, gender)
        self.department = department
        pass

    def to_string(self):
        return super(Worker, self).to_string() + "\ndepartment: " + self.department.value

    pass


class GroupLeader(Worker):
    def __init__(self, lastname: str = "", firstname: str = "", age: int = 0, gender: Gender = Gender.NONE_SPECIFIED,
                 department: Department = Department.NONE_SPECIFIED, subordinates: list = None):

        super(GroupLeader, self).__init__(lastname, firstname, age, gender, department)
        self.subordinates = subordinates
        pass

    def to_string(self):
        content = super(GroupLeader, self).to_string() + "\nSubordinates: "
        if self.subordinates is not None:
            for s in self.subordinates:
                content = content + "\n\t" + s.lastname + " " + s.firstname
        else:
            content = content + "\n\tNo subordinates"
        return content

    pass

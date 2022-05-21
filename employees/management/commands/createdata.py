import random
import sys
from datetime import date

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from employees.models import Employee

POSITIONS = [
    "Программист",
    "Ведущий программист",
    "Главный программист",
    "Специалист",
    "Ведущий специалист",
    "Главный специалист",
    "Консультант",
    "Ведущий консультант",
    "Советник",
    "Бухгалтер 1 категории",
    "Бухгалтер 2 категории",
    "Бухгалтер 3 категории",
    "Инженер",
    "Ведущий инженер",
    "Главный инженер",
]


class EmployeesProvider(faker.providers.BaseProvider):
    def fifth_level_positions(self):
        return self.random_element(POSITIONS)


class Command(BaseCommand):
    help = "The command creates 50 000 faked objects of model Employee"

    def handle(self, *args, **kwargs):

        fake = Faker(["ru_RU"])
        fake.add_provider(EmployeesProvider)

        self.create_faked_employees('Директор', 350000, 400000, 1)
        for _ in range(5):
            self.create_faked_employees('Заместитель директора',
                                        300000, 350000, 2)
        for _ in range(20):
            self.create_faked_employees('Руководитель', 200000, 300000, 3)
        for _ in range(200):
            self.create_faked_employees('Начальник', 150000, 200000, 4)
        for _ in range(400):
            faked_position = fake.fifth_level_positions()
            self.create_faked_employees(faked_position, 50000, 150000, 5)

    @staticmethod
    def randomize_names():

        fake = Faker(["ru_RU"])

        random_sex = random.choice(["Male", "Female"])
        if random_sex == "Male":
            faked_first_name = fake.first_name_male()
            faked_last_name = fake.last_name_male()
            faked_middle_name = fake.middle_name_male()
        else:
            faked_first_name = fake.first_name_female()
            faked_last_name = fake.last_name_female()
            faked_middle_name = fake.middle_name_female()
        random_names = [faked_first_name, faked_middle_name, faked_last_name]
        return random_names

    def create_faked_employees(self, position, min_salary, max_salary,
                               hierarchy_level):

        random_names = self.randomize_names()
        faked_first_name = random_names[0]
        faked_last_name = random_names[1]
        faked_middle_name = random_names[2]
        faked_position = position
        start_date = date(1990, 1, 1).toordinal()
        end_date = date.today().toordinal()
        faked_employment_date = date.fromordinal(random.randint(start_date, end_date))
        faked_salary = random.randint(min_salary, max_salary)

        if hierarchy_level == 1:
            faked_manager = None
        elif hierarchy_level in [2, 3, 4, 5]:
            probable_managers = \
                Employee.objects.filter(hierarchy_level=hierarchy_level - 1)
            faked_manager = random.choice(probable_managers)
        else:
            sys.exit("Invalid value of hierarchy level")

        Employee.objects.create(
            first_name=faked_first_name,
            middle_name=faked_middle_name,
            last_name=faked_last_name,
            position=faked_position,
            employment_date=faked_employment_date,
            salary=faked_salary,
            hierarchy_level=hierarchy_level,
            manager=faked_manager
        )

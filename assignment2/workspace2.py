# Workspace for Part #2
import json
class Professor():
    def __init__(self, name, staff_id, department, courses_taught):
        self.__name = name
        self.__staff_id = staff_id
        self.__department = department
        self.__courses_taught = courses_taught

    # Implement to_json method below
    def to_json(self):
        professor_data = {
            'name': self.__name,
            'staff_id': self.__staff_id,
            'department': self.__department,
            'courses_taught': self.__courses_taught
        }
        return json.dumps(professor_data)


professor1 = Professor("John Doe", 12345, "Computer Science", 5)
professor3 = Professor("Jane Smith", 54321, "Mathematics", None)


# Testing the to_json method
print(professor1.to_json())
print(professor3.to_json()) 
# Workspace for part 3
import json
class Professor():
    def __init__(self, name, staff_id, department, courses_taught):
        self.__name = name
        self.__staff_id = staff_id
        self.__department = department
        self.__courses_taught = courses_taught
   
    
    # Implement serialize_to_json_file method to serialize object to a JSON file below
    def serialize_to_json_file(self, file_path): 
        with open(file_path, 'w') as file:
            professor_data = {
                'name': self.__name,
                'staff_id': self.__staff_id,
                'department': self.__department,
                'courses_taught': self.__courses_taught
            }
            json.dump(professor_data, file, indent=4)


    # Copy and paste your to_json method from Part #2 below
    def to_json(self):
        professor_data = {
            'name': self.__name,
            'staff_id': self.__staff_id,
            'department': self.__department,
            'courses_taught': self.__courses_taught
        }
        return json.dumps(professor_data, indent= 4)


    # Complete the code for deserialize method below for deserializing a Professor object from a JSON file
    @staticmethod
    def deserialize(file_path:str):
        with open(file_path, 'r') as file:
            professor_data = json.load(file)
            return Professor(
                professor_data['name'],
                professor_data['staff_id'],
                professor_data['department'],
                professor_data['courses_taught']
            )
    

professor1 = Professor("John Doe", 12345, "Computer Science", 5)

file_path = 'professor1.json'

professor1.serialize_to_json_file(file_path)
professor_1_deserialized = Professor.deserialize(file_path)

print("Original professor object JSON string:", professor1.to_json())
print("Deserialized professor object JSON string", professor_1_deserialized.to_json()) 
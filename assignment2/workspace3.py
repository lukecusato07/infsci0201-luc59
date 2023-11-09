import json
class Professor():
    def __init__(self, name, staff_id, department, courses_taught):
        self.__name = name
        self.__staff_id = staff_id
        self.__department = department
        self.__courses_taught = courses_taught


    # Implement serialize_to_json_file method to serialize object to a JSON file below
    

    # Copy and paste your to_json method from Part #2 below
    def to_json(self):
        professor_data = {
            'name': self.__name,
            'staff_id': self.__staff_id,
            'department': self.__department,
            'courses_taught': self.__courses_taught
        }
        return json.dumps(professor_data)

    # Complete the code for deserialize method below for deserializing a Professor object from a JSON file
    # This method is implemented as a static method. Which means that this is not an instance method.
    # You can call this function by using the class name as follows: Professor.deserialize("file_path")
    @staticmethod
    def deserialize(file_path:str):
        # 0- Delete pass keyword
        # 1- Read the contents of file_path as a JSON string. Check the lecture slides to see how to do it.
        # 2- Create a Professor object by calling its constructor.
        # 2.1- To call its constructor, you need to get the saved instance properties and pass them to the constructor. 
        # 2.2- To do so, you need to convert the JSON string read in step 1 to a Python data structure (check your slides)
        # 2.3- Use the outcome of step 2.2 to access the instance properties.
        # 3- Return that object
        pass


professor1 = Professor("John Doe", 12345, "Computer Science", 5)

file_path = 'professor1.json'

professor1.serialize_to_json_file(file_path)
professor_1_deserialized = Professor.deserialize(file_path)

print("Original professor object JSON string:", professor1.to_json())
print("Deserialized professor object JSON string", professor_1_deserialized.to_json())

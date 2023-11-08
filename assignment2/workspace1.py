class Professor():
    def __init__(self, name, staff_id, department, courses_taught):
        self.__name = name
        self.__staff_id = staff_id
        self.__department = department
        self.__courses_taught = courses_taught

    # Override the __eq__ method below
    def __eq__(self, other):
        if not isinstance(other, Professor):
            return NotImplemented
        return (self.__name == other.__name and
                self.__staff_id == other.__staff_id and
                 self.__department == other.__department and
                  self.__courses_taught == other.__courses_taught)

    # Override the __hash__ method below
    def __hash__(self):
        return hash((self.__name, self.__staff_id, self.__department, self.__courses_taught))


professor1 = Professor("John Doe", 12345, "Computer Science", 5)
professor2 = Professor("John Doe", 12345, "Computer Science", 5)
professor3 = Professor("Jane Smith", 54321, "Mathematics", 3)

print("professor1 and professor2 are equal: ", professor1 == professor2)
print("professor1 and professor3 are equal: ", professor1 == professor3)

# Creating a set and adding professors
professors_set = {professor1, professor2, professor3}

# Testing the set size
print("Size of the set: ", len(professors_set))
class Student():
    #properties/attributes
    def __init__ (self, name, year, roll_number ):
        self.name = name
        self.year = year
        self.roll_number = roll_number
    #fuctions/methods
    def displayDeatails(self):
        print("Hello I am {} in year {} with roll number {}".format(self.name, self.year, self.roll_number))


#objects
Student1 = Student("Adhayan", "9", "2")
Student1.displayDeatails()
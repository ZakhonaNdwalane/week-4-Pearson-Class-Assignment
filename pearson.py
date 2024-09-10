# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Method to introduce the person
        print(f"Hi, I'm {self.name}. I'm {self.age} years old and I'm {self.gender}.")

# Step 2: Create an instance of Person and call the introduce method

# Create an instance of the Person class
person1 = Person("Jade", 27, "Female")

# Call the introduce method
person1.introduce()
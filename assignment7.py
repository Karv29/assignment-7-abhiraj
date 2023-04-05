class Assignment:

    def __init__(self,name,date,topic):
      self.name =name 
      self.date = date
      self.topic =  topic
    
training = Assignment("abhiraj",3,"python")
print(training.name)
print(training.date)


training1 = Assignment("vipul",24,"java")
print(training1.name)
print(training1.topic)
print((training1.date))

class Employee:
    company = "hello"
    id = 589
    designation = "Software Trainee"

    def __init__(self, company=None):
        self.company = company

    # @staticmethod
    def hello(self):
        print(self.designation)


akash = Employee("Google")

akash.company = "Amazon"  ## instance attribute

Employee.company = "cloudeq"  ## class attribute

print(akash.company)  ## prints Amazon

akash.hello()

#The Python super() function returns objects represented in the parent’s class and is very useful in  multiple and multilevel inheritances to find which class the child class is extending first.



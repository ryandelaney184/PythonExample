# The PersonBuilder class will allow you to create an immutable Person object
# this uses a builder pattern to allow you to chain together setter methods.
class PersonBuilder:
    name = ""
    age = 0

    # The setName allows you to set the person name. The desired name
    # needs to be at least 1 character long.
    def setName(self, name):

        if name.__sizeof__() < 1:
            error = "The person name needs to be at least 1 characters long"
            raise ValueError(error)

        self.name = name
        return self

    # The setAge allows you to set the Person age. The
    # desired age need to be greater than or equal to
    # 1 years of age.
    def setAge(self, age):
        if (age < 1):
            error = "Age must be greater than 1 years old"
            raise ValueError(error)

        self.age = age
        return self

    # The getInstance is a static method that will return an instance of the
    # PersonBuilder, so you can create a custom person. The lifetime of this
    # PersonBuilder is up till the build() method is called then it should
    # be returned to memory.
    @staticmethod
    def getInstance():
        return PersonBuilder()

    # The build method will create an immutable Person object using
    # what has been set. This will throw an error if the person name,
    # and or age hasn't been set, and this has been called.
    def build(self):
        error = ""

        if self.name.__sizeof__() < 1:
            error = "Name has not been set."
            raise ValueError(error)

        if self.age == -1:
            error = "Age has not been set."
            raise ValueError(error)

        return Person(self)


# The Person class is an immutable object that presents, and contains
# a person's information.
class Person:
    __name = ""
    __age = 0

    # The default constructor takes in the PersonBuilder that has
    # built the Person. This will copy the Person data from
    # PersonBuilder to Person.
    def __init__(self, builder: PersonBuilder):
        self.__name = builder.name
        self.__age = builder.age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    John = (PersonBuilder.getInstance()
           .setName("John Doe")
           .setAge(40)
           .build())

    Jane = (PersonBuilder.getInstance()
            .setName("Jane Doe")
            .setAge(39)
            .build())

print(f"Person Name: {John.getName()}")
print(f"Person Age: {John.getAge()}")

print(f"Person Name: {Jane.getName()}")
print(f"Person Age: {Jane.getAge()}")

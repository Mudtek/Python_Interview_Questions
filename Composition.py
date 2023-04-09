"""Example of Composition in Python"""

class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_address(self):
        print("1100 main str")

class Job:
    def __init__(self, title: str, salary: float) -> None:
        self.title = title
        self.salary = salary

class Person(Address, Job):
    def __init__(self, name: str, age: int, address: Address, job: Job) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.job = job

    
    def get_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Job Title: {self.job.title}, " \
            f"Job Salary: {self.job.salary}, Address: {self.address.street}, " \
            f"{self.address.city}, {self.address.state}, {self.address.zip_code}"

address = Address("123 Main St", "Anytown", "CA", "12345")
job = Job("Engineer", 100000)
person = Person("John Smith", 30, address, job)
person.get_address

info_string = person.get_info()
print(info_string)

# Output: Name: John Smith, Age: 30, Job Title: Engineer, Job Salary: 100000, Address: 123 Main St, Anytown, CA, 12345

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
    
class Admin(User):
    def __init__(self, first_name, last_name,*commands):
        super().__init__(first_name, last_name)
        self.commands = commands
    
    def commands(self):
        print(f"{self.first_name} {self.last_name} has these privileges:")
        for every_command in self.commands:
            print(f"{every_command}")
        
new_admin = Admin("john","doe","delete","edit")
print(new_admin.commands)
print(new_admin.first_name)
print(new_admin.last_name)
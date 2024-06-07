class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
    

class Privileges:
    def __init__(self,*commands):
        self.admin_commands = commands
    
    def show_commands(self):
        print(f"Commands: {self.admin_commands}")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.commands = Privileges("delete","post","edit")

new_admin = Admin("john","doe")
new_admin.commands.show_commands()


#9-6. Ice Cream Stand
class IceCreamStand:
    def __init__(self,*flavors) -> None:
        self.flavors = flavors
    
    def menu(self):
        print(f"Here are each flavors:")
        for each_flavor in self.flavors:
            print(f"{each_flavor.title()}")

my_stand = IceCreamStand("vanilla","chocolate")
my_stand.menu()
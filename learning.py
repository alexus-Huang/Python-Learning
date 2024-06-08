from random import choice
lottery = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
chosen_lottery = []
my_ticket = ["a",1]
counter = 0
class Lottery:
    """Picks out random letters and numbers from a list and tries to match it with a set list. Counts how many tries it took."""
    def __init__(self,lottery_selection = lottery,selections = 2):
        self.lottery_selection = lottery_selection
        self.selections = selections
        self.status = True
    
    def selection(self,counter = counter):
        while self.status:
            for selections_chosen in range (self.selections): # repeat however many times depending on the amount of selections
                chosen_shit = choice(lottery)  # randoly picks out stuff from the list
                chosen_lottery.append(chosen_shit) # adds the chosen lottery stuff to the list
            print(chosen_lottery)
            if chosen_lottery == my_ticket:
                print(f"You won! Chosen lottery: {chosen_lottery} - Your Ticket: {my_ticket}")
                print(f"It took {counter} tries.")
                self.status = False
            else:
                chosen_lottery.clear()
                counter += 1
                continue

lottery_one = Lottery()
lottery_one.selection()

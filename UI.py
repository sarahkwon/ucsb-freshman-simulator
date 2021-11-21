from Activity import activities
from __main__ import *

from Protagonist_class import protagonist

class ui:
    
    def option_selection(self, args):
        if len(args) == 0:
            print('')
        
        for index, value in enumerate(args):
            print(f'{index + 1}. Press {index + 1} to do {value}')
        
        print('Press 0 to show current stats')
        print('Press E to exit')

        user_choice = input('Please select an option (Enter the number): ')
        
        
        if user_choice == 'e' or user_choice == 'E':
            return 'e'
        
        try:
            if int(user_choice) > len(args):
                print("---Please enter a valid input---")
                return None
            else:
                return int(user_choice)
        except:
            print("---Please enter a valid input---")
            return None

if __name__ == "__main__":
    print()

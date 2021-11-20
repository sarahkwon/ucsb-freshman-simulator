from ClassActivity import activities

class ui:
    
    def option_selection(self, args):
        if len(args) == 0:
            print('')
        
        for index, value in enumerate(args):
            print(f'{index + 1}. Press {index + 1} to do {value}')
        
        print('Press 0 to exit')

        try:
            user_choice = int(input('Please select an option (Enter the number): '))
        
        except:
            print("---Please enter a valid input---")
            return None
        
        if user_choice > len(args):
            print("---Please enter a valid input---")
            return None
        elif user_choice == 0:
            return 0
        else:
            return user_choice


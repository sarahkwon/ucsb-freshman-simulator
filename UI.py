class ui:
    
    def option_selection(self, *args):
        if len(args) == 0:
            print('')
        
        for index, value in enumerate(args):
            print(f'{index + 1}. Press {index + 1} to do {value}')
        
        user_choice = int(input('Please select an option: '))
        
        return args[user_choice - 1]
class ui():
    def __init__(self):
        pass
       
    def option_selection(*args):
        if len(args) == 0:
            print('')
        
        for index, value in enumerate(args):
            print(f'{index + 1}. Press {index + 1} to do {value}')
        
        user_choice = int(input('Please select an option: '))
        
        return args[user_choice - 1]
    
    



if __name__ == "__main__":
    inp = "Do Homework"
    inp2 = "Study"
    inp3 = "Eat"
    ui1 = ui()
    choice = ui1.option_selection(inp, inp2, inp3)

    print(f'You have selected {choice}')
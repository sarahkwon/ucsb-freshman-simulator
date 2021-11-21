from Activity import activities
from Protagonist_class import Protagonist

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

    def outcome_text(self, arg):
        prot = Protagonist(" ", " ")
        print('|------------------------')
        print(f'| Stress   | {prot.stress + activities[arg].stress}' + '(' + ('+', "")[activities[arg].stress >= 0] + f'{activities[arg].stress})')
        print(f'| Energy   | {prot.energy + activities[arg].energy}' + '(' + ('+', "")[activities[arg].energy >= 0] + f'{activities[arg].energy})')
        print(f'| Money    | {prot.money + activities[arg].money}' + '(' + ('+', "")[activities[arg].money >= 0] + f'{activities[arg].money})')
        print('|------------------------')
        print(f'| Intel    | {prot.intelligence + activities[arg].intelligence}' + '(' + ('+', "")[activities[arg].intelligence >= 0] + f'{activities[arg].intelligence})')
        print(f'| Fitness  | {prot.fitness + activities[arg].fitness}' + '(' + ('+', "")[activities[arg].fitness >= 0] + f'{activities[arg].fitness})')
        print(f'| Charisma | {prot.charisma + activities[arg].charisma}' + '(' + ('+', "")[activities[arg].charisma >= 0] + f'{activities[arg].charisma})')

if __name__ == "__main__":
    print()

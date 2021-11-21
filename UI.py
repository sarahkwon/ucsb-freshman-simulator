import Protagonist_class as prot
import Activity as activity
import ScheduledEvent as event

class ui:
    
    def option_selection(self, activity, event):
        x = ord('a')
        if len(activity) == 0:
            print('')
        print('<>---------------------------------<>')
        for index, value in enumerate(activity):
            print(f'| {index + 1}. Press {index + 1} to do {value}')
        print('<>---------------------------------<>')
        
        for index, value in enumerate(event):
            print(f'| {chr(x)}. Press {chr(x)} to do {value}')
            x += 1
        
        print('<>---------------------------------<>')
        print('| Press 0 to show current stats')
        print('| Press Z to exit')

        user_choice = input('Please select an option (Enter the number): ')
        
        
        if user_choice == 'z' or user_choice == 'Z':
            return 'z'
        
        try:
            if int(user_choice) > len(activity):
                print("---Please enter a valid input---")
                return None
            else:
                self.perform_choice_action(int(user_choice))
        except:
            if ord(user_choice) >= x:
                print("---Please enter a valid input---")
                return None
            else:
                self.perform_choice_action(user_choice)
        
    #Performs the action user inputted
    def perform_choice_action(self, choice):
        if choice == 'z':
            return 'z'
        elif choice == None:
            pass
        elif choice == 0:
            prot.protagonist.printStats()
        else:
            prot.protagonist.printStatsUpdates(choice, choice)

if __name__ == "__main__":
    print()

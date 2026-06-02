# entry point to the app

def main():
      # To collect and save student details
      students = []
      status = True
      while status:
            print('======MENU======')
            print('\n1. Add Student')
            print('2. Add Scholarship Student')
            print('3. View all Student')
            print('4. Exit')

            user_choice = input("Enter your choice : ")
            
            if(user_choice == '1'):
                 ## methods to add student
                 pass
                 print('Student added successfully')
            elif(user_choice == '2'):
                ## methods to add Scholarship student
                pass
                print('Scholarship Student added successfully')
            elif(user_choice == '3'):
                ## Display entries in 'Students'
                pass
            elif(user_choice == '4'):
                status = False
                break # Used to break a loop ( for or while)
            else:
                 print('Please a select valid choice:')

if __name__ == '__main__':
      main()
      

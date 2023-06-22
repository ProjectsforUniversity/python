import basic_calculator, number_guessing_game, password_generator, todo_list,  URL_shortener

def main():
    while True:
        print("Which program do you want to use?")
        print("1 - Basic Calculator\n",
              "2 - Number Guessing Game\n",
              "3 - Password Generator\n",
              "4 - To-Do List\n",
              "5 - URl Shortener\n",
              "0 - Exit")
        program = int(input("Enter the Program: "))
        start_program(program)

def start_program(program):
        if program == 1:
            basic_calculator.main()
        elif program == 2:
            number_guessing_game.play_game()
        elif program == 3:
            password_generator.main()
        elif program == 4:
            todo_list.main()
        elif program == 5:
            URL_shortener.app.run()
        elif program == 0:
            exit(0)
        else:
            print("Wrong Input")

if __name__ == '__main__':
  main()
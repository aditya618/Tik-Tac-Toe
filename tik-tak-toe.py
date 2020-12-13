
first_row = [' ', ' ', ' ']
second_row = [' ', ' ', ' ']
third_row = [' ', ' ', ' ']
chosen_pattern = 'X'



def game_display(first_row, second_row, third_row):
    print(f' {first_row[0]} | {first_row[1]} | {first_row[2]}')
    print('-----------')
    print(f' {second_row[0]} | {second_row[1]} | {second_row[2]}')
    print('-----------')
    print(f' {third_row[0]} | {third_row[1]} | {third_row[2]}')

def choose_pattern():
    correctPattern = False
    while not correctPattern:
        chosenPattern = input("Please select 'X' or 'O': ")
        if chosenPattern.lower() == 'x' or chosenPattern.lower() == 'o':
            correctPattern = True
            chosen_pattern = chosenPattern.upper()
            choose_position(chosen_pattern)
        else:
            print('Please choose valid option')

def choose_position(chosenPattern):
    postions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    correctPosition = False
    while not correctPosition:
        position = input('Enter the position (1,2,3,4,5,6,7,8,9): ')
        print('\n')
        if position.isdigit():
            temp = int(position)
            if temp in postions:
                correctPosition = True
                global chosen_pattern
                chosen_pattern = chosenPattern
                updated_screen(chosen_pattern, temp)
            else:
                print('Please choose valid position (1,2,3,4,5,6,7,8,9)')
        else:
            print('position must be number. Choose again!!')

def updated_screen(pattern, position):
    if position == 1:
        if first_row[0] == ' ':
            first_row[0] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 2:
        if first_row[1] == ' ':
            first_row[1] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 3:
        if first_row[2] == ' ':
            first_row[2] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 4:
        if second_row[0] == ' ':
            second_row[0] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 5:
        if second_row[1] == ' ':
            second_row[1] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 6:
        if second_row[2] == ' ':
            second_row[2] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 7:
        if third_row[0] == ' ':
            third_row[0] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 8:
        if third_row[1] == ' ':
            third_row[1] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    elif position == 9:
        if third_row[2] == ' ':
            third_row[2] = pattern
            game_display(first_row, second_row, third_row)
        else:
            print('already chosen. Try different position')
            swap_pattern()
    else:
        print('some error occured')
    print('\n')
    
def swap_pattern():
    global chosen_pattern
    if chosen_pattern == 'O':
        chosen_pattern = 'X'
    elif chosen_pattern == 'X':
        chosen_pattern = 'O'
    else:
        choose_position(' ')

def data_reset():
    global first_row, second_row, third_row
    first_row = [" ", " ", " "]
    second_row = [" ", " ", " "]
    third_row = [" ", " ", " "]

def main():
    gameOn = True
    game_display(first_row, second_row, third_row)
    choose_pattern()
    while gameOn:
        if(first_row[0] != ' ' and first_row[1] != ' ' and first_row[2] != ' '
        and second_row[0] != ' ' and second_row[1] != ' ' and second_row != ' '
        and third_row[0] != ' ' and third_row[1] != ' ' and third_row[2] != ' '):
            print('----- Its a Draw!! -----\n')
            playAgain = input('Want to play again?: (Y or N) ')
            if playAgain.lower() == 'y':
                data_reset()
                choose_pattern()
            else:
                gameOn = False
        else:
            if (first_row[0] == first_row[1] == first_row[2] == 'X' or first_row[0] == first_row[1] == first_row[2] == 'O' 
            or second_row[0] == second_row[1] == second_row[2] == 'X' or second_row[0] == second_row[1] == second_row[2] == 'O' 
            or third_row[0] == third_row[1] == third_row[2] == 'X' or third_row[0] == third_row[1] == third_row[2] == 'O'
            or first_row[0] == second_row[0] == third_row[0] == 'X' or first_row[0] == second_row[0] == third_row[0] == 'O'
            or first_row[1] == second_row[1] == third_row[1] == 'X' or first_row[1] == second_row[1] == third_row[1] == 'O'
            or first_row[2] == second_row[2] == third_row[2] == 'X' or first_row[2] == second_row[2] == third_row[2] == 'O'
            or first_row[0] == second_row[1] == third_row[2] == 'X' or first_row[0] == second_row[1] == third_row[2] == 'O'
            or first_row[2] == second_row[1] == third_row[0] == 'X' or first_row[2] == second_row[1] == third_row[0] == 'O'):
                global chosen_pattern
                print(f'----- {chosen_pattern} has won!! -----\n')
                playAgain = input('Want to play again?: (Y or N) ')
                if playAgain.lower() == 'y':
                    data_reset()
                    choose_pattern()
                else:
                    gameOn = False
            else:
                swap_pattern()
                choose_position(chosen_pattern)
            
                        

main()
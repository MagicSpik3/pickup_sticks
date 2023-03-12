import random
import time

def display_board(rows):
    # Print the current state of the game board
    for row in rows:
        print(' ' * (6 - len(row)), end='')
        print(' '.join([str(match) for match in row]))

def get_input(player):
    # Get the user's input for the number of sticks to pick up
    while True:
        try:
            row, sticks = [int(x) for x in input("Player {}, choose a row and number of sticks (e.g. 2,3): ".format(player)).split(",")]
            if row < 1 or row > 6 or sticks < 1 or sticks > len(rows[row-1]):
                raise ValueError
            return row, sticks
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

def remove_sticks(rows, row, sticks):
    # Remove the specified number of sticks from the specified row
    rows[row-1] = rows[row-1][sticks:]

def game_over(rows):
    # Check if the game is over (no sticks left)
    return all([len(row) == 0 for row in rows])

def computer_move(rows):
    # Choose a random row and number of sticks to pick up
    # There may be empty rows, so we should exclude them from the choice
    populated_rows = [i for i, sublist in enumerate(rows) if len(sublist) > 0]
    #print(populated_rows)

    row = random.choice(populated_rows)
    row = row + 1

    #print(row)
    sticks = random.randint(1, len(rows[row-1]))
    #print(sticks)
    return row, sticks



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Initialize the game board
    max_rows = 6
    rows = [[i + 1] * (i + 1) for i in range(max_rows)]
    player = 1

    # Get user input for game mode
    game_mode = input("Choose game mode: 1) Play against the computer, 2) Watch the computer play against itself: ")
    if game_mode == "1":
        computer_player = 2
    else:
        computer_player = random.randint(1, 2)
        print("Computer player: {}".format(computer_player))
        time.sleep(1)

    # Main game loop
    while not game_over(rows):
        display_board(rows)
        if player == computer_player:
            # Computer's turn
            print("Computer player {} is thinking...".format(player))
            time.sleep(1)
            row, sticks = computer_move(rows)
            print("Player {} chooses row {} and picks up {} sticks.".format(player, row, sticks))
            remove_sticks(rows, row, sticks)
        else:
            # Human player's turn
            row, sticks = get_input(player)
            remove_sticks(rows, row, sticks)
        player = 3 - player  # Switch players (alternates between 1 and 2)

    # Game over, print the winner
    display_board(rows)
    if computer_player == 0:
        print("Player {} wins!".format(player))
    elif player == computer_player:
        print("Computer player {} wins!".format(player))
    else:
        print("Player {} wins!".format(player))


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def display_board(rows):
    # Print the current state of the game board
    for row in rows:
        print(' ' * (6 - len(row)), end='')
        print(' '.join([str(match) for match in row]))

def get_input(player):
    # Get the user's input for the number of sticks to pick up
    while True:
        try:
            #num = int(input("!Player {}, choose a row and number of sticks (e.g. 2,3): ".format(player)))
#            row, sticks = [int(x) for x in str(num)]
#            if row < 1 or row > 6 or sticks < 1 or sticks > len(rows[row-1]):
            row, sticks = [int(x) for x in input("=Player {}, choose a row and number of sticks (e.g. 2,3): ".format(player)).split(",")]
            print(row, 'row', sticks, 'sticks')
            if row < 1 or row > 6 or sticks < 1 or sticks > len(rows[row - 1]):
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Initialize the game board
    rows = [[i + 1] * (i + 1) for i in range(6)]
    player = 1

    # Main game loop
    while not game_over(rows):
        display_board(rows)
        row, sticks = get_input(player)
        remove_sticks(rows, row, sticks)
        player = 3 - player  # Switch players (alternates between 1 and 2)

    # Game over, print the winner
    print("Player {} wins!".format(player))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

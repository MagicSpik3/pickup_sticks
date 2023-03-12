import time

def print_rows(rows):
    for i, row in enumerate(rows):
        print(" " * (5-i), end="")
        for j in range(row):
            print("|", end="")
        print()

def take_turn(rows, player):
    print("Player", player)
    row = int(input("Choose a row (1-6): "))
    sticks = int(input("Choose sticks to take (1-" + str(len(rows[row-1])) + "): "))
    if row < 1 or row > 6 or sticks < 1 or sticks > len(rows[row-1]):
        print("Invalid input, try again")
        return False
    rows[row-1] = rows[row-1][:-sticks]
    return True

def computer_turn(rows):
    import random
    row = random.randint(1, 6)
    sticks = random.randint(1, len(rows[row-1]))
    print("Computer chooses row", row, "and takes", sticks, "sticks")
    rows[row-1] = rows[row-1][:-sticks]
    time.sleep(1)

def play_game():
    rows = [[i+1 for j in range(i+1)] for i in range(6)]
    print_rows(rows)

    mode = input("Choose mode: (1) Human vs. Computer, (2) Computer play against itself: ")
    current_player = 1
    while True:
        print_rows(rows)

        if current_player == 1 or mode == '2':
            if mode == '2' or current_player == 1:
                computer_turn(rows)
            else:
                take_turn(rows, current_player)
        else:
            take_turn(rows, current_player)

        if all(len(row) == 0 for row in rows):
            print("Player", current_player, "wins!")
            break

        current_player = 3 - current_player

play_game()

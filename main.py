from random import randint

# TILE TEMPLATE
# tile = {
#     "isOpened": False,
#     "hasMine": False,
#     "hasFlag": False,
#     "adjCount": 0
# }

# TITLE MENU
def display_title():
    title = """
        ___           ___                         ___                    ___           ___           ___           ___           ___         ___     
       /\__\         /\  \         _____         /\  \                  /\  \         /\  \         /\__\         /\  \         /\  \       /\  \    
      /:/ _/_        \:\  \       /::\  \       /::\  \                |::\  \        \:\  \       /:/ _/_       _\:\  \       /::\  \     /::\  \   
     /:/ /\  \        \:\  \     /:/\:\  \     /:/\:\  \               |:|:\  \        \:\  \     /:/ /\  \     /\ \:\  \     /:/\:\__\   /:/\:\__\  
    /:/ /::\  \   ___  \:\  \   /:/  \:\__\   /:/  \:\  \            __|:|\:\  \   _____\:\  \   /:/ /::\  \   _\:\ \:\  \   /:/ /:/  /  /:/ /:/  /  
   /:/_/:/\:\__\ /\  \  \:\__\ /:/__/ \:|__| /:/__/ \:\__\          /::::|_\:\__\ /::::::::\__\ /:/_/:/\:\__\ /\ \:\ \:\__\ /:/_/:/  /  /:/_/:/__/___
   \:\/:/ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  /          \:\~~\  \/__/ \:\~~\~~\/__/ \:\/:/ /:/  / \:\ \:\/:/  / \:\/:/  /   \:\/:::::/  /
    \::/ /:/  /   \:\  /:/  /   \:\  /:/  /   \:\  /:/  /            \:\  \        \:\  \        \::/ /:/  /   \:\ \::/  /   \::/__/     \::/~~/~~~~ 
     \/_/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /              \:\  \        \:\  \        \/_/:/  /     \:\/:/  /     \:\  \      \:\~~\     
       /:/  /       \::/  /       \::/  /       \::/  /                \:\__\        \:\__\         /:/  /       \::/  /       \:\__\      \:\__\    
       \/__/         \/__/         \/__/         \/__/                  \/__/         \/__/         \/__/         \/__/         \/__/       \/__/    
   
   (sudo mnswpr) If the game title doesn't fit your terminal, please readjust its size to fit the board.
"""
    print(title)
    # NEW GAME
    # EASY: 8x8, 10
    # MEDIUM: 16*16, 40
    # HARD: 24*24, 99
    print("Select board difficulty:\n[1] EASY\n[2] MEDIUM\n[3] HARD\n[0] EXIT")
    while True:
        try:
            choice = int(input("(sudo mnswpr) "))
            if choice < 1 or choice > 3:
                raise ValueError
        except ValueError:
            print("(sudo mnswpr) Not a valid input!")
        except TypeError:
            print("(sudo mnswpr) Not a valid input!")
        else:
            if choice == 1:
                return 8, 10
            elif choice == 2:
                return 16, 40
            elif choice == 3:
                return 24, 110
                break

# GRID AND MINE GENERATION
def create_grid(size, mines):
    grid = []
    for i in range(size):
        clmn = []
        for j in range(size):
            clmn.append({
                "isOpened": False,
                "hasMine": False,
                "hasFlag": False,
                "adjCount": 0
            })
        grid.append(clmn)
    
    mines_placed = 0
    while mines_placed < mines:
        x = randint(0, len(grid) - 1)
        y = randint(0, len(grid) - 1)
        tile = grid[x][y]
        if (tile["hasMine"] == False):
            tile["hasMine"] = True
            mines_placed += 1

    calculate_mines(grid)
    return grid

# PRINT THE GRID
def print_grid(grid):
    # LABEL
    tab = "     "
    col_label = ""
    print()
    for x in range(len(grid)):
        if len(str(x + 1)) == 1:
            col_label += "   " + str(x + 1) + "  "
        else:
            col_label += "  " + str(x + 1) + "  "
    print(tab + col_label)
    print(tab + "______" * len(grid))

    # ROWS AND COLUMNS
    for x in range(len(grid)):
        isOpened_values = []
        for y in range(len(grid)):
            tile = grid[x][y]
            isOpened_values.append(tile["isOpened"])
        st1 = ""
        st2 = ""
        st3 = ""
        for i in range(len(isOpened_values)):
            tile = grid[x][i]
            if not isOpened_values[i]:
                if i == 0:
                    st1 += tab + "|░░░░░"
                    if (len(str(x + 1)) == 1):
                        st2 += "  " + str(x + 1) + "  " + "|░░░░░"
                    else:
                        st2 += " " + str(x + 1) + "  " + "|░░░░░"
                    st3 += tab + "|░░░░░"
                elif i == len(grid) - 1:
                    st1 += "|░░░░░|"
                    st2 += "|░░░░░|"
                    st3 += "|░░░░░|"
                else:
                    st1 += "|░░░░░"
                    st2 += "|░░░░░"
                    st3 += "|░░░░░"
            else:
                if i == 0:
                    st1 += tab + "|     "
                    if (len(str(x + 1)) == 1):
                        st2 += "  " + str(x + 1) + "  " + "|" + "  " + str(tile["adjCount"]) + "  "
                    else:
                        st2 += " " + str(x + 1) + "  " + "|" + "  " + str(tile["adjCount"]) + "  "
                    st3 += tab + "|_____"
                elif i == len(grid) - 1:
                    st1 += "|     |"
                    st2 += "|" + "  " + str(tile["adjCount"]) + "  " + "|"
                    st3 += "|_____|"
                else:
                    st1 += "|     "
                    st2 += "|" + "  " + str(tile["adjCount"]) + "  "
                    st3 += "|_____"
        print(st1 + "\n" + st2 + "\n" + st3 )

# MINE DISPLAY NUMBER CALCULATOR
def calculate_mines(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y]["hasMine"]:
                continue
            # CHECK AROUND THE TILE
            if x > 0 and grid[x - 1][y]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if x < len(grid) - 1  and grid[x + 1][y]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if y > 0 and grid[x][y - 1]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if y < len(grid) - 1 and grid[x][y + 1]["hasMine"]:
                grid[x][y]["adjCount"] += 1 
            if x > 0 and y > 0 and grid[x - 1][y - 1]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if x > 0 and y < len(grid) - 1 and grid[x - 1][y + 1]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if x < len(grid) - 1 and y > 0 and grid[x + 1][y - 1]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if x < len(grid) - 1 and y < len(grid) - 1 and grid[x + 1][y + 1]["hasMine"]:
                grid[x][y]["adjCount"] += 1

# TODO: REVEAL TILE

# TODO: FLAG TILE

# MAIN
if __name__ == "__main__":
    n, mines = display_title()
    grid = create_grid(n, mines)

    print_grid(grid)

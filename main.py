from random import randint

# TILE TEMPLATE
# tile = {
#     "isOpened": False,
#     "hasMine": False,
#     "hasFlag": False,
#     "adjCount": 0
# }

"""
    INTIALIZATION FUNCTIONS
"""
# GRID AND MINE GENERATION
def create_grid(size, mines):
    grid = []

    # POPULATING THE GRID WITH TILES
    for x in range(size):
        clmn = []
        for y in range(size):
            clmn.append({
                "isOpened": False,
                "hasMine": False,
                "hasFlag": False,
                "adjCount": 0
            })
        grid.append(clmn)
    
    # GENERATING MINES
    mines_placed = 0
    while mines_placed < mines:
        x = randint(0, len(grid) - 1)
        y = randint(0, len(grid) - 1)
        tile = grid[x][y]
        if (tile["hasMine"] == False):
            tile["hasMine"] = True
            mines_placed += 1

    # CALCULATE MINES ON ADJACENT TILES
    calculate_mines(grid)
    return grid

# MINE DISPLAY NUMBER CALCULATOR
def calculate_mines(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y]["hasMine"]:
                continue
            # CHECK AROUND THE TILE
            if x > 0 and grid[x - 1][y]["hasMine"]:
                grid[x][y]["adjCount"] += 1
            if x < len(grid) - 1 and grid[x + 1][y]["hasMine"]:
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

# DIFFICULTY SELECT
def difficulty_select():
    print("(sudo mnswpr) Select board difficulty:\n\t[1] EASY\n\t[2] MEDIUM\n\t[3] HARD")
    
    # INPUT VALIDATION
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
            # RETURN BOARD SIZES AND NO OF MINES
            # EASY: 8x8, 10
            # MEDIUM: 16*16, 40
            # HARD: 24*24, 99
            if choice == 1:
                return 8, 10
            elif choice == 2:
                return 16, 40
            elif choice == 3:
                return 24, 110
                break

"""
    INPUT FUNCTIONS
"""
# MOVEMENT SELECTION
def select_move(x, y):
    global grid
    
    # INPUT VALIDATION
    tile = grid[x][y]
    while True:
        print("(sudo mnswpr) Select move:\n\t[1] Reveal Tile\n\t[2] Flag/Unflag Tile")
        try:
            choice = int(input("(sudo mnswpr) "))
            if choice < 1 or choice > 2:
                raise ValueError
        except ValueError:
            print("(sudo mnswpr) Not a valid input!")
        except TypeError:
            print("(sudo msnwpr) Not a valid input!")
        else:
            if choice == 1:
                if tile["isOpened"]:
                    print("Tile already revealed!")
                elif tile["hasFlag"]:
                    print("Flagged tiles cannot be revealed!")
                else:
                    reveal_tile(x, y)  
            elif choice == 2:
                if tile["isOpened"]:
                    print("Revealed tiles cannot be flagged!")
                else:
                    flag_tile(x, y)
            break

# DECISION BEFORE MOVEMENT
def decision():
    global gameloop
    global saved

    # INPUT VALIDATION
    print("(sudo mnswpr) Type (row column) to select a tile from the board ex. 5 6 or ESC to save progress and quit.")
    while True:
        try:
            user_input = input("(sudo mnswpr) ").split(" ")
            input_length = len(user_input)
            if input_length == 2:
                x, y = user_input
                x = int(x) - 1
                y = int(y) - 1
                if x < 0 or x > 7 or y < 0 or y > 7:
                    raise ValueError
            elif input_length == 1:
                save = user_input[0]
                if not save == "ESC":
                    raise ValueError
        except ValueError:
            print("(sudo mnswpr) Not a valid input!")
        except TypeError:
            print("(sudo mnswpr) Not a valid input!")
        else:
            if input_length == 2:
                select_move(x, y)
            elif input_length == 1:
                export_save()
                gameloop = False
                saved = True
            break

# FLAG AND UNFLAG TILE
def flag_tile(x, y):
    global grid

    if grid[x][y]["hasFlag"]:
        grid[x][y]["hasFlag"] = False
    else:
        grid[x][y]["hasFlag"] = True

"""
    RENDER FUNCTIONS
"""
# TITLE MENU
def display_title():
    global grid
    global size
    global mines

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
    try:
        file = open("save.csv", "r")
    except FileNotFoundError:
        size, mines = difficulty_select()
        grid = create_grid(size, mines)
    else:
        print("(sudo mnswpr) You have a save file. Do you want to load from your save?\n\t[1] YES\n\t[2] NO")

        # INPUT VALIDATION
        while True:
            try:
                choice = int(input("(sudo mnswpr) "))
                if choice < 1 or choice > 2:
                    raise ValueError
            except ValueError:
                print("(sudo mnswpr) Not a valid input!")
            except TypeError:
                print("(sudo mnswpr) Not a valid input!")
            else:
                if choice == 1:
                    print("(sudo mnswpr) Importing save...")
                    import_save()
                elif choice == 2:
                    print("(sudo mnswpr) Creating new game...")
                    size, mines = difficulty_select()
                    grid = create_grid(size, mines)
                break

# PRINT THE GRID
def print_grid():
    global grid

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
        row_tab = ""
        displayValue = ""
        for i in range(len(isOpened_values)):
            tile = grid[x][i]

            # DETERMINE ROW TAB WIDTH
            if (len(str(x + 1)) == 1):
                row_tab = "  " + str(x + 1) + "  " 
            else:
                row_tab = " " + str(x + 1) + "  " 

            if not isOpened_values[i]:
                # DETERMINE DISPLAY FOR FLAG
                if tile["hasFlag"]:
                    displayValue = "|░░F░░"
                else:
                    displayValue = "|░░░░░"

                # STRING SETUPS
                if i == 0:
                    st1 += tab + "|░░░░░"
                    st2 += row_tab + displayValue
                    st3 += tab + "|░░░░░"
                elif i == len(grid) - 1:
                    st1 += "|░░░░░|"
                    st2 += displayValue + "|"
                    st3 += "|░░░░░|"
                else:
                    st1 += "|░░░░░"
                    st2 += displayValue
                    st3 += "|░░░░░"
            else:
                # DETERMINE PRINT VALUES FOR REVEALED TILES
                if tile["hasMine"]:
                    displayValue = "X"
                else:
                    displayValue = str(tile["adjCount"])

                # STRING SETUPS
                if i == 0:
                    st1 += tab + "|     "
                    st2 += row_tab + "|" + "  " + displayValue + "  "
                    st3 += tab + "|_____"
                elif i == len(grid) - 1:
                    st1 += "|     |"
                    st2 += "|" + "  " + displayValue + "  " + "|"
                    st3 += "|_____|"
                else:
                    st1 += "|     "
                    st2 += "|" + "  " + displayValue + "  "
                    st3 += "|_____"

        print(st1 + "\n" + st2 + "\n" + st3)
    print()

# REVEAL GRID
def reveal_grid():
    global grid

    # OPEN ALL TILES
    for x in range(len(grid)):
        for y in range(len(grid)):
            grid[x][y]["isOpened"] = True
    print_grid()

# REVEAL TILE
def reveal_tile(x, y):
    global grid
    global gameloop
    global opened_tiles

    if not grid[x][y]["isOpened"]:
        grid[x][y]["isOpened"] = True
        opened_tiles.append(grid[x][y])
        if not grid[x][y]["hasMine"]:
            # RECURSIVE CALLS FOR WHEN TILE REVEALED IS A 0-TILE
            if grid[x][y]["adjCount"] == 0:
                if x > 0:
                    reveal_tile(x - 1, y)
                if x < len(grid) - 1:
                    reveal_tile(x + 1, y)
                if y > 0:
                    reveal_tile(x, y - 1)
                if y < len(grid) - 1:
                    reveal_tile(x, y + 1)
                if x > 0 and y > 0:
                    reveal_tile(x - 1, y - 1)
                if x > 0 and y < len(grid) - 1:
                    reveal_tile(x - 1, y + 1)
                if x < len(grid) - 1 and y > 0:
                    reveal_tile(x + 1, y - 1)
                if x < len(grid) - 1 and y < len(grid) - 1:
                    reveal_tile(x + 1, y + 1)
        else:
            gameloop = False

# FLAG REMAINING TILES
def flag_remain():
    global grid

    # CHECK ALL TILES IF NOT OPENED AND NO FLAG
    for x in range(len(grid)):
        for y in range(len(grid)):
            if not grid[x][y]["isOpened"] and not grid[x][y]["hasFlag"]:
                grid[x][y]["hasFlag"] = True

"""
    MISCELLANEOUS FUNCTIONS
"""
# EXPORT SAVE
def export_save():
    global grid

    save_file = open("save.csv", "w+")
    for x in range(len(grid)):
        for y in range(len(grid)):
            tile = grid[x][y]
            save_file.write("{},{},{},{}\n".format(tile["isOpened"], tile["hasMine"], tile["hasFlag"], tile["adjCount"]))
    print("Game Saved!")

# IMPORT SAVE
def import_save():
    global grid
    global size
    global mines

    save_file = open("save.csv", "r")
    save_data = []
    for line in save_file:
        save_data.append(line[:-1].split(","))

    i = 0
    size = int(len(save_data)**0.5)
    for x in range(size):
        clmn = []
        for y in range(size):
            isOpened_save = string_to_bool(save_data[i][0])
            hasMine_save = string_to_bool(save_data[i][1])
            hasFlag_save = string_to_bool(save_data[i][2])
            clmn.append({
                "isOpened": isOpened_save,
                "hasMine": hasMine_save,
                "hasFlag": hasFlag_save,
                "adjCount": int(save_data[i][3])
            })
            if hasMine_save:
                mines += 1
            i += 1
        grid.append(clmn)

# CHECK WHEN TO BREAK LOOP
def gameloop_check():
    global gameloop
    global opened_tiles
    global size
    global mines
    global win

    if len(opened_tiles) == size**2 - mines:
        gameloop = False
        win = True

# STRING TO BOOL FOR IMPORTING
def string_to_bool(string):
    if string == "True":
        return True
    else:
        return False

"""
    MAIN
"""
if __name__ == "__main__":
    # INITIALIZATION OF VARIABLES
    gameloop = True
    win = False
    saved = False
    grid = []
    size = mines = 0
    opened_tiles = []

    # SETTING UP
    display_title()

    # GAME LOOP
    while gameloop:
        # INPUT PROCESSING, UPDATE, AND RENDER
        print_grid()
        decision()
        gameloop_check()
    else:
        if win:
            flag_remain()
            print_grid()
            print("All mines avoided!")
            print("""
      ___           ___           ___                                             ___                   
     /\__\         /\  \         /\  \         _____                 ___         /\  \         _____    
    /:/ _/_       /::\  \       /::\  \       /::\  \               /\__\       /::\  \       /::\  \   
   /:/ /\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \             /:/__/      /:/\:\  \     /:/\:\  \  
  /:/ /::\  \   /:/  \:\  \   /:/  \:\  \   /:/  \:\__\           /::\  \     /:/  \:\  \   /:/ /::\__\ 
 /:/__\/\:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/ \:|__|          \/\:\  \   /:/__/ \:\__\ /:/_/:/\:|__|
 \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  /           ~~\:\  \  \:\  \ /:/  / \:\/:/ /:/  /
  \:\  /:/  /   \:\  /:/  /   \:\  /:/  /   \:\  /:/  /               \:\__\  \:\  /:/  /   \::/_/:/  / 
   \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /                /:/  /   \:\/:/  /     \:\/:/  /  
    \::/  /       \::/  /       \::/  /       \::/  /                /:/  /     \::/  /       \::/  /   
     \/__/         \/__/         \/__/         \/__/                 \/__/       \/__/         \/__/    
            """)
        elif saved:
            pass
        else:
            reveal_grid()
            print("You stepped on a mine!")
            print("""
      ___           ___           ___           ___                    ___                         ___           ___     
     /\__\         /\  \         /\  \         /\__\                  /\  \          ___          /\__\         /\  \    
    /:/ _/_       /::\  \       |::\  \       /:/ _/_                /::\  \        /\  \        /:/ _/_       /::\  \   
   /:/ /\  \     /:/\:\  \      |:|:\  \     /:/ /\__\              /:/\:\  \       \:\  \      /:/ /\__\     /:/\:\__\  
  /:/ /::\  \   /:/ /::\  \   __|:|\:\  \   /:/ /:/ _/_            /:/  \:\  \       \:\  \    /:/ /:/ _/_   /:/ /:/  /  
 /:/__\/\:\__\ /:/_/:/\:\__\ /::::|_\:\__\ /:/_/:/ /\__\          /:/__/ \:\__\  ___  \:\__\  /:/_/:/ /\__\ /:/_/:/__/___
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \:\/:/ /:/  /          \:\  \ /:/  / /\  \ |:|  |  \:\/:/ /:/  / \:\/:::::/  /
  \:\  /:/  /   \::/__/       \:\  \        \::/_/:/  /            \:\  /:/  /  \:\  \|:|  |   \::/_/:/  /   \::/~~/~~~~ 
   \:\/:/  /     \:\  \        \:\  \        \:\/:/  /              \:\/:/  /    \:\__|:|__|    \:\/:/  /     \:\~~\     
    \::/  /       \:\__\        \:\__\        \::/  /                \::/  /      \::::/__/      \::/  /       \:\__\    
     \/__/         \/__/         \/__/         \/__/                  \/__/        ~~~~           \/__/         \/__/            
            """)

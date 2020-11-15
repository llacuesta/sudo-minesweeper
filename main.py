from random import randint

# TILE TEMPLATE
# tile = {
#     "isOpened": False,
#     "hasMine": False,
#     "hasFlag": False,
#     "adjCount": 0
# }

# GRID AND MINE GENERATION
def create_grid(size, mines):
    # row = col = size
    # grid = []
    # while row > 0:
    #     column = []
    #     while col > 0:
    #         column.append(tile)
    #         col -= 1
    #     grid.append(column)
    #     row -= 1

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
        mine = grid[x][y]
        if (mine["hasMine"] == False):
            mine["hasMine"] = True
            mines_placed += 1

    return grid

# PRINT THE GRID
def print_grid(grid):
    title = """
      ___           ___           ___           ___           ___         ___     
     /\  \         /\  \         /\__\         /\  \         /\  \       /\  \    
    |::\  \        \:\  \       /:/ _/_       _\:\  \       /::\  \     /::\  \   
    |:|:\  \        \:\  \     /:/ /\  \     /\ \:\  \     /:/\:\__\   /:/\:\__\  
  __|:|\:\  \   _____\:\  \   /:/ /::\  \   _\:\ \:\  \   /:/ /:/  /  /:/ /:/  /  
 /::::|_\:\__\ /::::::::\__\ /:/_/:/\:\__\ /\ \:\ \:\__\ /:/_/:/  /  /:/_/:/__/___
 \:\~~\  \/__/ \:\~~\~~\/__/ \:\/:/ /:/  / \:\ \:\/:/  / \:\/:/  /   \:\/:::::/  /
  \:\  \        \:\  \        \::/ /:/  /   \:\ \::/  /   \::/__/     \::/~~/~~~~ 
   \:\  \        \:\  \        \/_/:/  /     \:\/:/  /     \:\  \      \:\~~\     
    \:\__\        \:\__\         /:/  /       \::/  /       \:\__\      \:\__\    
     \/__/         \/__/         \/__/         \/__/         \/__/       \/__/    

"""
    print(title)
    # LABEL
    tab = "     "
    col_label = ""
    for i in range(len(grid)):
        col_label += "   " + str(i + 1) + "  " 
    print(tab + col_label)
    print(tab + "______" * len(grid))

    # ROWS AND COLUMNS
    for x in range(len(grid)):
        isOpened_values = []
        for y in range(len(grid)):
            isOpened_values.append(grid[x][y]["isOpened"])
        st1 = ""
        st2 = ""
        st3 = ""
        for i in range(len(isOpened_values)):
            if not isOpened_values[i]:
                if i == 0:
                    st1 += tab + "|░░░░░"
                    st2 += "  " + str(x + 1) + "  " + "|░░░░░"
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
                    st2 += "  " + str(x + 1) + "  " + "|" + "  " + str(grid[x][i]["adjCount"]) + "  "
                    st3 += tab + "|_____"
                elif i == len(grid) - 1:
                    st1 += "|     |"
                    st2 += "|" + "  " + str(grid[x][i]["adjCount"]) + "  " + "|"
                    st3 += "|_____|"
                else:
                    st1 += "|     "
                    st2 += "|" + "  " + str(grid[x][i]["adjCount"]) + "  "
                    st3 += "|_____"
        print(st1 + "\n" + st2 + "\n" + st3 )

# MAIN
grid = create_grid(8, 64)
# for x in range(8):
#     for y in range(8):
#         print(grid[x][y]["hasMine"])
#         if (grid[x][y]["hasMine"]):
#             grid[x][y]["isOpened"] = True
# grid[4][0]["isOpened"] = True
# grid[0][3]["isOpened"] = True
# grid[1][3]["isOpened"] = True
# grid[1][2]["isOpened"] = True
# grid[2][4]["isOpened"] = True
print_grid(grid)

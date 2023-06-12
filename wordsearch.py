import os

# Set the current directory to the directory of the Python script
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# Read the word search grid from file
with open('1337-word-search.txt', 'r') as file:
    grid = [line.strip() for line in file]

# Define the flag to search
flag = "SEE{"

# Function to search for the flag recursively
def search_flag(grid, word, row, col, direction):
    # Base case: if we reach the end of the word, return True
    if len(word) == 0:
        return True

    # Check if current cell is out of bounds or doesn't match the next letter
    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or grid[row][col] != word[0]:
        return False

    # Store the current cell value and mark it as visited
    temp = grid[row][col]
    grid[row] = grid[row][:col] + '_' + grid[row][col+1:]

    # Explore all eight directions recursively
    found = search_flag(grid, word[1:], row-1, col, "up") if direction != "down" else False
    found = found or search_flag(grid, word[1:], row+1, col, "down") if direction != "up" else False
    found = found or search_flag(grid, word[1:], row, col-1, "left") if direction != "right" else False
    found = found or search_flag(grid, word[1:], row, col+1, "right") if direction != "left" else False
    found = found or search_flag(grid, word[1:], row-1, col-1, "upleft") if direction != "downright" else False
    found = found or search_flag(grid, word[1:], row-1, col+1, "upright") if direction != "downleft" else False
    found = found or search_flag(grid, word[1:], row+1, col-1, "downleft") if direction != "upright" else False
    found = found or search_flag(grid, word[1:], row+1, col+1, "downright") if direction != "upleft" else False

    # Restore the original cell value
    grid[row] = grid[row][:col] + temp + grid[row][col+1:]

    return found

# Function to search for the full flag recursively
def search_full_flag(grid, flag, row, col):
    # Base case: if we reach the end of the flag, return True
    if len(flag) == 0:
        return True

    # Check if current cell is out of bounds or doesn't match the next letter of the flag
    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or grid[row][col] != flag[0]:
        return False

    # Search for the remaining part of the flag in all directions
    found = search_full_flag(grid, flag[1:], row-1, col) or \
            search_full_flag(grid, flag[1:], row+1, col) or \
            search_full_flag(grid, flag[1:], row, col-1) or \
            search_full_flag(grid, flag[1:], row, col+1) or \
            search_full_flag(grid, flag[1:], row-1, col-1) or \
            search_full_flag(grid, flag[1:], row-1, col+1) or \
            search_full_flag(grid, flag[1:], row+1, col-1) or \
            search_full_flag(grid, flag[1:], row+1, col+1)

    return found

# Search for the starting point of the flag
flag_start_found = False
flag_start_coordinates = None
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if search_flag(grid, flag, row, col, ""):
            flag_start_found = True
            flag_start_coordinates = (row, col)
            break
    if flag_start_found:
        break

# If the starting point of the flag is found, search for the full flag
if flag_start_found:
    flag_end_found = search_full_flag(grid, flag, flag_start_coordinates[0], flag_start_coordinates[1])
    if flag_end_found:
        print("Flag found at starting coordinates:", flag_start_coordinates)
        print("Flag:", flag)
    else:
        print("Full flag not found.")
else:
    print("Flag not found.")

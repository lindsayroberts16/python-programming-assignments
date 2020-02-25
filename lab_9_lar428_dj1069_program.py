from turtle import*
from random import randint
from copy import deepcopy
# turn off live turtle
tracer(0)
hideturtle()


# draw_box
# params: (x,y)- coordinates
# params: size- size of box
# params: fill_color- color of box
def draw_box(x,y,size,fill_color):
    penup()
    goto(x,y)
    pendown()
    fillcolor(fill_color)
    begin_fill()
    setheading(90)
    for i in range(4):
        forward(size)
        right(90)
    end_fill()

# draw_grid
# params: none
# return value: none
# purpose- to draw grid
def draw_grid():
    start_x = -250
    start_y = 200
    box_size = 7
    square_color = "grey"
    for i in range(len(grid)):
        for j in range(rows):
            if grid[i][j]== "o":
                square_color = "white"
            if grid[i][j] == "#":
                square_color = "black"
            draw_box(start_x+j*box_size,start_y-i*box_size,box_size,square_color)

# random beginning
# params: grid_name- name of grid
# return value
# purpose: create random beginning
def random_beginning(grid_name):
    for r in range(rows):
        for c in range(cols):
            p = randint(1,5)
            if p == 1:
                m = str("#")
            elif p > 1:
                m = str("o")
            grid_name[r][c]= str(m)
    

# create original
# params: none
# return values: grid
# purpose: to create grid
def create_grid():
    grid=[]
    one_row=["o"]*cols
    for row in range(rows):
        grid.append(one_row+[])
    return grid

# print_grid
# params: none
# return values: none
# purpose: print grid
def print_grid():
    ind=0
    col_num = []
    row_num = []
    for column_count in range(cols):
        c_count= str(column_count)
        col_num.append(c_count)

    for row_count in range(rows):
        r_count= str(row_count)
        row_num.append(r_count)
        
        print(''.join(grid[ind]))
        ind+=1
        
# place_block
# params: block_row
# params: block_col
# purpose: place block
def place_block(block_row, block_col):
    grid[block_row][block_col]="#"
    grid[block_row][block_col+1]="#"
    grid[block_row-1][block_col]="#"
    grid[block_row-1][block_col+1]="#"

# place_blinker
# params: blinker_row
# params: blinker_col
# purpose: place blinker
def place_blinker(blinker_row, blinker_col):
    grid[blinker_row-1][blinker_col]="#"
    grid[blinker_row][blinker_col]="#"
    grid[blinker_row+1][blinker_col]="#"
    global blinker_r
    global blinker_c
    blinker_r = blinker_row
    blinker_c = blinker_col

# place glider
# params: glider_row
# params: glider_col
# purpose: place glider
def place_glider(glider_row, glider_col):
	grid[glider_row][glider_col]="#"
	grid[glider_row][glider_col-1]="#"
	grid[glider_row][glider_col-2]="#"
	grid[glider_row-1][glider_col]="#"
	grid[glider_row-2][glider_col-1]="#"
	global glider_r
	global glider_c
	glider_r = glider_row
	glider_c = glider_col
	

# countneighbors
# params: x- x coordinate
# params: y - y coordinate
# return values: neighbor_count
# purpose: count the neighbors
def countneighbors(x,y):
    neighbor_count=0
    if grid[(x+1)%rows][(y+1)%cols] == "#":
        neighbor_count +=1
    if grid[(x+1)%rows][(y-1)%cols] == "#":
        neighbor_count +=1
    if grid[(x+1)%rows][(y)%cols] == "#":
        neighbor_count +=1
    if grid[(x)%rows][(y-1)%cols] == "#":
        neighbor_count +=1
    if grid[(x)%rows][(y+1)%cols] == "#":
        neighbor_count +=1
    if grid[(x-1)%rows][(y-1)%cols] == "#":
        neighbor_count +=1
    if grid[(x-1)%rows][(y)%cols] =="#":
        neighbor_count +=1
    if grid[(x-1)%rows][(y+1)%cols] =="#":
        neighbor_count +=1
    return(neighbor_count)

#update_life
#params: orig_grid- original grid
# params: new_grid- new grid
# return values: new_grid
# purpose: update life

def update_life(orig_grid, new_grid):
    neighbor_count = 0
    for urow in range(len(orig_grid)):
        for ucol in range(len(orig_grid[0])):
            neighbor_count = countneighbors(urow,ucol)
            if orig_grid[urow][ucol] == "#":
                if neighbor_count < 2 or neighbor_count > 3:
                    new_grid[urow][ucol] = "o"
                elif neighbor_count == 2 or neighbor_count == 3:
                    new_grid[urow][ucol] = "#"
            elif orig_grid[urow][ucol] == "o":
                if neighbor_count == 3:
                    new_grid[urow][ucol] = "#"
    return new_grid


#main
#user input

rows = int(numinput("rows","rows: "))
cols = int(numinput("cols","cols: "))
print(" ")

#draw grid with blinker,block, glider
grid = create_grid()
random_beginning(grid)
place_block(22,4)
place_blinker(43,17)
place_glider(2,7)
print_grid()
print(" ")

# neighbor count and update
for x in range(len(grid)):
    for y in range(len(grid)):
        print(str(countneighbors(x,y)),end="")
    print()
draw_grid()
print_grid()
print("")
times= int(numinput("time steps","How many time steps? ") )
print("")
for i in range(times):
    new_grid=create_grid()
    new_grid = update_life(grid, new_grid)
    grid = deepcopy(new_grid)
##    print_grid()
    draw_grid()
    update()
    

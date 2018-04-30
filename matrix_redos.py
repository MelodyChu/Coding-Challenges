# flood fill algorithm w/ queue

# s = impl([
#         ['O', 'X', 'X', 'X', 'X'],
#         ['X', 'O', 'O', 'O', 'X'],
#         ['X', 'O', '#', 'O', 'X'],
#         ['X', 'O', 'O', 'O', 'X'],
#         ['X', 'X', 'X', 'X', 'X'],
#         ['X', 'X', 'X', '#', '#'],
#         ['X', 'X', 'X', 'X', 'X']
#     ])

# take starting coordinates
# figure out character / color
# create a queue using a list
# add first coordinates to the list queue
# while queue is not empty
# pop the first item in queue; check surrounding coords to see if they need to be color changed
# if so, add to queue

# def flood_fill(self, x, y, new_color): # self is matrix
#     height = len(self.pixels[0])
#     width = len(self.pixels)
#     orig_color = self[x][y] # x is height, y is width

#     fill_queue = []
#     fill_queue.append(x,y) # append coordinates as tuples

#     while len(fill_queue) > 0: # we will keep adding coords to this queue that need to be coloredd
#         current = fill_queue.pop(0)
#         current_x = current[0]
#         current_y = current[1]
#         self.pixels[current_x][current_y] = new_color # change to new color
#         # let's say current_x = 0, current_y = 1
#         # if coords are within index range and if they are of the same color; append them to queue
#         if current_x < width - 1 and self.pixels[current_x + 1][current_y] == orig_color:
#             fill_queue.append((current_x + 1, current_y))
#         if current_y < height - 1 and self.pixels[current_x][current_y+1] == orig_color:
#             fill_queue.append((current_x,current_y+1))
#         if current_x - 1 >= 0 and self.pixels[current_x-1][current_y] == orig_color:
#             fill_queue.append((current_x,current_y+1))
#         if current_y - 1 >= 0 and self.pixels[current_x][current_y-1] == orig_color:
#             fill_queue.append((current_x, current_y-1))

#     return self.pixels


# Classpass problem: Find number of people in image

s = [
        ['O', 'X', 'X', '0', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'O', '0', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['0', 'X', 'X', '0', 'X'],
        ['X', 'X', 'X', '0', '0'],
        ['X', 'X', 'X', '0', 'X']
    ]

# iterate through matrix
# find all coordinates with X's; put them all into a list

# now we have list of all coordinates with X's
# start a counter
# pop off e/ coordinate; check if left, right, top, bottom is in the queue; if it is, then remove that person from queue
# do this until the queue is empty
# return the counter

def count_people(matrix):
    list_coords = []
    for row in range(0,len(matrix)):
        for item in range(0,len(matrix[row])):
            if matrix[row][item] == "X":
                list_coords.append((row,item))

    print list_coords

    # now I have list of all rows with items

    counter = 0
    list_groups = [] # houses all the groups
    while len(list_coords) > 0:
        coord = list_coords.pop(0)
        counter += 1
        print counter
        print coord 

        row_coord = coord[0]
        item_coord = coord[1]

        indiv_groups = []

        # if is_X(row_coord,item_coord):
        #     list_groups.append(is_X(row_coord,item_coord))

        if row_coord < len(matrix) - 1 and matrix[row_coord+1][item_coord] == 'X':
            print (row_coord+1,item_coord)
            indiv_groups.append((row_coord+1,item_coord)) # remove adjacent X's from the queue
        if row_coord > 0 and matrix[row_coord-1][item_coord] == 'X':
            print (row_coord-1, item_coord)
            indiv_groups.append((row_coord-1, item_coord))
        if item_coord < len(matrix[0]) - 1 and matrix[row_coord][item_coord+1] == 'X':
            print (row_coord, item_coord+1)
            indiv_groups.append((row_coord, item_coord+1))
        if item_coord > 0 and matrix[row_coord][item_coord-1]=='X':
            print (row_coord,item_coord-1)
            indiv_groups.append((row_coord,item_coord-1))

        list_groups.append(indiv_groups)



        # put all of these in a new function; check all nearby coords
        

    return counter

print count_people(s)

def is_X(row_coord,item_coord):
    adjacent_list = []
    if row_coord < len(matrix) - 1 and matrix[row_coord+1][item_coord] == 'X':
        print (row_coord+1,item_coord)
        adjacent_list.append((row_coord+1,item_coord)) # remove adjacent X's from the queue
    if row_coord > 0 and matrix[row_coord-1][item_coord] == 'X':
        print (row_coord-1, item_coord)
        adjacent_list.append((row_coord-1, item_coord))
    if item_coord < len(matrix[0]) - 1 and matrix[row_coord][item_coord+1] == 'X':
        print (row_coord, item_coord+1)
        adjacent_list.append((row_coord, item_coord+1))
    if item_coord > 0 and matrix[row_coord][item_coord-1]=='X':
        print (row_coord,item_coord-1)
        adjacent_list.append((row_coord,item_coord-1))

    return adjacent_list







my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}

white_rect = {
    'left_x': 5,
    'bottom_y': 2,
    'width': 3,
    'height': 6
}

answer = {
    'left_x': 5,
    'bottom_y': 2,
    'width': 2,
    'height': 2
}

def find_intersections(rect1, rect2):
    # create a list of all squares that rectangles covered
    #list of lists

    all_rect1 = get_all_coord(rect1)
    all_rect2 = get_all_coord(rect2)

    overlaps = []

    for coord in all_rect1:
        if coord in all_rect2:
            overlaps.append(coord)

    print overlaps

    min_sum = sum(overlaps[0])
    min_x = overlaps[0][0]
    min_y = overlaps[0][1]
    for coord in overlaps:
        if coord[0] + coord[1] < min_sum:
            min_x = coord[0]
            min_y = coord[1]
            min_sum = coord[0] + coord[1]

    print "min_X is " + str(min_x)
    print "min_Y is " + str(min_y)

    max_width = 0
    max_height = 0
    for coord in overlaps:
        if coord[0] > max_width:
            max_width = coord[0]
        if coord[1] > max_height:
            max_height = coord[1]

    overlap_width = max_width - min_x
    overlap_height = max_height - min_y

    return {'left_x': min_x, 'bottom_y': min_y, 'width': overlap_width, 'height': overlap_height}

    
    # find min of lowest x & lowest y sum; that will be left x adn bottom y
    # find max x; subtraact min x
    # find max y; subtract miny
    # format into dictionary

def get_all_coord(rect1):
    rect1_squares = []
    for x_coord in range(0,rect1['width']+1):
        for y_coord in range(0,rect1['height']+1):
            rect1_squares.append([rect1['left_x']+x_coord, rect1['bottom_y']+y_coord])

    return rect1_squares




print find_intersections(my_rectangle, white_rect)
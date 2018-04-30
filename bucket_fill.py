"""
Bucket Fill Exercise

Imagine you are working on an image editing application. You need to implement a bucket fill tool similar to the one
in paint. The user will use the tool by selecting a color and clicking on the canvas. The tool fills the selected
region of color with the new color.

When a pixel is filled, all of its neighbors (above, below, left, or right) of the same color must also be filled,
as well as their neighbors, and so on, until the entire region has been filled with the new color.

In this exercise, you must write *TWO* implementations of the tool. Each implementation must be different. It is not
required that you invent the solutions yourself. You are encouraged to research the problem. Please write documentation
explaining the difference of each implementation, such as when one solution might be more appropriate than the other.
Don't forget to validate input. There is one existing test, however, you might consider adding some more. Keep in mind
that although the given canvas is small, the solution should be applicable for a real canvas that could have huge
resolutions.

Please use python3 to complete this assignment.
"""


class Canvas(object):
    def __init__(self, pixels):
        self.pixels = pixels

    def __str__(self):
        return '\n'.join(map(lambda row: ''.join(row), self.pixels))

    def fill(self, x, y, color):
        """
        Fills a region of color at a given location with a given color.

        :param x:  the x coordinate where the user clicked
        :param y: the y coordinate where the user clicked
        :param color: the specified color to change the region to
        """
        raise NotImplementedError  # Override this function in the Solution classes


class Solution1(Canvas):
    # TODO write documentation
    def fill_helper(self, x, y, orig_color, color):
        y_height = len(self.pixels[0]) # max height; y is like width

        # print "height is" + str(y_height)
        x_width = len(self.pixels) # max length; x is like height
        # print "width is" + str(x_width)

        if (x > x_width - 1) or (y > y_height - 1) or (x < 0) or (y < 0):
            return
        if self.pixels[x][y] != orig_color:
            return
        self.pixels[x][y] = color # that pixel becomes that color if it = original color
        #print x,y

        # check top, bottom, left, right pixels to see if they are original color
        # if (x+1 < x_width-1) and (y+1 < y_height-1):
        # if (self.pixels[x][y+1]) == orig_color and (y+1 < y_height-1):
        # if (self.pixels[x-1][y]) == orig_color:
        if x > 0: # check left; stop at left boundary
            Solution1.fill_helper(self, x-1, y, orig_color, color)

        # if (self.pixels[x][y-1]) == orig_color:
        if y > 0: # check up; stop at top boundary
            Solution1.fill_helper(self, x, y-1, orig_color, color)

        #if (self.pixels[x+1][y]) == orig_color:
        if x < x_width - 1: # check right; stop at right boundary
            Solution1.fill_helper(self, x+1,y, orig_color, color)

        #if (self.pixels[x][y+1]) == orig_color:
        if y < y_height - 1: # check down
            Solution1.fill_helper(self, x,y+1, orig_color, color) 
            
       
            
        
            
        # if (self.pixels[x+1][y]) == orig_color:
        
    
    def fill(self, x, y, color): 
        #print "SELF IS" + str(type(self))
        orig_color = self.pixels[x][y]  # original color of first pixel clicked
        #print "ORIG COLOr IS" + str(orig_color)
        #import pdb; pdb.set_trace()
        Solution1.fill_helper(self, x, y, orig_color, color)
        
                

        #print self.pixels #incorrect, nothing changes
        new_str = ''
        for arr in self.pixels:
            new_str += ''.join(arr)

        return new_str

            #import pdb; pdb.set_trace()
         # TODO write implementation



class Solution2(Canvas):
    # TODO write documentation

    def fill(self, x, y, color):
        pass
    #     #pass  # TODO write implementation - use a queue
    #     if self.pixels[x][y] != orig_color: #(create a helper for this)
    #         return

    #     q = [self]
    #     while q:
    #         n = q.pop(0)
    #         print n # debug
    #         n = color # changineg n

    #         if 

def test_solution(impl):
    s = impl([
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'O', '#', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', '#', '#'],
        ['X', 'X', 'X', 'X', 'X']
    ])
    #print "SOLUTION INPUT IS" + str(type(s)) + "********************"
    s.fill(0, 1, '*')
    s.fill(5, 4, 'O')
    s.fill(2, 2, '@')
    assert str(s) == 'O****\n*OOO*\n*O@O*\n*OOO*\n*****\n***OO\n*****'


if __name__ == '__main__':
    test_solution(Solution1)
    test_solution(Solution2)

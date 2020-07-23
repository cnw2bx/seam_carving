# CS4102 Fall 2019 -- Homework 5
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: cnw2bx
# Collaborators: emb2ug
# Sources: Introduction to Algorithms, Cormen
#################################

class SeamCarving:
    seam = []
    mem = [[]]

    def __init__(self):
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def diff(self, image, i,j,y,x):
        diff = ((image[y][x][0]-image[j][i][0])**2 + (image[y][x][1] - image[j][i][1])**2 + (image[y][x][2] - image[j][i][2])**2)**0.5
        return diff

    def energy(self, image, i, j):
        tot_diff = 0.0
        max_x = len(image[0])-1
        max_y = len(image)-1
        count = 0

        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x <= max_x and 0 <= y <= max_y:
                    if x != i or y != j:
                        count += 1
                        tot_diff += self.diff(image,i,j,y,x)

        return tot_diff/count

    def find_seam(self, image, x, y):
        max_x = len(image[0]) - 1
        max_y = len(image) - 1
        weight = 0.0
        min_path = []
        #mem = [[None for i in range(len(image[0]))] for j in range(len(image))]

        if(self.mem[y][x] is not None):
            return self.mem[y][x]

        if y == max_y:
            #BASE CASE
            weight = self.energy(image, x, y)
            min_path = [x]
            dict = {
                'weight': weight,
                'seam': min_path
            }
            self.mem[y][x] = dict

            return dict

        elif x == 0:
            b = self.find_seam(image, x, y+1)
            c = self.find_seam(image, x+1, y+1)
            #b = energy(self, image, x, y) + find_seam(self, image, x, y+1)[y+1][x].get('weight')
            #c = energy(self, image, x, y) + find_seam(self, image, x+1, y+1)[y+1][x+1].get('weight')

            if b.get('weight') < c.get('weight'):
                #b.get('seam').insert(0,x)
                #min_path.insert(0,x)
                weight = b.get('weight') + self.energy(image, x, y)
                min_path = [x] + b.get('seam')
                dict = {
                    'weight' : weight,
                    'seam' : min_path
                }
                self.mem[y][x] = dict
                return dict
            else:
                weight = c.get('weight') + self.energy(image, x, y)
                min_path = [x] + c.get('seam')
                dict = {
                    'weight': weight,
                    'seam': min_path
                }
                self.mem[y][x] = dict
                return dict


        elif x == max_x:
            a = self.find_seam(image, x - 1, y+1)
            b = self.find_seam(image, x, y+1)

            if a.get('weight') < b.get('weight'):
                weight = a.get('weight') + self.energy(image, x, y)
                min_path = [x] + a.get('seam')
                dict = {
                    'weight': weight,
                    'seam': min_path
                }
                self.mem[y][x] = dict
                return dict

            else:
                weight = b.get('weight') + self.energy(image, x, y)
                min_path = [x] + b.get('seam')
                dict = {
                    'weight': weight,
                    'seam': min_path
                }
                self.mem[y][x] = dict
                return dict

        else:
            a = self.find_seam(image, x - 1, y + 1)
            b = self.find_seam(image, x, y + 1)
            c = self.find_seam(image, x + 1, y + 1)

            if min(a.get('weight'), b.get('weight'), c.get('weight')) == a.get('weight'):
                weight = a.get('weight') + self.energy(image, x, y)
                min_path = [x] + a.get('seam')
                dict = {
                    'weight': weight,
                    'seam': min_path
                }
                self.mem[y][x] = dict
                return dict

            elif min(a.get('weight'), b.get('weight'), c.get('weight')) == b.get('weight'):
                weight = b.get('weight') + self.energy(image, x, y)
                min_path = [x] + b.get('seam')
                dict = {
                    'weight': weight,
                    'seam': min_path
                }
                self.mem[y][x] = dict
                return dict

            else:
                weight = c.get('weight') + self.energy(image, x, y)
                min_path = [x] + c.get('seam')
                dict = {
                    'weight': weight,
                    'seam': min_path
                }
                self.mem[y][x] = dict
                return dict

    def run(self, image):
        weight = float("inf")
        max_x = len(image[0])
        self.seam = []
        self.mem = [[None for i in range(len(image[0]))] for j in range(len(image))]
        for i in range(max_x):
            dict = self.find_seam(image, i, 0)
            if dict.get('weight') < weight:
                weight = dict.get('weight')
                self.seam = dict.get('seam')

        return weight

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam


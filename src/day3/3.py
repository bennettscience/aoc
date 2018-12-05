import re

test = [
'#1 @ 1,3: 4x4',
'#2 @ 3,1: 4x4',
'#3 @ 5,5: 2x2'
]

# set the size of the fabric
SIZE = 1000

# Define the fabric
fabric = [[0 for i in range(SIZE)] for n in range(SIZE)]

# set the default overlap
overlap = 0

# create a set to hold each claim and it's overlaps
claims = set()

# Get the text as a list
with open('input.txt') as f:
    input = f.readlines()

# loop over each input
for i in range(len(input)):

    # use regex to get three capture groups: ID, position, size
    regex = r'^#(\d+)\s@\s(\d+\,\d+):\s(\d+x\d+)'
    claim = re.match(regex, input[i])

    # Use .group() method for Python < 3.6
    id = claim.group(1)

    # Find square position in the grid as integers
    pos = claim.group(2).split(',')
    pos[0] = int(pos[0])
    pos[1] = int(pos[1])

    # Find the size of the input as integers
    size = claim.group(3).split('x')
    size[0] = int(size[0])
    size[1] = int(size[1])

    # Set an X search range start and end index
    # start = position 0 (x position) and x_max (start + width)
    for x in range(pos[0], (pos[0] + size[0])):
        # Set an Y search range start and end index
        # start = position 0 (y position) and y_max (start + height)
        for y in range(pos[1], (pos[1] + size[1])):
            # count that square as used
            fabric[x][y] += 1;

# Take the /entire/ fabric now and loop width and height
for x in range(SIZE):
    for y in range(SIZE):
        # if that spot has n > 1, there is an overlap /somewhere/
        # the actual overlap doesn't matter.
        if fabric[x][y] > 1:
            overlap += 1
        elif fabric[x][y] == 1:
            print(fabric[x][y])

print('There are', overlap, 'overlaps.') # 113716

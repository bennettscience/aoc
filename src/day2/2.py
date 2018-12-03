# Part 1 test
test = [
'abcdef',
'bababc',
'abbcde',
'abcccd',
'aabcdd',
'abcdee',
'ababab'
]

# Part 2 test
test_ids = [
'abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz'
]

# Set globals
double = 0  # tally the double instances
triple = 0  # tally the triple instances
result = [] # store the result data (part 2)

# Turn the list item into a set for faster processing
def find_matches(string):

    # open a list to hold the results
    result = [];

    # turn the string into a set - no duplicates!
    unique = set(string)

    # Loop through each character in the string...
    for char in unique:

        # push the result as a tuple into the array along with the number of
        # occurances of that item.
        result.append((char, string.count(char)))

    return result

# Search two strings for character differences
def find_single_diff(a, b):

    # set a couple flags for position and the number of diffs.
    pos = None
    count = 0

    # Run a loop for each letter in string A (B is equal in length)
    for i in range(len(a)):

        # if the letter is different atthe current position
        if a[i] != b[i]:

            # count 1, store the position
            count +=1
            pos = i

            # If the count is more that 1, break the loop because that breaks
            # the rules of the puzzle.
            if count > 1:
                break

    # Sanitize the return
    if count > 1:
        return False
    if i ==  None:
        return False

    # Send the position and input strings back if a single difference is found.
    return (pos, a, b)

# Part 1 - look for n times a character occurs
# open the file and loop each line
with open('input.txt') as f:
    for item in f.readlines():

        # pass the string into the unique set functio
        res = find_matches(item)

        # Set the variables
        # This prevents multiple triggers if two doubls or two triples are
        # found in the same string.
        dblSet = False
        trplSet = False

        # For the response item...
        for obj in res:

            # If the tuple has a 2, score a point and set the flag.
            if obj[1] == 2:
                if not dblSet:
                    dblSet = True
                    double += 1

            # Do the same for a 3
            elif obj[1] == 3:
                if not trplSet:
                    trplSet = True
                    triple += 1

    # Print the product of the doubles and triples
    print(int(double) * int(triple))

# Part 2 - find a single different character in the list

# convert text to list
with open('input.txt') as f:
    content = f.readlines()

# remove the newline characters
content = [x.strip() for x in content]

# Loop each item and compare it to the next in the list.
for i in range(len(content)):
        for j in range(i + 1, len(content)):

            # Send the strings to check for a difference
            result = find_single_diff(content[i], content[j])

            # If there is a true result, print the array
            if result != False:
                print(result)

work = '/Users/hfrantisak/text-search/corpus'

# Read single text file
def chapter1():
    f = open(work + '/mobydick-chapter1.txt')
    lines = f.readlines()
    f.close
    for i, line in enumerate(lines):
        print lines[i]

# Read single text file, removing whitespace
def chapter2():
    with open(work + '/mobydick-chapter2.txt') as f:
        content = f.readlines()
    # Removes newline characters
    content = [line.rstrip('\n') for line in open(work + '/mobydick-chapter2.txt')]
    print content

# Read single text file, explicitly
def chapter3():
    with open(work + '/mobydick-chapter3.txt', 'r') as text:
        array = []
        for line in text:
            array.append(line)
    array = [ws.strip() for ws in array]
    print array

# Read single text file, concisely
def chapter4():
    with open(work + '/mobydick-chapter4.txt') as f:
        content = f.read().splitlines()
    print content
    # Alternative for conciseness
    print tuple(open(work + '/mobydick-chapter4.txt', 'r'))

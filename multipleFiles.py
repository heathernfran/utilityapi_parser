import os

work = '/Users/hfrantisak/text-search/corpus/'

# Reference answer
# https://stackoverflow.com/a/2936955/5989537
for root, dirs, files in os.walk(work):
    print files
    for ch in files:
        with open(work + ch) as f:
            content = f.read().splitlines()
            print content




# f = open(work, 'r')
# while True:
#     text = f.readline()
#     print text

# for line in open(work, 'r'):
#     print line

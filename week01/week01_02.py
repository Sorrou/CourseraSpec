import sys
num_steps = int(sys.argv[1])

row = '#'

list = []
for i in range(num_steps):
    list.append(i+1)
list.reverse()

for inx, b in enumerate(list):
    print(' ' * (b - 1) + row * (inx+1))


#import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    print(num_steps - i - 1)
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")

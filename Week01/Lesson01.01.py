import sys

digit_string = sys.argv[1]

a = 0
for i in digit_string:
    a += int(i)
print(a)



#import sys

print(sum([int(x) for x in sys.argv[1]]))

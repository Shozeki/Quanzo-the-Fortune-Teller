#Missing Root directory printing name of user
#Misisng better file pathing

table = {}
with open('/Users/shobunch/Downloads/CMSC_140/Quanzo-the-Fortune-Teller') as f:
    next(f)
    for line in f.readlines():
        line = line.strip().split(',')
        order = line[0]
        fortune = line[1]
        table[order]=fortune
order = input('Hello, I am Quanzo the Fortune Teller.\nTo hear your fortune type in the number day you were born on \n')

while order not in table:
    print('You tell lies, try again')
    order = input()
else:
    print('Your fortune is:',table[order])
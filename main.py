fMax = 100  # max number of floors
mSequence = []  # modified floor sequence for choosing the closest floor to the starting floor
fSequence = []  # floor sequence
trackUp = []    # list of floors to stop at on the way up
trackDown = []  # list of floors to stop at on the way down

n = int(input("Enter the length of the floor sequence: "))

for i in range(0, n):
    floor = int(input(str(i + 1) + ' - Enter the number of the floor you want to stop at: '))

    while floor < 0 or floor > fMax:
        floor = int(input("Incorrect floor number! Please, enter the number from the range 0 - 100: "))

    fSequence.append(floor)

sFloor = int(input('Enter the number of the starting floor: '))

while sFloor < 0 or sFloor > fMax:
    sFloor = input("Incorrect number of the starting floor! Please, enter the number from the range 0 - 100: ")

fSequence.sort()
print('\nThe elevator will stop on these floors: ' + str(fSequence))
print('The starting point of the elevator is: ' + str(sFloor) + '\n')


def getDirection():     # gets direction from starting floor and the closest floor to it
    for j in fSequence:
        mSequence.append(j - sFloor)

    if (min(mSequence) + sFloor) == sFloor:
        mSequence.remove(0)

    if min(mSequence) > 0:
        direction = 1
    else:
        direction = -1

    return direction


def goUp():     # prints out all the floors, which will the elevator stop on on the way up
    for j in fSequence:
        if j > sFloor:
            print(j)


def goDown():   # prints out all the floors, which will the elevator stop on on the way down
    for j in fSequence:
        if j < sFloor:
            trackDown.append(j)
            trackDown.sort(reverse=True)
    for k in trackDown:
        print(k)


print('Final elevator sequence:')

if getDirection() == 1:
    goUp()
    goDown()
else:
    goDown()
    goUp()

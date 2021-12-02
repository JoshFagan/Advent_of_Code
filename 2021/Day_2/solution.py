#!/usr/bin/python


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def first_half(course):
    # Calculate the horizontal position and depth you would have after following
    # the planned course.
    horiz_pos = 0
    depth = 0

    for i in range(len(course)):
        direction, amount = course[i].split(' ')
        amount = int(amount) 

        if direction == 'forward':
            # Forward X increases the horizontal position by X units.
            horiz_pos += amount
        elif direction == 'down':
            # Down X increases the depth by X units.
            depth += amount
        elif direction =='up':
            # Up X decreases the depth by X units. 
            depth -= amount

    # What do you get if you multiply your final horizontal position by your 
    # final depth?
    solution = horiz_pos*depth
    print('\nSolution for first half!')
    print('Product of depth and horizontal position: {}\n'.format(solution))


def second_half(course):
    # Using the new interpretation of the commands, calculate the horizontal 
    # position and depth you would have after following the planned course.
    horiz_pos = 0
    depth = 0
    aim = 0

    for i in range(len(course)):
        direction, amount = course[i].split(' ')
        amount = int(amount) 
        if direction == 'forward':
            # Forward X does two things:
            # It increases your horizontal position by X units.
            horiz_pos += amount
            # It increases your depth by your aim multiplied by X.
            depth += (aim * amount)
        elif direction == 'down':
            # Down X increases your aim by X units.
            aim += amount
        elif direction =='up':
            # Up X decreases your aim by X units.
            aim -= amount

    # What do you get if you multiply your final horizontal position by your 
    # final depth?
    solution = horiz_pos*depth
    print('Solution for second half!')
    print('Product of depth and horizontal position: {}\n'.format(solution))


def main():
    course = load_data() 
    first_half(course)
    second_half(course)


if __name__ == '__main__':
    main()

#!/usr/bin/python


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()
    contents = [int(content) for content in contents]

    return contents 


def first_half(depths):
    # Count the number of times a depth measurement increases from the previous 
    # measurement.
    incs = [depths[i-1] < depths[i] for i in range(1,len(depths))]

    # How many measurements are larger than the previous measurement?
    solution = sum(incs)
    print('\nSolution for first half!')
    print('Number of increasing measurements: {}\n'.format(solution))


def second_half(depths):
    # Count the number of times a depth measurement increases from the previous 
    # measurement considering sums of a three-measurement sliding window.
    windows = [depths[i-2] + depths[i-1] + depths[i] 
               for i in range(2,len(depths))]
    incs = [windows[i-1] < windows[i] for i in range(1,len(windows))]
    
    # How many measurements are larger than the previous measurement?
    solution = sum(incs)
    print('Solution for second half!')
    print('Number of increasing measurements: {}\n'.format(solution))


def main():
    depths = load_data() 
    first_half(depths)
    second_half(depths)


if __name__ == '__main__':
    main()

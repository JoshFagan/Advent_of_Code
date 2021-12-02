#!/usr/bin/python


def load_data():
    # Read contents of file
    my_file = open('depth_measurement_data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()
    contents = [int(content) for content in contents]

    return contents 


def first_half(depths):
    incs = [depths[i-1] < depths[i] for i in range(1,len(depths))]

    print('\nSolution for first half!')
    print('Number of increasing measurements: {}\n'.format(sum(incs)))


def second_half(depths):
    windows = [depths[i-2] + depths[i-1] + depths[i] for i in range(2,len(depths))]
    incs = [windows[i-1] < windows[i] for i in range(1,len(windows))]
    
    print('Solution for second half!')
    print('Number of increasing measurements: {}\n'.format(sum(incs)))


def main():
    depths = load_data() 
    first_half(depths)
    second_half(depths)


if __name__ == '__main__':
    main()

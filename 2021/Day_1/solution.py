#!/usr/bin/python


def load_data():
    # Read contents of file
    my_file = open('depth_measurement_data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()
    contents = [int(content) for content in contents]

    return contents 


def main():
    depths = load_data() 
    
    diffs = [depths[i-1] < depths[i] for i in range(1,len(depths))]

    print('Number of increasing measurements: {}'.format(sum(diffs)))


if __name__ == '__main__':
    main()

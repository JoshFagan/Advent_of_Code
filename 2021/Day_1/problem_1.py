#!/usr/bin/python


def main():
    # Read contents of file
    my_file = open('depth_measurement_data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()
    depths = [int(content) for content in contents]


if __name__ == '__main__':
    main()

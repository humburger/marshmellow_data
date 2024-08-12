'''
used as external functions

reads data from file by lines and saves as simple array
'''

def read_file_to_array(directory, name):
    # directory = "C:\\Users\\User\\Downloads\\marshmellows_scripts\\mysql_to_excel\\"
    # directory = "C:\\Users\\User\\Downloads\\marshmellows_scripts\\konkrēta suga\\input"

    # some indicator, that if there was not ever opened file,
    # then it is not needed to close that
    file_not_found = False
    in_data = []

    try:
        f = open(directory + name, "r")

        while(1):

            line = f.readline()

            if not line: # if there is no new line to read, then cycle ends
                break
            in_data.append(line.strip())

        # data testing
        # for value in in_data:
        #     print(value)

    except FileNotFoundError as not_found_err:
        file_not_found = True
        print(not_found_err)

    finally:
        if file_not_found == False:
            f.close()
    return in_data


"""
array string is prepared for MySQL 'IN' bracket values
"""
# returns string value
def create_str_list(arr):
    result = ""
    for str in arr:
        if str == arr[0]:
            result = "'" + str + "'"
        else:
            result = result + ", '" + str + "'"
    return result


# read_file_to_array()
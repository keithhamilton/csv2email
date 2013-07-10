from re import search

def parse(filepath):
    name_email_dictionary = {}
    
    f = open(filepath,'r')
    
    for line in f.readlines():
        # remove newline char
        line.replace('\n','')
        # split at comma
        line_split = line.split(',')
        # firstName = zero-index
        # email = first-index
        if search('@',line_split[0]):
            name_email_dictionary[line_split[0]] = line_split[1]
        elif search('@', line_split[1]):
             name_email_dictionary[line_split[1]] = line_split[0]
        else:
            print('email address not found in {0}'.format(line))

    f.close()

    return name_email_dictionary

import os
name_of_file = 'C:\\Users\\daria\\progy\\data.txt'
total_number = 0

def Sequence(filename):
    file = open(filename, 'r')
    try:
        if (os.stat(filename).st_size == 0):
            return -1
    except OSError:
        print("File does not exist")
    temp_max = 0
    for line in file:
        length = len(line)
        if (line == ''):
            print("len is")
        prev_integer = ''
        index = 0
        flag = 0
        f = 0
        while (flag != 1):
            if (line[index] != ' '):
                prev_integer += line[index]
            if (line[index] == ' ') or (index == (length -1)):
                flag += 1
            index += 1
        prev_integer = int(prev_integer)
        integer = ''
        for i in range(index,length):
            if (line[i] != ' '):
                integer += line[i]
            if ((line[i] == ' ') or (i == (length - 1))):
                integer = int(integer)
                if (int(integer) == int(prev_integer)):
                    if(f==0):
                        temp_max = temp_max+2
                        f=1
                    elif  (f == 1):
                        temp_max += 1
                if ((int(integer) != int(prev_integer)) or ((int(integer) == int(prev_integer)) and i == length - 1)):
                    f=0        
                prev_integer = integer
                integer = ''
    return temp_max


total_number = Sequence(name_of_file)

if (total_number == 0):
    print("total number is 0")
elif (total_number > 0):
    print("total number is", total_number)
elif (total_number == -1):
    print("File is empty")
                

import json
import os

dir = os.getcwd()


def read_file(file_name):
    with open(dir + "/" + file_name, 'r') as file:
        data = json.load(file)
    return data


def compare_data(file_data1, file_data2, name):
    s = list()
    for value in range(len(file_data1)):
        for value2 in range(len(file_data2)):
            if file_data1[value]['id'] == file_data2[value2]['id']:
                for keys in file_data2[value2]:
                    if keys != 'id' and \
                            file_data1[value][keys] != file_data2[value2][keys]:
                        s.append("ID=" + file_data1[value]['id'] + ","
                                 + keys.upper()
                                 + " MISMATCH - " + file_data1[value][keys]
                                 + " / " + file_data2[value2][keys] + "\n")
        if file_data1[value]['id'] not in str(file_data2):
            s.append("ID=" + file_data1[value]['id'] + ", RECORD MISSING IN " + name + '\n')
    return s


def write_file(data):
    with open(dir + "/output.csv", 'w') as d:
        d.write("MISMATCH SUMMARY:\n")
        d.writelines(data)


data1 = read_file("value1.json")
data2 = read_file("value2.json")
if len(data1) >= len(data2):
    outputData = compare_data(data1['menu'], data2['menu'], 'JSON 2')
else:
    outputData = compare_data(data2['menu'], data1['menu'], 'JSON 1')
write_file(outputData)

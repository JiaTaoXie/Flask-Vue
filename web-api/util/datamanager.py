import json

gData = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]


def formNumber():
    data2 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
    return data2



def getData(fileName):
    fo = open(fileName, "r")
    # print ("文件名为: ", fo.name)
    # print(fo.read())
    return fo.read()
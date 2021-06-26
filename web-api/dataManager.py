import json


# # gData = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

# def formNumber():
#     data2 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
#     return data2



def errorCode():
    return json.dumps({'code':400,'msg':"token is expried."})

# 打开文件
fo = open("urlData/login.json", "r")
print ("文件名为: ", fo.name)

print(fo.read())
 
# for line in fo.readlines():                          #依次读取每行  
#     line = line.strip()                             #去掉每行头尾空白  
#     print ("读取的数据为: %s" % (line))
 
# 关闭文件
fo.close()
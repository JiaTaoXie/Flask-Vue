import server
from util import datamanager
# import util.datamanager


print("data:",datamanager.formNumber())

# 启动程序
if __name__ == '__main__':
    server.run()
    # app.run('0.0.0.0', debug=True, port=8100)
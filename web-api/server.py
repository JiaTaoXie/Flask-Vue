from flask import Flask
from flask import request
import json
from util import pubutil
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 定义路由以及试图函数
# 定义路由，是用装饰器实现的
# 路由默认只支持GET，如果需要增加，需要自行制定
@app.route('/', methods=["GET", "POST"])
def hello_world():
    data = pubutil.getData("urlData/login.json")
    return data

@app.route('/ping', methods=["GET", "POST"])
def deal_ping():
    data = "this is ping operation"
    return data

@app.route("/deal_info", methods=['POST'])
def deal_get_info():

    if request.method == 'POST':
        request_data = request.get_data().decode('utf-8')
        print("传入的数据是：",request_data)
        # 解析json前进行编码.不然出来的结果并不是中文的..
        print(type(request_data))
        print(request_data)
        print(json.loads(request_data))
        return 'deal_info'

@app.route("/login", methods=['POST'])
def deal_get_login():
    if request.method == 'POST':
        request_data = request.get_data().decode('utf-8')
        print("传入的数据是：",request_data)
        # 解析json前进行编码.不然出来的结果并不是中文的..
        print(type(request_data))
        print(request_data)
        print(json.loads(request_data))
        return 'this is login func back'

def run():
    app.run('0.0.0.0', debug=True, port=8100)


# # 启动程序
# if __name__ == '__main__':
#     app.run('0.0.0.0', debug=True, port=8100)

import socket
import json

def floor(x):
    return int(x)

def nroot(n, x):
    return x**(1/n)

def reverse(s):
    return s[::-1]

def validAnagram(s1, s2):
    return sorted(s1) == sorted(s2)

def sort(strArr):
    return sorted(strArr)

def process_request(request):
    method = request['method']
    params = request['params']

    # 各メソッドに対する処理を行う
    if method == 'floor':
        return floor(*params)
    elif method == 'nroot':
        return nroot(*params)
    elif method == 'reverse':
        return reverse(*params)
    elif method == 'validAnagram':
        return validAnagram(*params)
    elif method == 'sort':
        return sort(*params)
    else:
        return None

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    # 接続の確立
    while True:
        connection, client_address = s.accept()
        try:
            print('connection from', client_address)
            # データ読み込み
            data = connection.recv(4096)
            # JSONを構造に入れる
            request = json.loads(data.decode('utf-8'))

            if data:
                # リクエストを処理し、結果を取得
                result = process_request(request)
                # レスポンスの中身作成
                response = {
                    "result": result,
                    "result_type": type(result).__name__,
                    "id": request['id']
                }
                # データ送信
                connection.sendall(json.dumps(response).encode('utf-8'))
            else:
                print('no data from', client_address)
                break
        finally:
            print('Closing current connection')
            connection.close()

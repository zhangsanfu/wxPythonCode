from wsgiref.simple_server import make_server

def application(environ,start_response):

    start_response('200 OK',[('Content-Type','text/temples')])
    path = environ.get('PATH_INFO')
    print(path)

    if path == '/login':
        with open('./temples/login.temples','rb') as f:
            fdata = f.read()
    # 在用户指定浏览器发出请求后，会请求目标路径，但浏览器自己还会请求/favicon.ico路径，此时返回一个图标文件，将应用于网页标签的图标，一般在网页的head中查找icon
    elif path == '/favicon.ico':
        with open('./images/favicon.ico','rb') as f:
            fdata = f.read()
    else:
        with open('./temples/index.temples','rb') as f:
            fdata = f.read()
    return [fdata]

httped = make_server('',8805,application)

httped.serve_forever()
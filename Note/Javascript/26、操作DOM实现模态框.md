操作DOM实现模态框

**模态框：**点击按钮后，弹出的一个窗口，如点击登录按钮，在页面中弹出登录窗口（盒子）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        *{
            padding: 0;
            margin: 0;
        }
        #btn{
            float: left;
            position: absolute;
            z-index: 1;
        }
        #bgc{
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.3);
            position: absolute;
            top: 0;
            left: 0;
        }
        #login{
            width: 400px;
            height: 400px;
            background-color: white;
            margin: 0 auto;
            position: relative;
        }
        #close{
            width: 20px;
            height: 20px;
            background-color: aqua;
            color:red;
            text-align: center;
            line-height: 20px;
            position: absolute;
            right: 0;
            top: 0;
        }
    </style>
</head>
<body>
    <button id="btn">登录</button>
    <script type="text/javascript">
        function $(id){
            return document.getElementById(id);
        };
        
        var bgc = document.createElement('div');
        bgc.id = 'bgc';

        var login = document.createElement('div');
        login.id = 'login';

        var close = document.createElement('div');
        close.id = 'close';

        var form = document.createElement('form');
        form.id = 'register';
        
        //将背景图标签对象添加在按钮父级的子级，也就是与按钮同一层级
        $('btn').parentNode.appendChild(bgc);

        $('btn').onclick = function(){
                $('bgc').appendChild(login);
                $('login').appendChild(form);
                form.innerHTML = '<label for="username">用户名：</label> <input type="text" name="username" value="请输入用户名"/>';
                $('login').appendChild(close);
                close.innerText = 'X';

            $('close').onclick = function(){
                this.parentNode.parentNode.removeChild($('login'));
             };
        };
    </script>
</body>
</html>
```


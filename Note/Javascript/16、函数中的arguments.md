函数中的arguments

没有形参接收实参，但是在函数中通过arguments获取到函数的参数,arguments的作用域是在函数中

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script type="text/javascript">
        // 没有形参接收实参，但是在函数中通过arguments获取到函数的参数,arguments的作用域是在函数中
        function add(){
            console.log(arguments);
            for(var i = 0; i < arguments.length; i++){
            console.log(arguments[i])
        }
        }
        add(2,3);
    </script>
</body>
</html>
```


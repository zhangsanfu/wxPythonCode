TAB栏的选项卡

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
        .box{
            width:480px;
            height: 200px;
            background-color: red;
            margin: 50px auto 0px;
            text-align: center;
            line-height: 150px;
        }
        ul{
            list-style: none;
        }
        ul li{
            float: left;
            width: 160px;
            height: 50px;
        }
        ul li a{
            display: block;
            text-decoration: none;
            text-align: center;
            line-height: 50px;
            color: black;
        }
        .active{
            display: block;
            background-color: #ccc;
        }
        p{
            display: none;
        }
    </style>
</head>
<body>
    <div class="box">
        <ul>
            <li class="active">
                <a href="#">首页</a>
            </li>
            <li>
                <a href="#">新闻</a>
            </li>
            <li>
                <a href="#">图片</a>
            </li>
        </ul>
        <div>
            <p style = 'display:block;'>首页内容</p>
            <p>新闻内容</p>
            <p>图片内容</p>
        </div>
    </div>
    <script type="text/javascript">
        var tablis = document.getElementsByTagName('li');
        var ps = document.getElementsByTagName('p');
        for(var i = 0; i < tablis.length; i++){
            // 在for循环i的最终值没有变为3前，将每一次的i值赋值给对象的一个变量
            tablis[i].index = i;
            tablis[i].onclick = function(){
                for(var j=0; j < tablis.length; j++){
                    tablis[j].className = '';
                    ps[j].style.display = 'none';
                }
                this.className = 'active';
                // 如果使用ps[i]，在for循环时，i的最终值已经变成了3，所以一直为ps[3]
                ps[this.index].style.display = 'block';
            }
        }
    </script>
</body>
</html>
```



在es6中，使用let定义变量，它的作用域只在{...}中

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
        .box{
            width:480px;
            height: 200px;
            background-color: red;
            margin: 50px auto 0px;
            text-align: center;
            line-height: 150px;
        }
        ul{
            list-style: none;
        }
        ul li{
            float: left;
            width: 160px;
            height: 50px;
        }
        ul li a{
            display: block;
            text-decoration: none;
            text-align: center;
            line-height: 50px;
            color: black;
        }
        .active{
            display: block;
            background-color: #ccc;
        }
        p{
            display: none;
        }
    </style>
</head>
<body>
    <div class="box">
        <ul>
            <li class="active">
                <a href="#">首页</a>
            </li>
            <li>
                <a href="#">新闻</a>
            </li>
            <li>
                <a href="#">图片</a>
            </li>
        </ul>
        <div>
            <p style = 'display:block;'>首页内容</p>
            <p>新闻内容</p>
            <p>图片内容</p>
        </div>
    </div>
    <script type="text/javascript">
        var tablis = document.getElementsByTagName('li');
        var ps = document.getElementsByTagName('p');
        // 在es6中使用let定义变量，就不会在for循环时，直接将i变为最终值3，点击第几个元素i就是几
        for(let i = 0; i < tablis.length; i++){
            tablis[i].index = i;
            tablis[i].onclick = function(){
                for(var j=0; j < tablis.length; j++){
                    tablis[j].className = '';
                    ps[j].style.display = 'none';
                }
                this.className = 'active';
                console.log(i);
                ps[i].style.display = 'block';
            }
        }
    </script>
</body>
</html>
```


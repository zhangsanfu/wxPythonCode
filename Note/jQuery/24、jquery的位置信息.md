jquery的位置信息

获取、设置宽，jquery对象**.width(x)**

获取、设置高，jquery对象**.height(x)**



获取、设置，jquery对象**.innerWidth(x)**

获取、设置，jquery对象**.innerHeight(x)**



获取、设置，jquery对象**.outerWidth(x)**

获取、设置，jquery对象**.outerHeight(x)**



获取偏移量，jquery对象**.offset()**

获取偏移高度，jquery对象**.offset().top**

获取偏移宽度，jquery对象**.offset().left**



获取滚动量，jquery对象.scroll()，滚动条滚动所触发的事件

获取、设置距离顶部的滚动量，jquery对象**.scrollTop(x)**

获取、设置距离左边的滚动量，jquery对象**.scrollLeft(x)**



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
        body{
            height: 2000px;
        }
        .box{
            width: 100px;
            height: 100px;
            border: 1px solid red;
            padding: 10px;
            position: absolute;
            top: 50px;
            left: 200px;
        }
    </style>
</head>
<body>
    <div class="box"></div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 输出100，100，通过盒子的jquery对象获取盒子的宽高
        console.log($('.box').width());
        console.log($('.box').height());
        
        // 通过盒子的jquery对象设置盒子的宽高
        $('.box').width(500);
        $('.box').height(500);

        // 输出120,120，通过盒子的jquery对象获取盒子内部宽高，内容区域 + padding
        console.log($('.box').innerWidth());
        console.log($('.box').innerHeight());
        
        // 通过盒子的jquery对象设置盒子内部宽高
        $('.box').innerWidth(300);
        $('.box').innerHeight(300);

        // 输出122,122，通过盒子的jquery对象获取盒子外部宽高，内容区域 + padding + border
        console.log($('.box').outerWidth());
        console.log($('.box').outerHeight());
		
        // 通过盒子的jquery对象设置盒子外部宽高
        $('.box').outerWidth(600)
        $('.box').outerHeight(600)
        
        // 输出{top: 50, left: 200}，盒子的偏移量
        console.log($('.box').offset());
        // 单独打印距离顶部的偏移量，只读属性，不能设置
        console.log($('.box').offset().top);
        // 单独打印距离左边的偏移量，只读属性，不能设置
        console.log($('.box').offset().left);
        
        // 直接设置滚动条的位置，距离顶部1000px
        $(document).scrollTop(1000);
        // jquery中滚动页面触发的事件，在JS中是onScroll
        $(document).scroll(function(){
            // console.log($(this).scrollLeft());
            // 如果滚动条滚动的高度大于50，那么就在1秒内隐藏盒子，反之亦然
            if($(this).scrollTop() > 50){
                console.log('scrollTop' + $(this).scrollTop());
                console.log('offset' + $('.box').offset().top);
                $('.box').hide(1000);
            }else{
                $('.box').show(1000);
            }
        });


    </script>
</body>
</html>
```


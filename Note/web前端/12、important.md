！important

**总结：**

1、**当选择器都为选中标签时**，在权重比例低的样式添加！important，使权重比例变为最大

2、如果选择器一个选中，一个继承，此时肯定是选中状态的权重比例比未选中的选择器权重比例大，如果在未选中的样式中添加！important，那么它的权重仍然小于选中标签的选择器，无效

3、如果选择器都是继承的，以哪个描述的更精确、更近为准，如果此时在描述不精确的选择器中添加！important，是无效的

所以可以总结为，在选择器都为选中标签层级的状态时，！important才生效

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        /* 当选择器都为选中标签时，权重比例低的样式添加！important，使权重比例最大*/
        .wrap .box #innerbox{
            width: 100px;
            height: 100px;
            color: red  !important;
        }
        .wrap #box #innerbox{
            width: 100px;
            height: 100px;
            color: blue;
        }

        /* 如果选择器一个选中，一个继承，此时肯定是选中状态的权重比例比未选中的选择器权重比例大，如果在未选中的样式中添加！important，那么它的权重仍然小于选中标签的选择器，无效 */
        .wrap .box #innerbox{
            width: 100px;
            height: 100px;
            color: red;
        }
        .wrap #box{
            width: 100px;
            height: 100px;
            color: blue !important;
        }

        /* 如果选择器都是继承的，以哪个描述的更精确、更近为准，如果此时添加！important，是无效的 */
        .wrap #box{
            width: 100px;
            height: 100px;
            color: red !important;
        }
        .wrap .box #innerbox{
            width: 100px;
            height: 100px;
            color: blue;
        }
    </style>
</head>
<body>
    <div class="wrap">
        <div class="box" id="box">
            <div id="innerbox">
                <p>这是一个盒子</p>
            </div>
        </div>
    </div>
</body>
</html>
```


bootstrap翻页控件

`pagination`类，美 /,pædʒɪ'neʃən/ 标记页数；页码 。在ul层级，标记页数；页码。可以将列表横向变为翻页控件

`pagination-lg`类，在ul层级，可以将翻页控件整体变大显示

`pagination-sm`类，将翻页控件整体缩小显示

`pager`类：ul层级，可更快、更简单使li->a变为翻页按钮

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./bootstrap-3.3.7/css/bootstrap.css">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-4">
            <!-- 翻页控件，将分页组件包含在.nav类名中，页面中可能包含多个nav，所以使用 aria-label属性，为导航增加描述信息-->
                <nav aria-label="Page navigation">
                    <!-- pagination类表示将列表横向展示为翻页控件，pagination-lg将翻页控件放大显示，pagination-sm将翻页控件缩小显示 -->
                    <ul class="pagination pagination-lg">
                        <li>
                        <a href="#" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                        </a>
                        </li>
                        <!-- 添加class="disabled"类，可使当前翻页链接不可用 -->
                        <li class="disabled"><a href="#">1</a></li>
                        <li><a href="#">2</a></li>
                        <li><a href="#">3</a></li>
                        <li><a href="#">4</a></li>
                        <li><a href="#">5</a></li>
                        <li>
                        <a href="#" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                        </a>
                        </li>
                    </ul>
                </nav>
        </div>
            <div class="col-md-4">
                <!-- 超简单的翻页控件，ul继承于pager类后，将修改li->a的样式，变为翻页按钮 -->
                <nav>
                    <ul class="pager">
                        <li>
                            <a href="">previous</a>
                        </li>
                        <li>
                            <a href="">next</a>
                        </li>
                    </ul>
                </nav>
        </div>
    </div>
</body>
</html>
```


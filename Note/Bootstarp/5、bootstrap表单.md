bootstarp表单

`form-group`类：表单包裹在该类下可以得到最好排列

`form-control`类：添加了form-control类的`input`、`textarea`、`select`都会被附加width：100%的样式

`checkbox`类：将`type = "checkbox"`的`input`标签放置在`label`中，可以将文字和复选框放在一行中显示

`btn-info`、`btn-warning`、`btn-success`、`btn-danger`、`btn-active`类：为按钮添加颜色样式

`form-inline`类：将form中所有的控件在一行中显示

`disabled = "disabled"`属性：将文本框设置为禁用

`readonly`属性：设置文本框为只读状态

`has-success`、`has-warning`、`has-error`类，在控件所在盒子添加类，使控件颜色改变

`form-horizontal`：美 /'hɔrə'zɑntl/  水平的，将表单的label和input控件在一行中显示

`input-lg`、`input-sm`：调整input控件的高度

将组件图标类，放置在span标签中，展示图标图片

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./bootstrap-3.3.7/css/bootstrap.css">
    <style type="text/css">
        .thumbnail{
            height: 336px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- <div class="row"> -->
            <div class="col-md-8">
                <div class="thumbnail">
                    <form action="" >
                        <!-- 将表单控件包裹在form-group类下，可以得到最好的排列 -->
                        <div class="form-group">
                            <label for="username" class="col-md-2 control-label">用户名</label>
              <!-- 添加了from-control类的input、textarea、select都会被附加width：100%的样式 -->
                            <input type="text" class="form-control" name="username" placeholder="请输入用户名">
                        </div>
                        <div class="form-group">
                            <label for="pwd">密码</label>
                            <input type="password" class="form-control" name="pwd" placeholder="请输入密码">
                        </div>
                        <div class="form-group">
                            <label for="upload">上传文件</label>
                            <input type="file">
                        </div>
              <!--对于checkbox，添加checkbox类，以及将input放置在label中，可以将其放在一行中显示 -->
                        <div class="checkbox">
                            <label for="">
                                <input type="checkbox">同意协议
                            </label>
                        </div>
                        <div class="form-group">
                            <!-- 和表格一样，表单中的控件也支持这5个属性，区别是按钮的颜色不同 -->
                            <!-- btn-lg大、btn-sm小、btn-xs超级小分别设置按钮的大小样式 -->
                            <input type="submit" class="btn-default btn-lg">
                            <input type="submit" class="btn-info btn-sm">
                            <input type="submit" class="btn-warning btn-xs">
                            <input type="submit" class="btn-danger">
                            <input type="submit" class="btn-success">
                            <input type="submit" class="btn-active">
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-8">
                <!-- 在form标签添加form-inline，将form中所有的控件在一行中显示 -->
                <!-- 最初发现所有的控件并没有在一行中显示，是因为将form-group写为了from-group -->
                <form class="form-inline">
                    <div class="form-group">
                        <label for="username">Name</label>
                        <input type="text" class="form-control" id="username"  placeholder="请输入用户名">
                    </div>
                    <div class="form-group">
                        <label for="password">密码</label>
                        <input type="password" class="form-control" placeholder="请输入密码">
                    </div>
                    <!-- 按钮添加btn 和 btn-default样式 -->
                    <button class="btn btn-default">nihaop</button>
                </form>

                <form class="form-inline">
                    <div class="form-group">
                        <label for="exampleInputName2">Name</label>
                        <input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
                    </div>
                    <div class="form-group">
                        <label for="exampleInputEmail2">Email</label>
                        <input type="email" class="form-control" id="exampleInputEmail2" placeholder="jane.doe@example.com">
                    </div>
                    <button type="submit" class="btn btn-default">Send invitation</button>
                </form>
            </div>
        </div>
        <!-- form-horizontal类  美 /'hɔrə'zɑntl/  水平的，结合label的col-sm-2，以及input所在盒子的col-sm-10，将label和input放置在一行显示 -->
        <form action="" class="form-horizontal">
            <div class="form-group ">
                <label for="" class="col-sm-2 control-label">用户名</label>
                <div class="col-sm-10 form-group-lg">
                    <!-- disabled属性将文本框设置为禁用 -->
                    <input type="text" placeholder="请输入用户名" disabled>
                    <!-- readonly设置文本框为只读状态 -->
                    <input type="text" placeholder="请输入密码" readonly>
                </div>
            </div>
        </form>
        <div class="row">
            <div class="col-md-3">
                <div class="thumbnail">
               <!-- 在控件所在盒子添加has-success,has-warning、has-error校验类，使其控件颜色改变 -->
                    <div class="form-group has-success">
                        <label for="">用户名</label>
                        <!-- 通过input-lg和input-sm类，改变input的高度 -->
                        <input type="text" class="form-control input-sm" placeholder="请输入用户名">
                    </div>
                    <div class="form-group has-warning">
                        <label for="">用户名</label>
                        <input type="text" class="form-control input-lg" placeholder="请输入用户名">
                    </div>
                    <div class="form-group has-error">
                        <label for="">用户名</label>
                        <input type="text" class="form-control" placeholder="请输入用户名">
                    </div>
                    <!-- 在checkbox所在盒子添加校验状态类，也会为其添加颜色 -->
                    <div class="checkbox has-success">
                        <label for="">
                            <input type="checkbox">同意协议
                        </label>
                    </div>
                    <div class="checkbox has-warning">
                        <!-- 在页面中添加组件图标，将图片的类名写在span标签中 -->
                        <div>
                            <span class="glyphicon glyphicon-file"></span>
                        </div>
                        <label for="">
                            <input type="checkbox">同意协议
                        </label>
                    </div>
                    <div class="checkbox has-error">
                        <label for="">
                            <input type="checkbox">同意协议
                        </label>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</body>
</html>
```




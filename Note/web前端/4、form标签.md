form表单标签的属性

```html
action：提交表单，填写服务器的地址，提交给后台

method

get:最大为2KB，明文提交
参数都显示在URL中
https://www.baidu.com/?username=&password=&sex=on&hobbies=on&introduction=

post：隐式提交，无大小限制，安全性高

enctype

1、编码类型
2、取值，application/x-www-form-urlencoded，允许将普通、特殊字符提交给服务器，不允许提交文件
3、上传文件时配合post方法+multipart/form-data，允许提交文件
4、text/plain，只允许提交普通字符
```



```html
表单控件分类：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- form标签 块级元素 -->
    <div class="form">
        <!-- 点击类型为submit的按钮后，将提交到action所指定的服务端，请求类型为get -->
        <form action="https://www.baidu.com" method="GET">
            <p>
                <!-- label行内元素，关联表单字段文本与表单元素，点击表单字段相当于点击表单控件 -->
                <!-- 一般添加for属性，与input标签的id相关联，可以用value设置字段默认值 -->
                <label for="user">用户名</label>
                <!-- text类型表示输入的文本内容，，服务端会用到,placeholder表示默认显示的占位符 -->
                <!-- value表示字段显示的默认值 -->
                <!-- name表示控件名称，显示在提交表单后的url中，如username=wangxin&password=123 -->
                <input type="text" name="username" id="user" placeholder="请输入用户名" value="wangxin">
            </p>
            <p>
                <label for="password">密码</label>
                <!-- password类型标识密文显示输入的密码 -->
                <input type="password" name="password" id="password" placeholder="请输入密码">
            </p>
            <p>
                性别：
                <!-- 如果要产生2选1的效果，那么name参数的值必须一致，value是在submit后提交给服务端的参数值 -->
                <input type="radio" name="sex" value="男" checked>男
                <input type="radio" name="sex" value="女">女
            </p>
            <p>
                爱好：
                <!-- 类型为checkbox，多选，name的值设置为一样，在后端取值时会很方便 -->
                <!-- 写上name值后，就可以在submit后显示在URL中作为变量名，value属性则会作为参数值，如&checkfav=吃&checkfav=喝&checkfav=玩 -->
                <input type="checkbox" name="checkfav" value="吃" checked>吃 
                <input type="checkbox" name="checkfav" value="喝">喝 
                <input type="checkbox" name="checkfav" value="玩">玩 
                <input type="checkbox" name="checkfav" value="乐">乐 
            </p>
            <p>
                <!-- 类型为file，上传文件 -->
                <input type="file" name="textFile" id="upload">
            </p>
            <p>
                <!-- 下拉列表，select都是和option配合，添加size后由下拉列表变为滚动列表，表示同时显示几个下拉菜单选项-->
                <!--添加multiple表示允许多选,按住ctrl后点击选项，被多选 -->
                <select name="address" size="3" multiple="">
                    <!-- selected表示默认被选中 -->
                    <option value="深圳" selected>深圳</option>
                    <option value="北京">北京</option>
                    <option value="山东">山东</option>
                    <option value="杭州">杭州</option>
                </select>
            </p>
            <p>
                <!-- 文本域 -->
                <textarea cols="60" rows="5" name="selfintroduction" placeholder="自我介绍..."></textarea>
            </p>
            <p>
                <!-- 普通按钮，类型button，value表示按钮名称，仅仅是显示一个按钮，disable出现在标签中将禁用控件 -->
                <input type="button" name="btn" value="提交" disabled>
                <!-- 重置按钮 -->
                <input type="reset" name="">
                <!-- 提交按钮，类型submit，将表单内容提交至服务端 -->
                <input type="submit" name="btn" value="submit">
            </p>
        </form>
    </div>
</body>
</html>
```


math内置对象

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
        // 都是使用Math.开头
        // 1、向上取整，天花板函数，无论小数点是多少，直接向整数位进位
        var x = 1.2315;
        var a = Math.ceil(x);

        // 输出2，没有四舍五入的关系，直接向上取整
        console.log(a);

        // 用途：分页
        var x = 12345/30;

        // 实际结果411.5，得到结果412，实际分页结果为412页
        console.log(Math.ceil(x));

        // 2、向下取整，地板函数，取整数位，结果为1
        console.log(Math.floor(1.24125));

        // 3、求两个数的最大值和最小值
        console.log(Math.max(2,5,1,6));
        console.log(Math.min(2,5,1,6));

        // 4、随机值，输出0~1之间的随机数
        console.log(Math.random());

        // 取范围内的随机值，公式min + Math.random()*(Max-Min)
        // 逻辑是Math.random()*(300-200)表示100以内的随机值，最后再加上200，结果就是200 + （0~100），实则就是200~300之间的随机值
        console.log(200 + Math.random()*(300-200));
    </script>
</body>
</html>
```


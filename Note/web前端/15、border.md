**border**

**solid**   美 /'sɑlɪd/  实线

**dotted**   美 /'dɑtɪd/   点缀，圆点组成

**double** 双实线

**dashed**   美 /dæʃt/    虚线

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        .box{
            width: 300px;
            height: 500px;

            /* border默认总体设置三要素：粗细、线型、颜色 */
            border:5px solid red;
            
            /* 单独设置border的三要素 */
            /* 单独设置border的宽度，方向按照上、右、下、左依次设置 */
            border-width: 5px 10px 15px 20px;

            /* 单独设置border的线型，方向按照上右下左 */
            border-style: solid dotted double dashed;

            /* 单独设置border的颜色，方向按照上右下左 */
            border-color: red,green,blue,yellow;

            /* 按照方向设置border的上边框 */
            border-top-width:5px;
            border-top-style: double;
            border-top-color: red; 

            /* 表示设置上边框不设置任何属性，显示为空 */
            border-top:none;
            border-top:0;

            /* 线型不设置粗细，默认不显示边框 */
            /* 线型不设置颜色，默认显示为黑色 */

        }
    </style>
</head>
<body>
    <div class="box">

    </div>
</body>
</html>
```



**通过border制作小三角**

transparent   美 /træns'pærənt/    透明的；显然的；易懂的

原理是设置盒子的宽高位0px，并设置top、left、right的border为30px，左右border颜色为transparent

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

    <style type="text/css">
        .box{
            width: 0px;
            height: 0px;
            /* 变动边框，调整三角形方向 */
            border-top:30px solid red;
            border-left:30px solid transparent;
            border-right:30px solid transparent;
        }
    </style>
</head>
<body>
    <div class="box">

    </div>
</body>
</html>
```


forms组件

forms组件的作用是，引入`from django import forms`后，创建校验类，定义每个字段的规则，每一个字段的变量名与post请求中form表单的`name`相互匹配

```python
class UserForm(forms.Form):
    # 定义的所有变量必须和HTML的form表单中的name匹配，才会去进行验证，如username匹配form表单中name=username的用户名字段;min_length表示最小长度
    # 添加label参数，可在form表单中通过form对象.变量名.label读取出字段的名称
    username=forms.CharField(min_length=4,label='用户名')
    password=forms.CharField(min_length=4,label='密码')
    email=forms.EmailField()
```



在视图函数中根据定义的`UserForm({key:value,})`类传入指定参数实例化对象，或直接传入`request.POST`请求的内容`UserForm(request.POST)`，实例化后的`form`对象会根据`is_valid`方法判断参数是否校验成功，返回`True`和`False`，

- 如果校验成功，那么所有的字段以字典的形式存储在`form.cleaned_data`中
- 如果校验失败，那么正确的内容依然会存储在`form.cleaned_data`中，但是校验错误的字段会存储在`form.errors`中，形式为`key:[错误信息]`

**重点：**

**只要编写了form.is_valid()就会调用forms的校验类，执行UserForm中的代码，进行规则对象的校验，以及局部钩子和全局钩子的校验，且会对form(request.POST)中传入的数据进行校验，如果不存在定义的字段如username、password等is_valid()方法就会变为false！！！**

```python
def register(request):

    if request.method=='POST':
        print(request.POST)

        # 可以自己手动传入参数实例化对象进行测试，参数是字典形式
        form=UserForm({"username":"wang","email":"41234@qq.com"})

        # 实例化对象传入的参数可以多写，如request.POST冲的csrf_token，多的字段不会进行校验。但是绝不能少，少了is_valid()方法就会报False，而且key值也不能拼错
        form=UserForm(request.POST)

        if form.is_valid():
            # 如果表单字段验证成功，在form.cleaned_data中存储验证成功的字段key和value
            # {'username': 'alex', 'password': '1234', 'email': '1234@qq.com'}
            print(form.cleaned_data)
        else:
            # 如果验证失败，校验成功的字段依然会放存放在from.cleaned_data字典中
            print(form.cleaned_data)
            # 但是如果校验失败，校验失败的字段会存放在form.errors中，存放的格式是字段key:错误信息
            # errors的数据类型是ErrorDict,{'name':[.......]}
            print(form.errors)

            # errors的结果是ErrorList类型，格式为<ul class="errorlist"><li>Ensure this value has at least 4 characters (it has 1).</li></ul>，虽然是标签，但是是列表类型
            print(form.errors.get('name'))
            
            # 只去[0]位置取出错误信息，显示如下
            # Ensure this value has at least 4 characters (it has 1).
            print(form.errors.get('name')[0])

    return render(request,'register.html')
```

from django import forms
class Register(forms.Form):
    """
    要求用户必须在一定范围内
    不可以是admin
    """
    username =forms.CharField(required=True,label="用户名",error_messages={"required":"这个东西咋能为空呢"})
    password= forms.CharField(max_length=32,widget=forms.PasswordInput,label="密码",initial="hello world")
    email = forms.EmailField()
    def clean_username(self):
        """自定义校验函数的名字是固定的"""
        username =self.cleaned_data.get("username")
        if username =="admin":
            self.add_error("username","用户名不可以是:%s"%username)
        else:
            return username
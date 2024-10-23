from django import forms

class LoginForms(forms.Form):
    name = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Ex.: João da Silva"
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class RegisterForms(forms.Form):
    name = forms.CharField(
        label="Nome de Login",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João da Silva"  
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite seu email"
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=30,
                widget=forms.PasswordInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    confirm_password = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=30,
                widget=forms.PasswordInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_confirm_password(self):        
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password') 
        if password and confirm_password:
            print(f'password: {password}')
            print(f'confirm_password: {confirm_password}')
            if password != confirm_password:
                raise forms.ValidationError('As senhas não conferem!') 
            else:
                return confirm_password
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            name = name.strip()
            if " " in name:
                raise forms.ValidationError('O login não pode conter espaços vazios!')
            else:
                return name
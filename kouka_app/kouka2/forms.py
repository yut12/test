from django import forms

class Kouka2Form(forms.Form):
    name = forms.CharField(label='名前:', max_length=30)
    email = forms.EmailField(label='年齢:')
    title = forms.CharField(label='電話番号:', max_length=11)
    message = forms.CharField(label='Mail:')
    form = forms.CharField(label='住所:',max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = '氏名を入力'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = '年齢を入力'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = '電話番号を入力'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メールアドレスを入力'

        self.fields['form'].widget.attrs['class'] = 'form-control col-13'
        self.fields['form'].widget.attrs['placeholder'] = '住所を入力'

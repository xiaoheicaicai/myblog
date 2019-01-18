from django import forms

from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'placeholder': '请输入昵称'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': '请输入邮箱'}),
            'content': forms.Textarea(attrs={'id': 'content', 'class': 'form-control', 'placeholder': '请输入评论内容'}),
        }

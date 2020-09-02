# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost


# 文章表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含字段
        fields = ('title', 'body_content', 'tags', 'avatar')
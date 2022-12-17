from django import forms

from KetoGo.common.models import ProductComment


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'cols': 140,
                    'rows': 10,
                    'placeholder': 'Add comment...',
                },
            ),
        }


class SearchProductForm(forms.Form):
    search = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search in our menu...'
            }
        )
    )

from .models import Work, WorkPicture, Collection
from django import forms


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['work_name', 'work_description', 'work_artist']

        widgets = {
            'work_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Work name:'
            }),
            'work_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Work description:'
            }),
            'work_artist': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Work artist:'
            })
        }


class WorkPictureForm(forms.ModelForm):
    class Meta:
        model = WorkPicture
        fields = ['picture_source']


class CollectionForm(forms.ModelForm):
    work_select = forms.ModelMultipleChoiceField(
        queryset=Work.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control'
        }),
        label='Выбор работ:'
    )

    class Meta:
        model = Collection
        fields = ['collection_name', 'collection_description', 'collection_picture']

        widgets = {
            'collection_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Collection name:'
            }),
            'collection_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Collection description:'
            })
        }

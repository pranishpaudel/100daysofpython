from django.forms import ModelForm
from .models import Project,Review,Message
from django import forms

class ProjectForm(ModelForm):

    class Meta:
        model= Project
        fields= '__all__'
        exclude= ["vote_total","vote_ratio"]

        widgets= {
            'tags': forms.CheckboxSelectMultiple(),
        }

    
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'input', 'placeholder': "Add titlte"}
        )



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'rows': 5}) 




class MessageForm(ModelForm):
    class Meta:
        model= Message
        fields= '__all__'
        exclude=['sender','is_read']



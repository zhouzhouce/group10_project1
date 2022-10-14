from django import forms
from .models import GeeksModel
from .models import GeeksWithFieldModel

class InputForm(forms.Form):
    #each field would be mapped as an input field in HTML
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text= "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())

#create a model form


class GeeksForm(forms.ModelForm):
    #specify the name of model to use
    class Meta:
        model = GeeksModel
        fields = "__all__"

class GeeksWithFieldForm(forms.ModelForm):
    #specify the name of model to use
    class Meta:
        model = GeeksWithFieldModel
        fields = "__all__"

'''
class GeeksForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	views = forms.IntegerField()
	available = forms.BooleanField()
    '''

'''    
class GeeksForm(forms.Form):
    title = forms.CharField(widget = forms.Textarea)
    description = forms.CharField(widget = forms.CheckboxInput)
    views = forms.IntegerField(widget = forms.TextInput)
    available = forms.BooleanField(widget = forms.Textarea)
'''

'''
class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    date = forms.DateField(widget = forms.SelectDateWidget)
'''

'''
class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
'''

'''
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
'''
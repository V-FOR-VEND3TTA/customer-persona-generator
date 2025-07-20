from django import forms

class CustomerPersonaForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    occupation = forms.CharField(max_length=100)
    interests = forms.CharField(widget=forms.Textarea)
    challenges = forms.CharField(widget=forms.Textarea)
    goals = forms.CharField(widget=forms.Textarea)

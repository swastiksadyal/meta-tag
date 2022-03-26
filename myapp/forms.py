from django import forms

class input_form(forms.Form):
    website = forms.CharField(label=" " ,widget=forms.TextInput(attrs={'placeholder': 'Enter Webaddress here...'}),empty_value="enter web address here...",help_text="enter the web address, be sure to start with http/https for proper meta checking")
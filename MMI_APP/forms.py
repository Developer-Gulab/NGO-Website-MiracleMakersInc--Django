from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UsernameField
from  django.contrib.auth.models import User
from .models import Donor,Volunteer

class UserForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs=
                    {'class':'form-control','placeholder':"Enter Password"}))
    password2 = forms.CharField(label = 'Confirm Password (Again)', widget = forms.PasswordInput(attrs=
                    {'class':'form-control','placeholder':"Enter Password (Again)"}))
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}),  
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}) ,
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your EmailId'}),
        }


class DonorSignupForm(forms.ModelForm):
    userpic = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-control'})),
    class Meta:
        model=Donor
        fields = ['contact', 'userpic', 'address']
        widgets = {
            'contact':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'address':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Full Address'})
        }



# class UserForm1(UserCreationForm):
#     password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs=
#                     {'class':'form-control','placeholder':"Enter Password"}))
#     password2 = forms.CharField(label = 'Confirm Password (Again)', widget = forms.PasswordInput(attrs=
#                     {'class':'form-control','placeholder':"Enter Password (Again)"}))
#     class Meta:
#         model=User
#         fields = ['first_name','last_name','username','email','password1','password2']
#         widgets = {
#             'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}),  
#             'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}) ,
#             'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
#             'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your EmailId'}),
#         }


class VolunteerSignupForm(forms.ModelForm):
    userpic = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-control'})),
    idpic = forms.ImageField(widget=forms.TextInput(attrs={'class':'form-control'})),
    # idpic = forms.ImageField(),
    class Meta:
        model=Volunteer
        fields = ['contact', 'userpic', 'idpic', 'address', 'aboutme']
        widgets = {
            'contact':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'address':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Full Address'}),
            'aboutme':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type something yourself'}),
            # 'idpic' : forms.FileInput(attrs={'class' : 'form-control'}),
            # 'status':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type something yourself'})
        }

        labels = {
            'userpic' : 'Upload Your Image',
            'idpic' : 'ID Proof (Aadhar/Driving License/PAN Card/PassPort)',
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(required = True, widget = forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder' : 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder' : 'Password'}))
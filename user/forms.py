from django.contrib.auth.models import User
from django import forms


class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=15,
        required=True)
    last_name = forms.CharField(
        max_length=15,
        required=True)
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'style': 'border-color: grey;',
                'placeholder': 'Your email',
                }))

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        if not first_name and not email and not last_name:
            raise forms.ValidationError('Please, enter details!')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

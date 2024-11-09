from django import forms
from .models import InterviewRound  # Add this import

class InterviewRoundForm(forms.ModelForm):
    class Meta:
        model = InterviewRound
        fields = ['round_type']
        widgets = {
            'round_type': forms.Select(attrs={'class': 'form-control'})
        }

class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter interviewer email'
        })
    )
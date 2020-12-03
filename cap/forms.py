from django import forms
from cap.models import CampusAmbassador

class CampusAmbassadorForm(forms.ModelForm):
    
    class Meta:
        model = CampusAmbassador
        exclude = ['points']
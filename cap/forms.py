from django import forms
from cap.models import CampusAmbassador

YEAR_CHOICES =( 
    ("First Year", "First Year"), 
    ("Second Year", "Second Year"), 
    ("Third Year", "Third Year"), 
    ("Fourth Year", "Fourth Year"), 
    ("Other", "Other"), 
) 

class CampusAmbassadorForm(forms.ModelForm):
    
    year_of_study = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = CampusAmbassador
        exclude = ['points', 'year_of_study']
        widgets = {
            'best_suited': forms.Textarea(),
            'key_strengths': forms.Textarea(),
            'anticipate_learning': forms.Textarea(),
            'past_experience': forms.Textarea(),
        }

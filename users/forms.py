from django import forms
from .models import RoleDuty

class RoleDutyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoleDutyForm, self).__init__(*args, **kwargs)
        self.fields['duty'].widget.attrs.update({'cols': 80, 'rows': 5})

    class Meta:
        model = RoleDuty
        fields = ['duty', 'duty_ar']
 
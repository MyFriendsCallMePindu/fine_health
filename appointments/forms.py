from django import forms
from .models import Appointment
from services.models import Service

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'full_name',
            'phone',
            'email',
            'service',
            'preferred_date',
            'message'
        ]
        widgets = {
            'preferred_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'message': forms.Textarea(
                attrs={'rows': 4}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)

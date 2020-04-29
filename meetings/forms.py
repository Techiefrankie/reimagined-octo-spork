from datetime import date

from setup import get_logger

from django.forms import ModelForm, DateInput, TimeInput, TextInput
from django.core.exceptions import ValidationError

from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'duration': TextInput(attrs={'type': 'number', 'min': '15', 'max': '60'}),
        }

        def clean_date(self):
            dt = self.cleaned_data['date']
            if dt < date.today():
                raise ValidationError("Meeting cannot be in the past", code="invalid")
            return dt

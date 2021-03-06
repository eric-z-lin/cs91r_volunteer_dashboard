# events/forms.py

from django import forms
from events.models import Event
from volunteers.models import Volunteer 

class EventForm(forms.ModelForm):
	volunteers = forms.ModelMultipleChoiceField(
					queryset=Volunteer.objects.all(),
					required=False,
					widget = forms.CheckboxSelectMultiple,
				)

	class Meta:
		model = Event
		fields = (
			'name',
			'description',
			'address',
			'time',
			'cost',
			'volunteers',
		)
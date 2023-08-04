from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = Vehicle
        fields = '__all__'

        # widgets = {
        #     'booking_date' : DateInput(),

        # }
        labels={
            'vehicle_number':'Vehicle Number',
            'vehicle_type':'Vehicle Type',
            'vehicle_model':'Model',
            'vehicle_description':'Description of vehicle',

        }
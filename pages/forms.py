from django import forms
from django_typeahead.widgets import TypeaheadInput

class StateForm(forms.Form):
    query = forms.CharField(
        widget=TypeaheadInput(
            options={
                'hint': False,
                'highlight': False,
                'minLength': 1
            },
            datasets={
                ''
            }
        )
    )
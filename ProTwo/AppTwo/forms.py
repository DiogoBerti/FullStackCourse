from django import forms
from django.core import validators

# Validator customizado!
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Needs to start with Z')

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    text_area = forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField(label='Enter your e-mail again')
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])


    # Funçao que valida os campos do formulario no clean (pode ser usado para
    # Validações especificas)
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Emails must Match!')



# Não necessario pois o django ja possui validators
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return botcatcher

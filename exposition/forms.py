from django import forms
from .models import Agri_preneur

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}))
    envoyeur = forms.EmailField(label="Votre adresse e-mail", widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        """
        message = self.cleaned_data['message']
        if "putain" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de putain !")

        """
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "putain" in sujet and "putain" in message:
                raise forms.ValidationError(
                "Vous parlez de putain dans le sujet ET le message ? Non mais ho !")

        return message  # Ne pas oublier de renvoyer le contenu du champ traité

class Agri_preneurForm(forms.ModelForm):
    class Meta:
        model = Agri_preneur
        fields = '__all__'


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))


class CreationForm(forms.Form):
    username = forms.CharField(label="Email", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
    confpassword = forms.CharField(label="Confirmer Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))
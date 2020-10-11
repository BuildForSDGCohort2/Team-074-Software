from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from datetime import datetime
from exposition.models import Agri_preneur, Produit
from exposition.forms import ContactForm, Agri_preneurForm, ConnexionForm, CreationForm
from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login, logout

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'exposition/connexion.html', locals())

def creation(request):
    error = False

    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
        return redirect('home')
    else:
        form = CreationForm()
        return render(request, 'exposition/creation.html', locals())

    

def deconnexion(request):
    logout(request)
    return redirect('home')


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    #return HttpResponse("""
    #   <h1>Bienvenue sur AGRI-ANNUAIRE !</h1>
    #  <p>Une plateforme numérique qui fait la promotion des agri-preneurs de la RDC !</p>
    #""")
    """ Afficher tous les agri_preneurs de notre système """
    fournisseurs = Agri_preneur.objects.all()
    produits = Produit.objects.all()

    return render(request, 'exposition/index.html', {'fournisseurs':fournisseurs, 'produits':produits})

def lire(request, id, slug):
    f = get_object_or_404(Agri_preneur, id=id, slug=slug)
    return render(request, 'exposition/lire.html', {'fournisseur':f})

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'exposition/contact.html', locals())

def agri_preneur(request):
    agri = Agri_preneurForm(request.POST or None)
    
    return render(request, 'exposition/agri_preneur.html', locals())

def apropos(request):

    return render(request, 'exposition/apropos.html', locals())

def renommage(instance, nom_fichier):
    return "{}-{}".format(instance.id, nom_fichier)


def test(request, param):
    if param > 5 :
        raise Http404
    return redirect(vue_redirect)


def vue_redirect(request):
    return HttpResponse("Vous avez été rédirigés ici car l'élément cherché n'existe pas!")

def date_actuelle(request):
    return render(request, 'exposition/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'exposition/addition.html', locals())

#Exemple d'une vue générique
class FAQView(TemplateView):
   template_name = "blog/faq.html"  # chemin vers le template à afficher

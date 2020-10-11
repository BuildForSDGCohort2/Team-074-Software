from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Agri_preneur(models.Model):

    denomination = models.CharField(max_length=75)
    adresse_physique = models.CharField(max_length=255)
    email = models.CharField(max_length=75)
    contact_phone = models.CharField(max_length=13)
    date_inscr = models.DateTimeField(default=timezone.now, verbose_name="Date d'inscription")
    img_profil = models.ImageField(upload_to='renommage', null=True, verbose_name="Image de profil")
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        verbose_name="agri_preneur"
        ordering = ['date_inscr']


       
    def __str__(self):
        """
    
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration

        """

        return self.denomination

class Produit(models.Model):
    designation = models.CharField(max_length=75)
    prix_unit = models.FloatField(verbose_name="Prix Unitaire")
    devise_vente = models.CharField(max_length=10)
    qty_stock = models.IntegerField()
    description = models.TextField(null="True")
    image_produit = models.CharField(max_length=255, null="true")
    categorie = models.CharField(max_length=75)
    denomination = models.CharField(max_length=75, verbose_name="Fournisseur")

    class Meta:
        verbose_name="produit"
        ordering = ['designation']

    def __str__(self):
        return self.designation

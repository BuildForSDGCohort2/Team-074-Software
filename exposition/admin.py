from django.contrib import admin
from .models import Agri_preneur, Produit
from django.utils.text import Truncator

#Classe permettant de gérer facilement les données du model Agri_preneur
class Agri_preneurAdmin(admin.ModelAdmin):
   list_display   = ('denomination', 'apercu_adresse_physique', 'email', 'contact_phone', 'date_inscr')
   date_hierarchy = 'date_inscr'
   ordering       = ('date_inscr', )
   search_fields  = ('denomination', 'adresse_physique', 'email', 'contact_phone')
   # Les attributs à afficher dans le formulaire d'édition selon l'ordre donné
   # fields = ('denomination', 'email', 'adresse_physique', 'contact_phone', 'date_inscr')

   fieldsets = (
       #Field 1 : meta-info (denomination, email)
       ('Général',{
           'classes': ['collapse',],
           'fields': ('denomination', 'email', 'slug')
       }),
       #Field 2 : meta-info (adresse, contact)
       ('Adresse et contact',{
           'classes': ['collapse',],
           'description': 'Veuillez saisir une adresse physique exacte et un numéro opérationnel !',
           'fields': ('adresse_physique', 'contact_phone')
       }),
       #Field 3 : meta-info (date inscription)
       ('Adresse et contact',{
           'fields': ('date_inscr',)
       }),
       #Field 4 : meta-info (image profil)
       ('Image ou photo de profil',{
           'fields': ('img_profil',)
       }),
   )
   prepopulated_fields = {'slug': ('denomination', ), }

   
   def apercu_adresse_physique(self, agri_preneur):

       """ 
       Retourne les 40 premiers caractères de l'adresse de l'agri_preneur, 
       suivi de points de suspension si le texte est plus long. 
       On pourrait le coder nous même, mais Django fournit déjà la 
       fonction qui le fait pour nous ! """

       text = agri_preneur.adresse_physique[0:30]
       if len(agri_preneur.adresse_physique) > 30: 
           return '%s…' % text
       else: 
           return text
       apercu_adresse_physique.short_description = 'Adresse physique'

# Register your models here.
admin.site.register(Agri_preneur, Agri_preneurAdmin)
admin.site.register(Produit)
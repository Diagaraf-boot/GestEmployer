from django.db import models
# Create your models here.


class Departement(models.Model):
    #permet de stocker un departement
    nom = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Departements' 
    
    def __str__(self):
        #Retourne une représentation du sujet sous forme de chaine de caractères
        return self.nom

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    class Meta:  
        db_table = "employee" 

    def __str__(self):
        #Retourne une représentation du sujet sous forme de chaine de caractères
        return self.ename 
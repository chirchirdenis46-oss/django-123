from django.db import models

# Create your model here.
"""
-difine a model
-state the attributes and attach/difine its respective type

"""







class hobbies(models.Model):
    Name = models.CharField()
    age = models.IntegerField()
    dob = models.DateTimeField()
    specie = models.CharField(max_length=200)
    bio = models.CharField(max_length=255)
    weight = models.FloatField()
    image = models.CharField(max_length=255)
    
    

    def __str__(self):
        return f"(seif.name).__str__(seif.age)yrs old"


class Car(models.Model):
    fuel_type = {
        "D":"Diesel",
        "P": "Petrol"
    }
    name = models.CharField(max_length=100)
    yop = models.IntegerField()
    description = models.CharField(max_length=250)
    fuel_type = models.CharField(max_length=1,choices = fuel_type)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Interests(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    Place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


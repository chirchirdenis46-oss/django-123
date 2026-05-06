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




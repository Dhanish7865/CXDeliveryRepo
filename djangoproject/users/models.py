from django.db import models
#from django.urls import reverse

# Create your models here.
class UserModel(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    first_name = models.CharField(max_length=20, help_text='Enter First Name')
    last_name = models.CharField(max_length=20, help_text='Enter Surname')
    location = models.CharField(max_length=20, help_text='Enter Location')
    age = models.IntegerField(help_text="Enter Age")
    shoe_size = models.IntegerField(help_text="Enter Shoe Size")

    # Metadata
    class Meta: 
        ordering = ['last_name', 'first_name', 'age']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.first_name + " " + self.last_name
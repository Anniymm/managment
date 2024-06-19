from django.db import models
from django.contrib.auth.models import User


# personaluri gverdistvis
class PersonalSpace(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_space') #onetoone field, ert users erti personal space 
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, null=True)
    # mere kidev davamato

    def __str__(self):
        return f"Personal Space of {self.user.username}"
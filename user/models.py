from django.db import models

# Create your models here.


class UserModel(models.Model):
    class Meta:
        db_table = "my_user"


    username = models.EmailField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)

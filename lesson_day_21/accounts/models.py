from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)


# class GroupUser(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)

# class UserPermission(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


# Group.add_to_class('user_set', models.ManyToManyField(CustomUser, through=GroupUser, related_name='custom_groups'))
# Permission.add_to_class('user_set', models.ManyToManyField(CustomUser, through=UserPermission, related_name='custom_user_permissions'))
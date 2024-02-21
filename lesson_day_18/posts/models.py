from django.db import models

class Post(models.Model):
    text = models.TextField()
def __str__(self):
    return self.text[:50]


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        managed = False
        db_table = 'actor'

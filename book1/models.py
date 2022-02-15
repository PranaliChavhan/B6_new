from django.db import models



# Create your models here.
class ActiveBooksManager(models.Manager):  # Custom Model Manager
    def get_queryset(self):  # override -- 
        return super(ActiveBooksManager, self).get_queryset().filter(is_active='Y')

class InActiveBooksManager(models.Manager):
    def get_queryset(self):  # override -- 
        return super(InActiveBooksManager, self).get_queryset().filter(is_active='N')


class Book1(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qnty = models.IntegerField()
    is_active = models.CharField(max_length=1, default='Y')
    active_objects = ActiveBooksManager()
    Inactive_objects = InActiveBooksManager()
    objects = models.Manager()

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"{self.name}---{self.price}"


from django.db import models

class Advertisements(models.Model):
    tittle = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('торг', help_text = 'Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add = True)
    updeted_at = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id = {self.id}, title = {self.tittle}, price = {self.price}"

# Create your models here.

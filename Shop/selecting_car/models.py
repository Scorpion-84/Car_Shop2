from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()
class SelectCar(models.Model):
    
    car_choice = models.CharField(max_length = 300, verbose_name = 'انتخاب خودرو')
    color_choice = models.CharField(max_length = 300, verbose_name = 'رنگ خودرو')
    user = models.ForeignKey(user, on_delete = models.CASCADE, related_name = 'shopcar')
    class Meta:
        db_table = 'carchoice'
    

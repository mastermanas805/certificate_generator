from enum import unique
from django.db import models
import random
import math
from django.core.exceptions import ValidationError

class event(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateField()
    html = models.TextField()

class student(models.Model):

    def validate_moibil_no(value):
        if math.floor(math.log10(value)) != 9:
            raise ValidationError(
                _('%(value)s is not a valid mobile number'),
                params={'value': value},
            )
    
    first_name = models.CharField(max_length = 1000)
    last_name = models.CharField(max_length = 1000)
    position = models.CharField(max_length = 1000)
    event = models.ForeignKey(event, related_name='studets', on_delete= models.CASCADE)
    uid = models.IntegerField(unique = True, default = 0)
    mobile_no = models.IntegerField(validators=[validate_moibil_no], default = 0)
    email = models.EmailField(default=0)

    def save(self, *args, **kwargs):
        if self.uid == 0:
            id = random.randint(1000, 100000000)

            while(student.objects.filter(uid = id).exists()):
                id = random.randint(100000000, 999999999)
            self.uid = id
        super(student, self).save(*args, **kwargs)
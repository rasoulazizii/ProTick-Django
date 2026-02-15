from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=220)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField()

    def __str__(self):
        return self.company_name

class Event(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.PROTECT)
    description = models.TextField()
    location = models.CharField(max_length=440)
    image = models.ImageField(upload_to='event/')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description[:100]
    

class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=220)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    remaining_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
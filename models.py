from django.db import models
from django.utils import times.

class Exoplanet(models.Model):
    PLANET_TYPES = [
        ('terrestrial', 'Terrestrial'),
        ('gas_giant', 'Gas Giant'),
        ('ice_giant', 'Ice Giant'),
        ('super_earth', 'Super-Earth'),
        ('neptune_like', 'Neptune-like'),
        ('hot_jupiter', 'Hot Jupiter'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=PLANET_TYPES, default='other')
    distance = models.FloatField(help_text="Distance from Earth in light-years", default=0.0)
    discovery_year = models.IntegerField(default=1995)  # First exoplanet was discovered in 1995
    description = models.TextField(default='', blank=True)
    image_url = models.URLField(default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

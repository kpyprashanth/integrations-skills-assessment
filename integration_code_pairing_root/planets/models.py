from django.db import models


class Planet(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, serialize=True)
    planet_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    diameter = models.IntegerField()
    rotation_period = models.IntegerField()
    orbital_period = models.IntegerField()
    gravity = models.CharField(max_length=255)
    population = models.IntegerField()
    climate = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)
    surface_water = models.IntegerField()

    unserializable_fields = ('id',)

    class Meta:
        db_table = 'planets'

    def to_dict(self):
        seralized = {}
        for field in self._meta.get_fields():
            if field.name in self.unserializable_fields:
                continue
            
            seralized[field.name] = getattr(self, field.name)
        return seralized

    def to_imperial(self):
        seralized = {}
        # No other units can be converted to Imperial units except distance

        # Kilometers to miles
        self.diameter = self.diameter*0.621371

        for field in self._meta.get_fields():
            if field.name in self.unserializable_fields:
                continue

            seralized[field.name] = getattr(self, field.name)
        return seralized
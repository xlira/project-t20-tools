from django.db import models

class racas(models.Model):
    nomeRaca = models.TextField(primary_key=True)
    atributosRaca = models.TextField(max_length=255)
    habilidadesRaca = models.TextField(max_length=510)
    periciasRaca = models.TextField(max_length=510)
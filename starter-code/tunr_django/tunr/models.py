from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=100)
  nationality = models.CharField(max_length=100)
  photo_url = models.TextField()

  def __str__(self):
    return self.name

class Song(models.Model):
  title = models.CharField(max_length=100)
  album = models.CharField(max_length=100)
  preview_url = models.TextField()
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs", default=1)

  def __str__(self):
    return f"#{self.title} on albmum: #{self.album}"
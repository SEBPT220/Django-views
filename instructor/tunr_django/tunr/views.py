from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm, SongForm
# Create your views here.

# Role of controller
# - process http request
# - gather the necessary resources (information from the system <Models>)
# - pass the resources to the template

def artist_list(request):
  artists = Artist.objects.all()
  return render(request, 'artist_list.html', {'artists': artists})

def artist_detail(request, pk):
  artist = Artist.objects.get(id=pk)
  return render(request, 'artist_detail.html', {'artist': artist})

def artist_create(request):
    if request.method == 'POST':
      form = ArtistForm(request.POST)
      if form.is_valid():
        artist = form.save()
        return redirect('artist_detail', pk=artist.pk)
    else:
      form = ArtistForm()

    return render(request, 'artist_form.html', {'form': form})

# EDIT ARTIST
def artist_edit(request, pk):
    artist =  Artist.objects.get(id=pk)

    if request.method == 'POST':
      form = ArtistForm(request.POST, instance=artist)
      if form.is_valid():
        artist = form.save()
        return redirect('artist_detail', pk=artist.pk)
    else:
      form = ArtistForm(instance=artist)

    return render(request, 'artist_form.html', {'form': form})

# _ convention for unused variables required for positional arguments
def artist_delete(_, pk):
    artist =  Artist.objects.get(id=pk)
    artist.delete()
    return redirect('artist_list')

# SONGS

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'song_detail.html', {'song': song})

def song_create(request):
    if request.method == 'POST':
      form = SongForm(request.POST)
      if form.is_valid():
        song = form.save()
        return redirect('song_detail', pk=song.pk)
    else:
      form = SongForm()

    return render(request, 'song_form.html', {'form': form})

def song_edit(request, pk):
    song = Song.objects.get(id=pk)
    if request.method == 'POST':
      form = SongForm(request.POST, instance=song)
      if form.is_valid():
        song = form.save()
        return redirect('song_detail', pk=song.pk)
    else:
      form = SongForm(instance=song)

    return render(request, 'song_form.html', {'form': form})

def song_delete(_, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    return redirect('song_list')
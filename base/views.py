from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile, Movie, Video


def home(request):
    return render(request, 'base/index.html')


@login_required(login_url="login")
def profileList(request):
    profiles = request.user.profiles.all()
    context = {'profiles': profiles}
    return render(request, 'base/profileList.html', context)


@login_required(login_url="login")
def createProfile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('profile-list')

    return render(request, 'base/createProfile.html', {'form': form})


@login_required(login_url="login")
def watch(request, pk):
    try:
        profile = Profile.objects.get(uuid=pk)
        movies = Movie.objects.filter(age_limit=profile.age_limit)
        if profile not in request.user.profiles.all():
            return redirect('profile-list')

        return render(request, 'base/movieList.html', {'movies': movies})

    except Profile.DoesNotExist:
        return redirect('profile-list')


@login_required(login_url="login")
def movieDetail(request, pk):
    try:
        movie = Movie.objects.get(uuid=pk)
        return render(request, 'base/movieDetail.html', {'movie': movie})

    except Movie.DoesNotExist:
        return redirect('profile-list')


@login_required(login_url='login')
def showMovie(request, pk):
    try:
        movie = Movie.objects.get(uuid=pk)
        movie = movie.videos.values()

        return render(request, 'base/showMovie.html', {'movie': list(movie)})

    except Movie.DoesNotExist:
        return redirect('profile-list')









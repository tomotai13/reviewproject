from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import ScoreModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



# Create your views here.

def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        pass
    return render(request, 'signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)

            try:
                u = ScoreModel.objects.get(player=user.id)
            except:
                return redirect('create')

            return redirect('list')

        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def listview(request):
    object_list = ScoreModel.objects.order_by('-score')
    object_list = object_list[:20]

    play_id = request.user.id
    play_user = ScoreModel.objects.filter(player=play_id).first()
    return render(request, 'list.html', {'object_list':object_list, 'play_user':play_user})
'''
@login_required
def detailview(request, pk):
    object = ScoreModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})'''

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ScoreModel
    fields = ('score', 'player')
    success_url = reverse_lazy('list')

def logoutview(request):
    logout(request)
    return redirect('login')

@login_required
def playview(request):
    if request.method == "POST":
        userid = request.user.id
        player = ScoreModel.objects.get(player=userid)

        new_score = request.POST['score_data']
        score = player.score
        player.score = int(new_score) + score
        player.save()
        return redirect('list')









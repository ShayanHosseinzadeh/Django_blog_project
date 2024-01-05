from django.shortcuts import render,redirect,reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import  Game
from .forms import GameForm
# Create your views here.
# def Game_list_view(request):
#     game = Game.objects.all()
#     return render(request, 'game/game_list.html', {'games'  : game})

class GameListView(generic.ListView):
    model = Game
    template_name = 'game/game_list.html'
    context_object_name = 'games'


# class GameDetailView(generic.DetailView):
#     model = Game
#     template_name = 'game/game_detail.html'

def Game_Details_View(request,pk):
    game = get_object_or_404(Game,pk=pk)
    all_games = Game.objects.all()
    return render(request, 'game/game_detail.html',{'game':game,'all_games' : all_games})


# def Game_add_view(request):
#     if request.method == 'POST':
#         form = GameForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('Game_list_view'))
#     else: # get request
#         form = GameForm()
#     return render(request,'game/Create_game.html',context={'form':form})
class GameAddView(generic.CreateView):
    form_class = GameForm
    template_name = 'game/Create_game.html'

# def Game_edit_view(request,pk):
#     game = get_object_or_404(Game,pk=pk)
#     form = GameForm(request.POST or None,instance=game)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('Game_list_view'))
#     return render(request, 'game/edit_game.html',context={'form':form})


class GameUpdateView(generic.UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'game/edit_game.html'


# def Game_delete_view(request,pk):
#     game = get_object_or_404(Game,pk=pk)
#     if request.method == 'POST':
#         game.delete()
#         return redirect('Game_list_view')
#     return render(request,'game/game_delete.html',context={'game':game})
#
class GameDeleteView(generic.DeleteView):
    model = Game
    template_name = 'game/game_delete.html'
    success_url = reverse_lazy('Game_list_view')
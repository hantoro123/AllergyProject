from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from board.models import Board


# Create your views here.
# def board (request):
#     return render(request, 'board.html')

class BoardView(ListView):
    model = Board
    queryset = Board.objects.order_by('id')
    context_object_name = "board_list"

# def DetailView (request):
#     return render(request, 'boarddetail.html')

class DetailView(TemplateView):
    template_name = 'board/board_detail.html'


class BoardCreateView(CreateView):
    model = Board
    fields = "__all__"
    success_url = reverse_lazy("board:board_list")
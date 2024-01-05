from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameListView.as_view(),name='Game_list_view'),
    path('<int:pk>/', views.Game_Details_View, name='Game_detail_view'),
    path('add/', views.GameAddView.as_view(), name='Create_game'),
    path('<int:pk>/delete',views.GameDeleteView.as_view(), name='Delete_game'),
    path('<int:pk>/edit', views.GameUpdateView.as_view(), name='edit_game'),

]
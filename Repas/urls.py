from django.urls import path
from . import views


urlpatterns = [
 path('repass/', views.get_all_repass,name='repass'),
    path('repass/<str:pk>/', views.get_by_id_repas,name='get_by_id_repas'),
    path('repass/new', views.new_repas,name='new_repas'),
    path('repass/update/<str:pk>/', views.update_repas,name='update_repas'),
    path('repass/delete/<str:pk>/', views.delete_repas,name='delete_repas'),

    path('<str:pk>/reviews', views.create_review,name='create_review'),
    path('<str:pk>/reviews/delete', views.delete_review,name='delete_review'),
]
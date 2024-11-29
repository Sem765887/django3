from django.urls import path
from . import views

urlpatterns = [
   path('snippets/', views.snippet_list),
   path('snippets/<int:pk>/', views.snippet_detail),
   path('snippets/', views.SnippetList.as_view()),
   path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]



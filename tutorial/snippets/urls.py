from django.urls import path
from snippets import views
from .views import SnippetDetailView
#from . import views
#from snippets.views import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('', views.api_root),
# ]

urlpatterns = ([
    #path('', views.api_root),


    path('snippets/',views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view(),name='snippet-highlight'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    
    path('mymodels/<int:pk>/', SnippetDetailView.as_view(), name='snippets-detail'),
    #path(),
    
])



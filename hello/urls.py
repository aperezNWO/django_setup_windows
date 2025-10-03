from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("my_view", views.my_view, name="my_view"),
    path('health/', lambda r: JsonResponse({'status': 'ok'})),
    path('getAllLogs', views.getAllLogs,    name='getAllLogs'),
    path('getAllPersons', views.getAllPersons, name='getAllPersons'),
    path('getAllContactForms', views.getAllContactForms, name='getAllContactForms'),
]

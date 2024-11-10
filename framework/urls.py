from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)


urlpatterns =[
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.home,name="home"),
    path('advocate/',views.create_advocate,name="create_advocate"),
    path('supreme/',views.list_supreme,name="list_supreme"),
    path('advocate/<str:username>/',views.list_advocate,name="list_advocate"),
]
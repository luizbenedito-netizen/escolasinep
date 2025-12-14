from django.urls import path
from app.decorators import login_required
from app.views.home import HomeView

urlpatterns = [
    path("", login_required(HomeView.as_view()), name="home"),
]
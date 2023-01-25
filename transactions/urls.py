from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("transactions", views.transactions, name="transactions"),
    # path(
    #     "transactions/",
    #     views.TransactionsView.as_view(),
    #     name="transactions",
    # ),
]

from django.urls import path,include
from .views  import RegisterView,Home,TransactionCreateView,TransactionListView,GoalCreateView,GoalListView




urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('accounts/register/',RegisterView.as_view(),name='register'),
    # built in for login
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    path('transaction/',TransactionCreateView.as_view(),name='transaction_add'),
    path('transaction_list/',TransactionListView.as_view(),name='transaction_list'),
    path('goal/',GoalCreateView.as_view(),name='goal_add'),
    path('goal_list/',GoalListView.as_view(),name='goal_list')
]

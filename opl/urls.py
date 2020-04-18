from django.urls import path
from .views import opl_data,reserveSubView,fulfillmentEligibleView,ProvCompleteStatusSyncSolView

urlpatterns = [
    path('opl/', opl_data),
    path('opl/reserve', reserveSubView),
    path('opl/fulfillment/eligible',fulfillmentEligibleView),
    path('opl/provcomplete/syncback',ProvCompleteStatusSyncSolView.as_view()),


]
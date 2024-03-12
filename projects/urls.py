from django.contrib import admin
from django.urls import path
# from dashboard.apis.views import (
#     BudgetTotalView, BudgetDetailsView, 
#     BudgetValuesView, BudgetEconomyView, 
#     BudgetPercentView, BudgetDeviationView,
#     EntityAnalysisListViewOffset,
#     EntityAnalysisListViewCursor,
#       EntityAnalysisDetailView)

from projects.views import home, build #,query
from .views import ProjectListAPIView


urlpatterns = [
    path('', home, name='project-home'),
    path('list-projects', ProjectListAPIView.as_view(), name='project-list'),
    path('build', build, name='db-build'),


]
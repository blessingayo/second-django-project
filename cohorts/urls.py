from django.urls import path


import cohorts.views as cv

urlpatterns = [
    path('cohort/create', cv.create_cohort),
    path('cohort/all', cv.get_cohorts),
    path('cohort/get_one', cv.get_cohort),
    path('cohort/update', cv.update_cohort),
    path('cohort/delete', cv.delete_cohort),
]
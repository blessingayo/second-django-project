from django.urls import path

import natives.views as nv

urlpatterns = [
    path('native/create', nv.create_native),
    path('natives/all', nv.get_natives),
    path('native/get_one', nv.get_native),
    path('native/update', nv.update_native),
    path('native/delete', nv.delete_native),
]


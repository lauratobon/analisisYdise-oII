from django.urls import path
from . import views

urlpatterns = [
    path("", views.store_index, name="store_index"),
    path("<int:pk>/", views.store_detail,
         name="store_detail"),  # pk es el id y así
    # se vuelve dinámico
    path("reg", views.store_reg, name="store_reg"),
    path("new_store", views.new_store, name="new_store"),
    path("store_delete/<int:pk>", views.store_delete,
         name="store_delete"),
    path("edit_store/<int:pk>", views.edit_store,
         name="edit_store"),
    path("save_edit/<int:pk>", views.save_edit,
         name="save_edit"),
]

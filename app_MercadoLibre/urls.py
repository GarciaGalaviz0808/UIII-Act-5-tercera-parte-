from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_mercadolibre, name="inicio"),
    path("vendedor/agregar/", views.agregar_vendedor, name="agregar_vendedor"),
    path("vendedor/ver/", views.ver_vendedor, name="ver_vendedor"),
    path("vendedor/actualizar/<int:id_vendedor>/", views.actualizar_vendedor, name="actualizar_vendedor"),
    path("vendedor/realizar_actualizacion/<int:id_vendedor>/", views.realizar_actualizacion_vendedor, name="realizar_actualizacion_vendedor"),
    path("vendedor/borrar/<int:id_vendedor>/", views.borrar_vendedor, name="borrar_vendedor"),
    # Categoria (CRUD)
    path("categoria/agregar/", views.agregar_categoria, name="agregar_categoria"),
    path("categoria/ver/", views.ver_categoria, name="ver_categoria"),
    path("categoria/actualizar/<int:id_categoria>/", views.actualizar_categoria, name="actualizar_categoria"),
    path("categoria/realizar_actualizacion/<int:id_categoria>/", views.realizar_actualizacion_categoria, name="realizar_actualizacion_categoria"),
    path("categoria/borrar/<int:id_categoria>/", views.borrar_categoria, name="borrar_categoria"),
    #Producto CRUD
    path("producto/agregar/", views.agregar_producto, name="agregar_producto"),
    path("producto/ver/", views.ver_producto, name="ver_producto"),
    path("producto/actualizar/<int:id_producto>/", views.actualizar_producto, name="actualizar_producto"),
    path("producto/realizar_actualizacion/<int:id_producto>/", views.realizar_actualizacion_producto, name="realizar_actualizacion_producto"),
    path("producto/borrar/<int:id_producto>/", views.borrar_producto, name="borrar_producto"),

]
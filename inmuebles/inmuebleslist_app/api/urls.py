from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import ComentarioDetail, ComentarioList, EmpresaAV, EmpresaDetalleAV, EdificacionAV, EdificacionDetalleAV
from inmuebleslist_app.models import Comentario

urlpatterns = [
    # path('list/', inmueble_list, name='inmueble-list'),
    # path('<int:pk>', inmueble_detalle, name='inmueble-detalle'),
    path('list/', EdificacionAV.as_view(), name='edificacion'),
    path('<int:pk>/', EdificacionDetalleAV.as_view(), name='edificacion-detail'),
    path('empresa/', EmpresaAV.as_view(), name='empresa'),
    path('empresa/<int:pk>/', EmpresaDetalleAV.as_view(), name='empresa-detail'),
    path('comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('comentario/<int:pk>/', ComentarioDetail.as_view(), name='comentario-detail'),
]

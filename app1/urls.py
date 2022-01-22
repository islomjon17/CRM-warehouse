from django.urls import path
from .views import BolimView, MahsulotView, ClientView, MahsulotEdit, ClientEdit

urlpatterns = [
    path("", BolimView.as_view(), name='bolim'),
    path("mahsulotlar/", MahsulotView.as_view(), name='mahsulotlar'),
    path("mahsulotlar/<int:son>/", MahsulotEdit.as_view(), name='product-update'),
    path("clientlar/", ClientView.as_view(), name='clientlar'),
    path("clientlar//<int:son>/", ClientEdit.as_view(), name='client-update'),
]



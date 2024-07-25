from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('getproducts/',views.getAllProducts,name='getproducts'),
    path('addProducts/',views.addProducts),
    path('deleteProduct/<int:id>',views.deleteProduct),
    path('updateProduct/<int:id>',views.updateProduct),
    path('addProductsWithForm/',views.addProductWithForm),
    path('productdetail/<int:id>',views.getProductDetail,name='productdetail'),
    path('update/<int:id>',views.updateProductWithForm,name ="updateproduct"),
    
    
    path('addcategory/',views.addCategory,name='addcategory'),
    path('getcategories/',views.getAllCategories,name='getcategories'),
    path('deletecategory/<int:id>',views.deleteCategory,name='deletecategory'),
    path('updatecategory/<int:id>',views.updateCat,name='updatecategory'),
    path('sendmail/',views.sendMail,name='sendmail'),

]

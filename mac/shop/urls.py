from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutPage"),
    path("contact/", views.contact, name="contactPage"),
    path("tracker/", views.tracker, name="trackerPage"),
    path("checkout/", views.checkout, name="checkoutPage"),
    path("products/<int:myid>", views.product_view, name="productPage"),
    path("search/", views.search, name="searchPage"),
    path("handlerequest/", views.handlerequest, name="Handlerequest"),

]

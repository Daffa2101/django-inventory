from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, update_amount, delete_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_item, name='create_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('update-amount/<str:item_name>/<str:action>/',
         update_amount, name='update_amount'),
    path('delete-item/<str:item_name>/', delete_item, name='delete_item'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]

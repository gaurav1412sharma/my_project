from django.urls import path
from ntpweb.views import get_ntp_time, dynamic_graph, SearchView, csrf_token_view

urlpatterns = [
    path('dynamic-graph/', dynamic_graph, name='dynamic_graph'),
    path('search/', SearchView.as_view(), name='search_view'),
    path('get-ntp-time/', get_ntp_time, name='get_ntp_time'),
    path('api/csrf_token/', csrf_token_view, name='csrf_token'),
    path('packet-details/', SearchView.as_view(), name='packet_details'),  # Added this line
]

from django.urls import path, include
from .views import RetreatViewSet,BookingViewSet

urlpatterns = [
    path(
        "retreats/",
        include(
            [
                path(
                    "add/",
                    RetreatViewSet.as_view(
                        {
                            "post": "create_retreat",
                        }
                    ),
                ),
                path(
                    "get-details/",
                    RetreatViewSet.as_view(
                        {
                            "get": "get_all_search_filter_retreat",
                        }
                    ),
                ),
            ]
        ),
    ),
    path(
        "booking/add/",
        BookingViewSet.as_view(
            {
                "post": "create_booking",
            }
        ),
    ),
    
]

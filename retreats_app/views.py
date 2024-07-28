from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import RetreatDetails
from .serializers import BookingSerializer,RetreatSerializer
from .utils.serializers_errors import serializer_error
from .utils.pagination_utility import pagination_utility
from django.db.models import Q

# Creating API View set
class RetreatViewSet(viewsets.ViewSet):
   
    def create_retreat(self, request):
        try:
            serializer = RetreatSerializer(
                data=request.data,
                context={"request": request},
            )
           
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data={
                        "status": status.HTTP_201_CREATED,
                        "success": serializer.data,
                        "message": "Retreat  created successfully.",
                    },
                    status=status.HTTP_201_CREATED,
                )
            elif serializer.errors:
                serializer_errors = serializer.errors
                error_message = serializer_error(serializer_errors)
                return Response(
                    data={
                        "status": status.HTTP_400_BAD_REQUEST,
                        "error": error_message,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                data={
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


    def get_all_search_filter_retreat(self, request):
        """
        Retrieves and filters retreat details based on search queries and filters.
        """
        try:
            # Pagination parameters
            try:
                page = int(request.query_params.get("page", 1))
                items = int(request.query_params.get("items", 10))
            except Exception:
                page, items = 1, 10

            page = 1 if page == 0 else page
            items = 10 if 0 < items <= 1 else items

            offset = (page - 1) * items
            limit = page * items

            # Initial queryset
            retreat_details = RetreatDetails.objects.all()

            # Apply location filter if present
            location_filter = request.query_params.get("location", None)
            if location_filter:
                retreat_details = retreat_details.filter(location__icontains=location_filter)

            # Apply search filter if present
            search_query = request.query_params.get("search", None)
            filter_query = request.query_params.get("filter",None)
            if search_query:
                search_filter = (
                    Q(title__icontains=search_query) |
                    Q(description__icontains=search_query) |
                    Q(location__icontains=search_query) |
                    Q(retreat_type__icontains=search_query) |
                    Q(condition__icontains=search_query)
                )
                retreat_details = retreat_details.filter(search_filter)
            if filter_query:
                filter_query = (
                    Q(title__icontains=filter_query) |
                    Q(description__icontains=filter_query) |
                    Q(location__icontains=filter_query) |
                    Q(retreat_type__icontains=filter_query) |
                    Q(condition__icontains=filter_query)
                )
                retreat_details = retreat_details.filter(filter_query)
            

            # Check if any results are returned
            if not retreat_details.exists():
                return Response(
                    data={
                        "status": status.HTTP_200_OK,
                        "error": "No retreats available matching the criteria.",
                    },
                    status=status.HTTP_200_OK,
                )

            # Paginate results
            paginated_retreats = retreat_details[offset:limit]
            if not paginated_retreats:
                return Response(
                    data={
                        "status": status.HTTP_400_BAD_REQUEST,
                        "error": "Invalid page number or no results found.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Serialize data
            serializer = RetreatSerializer(instance=paginated_retreats, many=True)
            if serializer.data:
                paginated_data = pagination_utility(
                    total_entries=retreat_details,
                    page=page,
                    items=items,
                )
                return Response(
                    data={
                        "status": status.HTTP_200_OK,
                        "success": serializer.data,
                        "page_details": paginated_data,
                        "message": "Retreat details retrieved successfully.",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                serializer_errors = serializer.errors
                error_message = serializer_error(serializer_errors)
                return Response(
                    data={
                        "status": status.HTTP_400_BAD_REQUEST,
                        "error": error_message,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            return Response(
                data={
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

# Creating Booking View Set 
class BookingViewSet(viewsets.ViewSet):
    """
    Creates a new booking entry using data provided in the request.
    """
    def create_booking(self, request):
        try:

            serializer = BookingSerializer(
                data=request.data,
                context={"request": request},
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data={
                        "status": status.HTTP_201_CREATED,
                        "success": serializer.data,
                        "message": "Retreat Booked Successfully.",
                    },
                    status=status.HTTP_201_CREATED,
                )
            elif serializer.errors:
                serializer_errors = serializer.errors
                error_message = serializer_error(serializer_errors)
                return Response(
                    data={
                        "status": status.HTTP_400_BAD_REQUEST,
                        "error": error_message,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                data={
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

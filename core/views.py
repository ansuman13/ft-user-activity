# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from core.helpers.create_response import create_response
from core.models import User
from core.serializers import UserActivitySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


# TODO: incorporate create_response and exception handling
class UserActivityViewWithPagination(mixins.ListModelMixin,
                                     viewsets.GenericViewSet):
    """ User activity view with standard pagination
        url: '/api/users-paginated/
    """
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserActivitySerializer
    pagination_class = StandardResultsSetPagination


class UserActivityView(viewsets.ViewSet):
    """ User activity viewset, matching to given .json file
            url: '/api/users/
    """

    def list(self, request):
        try:
            # all users except django staff users.
            queryset = User.objects.filter(is_staff=False)
            serializer = UserActivitySerializer(queryset, many=True)
            return Response(create_response(True, data=serializer.data))
        except Exception as e:
            return Response(create_response(False, err_name='Something Went '
                                                            'Wrong',
                                            err_message=f'{e}'))

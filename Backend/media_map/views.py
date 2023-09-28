from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Media
from .serializers import MediaSerializer
from django.contrib.gis.geos import Point

@csrf_exempt
@require_POST
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        location = request.POST.get('location')  # Извлекаем location из запроса

        # Преобразуем строку location в объект Point
        if location:
            lat, lon = map(float, location.split(','))
            location_point = Point(lon, lat)
        else:
            location_point = None

        media = Media(image=image, location=location_point)
        media.save()
        serializer = MediaSerializer(media)
        return JsonResponse(serializer.data, safe=False, status=201)
    return JsonResponse({"error": "only POST method allowed"}, status=405)


def get_images(request):
    media = Media.objects.all()
    serializer = MediaSerializer(media, many=True)
    return JsonResponse(serializer.data, safe=False)

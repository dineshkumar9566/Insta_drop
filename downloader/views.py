from django.http import JsonResponse
from rest_framework.decorators import api_view
from .download_instagram_post import download_instagram_post,download_instagram_vedio,download_instagram_story  # Ensure this path is correct

@api_view(['POST'])
def download_post(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    try:
        download_instagram_post(url)
        return JsonResponse({'message': 'Post downloaded successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    


@api_view(['POST'])
def download_vedio(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    try:
        download_instagram_vedio(url)
        return JsonResponse({'message': 'Post downloaded successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def download_story(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    ig_username = 'safije15696'
    ig_password = 'Instadrop@1234'

    result = download_instagram_story(url, ig_username, ig_password)
    if 'error' in result:
        return JsonResponse({'error': result['error']}, status=500)
    else:
        return JsonResponse({'message': result['message']})
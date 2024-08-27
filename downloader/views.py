from django.http import JsonResponse,FileResponse
from rest_framework.decorators import api_view
from .download_instagram_post import download_instagram_post,download_instagram_video,download_instagram_story  # Ensure this path is correct
from io import BytesIO

@api_view(['POST'])
def download_post(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    # Instagram credentials
    ig_username = 'ranjithignored1one@gmail.com'  # Replace with your Instagram username
    ig_password = 'Instadrop@12345'  # Replace with your Instagram password

    try:
        # Pass the username and password as arguments to the function
        img_io, filename = download_instagram_post(url, ig_username, ig_password)
        if img_io:
            response = FileResponse(img_io, as_attachment=True, filename=filename)
            return response
        else:
            return JsonResponse({'error': 'Failed to download image'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# @api_view(['POST'])
# def download_video(request):
#     url = request.data.get('url')
#     if not url:
#         return JsonResponse({'error': 'URL parameter is required'}, status=400)

#     # Instagram credentials
#     ig_username = 'safije15696'  # Replace with your Instagram username
#     ig_password = 'Instadrop@1234'  # Replace with your Instagram password

#     try:
#         # Pass the username and password as arguments to the function
#         video_io, filename = download_instagram_video(url, ig_username, ig_password)
#         if video_io:
#             response = FileResponse(video_io, as_attachment=True, filename=filename)
#             return response
#         else:
#             return JsonResponse({'error': 'Failed to download video or the post is not a video'}, status=500)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def download_video(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    # Instagram credentials
    ig_username = 'ranjithignored1one@gmail.com'  # Replace with your Instagram username
    ig_password = 'Instadrop@12345'  # Replace with your Instagram password

    try:
        # Pass the URL, username, and password to the function
        video_io, filename = download_instagram_video(url, ig_username, ig_password)
        if video_io:
            response = FileResponse(video_io, as_attachment=True, filename=filename)
            return response
        else:
            return JsonResponse({'error': 'Failed to download video or the post is not a video'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)





from django.http import FileResponse, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .download_instagram_post import download_instagram_story
from io import BytesIO


@api_view(['POST'])
def download_story(request):
    url = request.data.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    # Instagram credentials
    ig_username = 'ranjithignored1one@gmail.com'  # Replace with your Instagram username
    ig_password = 'Instadrop@12345'  # Replace with your Instagram password

    try:
        # Pass the URL, username, and password to the function
        story_io, filename = download_instagram_story(url, ig_username, ig_password)
        if story_io:
            response = FileResponse(story_io, as_attachment=True, filename=filename)
            return response
        else:
            return JsonResponse({'error': 'Failed to download story or the post is not a story'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
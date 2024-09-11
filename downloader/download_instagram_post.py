import re
import instaloader
from PIL import Image
import time  # Add this import at the beginning
from io import BytesIO
import requests

# def download_instagram_video(url):
#     # Create an instance of Instaloader
#     loader = instaloader.Instaloader()

#     # Extract shortcode from the URL
#     shortcode = url.split("/")[-2]

#     print("shortcode:", shortcode)

#     # Download the video using the shortcode
#     try:
#         post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
#         # Check if the post is a video
#         if post.is_video:
#             video_url = post.video_url
            
#             # Fetch the video from the URL
#             response = requests.get(video_url)
#             video_io = BytesIO(response.content)
#             return video_io, f"{shortcode}_video.mp4"
#         else:
#             print("The post is not a video.")
#             return None, None
#     except Exception as e:
#         print(f"Error downloading video: {e}")
#         return None, None


import instaloader
import requests
from io import BytesIO

def download_instagram_video(url, ig_username, ig_password):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Login to Instagram
    try:
        loader.login(ig_username, ig_password)
    except Exception as e:
        print(f"Login failed: {e}")
        return None, None

    # Extract shortcode from the URL
    shortcode = url.split("/")[-2]

    print("shortcode:", shortcode)

    # Download the video using the shortcode
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        # Check if the post is a video
        if post.is_video:
            video_url = post.video_url
            
            # Fetch the video from the URL
            response = requests.get(video_url)
            video_io = BytesIO(response.content)
            return video_io, f"{shortcode}_video.mp4"
        else:
            print("The post is not a video.")
            return None, None
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None, None



# def download_instagram_post(url, username, password):
#     # Create an instance of Instaloader and log in
#     loader = instaloader.Instaloader()

#     try:
#         loader.login(username, password)

#         # Extract shortcode from the URL
#         shortcode = url.split("/")[-2]
#         print("shortcode:", shortcode)

#         # Retry logic in case of rate limiting
#         for _ in range(3):  # Retry up to 3 times
#             try:
#                 post = instaloader.Post.from_shortcode(loader.context, shortcode)
#                 break  # Exit loop if successful
#             except Exception as e:
#                 if "Please wait a few minutes" in str(e):
#                     print("Rate limited. Waiting before retrying...")
#                     time.sleep(60)  # Wait for 60 seconds before retrying
#                 else:
#                     raise e

#         # Get the thumbnail URL
#         thumbnail_url = post.url

#         # Fetch the image from the URL
#         response = requests.get(thumbnail_url)
#         image = Image.open(BytesIO(response.content))

#         # Convert image to BytesIO
#         img_io = BytesIO()
#         image.save(img_io, format='JPEG')
#         img_io.seek(0)

#         return img_io, f"{shortcode}_thumbnail.jpg"

#     except Exception as e:
#         print(f"Error downloading thumbnail: {e}")
#         return None, None



import requests
from io import BytesIO
from PIL import Image

def download_instagram_post(url, api_key, api_host):
    try:
        # Extract shortcode from the URL
        shortcode = url.split("/")[-2]
        print("shortcode:", shortcode)

        # Call the RapidAPI service to get post details
        api_url = f"https://{api_host}/media_info"
        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": api_host,
        }
        params = {"url": url}

        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 403:
            print("Access forbidden: Check your API key, host, or account status.")
            return None, None
        
        response.raise_for_status()  # Raise an error for other bad responses

        # Extract the image URL from the API response
        post_data = response.json()
        thumbnail_url = post_data['media']['display_url']

        # Fetch the image from the thumbnail URL
        image_response = requests.get(thumbnail_url)
        image_response.raise_for_status()

        # Convert image to BytesIO
        img_io = BytesIO(image_response.content)
        image = Image.open(img_io)
        img_io = BytesIO()
        image.save(img_io, format='JPEG')
        img_io.seek(0)

        return img_io, f"{shortcode}_thumbnail.jpg"

    except requests.RequestException as e:
        print(f"Error downloading thumbnail: {e}")
        return None, None



# import instaloader
# import requests
# from io import BytesIO
# from urllib.parse import urlparse, parse_qs

# def download_instagram_story(url, ig_username, ig_password):
#     # Create an instance of Instaloader
#     loader = instaloader.Instaloader()

#     # Login to Instagram
#     try:
#         loader.login(ig_username, ig_password)
#     except Exception as e:
#         print(f"Login failed: {e}")
#         return None, None

#     try:
#         # Extract the shortcode from the URL
#         parsed_url = urlparse(url)
#         path_parts = parsed_url.path.strip('/').split('/')
#         if len(path_parts) >= 2 and path_parts[0] == "stories":
#             username = path_parts[1]
#             story_id = path_parts[2]
#             print(f"Extracted username: {username}, story ID: {story_id}")
#         else:
#             print("Invalid URL structure. Could not extract username and story ID.")
#             return None, None

#         # Get the user's profile
#         profile = instaloader.Profile.from_username(loader.context, username)

#         # Iterate through stories to find the specific one with the extracted story_id
#         for story in loader.get_stories(userids=[profile.userid]):
#             for item in story.get_items():
#                 if item.mediaid == int(story_id):  # Match the story ID
#                     if item.is_video:
#                         video_url = item.video_url
#                         response = requests.get(video_url)
#                         video_io = BytesIO(response.content)
#                         return video_io, f"{username}_story_{item.date_utc}.mp4"
#                     else:
#                         print("The story is not a video.")
#                         return None, None

#     except Exception as e:
#         print(f"Error downloading story: {e}")
#         return None, None




import instaloader
import requests
from io import BytesIO
from urllib.parse import urlparse

def download_instagram_story(url, ig_username, ig_password):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Login to Instagram
    try:
        loader.login(ig_username, ig_password)
    except Exception as e:
        print(f"Login failed: {e}")
        return None, None

    try:
        # Extract the shortcode from the URL
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.strip('/').split('/')
        if len(path_parts) >= 2 and path_parts[0] == "stories":
            username = path_parts[1]
            story_id = path_parts[2]
            print(f"Extracted username: {username}, story ID: {story_id}")
        else:
            print("Invalid URL structure. Could not extract username and story ID.")
            return None, None

        # Get the user's profile
        profile = instaloader.Profile.from_username(loader.context, username)

        # Iterate through stories to find the specific one with the extracted story_id
        for story in loader.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                if item.mediaid == int(story_id):  # Match the story ID
                    if item.is_video:
                        # Download video
                        media_url = item.video_url
                        extension = ".mp4"
                    else:
                        # Download image
                        media_url = item.url
                        extension = ".jpg"
                    
                    response = requests.get(media_url)
                    media_io = BytesIO(response.content)
                    return media_io, f"{username}_story_{item.date_utc}{extension}"

    except Exception as e:
        print(f"Error downloading story: {e}")
        return None, None

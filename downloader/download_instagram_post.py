import re
import instaloader

def download_instagram_vedio(url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Extract shortcode from the URL
    shortcode = url.split("/")[-2]

    print("shortcode:", shortcode)

    # Download the video using the shortcode
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        # Check if the post is a video
        if post.is_video:
            video_url = post.video_url
            loader.download_pic(filename=f"{shortcode}_video.mp4", url=video_url, mtime=None)
            print(f"Video downloaded successfully as {shortcode}_video.mp4")
        else:
            print("The post is not a video.")
    except Exception as e:
        print(f"Error downloading video: {e}")


def download_instagram_post(url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Extract shortcode from the URL
    shortcode = url.split("/")[-2]

    print("shortcode:", shortcode)

    # Download the thumbnail using the shortcode
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        # Download the thumbnail
        thumbnail_url = post.url
        loader.download_pic(filename=f"{shortcode}_thumbnail.jpg", url=thumbnail_url, mtime=None)
        
        print(f"Thumbnail downloaded successfully as {shortcode}_thumbnail.jpg")
    except Exception as e:
        print(f"Error downloading thumbnail: {e}")


def download_instagram_story(story_url, ig_username, ig_password):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Login to be able to download stories
    try:
        loader.login(ig_username, ig_password)
    except Exception as e:
        return {'error': f'Error logging in: {e}'}

    # Extract the username from the URL
    match = re.search(r"instagram\.com/stories/([^/]+)/", story_url)
    if match:
        username = match.group(1)
        print(f"Extracted username: {username}")

        # Fetch the user's profile
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
        except Exception as e:
            return {'error': f'Error fetching profile: {e}'}

        # Download the user's stories
        try:
            stories = loader.get_stories(userids=[profile.userid])
            for story in stories:
                for item in story.get_items():
                    loader.download_storyitem(item, f"{username}_stories")
            
            return {'message': f'Stories downloaded successfully for user {username}'}
        except Exception as e:
            return {'error': f'Error downloading stories: {e}'}
    else:
        return {'error': 'Could not extract username from the provided URL.'}
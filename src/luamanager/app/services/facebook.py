from django.conf import settings
import facebook
import requests
from datetime import datetime

class FacebookFeed:
    token_url = 'https://graph.facebook.com/oauth/access_token'
    params = dict(client_id=settings.SOCIAL_AUTH_FACEBOOK_KEY, 
                  client_secret=settings.SOCIAL_AUTH_FACEBOOK_SECRET,
                  grant_type='client_credentials')

    @classmethod
    def get_fb_data(self, user, count=10,locale='pt_BR'):
        try:
            token_response = requests.get(url=self.token_url, params=self.params)
            access_token = token_response.text.split('=')[1]
            graph = facebook.GraphAPI(access_token)
            profile = graph.get_object(user)
            query_string = 'posts?limit={0}&locale={1}'.format(count, locale)
            posts = graph.get_connections(profile['id'], query_string)
            return profile, posts
        except facebook.GraphAPIError:
            return None

    @classmethod
    def parse_posts(self, posts, profile):
        parsed_posts = []

        for raw_post in posts:
            parsed_post = {}

            parsed_post['link'] = raw_post.get('link', profile.get('link'))
            parsed_post['created_at'] = datetime.strptime(raw_post.get(
                'created_time'), '%Y-%m-%dT%H:%M:%S%z')
            parsed_post['description'] = raw_post.get('story', raw_post.get('description', ''))
            parsed_post['message'] = raw_post.get('message', raw_post.get('description'))
            parsed_post['picture_url'] = raw_post.get(
                'picture', raw_post.get('icon', 'http://graph.facebook.com/{}/picture'.format(
                    profile.get('id'))))
            parsed_post['author'] = raw_post.get('name', raw_post.get('from', {}).get('name'))
            parsed_post['shares'] = raw_post.get('shares', {}).get('count', 0)

            parsed_posts.append(parsed_post)

        return parsed_posts


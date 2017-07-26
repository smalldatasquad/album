import datetime
from osf.scrapers.facebook import FbScraper
import json
import secrets

if __name__ == '__main__':

    # initialize scraper
    scraper = FbScraper(
        fb_username=secrets.fb_username,
        fb_password=secrets.fb_password
    )


    # fetch posts
    posts = scraper.get_posts(params={
        # list of usernames to pull posts from (as returned by get_friends above),
        'users': [secrets.fb_name],
        'after_date': datetime.datetime.now() - datetime.timedelta(days=secrets.num_days),
        # it will only get a maximum of this many posts from each user (no limit, if not supplied)
        'max_num_posts_per_user': secrets.max_posts,
    })

    with open('fb_posts.json', 'w') as fbp:
        json.dump(posts, fbp)

    print posts

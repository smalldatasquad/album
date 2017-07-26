import datetime

from osf.scrapers.facebook import FbScraper

if __name__ == '__main__':

    # initialize scraper
    scraper = FbScraper(
        fb_username='your-fb-email',    # the username you use to login to facebook with
        fb_password='your-fb-password'  # the password you use to login to facebook with
    )

    # fetch friends
    friends = scraper.get_friends_of_user(
        user='your-fb-username'     # the sting that appears in the URL when you navigate to your fb profile
    )
    print friends

    # fetch posts
    posts = scraper.get_posts(params={
        # list of usernames to pull posts from (as returned by get_friends above),
        'users': ['user1', 'user2'],
        # will only return posts after this date (in this case, posts in the last 7 days)
        'after_date': datetime.datetime.now() - datetime.timedelta(days=7),
        # it will only get a maximum of this many posts from each user (no limit, if not supplied)
        'max_num_posts_per_user': 25,
    })
    print posts

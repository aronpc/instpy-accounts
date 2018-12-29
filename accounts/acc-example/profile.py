import sys,os

sys.path.insert(0, '/code/')
sys.path.insert(0, '/personal/')

from instapy import InstaPy

insta_username  = ''
insta_password  = ''

bot = InstaPy(
        username=insta_username,
        password=insta_password,
        selenium_local_session=False, 
        multi_logs=True,
        nogui=True
)

bot.set_selenium_remote_session(selenium_url="http://%s:4444/wd/hub" % (os.environ['SELENIUM_URL']))
bot.login()

bot.set_skip_users(
        skip_private=True,
        private_percentage=100,
        skip_no_profile_pic=True,
        no_profile_pic_percentage=100,
        skip_business=True,
        business_percentage=100,
        skip_business_categories=[],
        dont_skip_business_categories=[]
)

bot.set_relationship_bounds(
        enabled=True,
        delimit_by_numbers=True,
        max_followers=8500,
        max_following=4490,
        min_followers=100,
        min_following=56,
        min_posts=10,
        max_posts=1000
)

bot.set_user_interact(amount=6, randomize=True, percentage=72, media='Photo')
bot.set_user_interact(amount=6, randomize=True, percentage=30, media='Video')
bot.set_do_follow(enabled=True, percentage=70)
bot.set_delimit_liking(enabled=True, max=1005, min=20)
bot.set_delimit_commenting(enabled=True, max=32, min=0)
bot.set_do_comment(True, percentage=80)
bot.set_dont_like([])
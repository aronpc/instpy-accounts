from selenium.common import exceptions
import time
import schedule
from profile import bot

def followComment():
    try:
        bot
        bot.set_comments(['@{} já fez passeio em arraial? Visite nosso ig e entre em contato com a gente']);
        bot.like_by_tags(['carioquissimo','cariocandonorio','021rio','destinoerrejota','napraiario','porainorio','partiubrasil','brasilpraiano','missaovt','voegol','beachesnresorts','thebestdestinations','caribebrasileiro','brasilpraiano','arraialdocabo','trip','022','regiaodoslagos','turismo','paradise','travel','vacation','riodejaneirogram','verao','destinocerto','destinobrasil','fantrip'],amount=100)

        unfollow
    except:
        import traceback
        print(traceback.format_exc())
        
def unfollow():
    try:
        bot
        bot.unfollow_users(amount=60, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
    except:
        import traceback
        print(traceback.format_exc())
def unfollowers():
    try:
        bot
        all_unfollowers, active_unfollowers = bot.pick_unfollowers(username=insta_username, compare_by="month", compare_track="first", live_match=True, store_locally=True, print_out=True)
    except:
        import traceback
        print(traceback.format_exc())


# Run Follow and comment
bot
unfollow
followComment

# Create schedule
schedule.every(6).to(8).hours.do(followComment())
schedule.every().day.at("06:30").do(unfollowers())

while True:
    schedule.run_pending()
    time.sleep(1)

import tweepy
import countdown
import datetime
import twitterCredentials as tc

auth = tweepy.OAuthHandler(tc.API_KEY, tc.API_SECRET_KEY)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

if __name__ == "__main__":
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        today = datetime.datetime.now()
        christmas = datetime.datetime(today.year, 12, 25)
        daysLeft = countdown.getDaysUntil(christmas)
        if daysLeft == 1:
            api.update_status("{} day until Christmas Day {}".format(daysLeft, today.year)) 
        else:
            api.update_status("{} days until Christmas Day {}".format(daysLeft, today.year))
    except tweepy.error.TweepError:
        print("Authentication Error")
        
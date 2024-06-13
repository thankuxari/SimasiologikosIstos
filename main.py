import twitter

consumer_key = '' #Your Consumer Key
consumer_secret = '' #Your Consumer Secret
access_token_key = '' #Your Acess Token Key
access_token_secret = '' #Your Acess Token Secret


api = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token_key,
                    access_token_secret=access_token_secret)
print(api.VerifyCredentials())
print('===')


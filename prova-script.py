consumer_key        = "ABCDEFGHIJKLKMNOPQRSTUVWXYZ"
consumer_secret     = "1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ"
access_token        = "ZYXWVUTSRQPONMLKJIHFEDCBA"
access_token_secret = "0987654321ZYXWVUTSRQPONMLKJIHFEDCB"

messages = [
    		"come state?",
    		"io molto bene!",
    		"oggi fa caldo!",
    		"domani piove!",
    		"che bel sole!",
    		"speriamo faccia bello..",
    		"che bella giornata!",
    		"che sonno!",
    		"si lavora!",
    		"pyhton <3",
    		"polpette!",
    		"ikea!",
    		"computer <3",
    		"fame!",
    		"sete!",
    		"biscotti <3",
    		"torta!",
    		"patatine <3",
    		"stanchissimo..",
    		"manca poco ;)",
    		"super caldo!",
    		"piscina!",
    		"argentina!",
    		"calcio!",
    		"forza ragazzi!",
	]


	import random

	from twython import Twython

	from auth import (
    		consumer_key,
    		consumer_secret,
    		access_token,
    		access_token_secret
	)

	twitter = Twython(
    		consumer_key,
    		consumer_secret,
    		access_token,
    		access_token_secret
	)


	message = random.choice(messages)
	twitter.update_status(status=message)
	print("Tweeted: %s" % message)

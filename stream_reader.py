import json
from pprint import pprint
import PIL, textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


import tweepy, time, sys, json, random
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'p2nfNrvxlcfkTTnh3HbdpSoBz' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'm8SxwarZuiqU0yCAd3e9RY8AIDAzJaiaWSw03wm4PZjtPoH3dh'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3066074927-IWBSMe5NHeNxK09avcgtD8qjDX2tdWXeRTFaEjs'#keep the quotes, replace this with your access token
ACCESS_SECRET = '7o9NL6YxRc81y9tkoY6iM0EDt48M4A5ZhBToVvhDaA8la'#keep the quotes, replace this with your access token secret

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

users_list = ["3066074927"]

def tweet_reply():
	#print t
	tweets_data_path = 'out.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
		#print line
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			continue

	#print tweets_data[0]['text']
	#print(tweets_data)
	print("Will call extract")
	tweet_data = tweets_data[0]
	user = tweet_data['user']['id_str']
	if user in users_list:
		print tracking user found


'''
def fact_from_same_decade():
	factList = []
	with open('scrape.txt') as f:
		lines = f.readlines()
		year = 1945
		lower_limit = year-10
		upper_limit = year+10
		for line in lines:
			#year_int = int(line[0:4])
			year_int = year_int_converter(line)
			#if year_int>=lower_limit and year_int<=upper_limit:
			factList.append(line)
				#count = count+1				
				#print("Line:"+line)
	random_fact = randomLine(factList)
	return random_fact

def year_int_converter(tweet):
	s = ""
	for i in tweet:
		if i==" ":
			break
		s = s+i
	return int(s)

def pList(factList):
	for val in factList:
		print(val)

def randomLine(factList):
	return random.choice(factList)

def subfilter(msg):
	print("In subfilter")
	print(msg)
	keyword_set = ["war","riot","riots","demonstration","demonstrations","march","rally"]
	for key in keyword_set:
		if key in msg.lower():
			print(msg)	
			return True
		else:
			print("Subfilter miss!!")
	return False
		
	

def extract(t,tweet_data):
	user = tweet_data['user']['screen_name']
	tweet = tweet_data['text']
	tweet_id = tweet_data['id']
	print("user:"+user+" "+str(tweet_id))
	if subfilter(tweet):
		message(t,user,tweet_id)
	return		

def check_api_limit():
	print("API limit checker code here")

def wrap_text(wrap,font,draw):
	margin = offset = 20
	margin = 40
	for line in wrap:
		draw.text((margin,offset),line,font=font,fill="#333333")
		offset += font.getsize(line)[1]

def create_image(message):
	wrap = textwrap.wrap(message,width=50)
	print(wrap)
	font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf",15)
	img=Image.new("RGBA", (450,150),(255,255,255))
	draw = ImageDraw.Draw(img)
	#draw.text((10, 10),message,(0,0,0),font=font)
	wrap_text(wrap,font,draw)
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)
	img.save("tweet_reply.png")


def message(t,user,tweet_id):
	f = fact_from_same_decade()
	print("In messages:"+t)
	#api.update_status(status=msg,in_reply_to_status_id=tweet_id)
	uni = unicode(f,"utf-8")
	create_image(uni)
	at = "@"+user
	at =""
	status = at+" "+"Did you also know that..."
	image = "tweet_reply.png"
	reply(image,status,tweet_id)
	#tall_tweet(f,tweet_id)
	return

def reply(image,status,reply_id):
	probability = 1
	rand = random.random()
	print("Probability value generated: "+str(rand))
	if rand<=probability:
		print("###################################################################")
		api.update_with_media(filename=image,status=status,in_reply_to_status_id=reply_id)	


def tall_tweet(tweet,tweet_id):
	n = len(tweet)
	if n > 140:
		n_tweet = n/125+1
		lower = 0
		higher = 125
		for i in range(0,n_tweet):
			s = tweet[lower:higher]
			if i==0:
				m = str((i+1))+"/"+str(n_tweet)+" "+s+"..."
				api.update_status(status=m,in_reply_to_status_id=tweet_id)		
			elif i<n_tweet-1:
				m= str((i+1))+"/"+str(n_tweet)+" "+"..."+s+"..."
				api.update_status(status=m,in_reply_to_status_id=tweet_id)
			else:
				m = str((i+1))+"/"+str(n_tweet)+" "+"..."+s
				api.update_status(status=m,in_reply_to_status_id=tweet_id)				
			lower = higher					
			higher = higher+125
	else:
		api.update_status(status=tweet,in_reply_to_status_id=tweet_id)

def do_print():

	tweets_data_path = 'out.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
		#print line
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			continue

#print tweets_data[0]['text']
	for tweet in tweets_data:
		print("Tweet-> ")
		print tweet['text']
		print tweet['user']['name']
	print "----------------------"
'''

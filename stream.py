#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime, sys, json, stream_reader

#enter the corresponding information from your Twitter application:
consumer_key = 'p2nfNrvxlcfkTTnh3HbdpSoBz' #keep the quotes, replace this with your consumer key
consumer_secret = 'm8SxwarZuiqU0yCAd3e9RY8AIDAzJaiaWSw03wm4PZjtPoH3dh'#keep the quotes, replace this with your consumer secret key
access_token = '3066074927-IWBSMe5NHeNxK09avcgtD8qjDX2tdWXeRTFaEjs'#keep the quotes, replace this with your access token
access_token_secret = '7o9NL6YxRc81y9tkoY6iM0EDt48M4A5ZhBToVvhDaA8la'#keep the quotes, replace this with your access token secret


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
	def __init__(self,api=None):
		super(StdOutListener, self).__init__()
		self.num_tweets = 0
		#self.tweet_reply = tweet
		self.date = datetime.datetime.now().day

	def check_day_change(self):
		print("pre invoked")
		current_date = datetime.datetime.now().day
		print(current_date)
		if self.date!=current_date:
			print("----------Date Changed!!!----------")
			self.date = current_date
			return False
		return 

	def on_data(self, data):
		#obj = json.loads(data)
		#print obj		
		'''		
		flag = self.check_day_change()
		if flag == False:
			return False
		'''
		#print self.pre()
		f = open('out.txt','a')
		f.write(data)
		f.close()
		self.num_tweets = self.num_tweets + 1
		if self.num_tweets < 1:
			return True
		else:
			self.answer()
			f = open('out.txt','w')
			f.truncate
			f.close
			return True
	def answer(self):
		print("Hello")
		stream_reader.tweet_reply()
		#stream_reader.do_print()
		self.num_tweets = 0
		return
	def on_error(self, status):
		print status

def stream_filter():
	print("Chintan")

#if __name__ == '__main__':
def main():
	#preprocessed_data = preprocess()
	#print("This is the reply:"+tweet_reply)
	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth,l)

	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	trackObj = ['#ThisDayInHistoryz','#factbotzz']
	stream.filter(track=trackObj)
	#print stream
	print("reaching end")
	return
main()	

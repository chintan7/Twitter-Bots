import urllib, json, mail
url = "https://www.googleapis.com/customsearch/v1?cx=008662286429643511382%3Ahuhedx4o3oq&num=5&key=AIzaSyBYwpXxkmbmofZsiLlB3UTVeuB3SF_PYfU&q=samsung+galaxy+s6"

#https://www.googleapis.com/customsearch/v1?cx=008662286429643511382%3Ascc_adghqs&key=AIzaSyBYwpXxkmbmofZsiLlB3UTVeuB3SF_PYfU&q=Apple

base_url = "https://www.googleapis.com/customsearch/v1?"
#https://www.googleapis.com/customsearch/v1?cx=008662286429643511382%3Ascc_adghqs8&q=Apple&key=AIzaSyBYwpXxkmbmofZsiLlB3UTVeuB3SF_PYfU
q="Apple"

#url = "https://www.googleapis.com/customsearch/v1?cx=008662286429643511382%3Ascc_adghqs8&q=Intel+Skylake&dateRestrict=d1&key=AIzaSyBYwpXxkmbmofZsiLlB3UTVeuB3SF_PYfU"


def set_query_from_tweet(query):
	q = query
	return config(q)

def get_json(url):
	print url
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	#print data
	#return data["items"][0]['formattedUrl']
	return data

def configuration_array():
	config_array = []
	with open('input.txt') as f:
		content = f.readlines()
		for line in content:
			config_array.append(line)
	return config_array 

def split_obj_on_equal(obj):
	key = []		
	val = []
	result_map = {}
	for each in obj:
		key.append(each.split('=')[0].strip())
		val.append(each.split('=')[1].strip())
	result_map['key'] = key
	result_map['value'] = val
	return result_map

def mapping():
	dictionary = {'custom_search_engine':'cx=','number_of_records':'&num=','key':'&key=','filetype':'&filetype=','daterestrict':'&daterestrict='}
	return dictionary

def package(map,q):
	url = base_url
	key = map['key']
	val = map['value']
	#print key,val
	mapper = mapping()
	count = 0
	for k in key:
		if k in mapper:
			if val[count]!="":
				url = url+mapper[k]+val[count]
				print (mapper[k]+val[count])
		count = count + 1
	return url+"&q="+q
	#print key

def package_text_file(content,q):
	package = q+"\n"
	try:
		items = content["items"]
		for item in items:
			title = item['title']
			link = item['link']
			snippet = item['snippet']
			package = package+title+"\n"+link+"\n"+snippet+"\n\n"
	except:
		print "Exception occured"
		package=""
		return package
	return package
	
def config(q):					#q is the Query that comes from Twitter
	lines = configuration_array()		#returns an array with the configuration
	config = split_obj_on_equal(lines)	#create result map with key and val
	url = package(config,q)			#package & build the url for the GET request
	url_search = get_json(url)		#returns JSON from the GET request
	pack = package_text_file(url_search,q)	#creates a Text file the content to email
	if pack!="":				#if the GET request doesn't include valid JSON, we neglect it 
		pack = pack.encode('utf-8')
		print pack
	#print str(url_search)
		result = mail.run(pack)		#calls mail script and sends the String to be sent as a text file
		if result:
			print("tweet sent")
		else:
			print("tweet error")
	else:
		print("Error in Google Search")
	return result
	
#config(q)
#015796917904326428222:ykywojpcoes - Media news
#https://www.googleapis.com/customsearch/v1?cx=008662286429643511382:scc_adghqs8&key=AIzaSyBYwpXxkmbmofZsiLlB3UTVeuB3SF_PYfU&num=5&q=Apple

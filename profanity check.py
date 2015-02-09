import urllib

def read_text(): 
	quotes= open("C:\detect_profanity\movie_quotes.txt")
	contents_of_file= quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profnaity(contents_of_file)


def check_profanitiy(text_tocheck): 
	 connection = urllib.urlopen("http://www.wdyl.com/profanity?q=shot")
	 print(output)
	 connection.close()


read_text() 

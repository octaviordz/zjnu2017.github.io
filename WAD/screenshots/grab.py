
#username,  github
githuburls = '../marks/data/github.csv'

fp = open(githuburls, 'r')
txt = fp.read()
fp.close()
fp = 0

urls = []
lines = txt.split('\n')
for x in range(1,len(lines)):
	line = lines[x]
	urlparts = line.split(',')
	if len(urlparts) < 2:
		continue
	url = urlparts[1]
	
	if x == 1:
		if 'http' not in url:
			1/0
	url = url.replace(' ', '')
	url = url.replace('\t', '')
	urls.append( url )
	

#urls = [ 'http://www.bing.com',
#		 'http://www.baidu.com',
#         'https://zjnu2017.github.io',
#		 'http://www.cats.com' ]

import os
if not os.path.exists( 'screenshots' ):
    os.makedirs( 'screenshots' )
		 

		 
import ghost

g = ghost.Ghost()


session = g.start(wait_timeout=20)
for i in range(0, len(urls) ):
	
	url = urls[i]
	print('Opening url: ' + url)
	try:
		page, extra_resources = session.open( url )
			#page, extra_resources = session.open("https://zjnu2017.github.io")
			#if page.http_status == 200 and \
			#      'The Universal Operating System' in page.content:
		if page.http_status == 200:
			print("Good!")
		else:
			print('Bad')
				
		print('Starting saving screenshot:' + url)
		screenshotname = 'screen%02d' % (i)
		session.capture_to('screenshots//' + screenshotname + '.png')
		print('Finished saving screenshot' + screenshotname + '.png')
	except:
		print('Error trying to get page')
		pass
#	g.stop();

g.exit()

print('Goodbye')
exit()

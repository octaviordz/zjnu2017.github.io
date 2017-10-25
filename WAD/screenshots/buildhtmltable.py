

html='''</head>
<body>
<div id="wrapper">
    <div id="content">
        <h2>GitHub Web Design and Development (WDD)</h2>
        <table>
            <tbody>
                <TABLEBODY>
            </tbody>
        </table>    
    </div>
<div>
</body>
</html>'''

import os
#files = os.listdir( './screenshots/' )



#username,  github
githuburls = '../marks/data/github.csv'

fp = open(githuburls, 'r')
txt = fp.read()
fp.close()
fp = 0

table = ""
table += "<tr>\n"

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
	
	table += '<td width=220 height=220 style="vertical-align:bottom;">\n'
	filename = './screenshots/screen%02d.png' % (x-1);
	print filename
	if ( os.path.exists( filename ) ):
		table += '<img src="'
		table += filename
		table += '" width="220" height="220"><br>\n'
	table += 'url: ' + '<a href="' + url + '">' + url + '</a>\n'
	table += "</td>\n"

	if ( x % 4 == 0 ):
		table += "</tr>\n"
		table += "<tr>\n"
	
table += "</tr>\n"	


#for x in range(0, len(files)):
#	filename = files[x]
#	if '.png' not in filename:
#		1/0
#	num = filename[6:8]
#	print num
#	num = int(num)
#	urlname = urls[num]
	

html = html.replace('<TABLEBODY>', table)
	
fp = open('table.html', 'w')
fp.write(html)
fp.close()
fp = 0
	
	
	
	
	
	
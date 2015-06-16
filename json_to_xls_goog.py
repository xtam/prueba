import re, htmlentitydefs
import json
from sys import argv


def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is 
    return re.sub("&#?\w+;", fixup, text)
    

print "JSON File?"	
file = raw_input()
inn = file + ".json"
out= file + ".txt"

data = []
with open(inn) as f:
    for line in f:
        data.append(json.loads(line))
#pprint(data)

f = open(out,"w+")

for e in data[0]:
	f.write(e + "\t")
f.write("\n")
for e in data:
	for a, b in e.items():
		if type(b) == int:
			b = str(b)
		b = ''.join(b)
		b = unescape(b)
		b = b.encode('utf-8')
		b = re.sub('<.*?>','',b)
		b = re.sub('\\n','',b)
		b = re.sub('\s\s\(\)\s\s','',b)
		f.write(b + "\t")
	f.write("\n")
f.close()

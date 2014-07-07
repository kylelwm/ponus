from modules.models import Module
import json
import io

json_modules = io.open('modules.json', encoding='utf-8').read()
decoded_modules = json.loads(json_modules)

a = []

for module in decoded_modules:
	c = str(module['Department'])
	print "Adding %s to the list." % c
	a.append(c)

b = set(a)
print b;

d = '": "",\n"'.join(b)
text = open('AllDepartment.txt', 'a+')
text.write(d)
text.close()
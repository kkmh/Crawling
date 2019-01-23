```
shodan host 
```

import shodan

SHODAN_API_KEY = " key "
api = shodan.Shodan(" key ")
host = api.host(' IP ', history=True)

print """

IP : %s
Organization : %s
Operating System : %s
""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))


for item in host['data']:
	print """
		Port : %s
		Banner : %s
		""" % (item['port'], item['data'])

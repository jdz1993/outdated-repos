# -*- coding:utf-8 -*-
import urllib
import urllib2
import json

url = "10.231.10.82:6888/call/CCLiveService?method=AnchorsOnline"

def http_get(url,params):
	req = urllib2.Request(url)
	print req

# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print res



def process():
	d = {
		'method':'AnchorsOnline',
		'args':{
			'game':10109,
			'anchor_urs': 'abc@163.com',
			'anchor_ccid': 12345,
			'anchor_nick': u'我是一个兵',
			'anchor_uid': 	12345908,
			'invite_msg': u'来看直播了',
			'game_uid': 123456789,
			'game_host': 9999,
		},
	}
	#d= []
	params = d # json.dumps(d)
	url = "10.231.10.82:6888/call/CCLiveService"
	urlencode_params = urllib.urlencode(params)
	final_url = '{}?{}'.format(url,urlencode_params)
	print '[d]{} [params]{} [url]{} [urlencode_params]{} [final_url]{}' \
		  ''.format(d,params,url,urlencode_params,final_url)

def main():
	process()

if __name__ == '__main__':
	main()

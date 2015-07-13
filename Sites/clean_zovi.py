import sys
import json

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    lst = []
    k=0
    l = len(json_data)
    for item in json_data:
        if k == l-1:
            break
    	new_json = {}
        if item['price'][0] == " ":
            new_json['price'] = item['price'][1]
        else:
            new_json['price'] = item['price'][0]
    	new_json['prodlink'] = "http://zovi.com/"+item['prodlink'][0]
    	new_json['brand'] = item['brand']
    	new_json['imglink'] = "http:"+item['imglink'][0]
    	new_json['desc'] = item['desc'][0]
    	lst.append(new_json)
        k = k+1

    for item in lst:
    	s_lstripped = item['price'].lstrip()
    	s_rstripped = s_lstripped.rstrip()
    	item['price'] = "Rs."+s_rstripped

    print json.dumps(lst)

    # try:
    # 	# with open('zovi_legjeg_clean_nov14.json', 'w') as outfile:
    # 	# 	json.dump(lst, outfile)
    # except:
    # 	print "nahin chala bey"


if __name__ == '__main__':
    main()
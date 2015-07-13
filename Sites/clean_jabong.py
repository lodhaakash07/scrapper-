import sys
import json

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    lst = []
    i = 0
    for item in json_data:
        new_json = {}
        new_json['price'] = item['price'][0]
        new_json['prodlink'] = item['prodlink'][0]
        new_json['brand'] = item['brand'][0]
        new_json['imglink'] = item['imglink'][0]
        new_json['desc'] = item['desc'][0]
        lst.append(new_json)
        i+=1

    for item in lst:
    	s_lstripped = item['desc'].lstrip()
    	s_rstripped = s_lstripped.rstrip()
    	item['desc'] = s_rstripped

    print json.dumps(lst)

    # try:
    # 	with open('jab_trends_clean_nov15.json', 'w') as outfile:
    # 		json.dump(lst, outfile)
    # except:
    # 	print "nahin chala bey"


if __name__ == '__main__':
    main()
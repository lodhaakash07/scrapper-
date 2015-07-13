import sys
import json

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    lst = []
    i = 0
    for item in json_data:
        try:
            new_json = {}
            new_json['price'] = item['price'][0]
            new_json['prodlink'] = "http://www.fashionara.com"+item['prodlink'][0]
            new_json['brand'] = item['brand'][0]
            new_json['imglink'] = item['imglink'][0]
            new_json['desc'] = item['desc'][0]
            lst.append(new_json)
            i+=1
        except:
            pass

    for item in lst:
        s_lstripped = item['price'].lstrip()
        s_lstripped_des = item['desc'].lstrip('\n')
        s_lstripped_des = s_lstripped_des.lstrip('\t')
        s_rstripped_des = s_lstripped_des.rstrip('\t')
        # s_rstripped_des = s_rstripped_des.split('(')[0]
        item['price'] = "Rs."+s_lstripped
        item['desc'] = s_rstripped_des


    print json.dumps(lst)

    # try:
    # 	with open('jab_trends_clean_nov15.json', 'w') as outfile:
    # 		json.dump(lst, outfile)
    # except:
    # 	print "nahin chala bey"


if __name__ == '__main__':
    main()
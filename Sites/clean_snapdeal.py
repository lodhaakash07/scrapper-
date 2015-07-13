import sys
import json

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    lst = []
    for item in json_data:
    	new_json = {}
    	new_json['price'] = item['price'][0]
    	new_json['prodlink'] = item['prodlink'][0]
    	new_json['brand'] = item['brand']
    	new_json['imglink'] = item['imglink'][0]
    	new_json['desc'] = item['desc'][0]
    	lst.append(new_json)

    # brandlist = ["Vero Moda", "Wills Lifestyle", "Van Heusen", "Allen Solly", "Levi's", "Remanika", "Jealous 21"]

    # for brand in brandlist:
    #     for item in lst:
    #         if brand in item['desc']:
    #             # s = item['desc'].split(brand)[0]
    #             item['brand'] = brand

    print json.dumps(lst)


if __name__ == '__main__':
    main()
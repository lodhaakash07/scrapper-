import sys
import json

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    lst = []
    for item in json_data:
        new_json = {}
        new_json['price'] = item['price'][0]
        new_json['prodlink'] = 'http://www.myntra.com/'+item['prodlink'][0]
        new_json['brand'] = item['brand'][0]
        new_json['imglink'] = item['imglink'][0]
        new_json['desc'] = item['desc'][0]
        lst.append(new_json)
    print json.dumps(lst)
    
if __name__ == '__main__':
    main()
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

    for item in lst:
    	s_lstripped = item['price'].lstrip()
    	#s_rstripped = s_lstripped.rstrip()
    	item['price'] = "Rs."+s_lstripped

    brandlist = ["3 Mad Chicks", "AKA Designed by PATRICK COX for KOOVS", "AX PARIS", "Baggit", "Bellfield", "BRAVE SOUL", "CATWALK88", "Cheap Monday", "Cupidity", "DAISY STREET", "Desi Drama Queen", "DEAD LOVERS", "Done by None", "DREAMS", "FabAlley", "Femella", "Femme Fatale", "FOREVER NEW", "GAS", "GINGER FIZZ", "GIRLS ON FILM", "Glamorous", "HENRY HOLLAND for KOOVS", "J.D.Y", "KOOVS", "Ladida", "Lipsy", "Little Mistress", "Melika M", "NEON ROSE", "New Look", "Nike", "OASIS", "OLIV", "ONLY", "PAPER DOLLS", "Pepe Jeans", "Spring Break", "Stalk Buy Love", "Steve Madden", "Style Fiesta", "VERO MODA", "Vila", "WAREHOUSE", "Youshine"]

    for brand in brandlist:
        for item in lst:
            if brand in item['desc']:
                # s = item['desc'].split(brand)[0]
                item['brand'] = brand

    print json.dumps(lst)

    # try:
    # 	with open('koovs_legjeg_clean_nov13.json', 'w') as outfile:
    # 		json.dump(lst, outfile)
    # except:
    # 	print "nahin chala bey"


if __name__ == '__main__':
    main()
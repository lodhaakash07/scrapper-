import sys
import json
import urllib2
import time
import os

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    i = 0
    lst=[]
    save_path = "~/pro_candice/images/fashionara/cropped_faslegging/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for item in json_data:
        # try:
        #     item['imglink'][0]
        # except:
        #     print item['imglink']
        # if i > 6865:
        try:
            # if i < 500:
            localimg = {}
            # print type(item['imglink'])
            img = urllib2.urlopen(item['imglink'])
            localfile = open('~/pro_candice/images/fashionara/cropped_faslegging/'+'fas_00_lj'+str(i)+'.jpg', 'wb')
            localimg[item['prodlink']] = localfile.name
            localfile.write(img.read())
            localfile.close
            lst.append(localimg)
            time.sleep(1)
            i+=1
            print i
        except:
            # print item['imglink'] + '' + "not found"
            pass
        # else:
        #     localimg = {}
        #     localfile = open('/home/deb/pro_candice/images/myntra/topsdummy/'+'myn_00_tp'+str(i)+'.jpg', 'wb')
        #     localimg[item['prodlink']] = localfile.name
        #     localfile.close
        #     lst.append(localimg)
        #     i+=1
        #     print i


    try:
        with open('~/pro_candice/images/fashionara/cropped_faslegging/fas_localimg_legging.json', 'w') as outfile:
            json.dump(lst, outfile)
    except:
        print "nahin chala bey"

if __name__ == '__main__':
    main()
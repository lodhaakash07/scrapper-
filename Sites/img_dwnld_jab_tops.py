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
    save_path = "~/pro_candice/images/jabong/cropped_jtops/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for item in json_data:
        # try:
        #     item['imglink'][0]
        # except:
        #     print item['imglink']
        # if i > 1824:
        try:
            # if i < 500:
            localimg = {}
            # print type(item['imglink'])
            img = urllib2.urlopen(item['imglink'])
            localfile = open('~/pro_candice/images/jabong/cropped_jtops/'+'ja_00_tp'+str(i)+'.jpg', 'wb')
            localimg[item['prodlink']] = localfile.name
            localfile.write(img.read())
            localfile.close
            lst.append(localimg)
            time.sleep(1)
            i+=1
            print i
        except:
            # print item['imglink'][0] + '' + "not found"
            pass
        # else:
        #     localimg = {}
        #     localfile = open('~/pro_candice/images/jabong/bagsdummy/'+'ja_00_bg'+str(i)+'.jpg', 'wb')
        #     localimg[item['prodlink']] = localfile.name
        #     localfile.close
        #     i+=1
        #     print i

    try:
        with open('~/pro_candice/images/jabong/cropped_jtops/jab_localimg_tops.json', 'w') as outfile:
            json.dump(lst, outfile)
    except:
        print "nahin chala bey"

if __name__ == '__main__':
    main()
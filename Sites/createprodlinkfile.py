import sys
import json

def main():
    json_file = open(sys.argv[1])
    json_data = json.load(json_file)
    for item in json_data:
      print item['prodlink']
if __name__ == '__main__':
    main()  
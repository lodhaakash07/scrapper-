declare -a spiders=(koovs_dress koovs_leggings koovs_tops koovs_handbags)
declare -a big_spiders=(big_koovs_dress big_koovs_leggings big_koovs_tops big_koovs_handbags)
declare -a download_py=(img_dwnld_koovs_dress.py img_dwnld_koovs_legging.py img_dwnld_koovs_tops.py img_dwnld_koovs_bags.py)
n=0
for i in "${spiders[@]}"
do
   filename="$i.json"
   clean_filename="clean$i.json"
   url_filename="url$i.json"
   big_filename="big$i.json"
   rm $filename
   rm $clean_filename
   rm $big_filename
   scrapy crawl $i -o $filename -t json
   python clean_koovs.py $filename > $clean_filename
   rm $url_filename
   python createprodlinkfile.py $clean_filename > $url_filename
   scrapy crawl ${big_spiders[n]} -o $big_filename -t json  
   python ${download_py[n]} $big_filename
   n=$(( n + 1 ))
done
rm *.pyc
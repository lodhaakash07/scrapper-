declare -a spiders=(jabong_dress jabong_leggings jabong_tops jabong_handbags)
declare -a big_spiders=(big_jabong_dress big_jabong_leggings big_jabong_tops big_jabong_handbags)
declare -a download_py=(img_dwnld_jab_dress.py img_dwnld_jab_legging.py img_dwnld_jab_tops.py img_dwnld_jab_bags.py)
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
   python clean_jabong.py $filename > $clean_filename
   rm $url_filename
   python createprodlinkfile.py $clean_filename > $url_filename
   scrapy crawl ${big_spiders[n]} -o $big_filename -t json  
   python ${download_py[n]} $big_filename
   n=$(( n + 1 ))
done
rm *.pyc
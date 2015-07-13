declare -a spiders=(yepme_dress yepme_leggings yepme_tops)
declare -a big_spiders=(big_yepme_dress big_yepme_leggings big_yepme_tops)
declare -a download_py=(img_dwnld_yepme_dress.py img_dwnld_yepme_legging.py img_dwnld_yepme_tops.py)
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
   python clean_yepme.py $filename > $clean_filename
   rm $url_filename
   python createprodlinkfile.py $clean_filename > $url_filename
   scrapy crawl ${big_spiders[n]} -o $big_filename -t json  
   python ${download_py[n]} $big_filename
   n=$(( n + 1 ))
done
rm *.pyc
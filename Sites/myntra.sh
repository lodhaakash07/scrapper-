declare -a spiders=(myntra_dress myntra_leggings myntra_tops myntra_handbags)
declare -a big_spiders=(big_myntra_dress big_myntra_leggings big_myntra_tops big_myntra_handbags)
declare -a download_py=(img_dwnld_myn_dress.py img_dwnld_myn_legging.py img_dwnld_myn_tops.py img_dwnld_myn_bags.py)
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
   python clean_myntra.py $filename > $clean_filename
   rm $url_filename
   python createprodlinkfile.py $clean_filename > $url_filename
   scrapy crawl ${big_spiders[n]} -o $big_filename -t json  
   python ${download_py[n]} $big_filename
   n=$(( n + 1 ))
done

rm *.pyc
#!/bin/bash
cd ./Sites
cmd=(dialog --separate-output --checklist "Kitne bhi choose kar :D " 22 76 16)
options=(1 "Jabong" off    
         2 "Myntra" off
         3 "Snapdeal" off
         4 "Flipkart" off
         5 "Fashionara" off
         6 "Koovs" off
         7 "Stackbuylove" off
         8 "Zovi" off
         9  "Yepme" off
         10 "Bahar Nikal" off)
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
clear
for choice in $choices
do
    case $choice in
            1)
            ./jabong.sh
            ;;
            2)
            ./myntra.sh
            ;;
            3)
            ./snapdeal.sh
            ;;
            4)
            ./flipkart.sh
            ;;
            5)
            ./fashionara.sh
            ;;
            6)
            ./koovs.sh
            ;;
            7)
            ./stackbuylove.sh
            ;;
            8)
            ./zovi.sh
            ;;
            9)
            ./yepme.sh
            ;;
            10)
            echo chutiya hai kya
            ;;
    esac
done

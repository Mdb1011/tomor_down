#Mohammad
#Tomor.apk
clear
kill_color=$'\e[0m'
command -v youtube-dl &>/dev/null || printf "\e[031m Please install Youtube-dl manualy or run the the install.sh script again.\n$kill_color"

#uncomment me if you wish :)
#[[ -f ~/bin ]] || printf "\e[031m Please Run the the install.sh script.\n$kill_color"


echo -e "\e[031m" "     + +  ▄▀▄     ▄▀▄   +  +"  
echo -e "\e[031m" "       + ▄█░░▀▀▀▀▀░░█▄ +"
echo -e "\e[031m" "     ▄▄  █░░░░░░░░░░░█  ▄▄"
echo -e "\e[031m" "    █▄▄█ █░░█░░┬░░█░░█ █▄▄█"
echo -e "\e[036m" "╔════════════════════════════════════════╗"                                                                          
echo -e "\e[032m" "║ ♚ Project Name : Tomor-Down            ║"
echo -e "\e[032m" "║ ♚ Author : Mohammad Tomor              ║"
echo -e "\e[032m" "║ ♚ Github :g̲i̲t̲h̲u̲b̲.̲c̲o̲m̲/̲Mdb1011/tomor_down║"
echo -e "\e[032m" "║ ♚ Rubika : Tomor_apk                   ║"
echo -e "\e[036m" "╠════════════════════════════════════════╝"
echo -e "\e[036m" "╠═▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁]  ➳"
echo -e "\e[032m" "╠═▶ 1. Music Mp3♫"
echo -e "\e[032m" "╠═▶ 2. Video 360p"
echo -e "\e[032m" "╠═▶ 3. Video 480p"
echo -e "\e[032m" "╠═▶ 4. Video 720p"
echo -e "\e[032m" "╠═▶ 5. Video 1080p"
echo -e "\e[032m" "╠═▶ 6. Video 2160p"
echo -e "\e[032m" "╠═▶ 7. Exit TOMOR-down" # Added
command='-no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s -f'

#Edit From Oak Atsume 
printf "\e[032m ╚═:➤  $kill_color"
read option

if [[ -z $option ]];
then
	clear
	printf "\e[031m Please choose a option!\n$kill_color"
else
case $option in #Make Case list
	1)
	echo "$command 140" > ~/.config/youtube-dl/config #option 1
	youtube-dl $1
	;;
	2)
	echo "$command \"best[height<=360]\"" > ~/.config/youtube-dl/config #option 2
	youtube-dl $1
	;;
	3)
	echo "$command \"best[height<=480]\"" > ~/.config/youtube-dl/config #option 3
	youtube-dl $1
	;;
	4)
	echo "$command \"best[height<=720]\"" > ~/.config/youtube-dl/config #option 4
	youtube-dl $1
	;;
	5)
	echo "$command \"best[height<=1080]\"" > ~/.config/youtube-dl/config #option 5
	youtube-dl $1
	;;
	6)
	echo "$command \"best[height<=2160]\"" > ~/.config/youtube-dl/config
    	youtube-dl $1
	;;
	7)
	break
	;;
esac 
fi



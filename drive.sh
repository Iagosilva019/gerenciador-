
desmontar(){
          cd docs/TXT && fusermount -u  gdrive
          echo " "
          echo -e "Desmontado com sucesso"

          rmdir gdrive
          echo -e "pasta deletada com sucesso"

}
montar(){
         cd docs/TXT && mkdir gdrive && google-drive-ocamlfuse gdrive
         echo " "
         echo -e "Pasta criada com sucesso"
}

repositorio(){
         echo " "
         echo -e "-----------------------Adicionando repositório do gdrive--------------------------"
         echo " "
         sudo add-apt-repository ppa:alessandro-strada/ppa -y && sudo apt-get update -y #Adicionanando repositorio
         echo " "
         echo -e "-------------------------Instalando gdrive------------------------------"
         echo " "
         sudo apt-get install google-drive-ocamlfuse -y #Instalando gdrive
         echo " "
         echo -e "-------------------------Acesso ao google drive---------------------------"
         echo " "
         google-drive-ocamlfuse  #acesso ao google drive
         echo " "
         echo -e "--------------------------Concluido com sucesso--------------------------"

}

echo -e "╭━━━╮  ╭╮
┃╭━╮┃  ┃┃
┃┃ ╰╯╭━╯┃╭━╮╭╮╭╮╭╮╭━━╮
┃┃╭━╮┃╭╮┃┃╭╯┣┫┃╰╯┃┃┃━┫
┃╰┻━┃┃╰╯┃┃┃ ┃┃╰╮╭╯┃┃━┫
╰━━━╯╰━━╯╰╯ ╰╯ ╰╯ ╰━━╯"
menu(){
        echo " "
        echo -e "[1] - Adicionar repositorio"
        echo -e "[2] - Montar gdrive"
        echo -e "[3] - Desmontar gdrive"
        echo -e "[0] - Sair"
        echo  " "
        read  -n 1 -p "[+] O que deseja fazer:" s
        case $s in
        1) repositorio ;;
        2) montar ;;
        3) desmontar ;;
        0) exit;;
        esac
menu
}

menu


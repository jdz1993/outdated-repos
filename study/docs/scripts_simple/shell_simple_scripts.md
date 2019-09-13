1.ssh remote control or copy or etc.

    sudo service ssh start
    ssh <username>@<hostname>
    scp <username>@<hostname>:file <localfile>
    
2.find file

    find / -iname 'ABC*DE'
    find . -iname 'ABC*DE'
    
3.simple shell script

    i=0;
    while [ $i -le 5 ]
    do 
        echo "hello world $i times"
        i=$((i+1))
    done 

    #fakedir= /home/dezhi/Dezhi/Models/model1
    #dir="/home/dezhi/Dezhi/Models"
    #for VAR  in  /home/dezhi/Dezhi/Models/model1
    #do
    #	echo VAR
    #	echo $VAR
    #	echo "$VAR"
    #done
    #


    dir="/home/dezhi/Dezhi/Models"
    for VAR in $dir/*
    do
        echo $VAR
    done
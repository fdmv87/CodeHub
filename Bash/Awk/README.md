# awk

awk is a text-processing tool in Unix and Linux, mostly used for pattern scanning and processing.

## Commonly Used Special Variables

* **FS**    Field separator (default: a blank)
* **NF**    Number of fields in current record
* **NR**    Number of the current record
* **OFS**   Output field separator (default: a blank)
* **ORS**   Output record separator (default: a newline)
* **RS**    Record separator (default: a newline)


## Commands

* **if** (conditional) statement [**else** statement]
* **while** (conditional) statement
* **for** (expression; conditional; expression) statement
* **for** (variable in array) statement
* **break**
* **continue**
* {**[statement]**}
* **variable=expression**
* **print[expression-list][> expression]**
* **printf format [, expression-list][> expression]**
* **next**
* **exit**


## General format of an awk script

    BEGIN { action(s) }         # do actions before the line-by-line processing. i.e. at set up
    pattern { action }          # for each line, check against the given pattern in the given order. If a match, perform the corresponding action
    pattern { action }
    ...
    END { action(s) }           # do actions after the line-by-line processing.

### awk script sample

```bash
#! /usr/bin/awk -f

BEGIN {FS=";"}                  #delimiter is ;

NR==1 {next;}                   #if number of row is 1, skip it (skip the header)
$3 == "M" { print;count++;}     #if colunm 3 has M, print the record and increment the count

END {print "The number of masculine nouns are ", count}
```

######

to execute:

    cat <filename> | script_name.awk

## Arrays

```bash
#! /usr/bin/awk -f

BEGIN {FS=";"}

NR==1 {next;}

$3 ~ /M/ {masc[$2]=$1}
$3 ~ /F/ {fem[$2]=$1}

END {

print "\nMasculine Nouns\n";
    for (x in masc)
        { print x " - " masc[x] }
print "\nFeminine Nouns\n";
    for (y in fem)
        { print y " - " fem[y] }
}
```


## print function

    $ps

    PID TTY           TIME CMD
    22238 ttys004    0:00.02 /bin/zsh -il

    ps | awk '{print $1}'
    PID
    22238

    ps | awk '{print $2}'
    TTY
    ttys004


######

    df | awk 'NR==7, NR==11 {print NR, $0}'
    #NR number of records (line numbers)
    #NR==7, NR==11 is a range between 7 and 11

    7 /dev/disk1s2      1024000     12328    987064     2%       1    4935320    0%   /System/Volumes/xarts
    8 /dev/disk1s1      1024000     12520    987064     2%      29    4935320    0%   /System/Volumes/iSCPreboot
    9 /dev/disk1s3      1024000      2368    987064     1%      51    4935320    0%   /System/Volumes/Hardware
    10 /dev/disk3s5    965595304 145784408 766687608    16%  264592 3833438040    0%   /System/Volumes/Data
    11 map auto_home           0         0         0   100%       0          0     -   /System/Volumes/Data/home


## Count lines

    cat /etc/shells | wc -l
    11

    awk 'END {print NR}' /etc/shells
    #END returns only the last line number
    11


## Read files

    cat /etc/passwd

    nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1:System Services:/var/root:/usr/bin/false

######

    awk -F ":" '{print $1}' /etc/passwd
    #-F for field separator

    nobody
    root
    daemon

######

    awk -F ":" '{print $1"\t"$6"\t"$7}' /etc/passwd

    nobody  /var/empty      /usr/bin/false
    root    /var/root       /bin/sh
    daemon  /var/root       /usr/bin/false

######

    awk 'BEGIN{FS=":"; OFS="\t"} {print $1,$6,$7}' /etc/passwd
    #FS field separator
    #OFS output field separator

    nobody  /var/empty      /usr/bin/false
    root    /var/root       /bin/sh
    daemon  /var/root       /usr/bin/false

###### 

    cat /etc/shells
    
    /bin/bash
    /bin/csh
    /bin/dash
    /bin/ksh
    /bin/sh
    /bin/tcsh
    /bin/zsh

    awk -F "/" '/^\// {print $NF}' /etc/shells | uniq | sort
    #-F "/": This option sets the field separator to a forward slash
    #regular expression must be inside / /  
    #search for text begin with "/". \ is the escape character
    #$NF prints last field
    #uniq remove duplicates
    #sort alphabetically

    bash
    csh
    dash
    ksh
    sh
    tcsh
    zsh

######

    awk '$1 ~/^[b,c]/ {print $0}' <filename>
    #print every line which the first column needs to match ^[b,c] (begin with b or c)


## IF statement

    ps -ef | awk '{ if($NF == "/usr/libexec/WiFiVelocityAgent") print $0 }'


## FOR loop

    awk 'BEGIN { for(i=1; i<=10; i++) print "The square root of", i, "is", i*i; }'

    The square root of 1 is 1
    The square root of 2 is 4
    The square root of 3 is 9
    The square root of 4 is 16
    The square root of 5 is 25
    The square root of 6 is 36
    The square root of 7 is 49
    The square root of 8 is 64
    The square root of 9 is 81
    The square root of 10 is 100


## length() function

    awk 'length($0) < 8' /etc/shells
    #only shows the text less then 8 chars


## substr() function

    cat <filename>
    1       variables
    2       arrays
    3       lists
    4       functions
    5       classes
    6       methods

    awk '{print substr($0, 3)}' <filename>
    #remove the first 3 characters

    variables
    arrays
    lists
    functions
    classes
    methods


## match() function

    awk 'match($0, /o/) {print "\""$0"\" has \"o\" character at position " RSTART}' <filename>
    #match every line with letter "o" and print the index location of the o
    
    "today" has "o" character at position 2
    "programming" has "o" character at position 3




## References

[Learning Awk Is Essential For Linux Users](https://www.youtube.com/watch?v=9YOZmI-zWok&t=66s&ab_channel=DistroTube)
[Techniques with AWK](https://www.youtube.com/watch?v=rzXliWSTQPE&t=814s&ab_channel=DebraMcCusker)
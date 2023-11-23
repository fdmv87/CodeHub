## Bash: Shell script

### first line of the script
Bash scripts start with a shebang. Shebang is a combination of bash # and bang ! followed by the bash shell path. This is the first line of the script. Shebang tells the shell to execute it via bash shell. Shebang is simply an absolute path to the bash interpreter.

    #!/bin/bash

### some commands

| Command       | Description                                                                    |
| --------------| -------------------------------------------------------------------------------|	
| pwd           | Display current directory
| cd  	        | Change directory
| cd ..  	    | Change to parent directory of the current directory
| cd ~          | Change to user home directory
| cd -  	    | Switch to previous working directory
| ls	        | List directory contents
| echo	        | Write arguments to the standard output
| which	        | Locate a program file in the user's path
| date	        | Displays the current date
| read	        | Reads the input and stores it in a variable
| cp  	        | Copy a file or directory
| touch         | Create a new file
| rm  	        | Remove a file
| rm -r         | Recursively removes the specified directory and its contents
| mv  	        | Move or rename a file or directory
| cat  	        | Concatenate and print the contents of a file
| grep     	    | Search for a pattern in a file
| chmod         | Change the permissions of a file or directory
| sudo       	| Run a command with administrative privileges 
| df       	    | Display the amount of disk space available
| history  	    | Show a list of previously executed commands
| ps       	    | Display information about running processes
| w             | Display who is logged in and what they are doing 
| cut           | Cut out selected portions of each line of a file



## give permition to execute
```bash
chmod u+x <file_name>.sh
```

- chmod modifies the ownership of a file for the current user :u.
- +x adds the execution rights to the current user. This means that the user who is the owner can now run the script.

## running a script
```bash
sh <file_name>.sh
bash <file_name>.sh
./<file_name>.sh
```

## Comments
Comments start with a # in bash scripting

```bash
# This is an example comment
# Both of these lines will be ignored by the interpreter
```

## Variables and data types in Bash
There are no data types in Bash. 

1. Assign the value directly:

```bash
country_code=PT
country_name=Portugal
country_description="add your description here"
```
 

2. Assign the value based on the output obtained from a program or command, using command substitution. Note that $ is required to access an existing variable's value.

```bash
same_country=$country_name
```

### Access variables
To access the variable value, append $ to the variable name.

```bash
echo $country_name
```

### Variable naming conventions

1. Variable names should start with a letter or an underscore (_).
2. Variable names can contain letters, numbers, and underscores (_).
3. Variable names are case-sensitive.
4. Variable names should not contain spaces or special characters.
5. Use descriptive names that reflect the purpose of the variable.
6. Avoid using reserved keywords, such as if, then, else, fi, and so on as variable names.


## Reading user input

    echo "enter your name:"
    read your_name
    echo "Your name is: "$your_name


## Reading from a file

    while read line
    do
        echo $line
    done < input_file.txt

## Command line arguments
In a bash script or function, $1 denotes the initial argument passed, $2 denotes the second argument passed, and so forth.

    #!/bin/bash
    echo "Hello, $1!"

##### running it:

    ./greetings.sh Filipe

    >Hello, Filipe


## Writing to a file:

    echo "This is some text." > output.txt

## Appending to a file:

    echo "More text." >> output.txt

## Redirecting output

    ls > files.txt

## Conditional statements (if/else)

    if [[ condition ]];
    then
        statement
    elif [[ condition ]]; then
        statement 
    else
        do this by default
    fi

## AND (-a), OR (-o)

    if [ $a -gt 60 -a $b -lt 100 ]


## Numeric and String Comparisons

| Description         |   Numeric Comparison             | String Comparison             |
| --------------------| ---------------------------------|--------------------------------	
| less than	          | -lt                              | <
| greater than        | -gt                              | >
| equal               | -eq                              | =
| not equal           | -ne                              | !=
| less or equal       | -le                              | N/A
| greater or equal    | -ge                              | N/A


## IF/ELIF/ELSE example

    #!/bin/bash

    echo "Please enter a number: "
    read num

    if [ $num -gt 0 ]; then
        echo "$num is positive"
    elif [ $num -lt 0 ]; then
        echo "$num is negative"
    else
        echo "$num is zero"
    fi


## While loop

    #!/bin/bash
    i=1
    while [[ $i -le 10 ]] ; do
        echo "$i"
        (( i += 1 ))
    done


## For loop

    #!/bin/bash

    for i in {1..5}
    do
        echo $i
    done


## Case statement

    case expression in
        pattern1)
            # code to execute if expression matches pattern1
            ;;
        pattern2)
            # code to execute if expression matches pattern2
            ;;
        pattern3)
            # code to execute if expression matches pattern3
            ;;
        *)
            # code to execute if none of the above patterns match expression
            ;;
    esac

######

    fruit="apple"

    case $fruit in
        "apple")
            echo "This is a red fruit."
            ;;
        "banana")
            echo "This is a yellow fruit."
            ;;
        "orange")
            echo "This is an orange fruit."
            ;;
        *)
            echo "Unknown fruit."
            ;;
    esac


## Schedule Scripts using cron

    # Cron job example
    * * * * * sh /path/to/script.sh

| SCHEDULE       | DESCRIPTION                                         | EXAMPLE                               |
| --------------| -----------------------------------------------------|----------------------------------------	
| 0 0 * * *	    | Run a script at midnight every day                   |	0 0 * * * /path/to/script.sh
| */5 * * * *	| Run a script every 5 minutes                         |	*/5 * * * * /path/to/script.sh
| 0 6 * * 1-5	| Run a script at 6 am from Monday to Friday           |	0 6 * * 1-5 /path/to/script.sh
| 0 0 1-7 * *	| Run a script on the first 7 days of every month      |	    0 0 1-7 * * /path/to/script.sh
| 0 12 1 * *	| Run a script on the first day of every month at noon |	0 12 1 * * /path/to/script.sh


## Using crontab

**crontab -l** lists the already scheduled scripts for a particular user.

You can add and edit the cron through **crontab -e**.

[more about crontab](https://www.freecodecamp.org/news/cron-jobs-in-linux/)


## Debug and Troubleshoot Bash Scripts

### set -x option
This option enables debugging mode, which causes Bash to print each command that it executes to the terminal, preceded by a + sign.

    #!/bin/bash

    set -x

    # Your script goes here


### set -e option
If you want your script to exit immediately when any command in the script fails, you can use the set -e option. This option will cause Bash to exit with an error if any command in the script fails, making it easier to identify and fix errors in your script.

    #!/bin/bash

    set -e

    # Your script goes here


### Check the exit code
When Bash encounters an error, it sets an exit code that indicates the nature of the error. You can check the exit code of the most recent command using the $? variable. A value of 0 indicates success, while any other value indicates an error.

    #!/bin/bash

    # Your script goes here

    if [ $? -ne 0 ]; then
        echo "Error occurred."
    fi


### Use echo statements
Another useful technique for debugging Bash scripts is to insert echo statements throughout your code. This can help you identify where errors are occurring and what values are being passed to variables.

    #!/bin/bash

    # Your script goes here

    echo "Value of variable x is: $x"

    # More code goes here


### Troubleshooting crons by verifying logs
We can troubleshoot crons using the log files. Logs are maintained for all the scheduled jobs. You can check and verify in logs if a specific job ran as intended or not.

For Ubuntu/Debian, you can find cronlogs at:

    /var/log/syslog

The location varies for other distributions.


## Input, Output and Error Redirections
When executing a command, three possible outcomes might happen. The first scenario is that the command will produce an expected output, second, the command will generate an error, and lastly, your command might not produce any output at all.

* **stdout**: standard output
* **stderr**: standard error output

The > notation is used to redirect stdout to a file whereas 2> notation is used to redirect stderr and &> is used to redirect both stdout and stderr

    $ls non_existing_file existing_file 
    ls: cannot access 'non_existing_file': No such file or directory                                                     
    existing_file

    $ls non_existing_file > stdout.txt
    cat stdout.txt
    ls: cannot access 'non_existing_file': No such file or directory

    $ls non_existing_file 2> stderr.txt
    cat stderr.txt
    existing_file

    $ls non_existing_file &> both_stdout_stderr.txt
    cat both_stdout_stderr.txt
    existing_file


### /dev/null
Now that we have a basic understanding of the output redirection we can eliminate this unwanted stderr message by redirecting it with 2> notation to /dev/null

    ls non_existing_file 2> stderr.txt

***

# Samples

***

##### reading input data:

    #!/bin/bash
    echo "Today is " `date`
    echo -e "\nenter the path to directory"
    read the_path
    echo -e "\n you path has the following files and folders: "
    ls $the_path

***

#####  executes some well-known commands (date, w, uname, uptime) to display information about you and your machine:

```bash
#!/bin/bash
clear
echo "Program starts now."

echo "Hello, $USER"
echo

echo "Today's date is `date`, this is week `date +"%V"`."
echo

echo "These users are currently connected:"
w | cut -d " " -f 1 - | grep -v USER | sort -u
echo

echo "This is `uname -s` running on a `uname -m` processor."
echo

echo "This is the uptime information:"
uptime
echo
```

***

##### create a backup of a user's home directory and save it as a compressed tarball (.tar.gz) in the /tmp/ directory

```bash
#!/bin/bash

# This bash script is used to backup a user's home directory to /tmp/.

user=$(whoami)
input=/home/$user
output=/tmp/${user}_home_$(date +%Y-%m-%d_%H%M%S).tar.gz

tar -czf $output $input
#c: create a new archive.
#z: compress the archive using gzip.
#f: specify the filename of the archive.

echo "Backup of $input completed! Details about the output backup file:"
ls -l $output
```


***

## References

[https://www.freecodecamp.org/](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/#pre-requisites)
[Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
# Linux Commands

## Chroot
Run Commands With a Different Root Directory

    chroot /home/testdir

After that, any commands you run will be relative to / in the /home/testdir directory

## Crontab
Schedule Tasks to Run Automatically

    0 0 * * * /home/user/daily_script.sh 
    # would run the daily_script.sh script at midnight every day. 
    
    30 8 * * 1-5 /home/user/work_script.sh 
    # would run work_script.sh at 8:30am every weekday.

## Df
Check Disk Space Usage

    df -h

    df -h /home


-h flag formats the output in human-readable format, showing sizes in GB and MB instead of bytes. The output will show:

* **Filesystem**: The drive or partition name
* **Size**: Total space
* **Used**: Space currently in use
* **Available**: Free space still available
* **Use%**: Percentage of space used


## Dmesg
View Kernel messages: updates, diagnostics, errors, and more as your system came to life. Skim through to check for any issues, or search for specific keywords like the name of your Wi-Fi adapter or other hardware components.


## Grep
Search for Patterns in Files

    grep error log.txt
    grep ^A[0-9] log.txt

* **-i** to ignore case
* **-v** to invert the search and show lines that don’t match
* **-c** to just get a count of matches
* **-r** to recursively search all files in a directory


## Head/Tail
View the First/Last Part of a File

    # head command shows you the first 10 lines of a file by default
    head -n 5 <filename>

    # tail command shows you the last 10 lines of a file by default
    tail -n 20 <filename>


## Ps
List Running Processes

    ps aux

* **A**: All processes
* **U**: User
* **X**: Processes without terminals

The output will contain info like:

* **USER**: The owner of the process
* **PID**: The process ID
* **%CPU**: The CPU usage
* **%MEM**: The memory usage
* **VSZ**: The virtual memory usage
* **TTY**: The terminal associated with the process
* **STAT**: The process state (Running, Sleeping, Zombie, and so on.)
* **START**: The start time of the process
* **TIME**: The CPU time used
* **COMMAND**: The command that started the process

You can also filter the Ps output by:

* **Username**: ps aux | grep root
* **Process name**: ps aux | grep cron
* **PID**: ps aux | grep 555


## Rsync
Sync Files and Folders

Rsync is a fast and versatile file copying tool. It can copy and sync files and folders locally or remotely over SSH. It’s smart enough to only transfer the differences between two locations, saving time and bandwidth.

    rsync [options] source destination

* **-a**: Archive mode which preserves permissions, timestamps, group, owner and symlinks
* **-v**: Verbose output so you can see what’s being copied
* **-z**: Compression to speed up transfers over slow networks
* **-h**: Human-readable sizes (e.g. 1K, 234M, 2G)


## Pipe Viewer (pv)
Shows you the progress of data through a pipeline

    cat mylargefile.mp4 | pv | gzip > mylargefile.mp4.gz
    #pv will display the throughput and estimated time remaining as your data is compressed

    rsync -avz myfiles user@host:/backup | pv


## mtr
Network Diagnostics

    mtr [domain name or IP address]

    mtr google.com


## jq
Parse JSON

    cat data.json | jq '.[] | select(.name == "John")'


* **.key**: Access a key from objects
* **.[10:]**: Show elements from index 10 onwards
* **.[10:15]**: Show elements from index 10 to 15
* **length**: Print the length of an array
* **map(.)**: Apply a filter to each element of an array
* **group_by(.key)**: Group objects by a key


## tac
View Config Files in Reverse

The tac command allows you to quickly view config files in reverse, so you can see what the file looked like before your edits.

    tac config.txt


## perf
Analyze CPU Performance

* **cpu-clock**: Measure the CPU clock cycles
* **task-clock**: Measure the time spent on task execution
* **cache-misses**: Count the number of cache misses
* **branch-misses**: Count the number of branch prediction misses

    perf list
    perf stat -e cpu-clock sleep 5
    #This will run the sleep 5 command and measure the cpu-clock event while it's running. Perf will then give you a summary of the stats for that event.

    perf record script.sh
    #To get more detailed profiling info

    perf report
    #This gives you an interactive report to analyze the results


## 
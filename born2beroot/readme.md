`This project has been created as a part of the 42 curriculum by: jabettin`

## Description ##
>Born2beroot as a project stands out from the other in Milestone 1, especially now considering 42Next.
The goal is to create and set-up a Virtual Machine in accordance to the subject guidelines, and is (in my opinion amongst the easier projects) as the actual set-up does not take much time (unless you do not follow any guides).
The only part that takes quite some time is the evaluation for b2br, as you will follow a long checklist.
Anyways, i am not going to lay-out the entire project and its contents here, as there are plenty of guides that do so perfectly fine. What i *will* be doing is laying out exactly what *i* did and telling you what guides i used and in which order. So this Readme will be rather short, but i don't think there needs to be another complex or long gitbook/gitguide on b2br. So we will jump straight to resources

## Resources ##
>I started with the following guide by: 
- [Gemartin99](https://noreply.gitbook.io/born2beroot)
`(Important note, that in the step of creating the logfile in /var/log/sudo instead of using sudo_config for your logging, i changed the name to sudo_log, ofcourse this also then needs to be added to your sudoers.d as path to your logfile)`
Until the script.sh slide, as i then switched to
- [Thuggonaut's github guide](https://github.com/Thuggonaut/42IC_Ring01_Born2beRoot)
And lastly i followed:
- [Vikingu-del's](https://github.com/Vikingu-del/Born2beRoot) Comprehensive guide for knowledge about the actual project.
These three project guides should be more than enough to get you through b2br, Now lastly i will add my own cheatsheet that you can memorize or use for the evaluation.

## The corrected sudoers.d/sudo_config file ##
```Bash
Defaults  passwd_tries=3
Defaults  badpass_message="Personalized message"
Defaults  logfile="/var/log/sudo/sudo_log"
Defaults  log_input, log_output
Defaults  iolog_dir="/var/log/sudo"
Defaults  requiretty
Defaults  secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
```

## Cheatsheet ##
```Bash
Crontab time indicator:
minute, hour, day of month, month, day of week

Monitoring shell script in: /usr/local/bin/...

Password policy
nano /etc/login.defs

Password quality
nano /etc/pam.d/common-password

Sudo rules
nano /etc/sudoers.d/sudo_config

Sudo logs
cd cd /var/log/sudo cat sudo_config
is included in sudo visudo with: @ include /etc/sudoers.d/sudo_config

Sudo log file: /var/log/sudo, is included as filepath in sudoers file with: Defaults  logfile="/var/log/sudo/sudo_config"

lvm disk manager
cron linux version of windows taskschd or job scheduler

User config
sudo adduser <login>
sudo addgroup user42

No graph interface check
ls /usr/bin/*session

Check ufw
sudo ufw status
or sudo service ufw status

Check ssh
sudo service ssh status

Check os
uname --kernel-version

Check user and group
getent group sudo user42

Change hostname
sudo nano /etc/hostname & sudo nano /etc/hosts
sudo reboot

Check partitions
lsblk

Check sudo
which sudo

Check groups and users
getent group (group name)

Check ufw advanced
dpkg -s ufw
sudo service ufw status

Active ufw rules
sudo ufw status

Rule creation
sudo ufw allow 8080
sudo ufw status 

Rule deletion
sudo ufw delete (number of rule, so 2 and 4/3 after deletion)

Check ssh
which ssh
sudo service ssh status

Ssh usage
ssh jabettin@127.0.0.1 -p 4242

Check crontab
sudo crontab -u root -e

SCRIPT
BORN2BEROOT – MONITORING SCRIPT EXPLANATION
==========================================

SCRIPT OVERVIEW
---------------
This Bash script collects system information (CPU, RAM, disk, network, users, sudo usage, etc.)
and broadcasts it to all logged-in users using the `wall` command.
It is typically executed every 10 minutes via cron in the Born2beroot project.


--------------------------------------------------
1. SHEBANG
--------------------------------------------------
#!/bin/bash

Tells the system to execute the script using the Bash shell.


--------------------------------------------------
2. ARCHITECTURE
--------------------------------------------------
arch=$(uname -a)

Command: uname -a
- Displays kernel name, version, architecture, and OS.
- Example output:
  Linux debian 6.1.0-18-amd64 x86_64 GNU/Linux

Stored in variable: arch


--------------------------------------------------
3. CPU PHYSICAL
--------------------------------------------------
cpuf=$(grep "physical id" /proc/cpuinfo | wc -l)

Files used:
- /proc/cpuinfo: virtual file containing CPU details.

Commands:
- grep "physical id": filters physical CPU identifiers.
- wc -l: counts lines.

Result:
- Number of physical CPUs.


--------------------------------------------------
4. CPU VIRTUAL (vCPU / CORES)
--------------------------------------------------
cpuv=$(grep "processor" /proc/cpuinfo | wc -l)

Each "processor" entry represents one core/thread.

Result:
- Total number of virtual CPUs (cores).


--------------------------------------------------
5. RAM USAGE
--------------------------------------------------
ram_total=$(free --mega | awk '$1 == "Mem:" {print $2}')
ram_use=$(free --mega | awk '$1 == "Mem:" {print $3}')
ram_percent=$(free --mega | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')

Command: free --mega
- Displays memory usage in MB.

AWK explanation:
- $1 == "Mem:" → select memory line
- $2 → total RAM
- $3 → used RAM

printf("%.2f"):
- Formats percentage to 2 decimal places.


--------------------------------------------------
6. DISK USAGE
--------------------------------------------------
df -m | grep "/dev/" | grep -v "/boot"

Command breakdown:
- df -m: disk usage in MB
- grep "/dev/": only real disks
- grep -v "/boot": exclude boot partition

Disk total:
awk '{disk_t += $2} END {printf ("%.1fGb\n"), disk_t/1024}'
- $2 = total space
- Converts MB to GB

Disk used:
awk '{disk_u += $3} END {print disk_u}'
- $3 = used space

Disk percentage:
awk '{disk_u += $3} {disk_t+= $2} END {printf("%d"), disk_u/disk_t*100}'


--------------------------------------------------
7. CPU LOAD
--------------------------------------------------
cpul=$(vmstat 1 2 | tail -1 | awk '{printf $15}')

Command: vmstat 1 2
- Samples system twice
- Second result is accurate

$15:
- CPU idle percentage

Calculation:
cpu_op = 100 - idle
cpu_fin = formatted to 1 decimal place


--------------------------------------------------
8. LAST BOOT TIME
--------------------------------------------------
lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')

Command: who -b
- Shows last system boot time.

AWK extracts date and time.


--------------------------------------------------
9. LVM USAGE
--------------------------------------------------
lvmu=$(if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo yes; else echo no; fi)

Commands:
- lsblk: lists block devices
- grep lvm: checks Logical Volume Manager usage

Result:
- "yes" if LVM is used, otherwise "no".


--------------------------------------------------
10. TCP CONNECTIONS
--------------------------------------------------
tcpc=$(ss -ta | grep ESTAB | wc -l)

Command: ss -ta
- t: TCP
- a: all sockets

ESTAB:
- Only established connections.


--------------------------------------------------
11. LOGGED-IN USERS
--------------------------------------------------
ulog=$(users | wc -w)

Commands:
- users: shows logged-in users
- wc -w: counts users


--------------------------------------------------
12. NETWORK INFORMATION
--------------------------------------------------
ip=$(hostname -I)
mac=$(ip link | grep "link/ether" | awk '{print $2}')

Commands:
- hostname -I: shows IP address
- ip link: shows network interfaces
- link/ether: MAC address


--------------------------------------------------
13. SUDO COMMAND COUNT
--------------------------------------------------
cmnd=$(journalctl _COMM=sudo | grep COMMAND | wc -l)

Commands:
- journalctl: system logs
- _COMM=sudo: only sudo logs
- COMMAND: executed sudo commands

Result:
- Total sudo commands executed.


--------------------------------------------------
14. WALL OUTPUT
--------------------------------------------------
wall "..."

Command: wall
- Sends message to all logged-in users' terminals.

Used with cron to display system status regularly.


--------------------------------------------------
CORE COMMANDS SUMMARY
--------------------------------------------------
grep       → filters lines
grep -v    → excludes lines
awk        → column-based text processing
$1, $2     → field selectors
|          → pipe output
wc -l      → count lines
wc -w      → count words
printf     → format output
```
<ins>`This file is missing the Signature.txt` <ins>
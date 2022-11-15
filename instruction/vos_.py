
''' Set of commands to be executed  '''

vos_cmds = [
            {'type': "PWord", 'command': 'cat /etc/passwd'},
            #{'type': "WorkDir", 'command': 'll -a .'},
            #{'type': "Process", 'command': 'ps -aux'},
            #{'type': "NS", 'command': 'netstat -antp'},
            {'type': "Last", 'command': 'last | grep -a -E -o \'([0-9]{1,3}\.){3}[0-9]{1,3}\' |sort | uniq -c | sort -n -r'},
            #{'type': "Lastb", 'command': 'sudo lastb | grep -a -E -o \'([0-9]{1,3}\.){3}[0-9]{1,3}\' |sort | uniq -c | sort -n -r'},
            #{'type': "Cronjobs", 'command': 'sudo cat /etc/crontab'},
            #{'type': "RC", 'command': 'cat /etc/rc.local'},
]

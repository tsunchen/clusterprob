
''' Set of commands to be executed  '''

os_cmds = [
            {"type": "Memory Utilization", "command":'free -t|grep Total|awk \'{print $2","$3}\''},
            {"type": "Interfaces", "command": "for i in `ifconfig -s|grep -v 'Iface\|lo'|awk '{print $1}'`; do echo -n $i:;ifconfig $i | grep -w inet | awk '{print $2}'| tr -d ' [a-z]:'; done"}
]

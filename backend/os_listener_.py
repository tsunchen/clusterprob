
def sanitize_op(un_ip):
    return [ str(ui).strip('\n').strip('\t') for ui in un_ip ]


''' Result ex OS Commands '''

def result_os_cmds_(c, dict_host, os_cmds, host, observations, alias_):
    for o in os_cmds:
        store_stdout = ""
        print(f'  |- Checking {str(o["type"])}: ')
        stdin, stdout, stderr = c.exec_command(o['command'])
        store_stdout = sanitize_op(stdout.readlines())
        # print('{:100}'.format("  [Done]"))
        # dict_host[o['type']] = store_stdout

        ''' if expression  '''
        if "Memory Utilization" == o['type']:
            used, total = str(store_stdout[0].split(',')[1]), str(store_stdout[0].split(',')[0])
            util = (float(used) * 100 / float(total))
            if float(util) > 70.0:
            # if float(util) > 2.0:
                print('{:100}'.format("  [Critical]"))
                dict_host[o['type']+"_status"] = "Critical"
                dict_host[o['type']+"_percent"] = str(util) + "%"
                msg = "Memory utilization is high to reach " + str(util) + "% on " + host + "(" + alias_ + ")"
                observations.append(msg)
            else:
                print('{:100}'.format("  [Good]"))
                dict_host[o['type']+"_status"] = "Good"
                dict_host[o['type']+"_percent"] = str(util) + "%"
        elif "Interfaces" == o['type']:
            dict_host[o['type']] = store_stdout
            print('{:100}'.format("  [Done]"))

    return dict_host

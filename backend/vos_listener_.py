
def sanitize_op(un_ip):
    return [ str(ui).strip('\n').strip('\t') for ui in un_ip ]


''' Result ex VOS Commands '''

def result_vos_cmds_(c, dict_host, vos_cmds):
        for v in vos_cmds:
            store_stdout = ""
            print(f'  |- Checking {str(v["type"])}: ')
            stdin, stdout, stderr = c.exec_command(v['command'])
            store_stdout = sanitize_op(stdout.readlines())
            print('{:100}'.format("  [Done]"))
            dict_host[v['type']] = store_stdout
        return dict_host

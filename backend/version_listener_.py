
def sanitize_op(un_ip):
    return [ str(ui).replace(',',':').strip('\n').strip('\t') for ui in un_ip ]


''' Result ex Version Commands '''

def result_version_cmds_(c, dict_host, version_cmds):
        for v in version_cmds:
            store_stdout = ""
            print(f'  |- Checking {str(v["type"])}: ')
            stdin, stdout, stderr = c.exec_command(v['command'])
            store_stdout = sanitize_op(stdout.readlines())
            print('{:100}'.format("  [Done]"))
            dict_host[v['type']] = store_stdout
        return dict_host

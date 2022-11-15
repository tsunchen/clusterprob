#!/usr/bin/env python
import time
from datetime import datetime
import paramiko
from api.loggal import *
from backend.os_listener_ import *
from instruction.os_ import *
from backend.version_listener_ import *
from instruction.version_ import *
from backend.vos_listener_ import *
from instruction.vos_ import *
observations = []


def connect_by_ssh(host, username, password, alias_):
    dict_host = {}
    log_date = datetime.today().strftime("%Y-%m-%d")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Trying to connect to ip provided
    dict_host['host'] = str(host)
    dict_host['alias'] = str(alias_)
    try:
        c.connect(host, username = username, password = password, allow_agent = False)
        logfile("- Connection to " + str(host) + " Successful. ")
        dict_host['connection'] = "Success"
        print("- Connected to ", str(host))
        # global observations
        dict_host = result_os_cmds_(c, dict_host, os_cmds, str(host), observations, alias_)
        dict_host = result_version_cmds_(c, dict_host, version_cmds)
        # 2022.7.19 VOS Commands
        dict_host = result_vos_cmds_(c, dict_host, vos_cmds)
        # dict_host output
        return dict_host
    except Exception as e:
        print(f'- Connection to {str(host)} FAILED. \n- ! With Error: {str(e)}')
        logfile(f'@ Connection to {str(host)} FAILED. \n With Error: {str(e)}')
        dict_host['connection'] = "Fail"
        return
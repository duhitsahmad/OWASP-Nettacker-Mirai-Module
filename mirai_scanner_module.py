#!/usr/bin/env python3
# GSoC 2026 - OWASP Nettacker Module
# Author: Muhammad Ahmad
# Module: Mirai Botnet Default Credential Scanner

import telnetlib
from core.module import BaseModule

class Module(BaseModule):
    def __init__(self):
        super().__init__()
        self.info = {
            'Name': 'Mirai Botnet Credential Scanner',
            'Author': 'Muhammad Ahmad',
            'Description': 'Scans for IoT devices with default telnet credentials used by Mirai botnet',
            'Category': 'brute_force'
        }
        self.mirai_creds = [
            ('root', 'xc3511'), ('root', 'vizxv'), ('root', 'admin'),
            ('admin', 'admin'), ('root', '888888'), ('root', 'xmhdipc'),
            ('root', 'default'), ('root', 'juantech'), ('root', '123456'), ('support', 'support')
        ]

    def run(self, target, port=23):
        self.log(f"Starting Mirai scan on {target}:{port}")
        try:
            for username, password in self.mirai_creds:
                if self.check_telnet_login(target, port, username, password):
                    self.report_vulnerability(
                        target=target,
                        port=port,
                        username=username,
                        password=password,
                        description=f"Device vulnerable to Mirai - Default creds: {username}:{password}"
                    )
                    return True
        except Exception as e:
            self.log_error(f"Error scanning {target}: {str(e)}")
        return False

    def check_telnet_login(self, host, port, user, passwd):
        try:
            tn = telnetlib.Telnet(host, port, timeout=5)
            tn.read_until(b"login: ", timeout=3)
            tn.write(user.encode('ascii') + b"\n")
            tn.read_until(b"Password: ", timeout=3)
            tn.write(passwd.encode('ascii') + b"\n")
            response = tn.read_some()
            tn.close()
            if b'$' in response or b'#' in response or b'>' in response:
                return True
        except:
            return False
        return False

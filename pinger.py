import re
import subprocess

re_ip = re.compile(b'

def pinger(addr):
    response = subprocess.check_output(['ping','-c1',addr])
    return int(re_ip.search(b'(\d*)% packet loss', ret).group(1))

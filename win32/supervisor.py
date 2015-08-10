"""
A very small and lightweight supervisor for Windows whose aim is to launch and
monitor the processes launched by the agent
"""

import subprocess

if __name__ == '__main__':
    subprocess.Popen(['./embedded/python.exe', './agent/agent.py', 'foreground',
                      '--use-local-forwarder'], 1)
    subprocess.Popen(['./embedded/python.exe', './agent/ddagent.py'], 1)
    subprocess.Popen(['./embedded/python.exe', './agent/dogstatsd.py'], 1)
    subprocess.Popen(['./embedded/python.exe', './agent/jmxfetch.py'], 1)

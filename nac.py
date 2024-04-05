import tkinter as tk
import os
import netifaces
import urllib.request


def ping_host(hostname):
    if os.sys.platform == "win32":
        ping_param = "-n"
    else:
        ping_param = "-c"
    response = os.system(f"ping {ping_param} 1 {hostname}")
    if response == 0:
        return hostname + " UP"
    else:
        return hostname + " DOWN"


def check_url(hostname):
    response = urllib.request.urlopen(hostname).getcode()
    if response == 200:
        return hostname + " UP"
    else:
        return hostname + " DOWN"


gws = netifaces.gateways()
default_gateway_line = gws["default"][netifaces.AF_INET]


TO_CHECK = [
    {
        "check_function": ping_host,
        "params": default_gateway_line[0],
    },
    {
        "check_function": ping_host,
        "params": "8.8.8.8",
    },
    {
        "check_function": ping_host,
        "params": "gooogle.com",
    },
    {
        "check_function": check_url,
        #"params": {"args": ("http://www.gooogle.com",), "kwargs": {}},
        "params": "http://www.gooogle.com",
    },
]


# --- INTERFACE ---

window = tk.Tk()

for param in TO_CHECK:
    func = param["check_function"]
    status_txt = func(param['params'])
    #status_txt = func( *param["params"]["args"], **param["params"]["kwargs"])
    tk.Label(text=status_txt).pack()


window.mainloop()

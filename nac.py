import tkinter as tk
import os
import netifaces
import urllib.request

window = tk.Tk()

labels_host = ["default_gateway", "8.8.8.8", "gooogle.com", "http://www.gooogle.com"]
labels_status = ["", "", "", ""]

gws = netifaces.gateways()
default_gateway_line = gws["default"][netifaces.AF_INET]
labels_host[0] = default_gateway_line[0]


if os.sys.platform == "win32":
    ping_param = "-n"
else:
    ping_param = "-c"


def ping_host(hostname):
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


labels_status[0] = ping_host(labels_host[0])
labels_status[1] = ping_host(labels_host[1])
labels_status[2] = ping_host(labels_host[2])
labels_status[3] = check_url(labels_host[3])


label0 = tk.Label(text=labels_status[0])
label0.pack()
label1 = tk.Label(text=labels_status[1])
label1.pack()
label2 = tk.Label(text=labels_status[2])
label2.pack()
label3 = tk.Label(text=labels_status[3])
label3.pack()

window.mainloop()

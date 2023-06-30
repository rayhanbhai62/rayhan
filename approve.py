import requests,random,os,sys
try:
  file=open("/data/data/com.termux/files/usr/bin/.k","r")
  key=file.read()
  file.close()
except FileNotFoundError:
  file=open("/data/data/com.termux/files/usr/bin/.k","w")
  a=os.getuid()
  b=os.getlogin()
  file.write(str(a)+str(b))
  file.close()
  print("YOUR ID IS NOT APPROVED")
  print("YOUR ID: "+str(a)+str(b))
  print("CONTRACT WITH ME WITH THIS ID FOR APPROVE")
  sys.exit()
req=requests.get("https://raw.githubusercontent.com/STLP-TEAM/Open-Source/main/ap.txt").text
if key in req:
  print("CONGRATULATIONS!YOUR DEVICE IS APPROVED BY ADMIN")
else:
  a=os.getuid()
  b=os.getlogin()
  print("YOUR ID IS NOT APPROVED")
  print("YOUR ID: "+str(a)+str(b))
  print("CONTRACT WITH ME WITH THIS ID FOR APPROVE")
  sys.exit()

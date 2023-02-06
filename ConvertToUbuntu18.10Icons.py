import os;
filename=["places/","status/","apps/","categories/"]
path=["16x16/","16x16@2x/","24x24/","24x24@2x/","32x32/","32x32@2x/","48x48/","48x48@2x/","256x256/","256x256@2x/"]

os.system("apt -y install ./yaru-theme-icon_22.04.4_all.deb")
os.system("dpkg-deb --extract ./yaru-theme-icon_18.10.6_all.deb /home/redmi/")

a=-1;
while(a<=10):
  a=a+1;
  b=-1;
  while(b<=2):
    b=b+1;
    list=["/bin/cp --force --remove-destination --recursive /home/redmi/usr/share/icons/Yaru/",path[a],filename[b]," /usr/share/icons/Yaru/",path[a]]
    sp="";
    cmd=sp.join(list);
    print(cmd);
    os.system(cmd);
  

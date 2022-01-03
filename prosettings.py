from bs4 import BeautifulSoup
import requests
from pathlib import Path
import time
import winreg

#players from whom settings are most commonly stolen!
top_players = [
    "https://prosettings.net/counterstrike/s1mple/",
    "https://prosettings.net/counterstrike/niko",
    "https://prosettings.net/counterstrike/coldzera",
    "https://prosettings.net/counterstrike/stewie2k",
    "https://prosettings.net/counterstrike/zywoo",
    "https://prosettings.net/counterstrike/dev1ce",
]

names = [ "s1mple", "niko", "coldzera", "stewie2k", "zywoo", "device"] #PYTHON DOESNT HAVE PAIRS

def get_steam_path():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\WOW6432Node\Valve\Steam")
    path = winreg.QueryValueEx(key, "InstallPath")
    return str(path[0])
    
def get_cfg_path():
    path = Path(get_steam_path() + "\steamapps\common\Counter-Strike Global Offensive\csgo\cfg")

    if (path.exists()):
        return path    
            
    if (path == ""):
        return str(input("Error, please manually specify path to CFG folder: "))
        


def make_cfg(name, path, url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")

    settings = [] # array of strings

    for i in range(0, 3):
      settings = soup.find_all("code")

    crosshair = settings[0].text
    viewmodel = settings[1].text
    bob = settings[2].text

    file = open("%s\%s.cfg" % (path, name), "w")
    file.write(crosshair)
    file.write(viewmodel)
    file.write(bob)
    file.close()

def main():
    choice = int(input("0 = manual download, 1 = download 5 popular configs: "))
    path_to_cfg_folder = get_cfg_path()

    if (choice == 0):
        url = str(input("URL: "))
        pro_name = str(input("Name of player: "))
        make_cfg(pro_name, path_to_cfg_folder, url)
        print("Successfully made a file named %s.cfg in %s!" % (pro_name, path_to_cfg_folder))
    elif (choice == 1):
        for i in range(len(top_players)):
            urlxd = top_players[i]
            make_cfg(names[i], path_to_cfg_folder, urlxd)
            print("Successfully made a file named %s.cfg in %s!" % (names[i], path_to_cfg_folder))
    else:
        print("go kys")



main()
time.sleep(2)



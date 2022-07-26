from bs4 import BeautifulSoup
import requests
from pathlib import Path
import time
import winreg

#players from whom settings are most commonly stolen!
top_players = [
    "https://prosettings.net/players/s1mple/",
    "https://prosettings.net/players/niko/",
    "https://prosettings.net/players/xantares/",
    "https://prosettings.net/players/stewie2k/",
    "https://prosettings.net/players/zywoo",
    "https://prosettings.net/players/dev1ce/",
    "https://prosettings.net/players/rigon/",
    "https://prosettings.net/players/m0nesy/",
]

names = [ "s1mple", "niko", "xantares", "stewie2k", "zywoo", "device", "rigoN", "monesy"] #PYTHON DOESNT HAVE PAIRS

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
        
def kek(source):
    soup = BeautifulSoup(source, "lxml")
    div = soup.find(id = "csgo-settings")

    crosshair = div.find(id = "csgo_crosshair")
    viewmodel = div.find(id = "csgo_viewmodel")
    bob = div.find(id = "csgo_bob")

    commands = []

    
    crosshaircmd = crosshair.find_all(attrs = {"class" : "format-number"})
    bobcmd = bob.find_all(attrs = {"class" : "format-number"})
    viewmodelcmd = viewmodel.find_all(attrs = {"class" : "format-number"})

    bobvalues = bob.find_all("dd")
    crosshairvalues = crosshair.find_all("dd")
    viewmodelvalues = viewmodel.find_all("dd")

    for k, i in enumerate(bobcmd):
        cmd1 = i.get("data-field") + " " + bobvalues[k].text + ";"
        commands.append(cmd1)

    for l, j in enumerate(viewmodelcmd):
        cmd2 = j.get("data-field") + " " + viewmodelvalues[l].text + ";"
        commands.append(cmd2)

    for x, y in enumerate(crosshaircmd):
        cmd3 = y.get("data-field") + " " + crosshairvalues[x].text + ";"
        commands.append(cmd3)
        

    return commands

def make_cfg(name, path, url):
    source = requests.get(url).text
    settings = kek(source) # array of strings
    file = open("%s\%s.cfg" % (path, name), "w")
    
    for kekw in settings:
        writing = kekw + "\n"
        file.write(writing)
        
    file.close()

def main():
    choice = int(input("0 = manual download, 1 = download popular configs: "))
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


    

if __name__ == "__main__":
    main()
    time.sleep(2.0)




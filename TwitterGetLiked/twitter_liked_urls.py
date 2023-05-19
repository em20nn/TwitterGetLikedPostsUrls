# import encodings
import hashlib
# from dataclasses import dataclass
# from select import select
# from webbrowser import Chrome
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
import time
import os
import keyboard
import warnings
import argparse
import getpass

#--------------------- argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help="input username", type=str)
parser.add_argument('-p', '--passwd', help="input password", type=str)
parser.add_argument('-a', '--account',
                    help="account name to capure liked post urls", type=str)
parser.add_argument(
    '-t', '--type', help="registeration type (new_lines or spaces) (default=new_lines)", type=str)
parser.add_argument(
    '--until', help="script stops after reaching the following element", type=str)
parser.add_argument('-o', '--output', help="output file name", type=str)
parser.add_argument(
    '-f', '--fast', help='choose between 1 and 10, 10 being the fastest, default=2', type=int)
parser.add_argument(
    '-e', '--err', help='choose between 1 and 20 as maximum errors tolarenced, default = 8', type=int)
args = parser.parse_args()

#---------------------- ignore selenium warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

#------------------------ settings

headless = True
browserProfile = webdriver.ChromeOptions()
browserProfile.add_argument("--lang=en-us")
if headless == True:
    browserProfile.add_argument("--headless")
    browserProfile.add_argument("--window-size=1920,1080")
    browserProfile.add_argument("--disable-notifications")

#---------------------- check if chromedriver.exe is competible

try:
    browser = webdriver.Chrome('chromedriver.exe', options=browserProfile)
except Exception as e:
    if os.path.isfile(f"{os.getcwd()}/chrome_driver/chromedriver.exe"):
        if os.path.isfile("chromedriver.exe"):
            os.remove("chromedriver.exe")
        browser = webdriver.Chrome(
            f'{os.getcwd()}/chrome_driver/chromedriver.exe', options=browserProfile)
    else:
        if os.path.isfile("chromedriver.exe"):
            print("Your chromedriver.exe is not up to date, automatic update started")
        k = []
        ll = 0
        k.append(str(e).replace(" ", "\n").split())
        for i in k:
            while True:
                try:
                    i[ll]
                except IndexError:
                    print("Please download chromedriver.exe")
                    exit()
                if i[ll] == "is":
                    version = i[ll+1]
                    if version[0:3] == "103":
                        ver_url = "103.0.5060.24"
                    elif version[0:3] == "104":
                        ver_url = "104.0.5112.79"
                    elif version[0:3] == "105":
                        ver_url = "105.0.5195.52"
                    elif version[0:3] == "106":
                        ver_url = "106.0.5249.61"
                    elif version[0:3] == "107":
                        ver_url = "107.0.5304.62"
                    elif version[0:3] == "102":
                        ver_url = "102.0.5005.61"
                    elif version[0:3] == "101":
                        ver_url = "101.0.4951.15"
                    elif version[0:3] == "100":
                        ver_url = "100.0.4896.60"
                    elif version[0:2] == "99":
                        ver_url = "99.0.4844.51"
                    elif version[0:3] == "108":
                        ver_url = "108.0.5359.71"
                    elif version[0:3] == "109":
                        ver_url = "109.0.5414.74"
                    elif version[0:3] == "110":
                        ver_url = "110.0.5481.77"
                    elif version[0:3] == "111":
                        ver_url = "111.0.5563.64"
                    elif version[0:3] == "112":
                        ver_url = "112.0.5615.49" 
                    elif version[0:3] == "113":
                        ver_url = "113.0.5672.63" 
                    elif version[0:3] == "114":
                        ver_url = "114.0.5735.16" 
                    elif version[0:3] == "new":
                        ver_url = "new"                                                                                                                                                
                    else:
                        ver_url = version
                    import wget
                    import zipfile
                    print(ver_url)
                    wget.download(
                        f"https://chromedriver.storage.googleapis.com/{ver_url}/chromedriver_win32.zip", f"chromedriver.zip")
                    with zipfile.ZipFile(f"chromedriver.zip", 'r') as zip_ref:
                        if not os.path.isdir("chrome_driver"):
                            zip_ref.extractall("chrome_driver")
                            zip_ref.close()
                            os.remove("chromedriver.zip")
                            cwd = os.getcwd()
                            try:
                                browser = webdriver.Chrome(
                                    f'{cwd}/chrome_driver/chromedriver.exe', options=browserProfile)
                                if os.path.isfile("chromedriver.exe"):
                                    os.remove("chromedriver.exe")
                                break
                            except:
                                print(
                                    f"Your version is {version}, please download chromedriver.exe manually into {os.getcwd()}")
                                exit()
                        else:
                            os.remove("chromedriver.zip")
                            print(
                                f"\nDelete chrome_driver file in {os.getcwd()} and run again")
                            exit()
                else:
                    ll = ll+1

#----------------------- set and auth

if args.username:
    username = args.username
else:
    username = input('Twitter login username:')
if args.passwd:
    password = args.passwd
else:
    password = getpass.getpass('Twitter login password:')
if args.account:
    which_accounts_liked_posts = args.account
else:
    which_accounts_liked_posts = username
if args.type:
    new_lines_or_spaces = args.type
else:
    new_lines_or_spaces = "new_lines"
auto_del_ss = True
ss_with_key_stroke = True
quit_with_key_stroke = True
dev_infos = False
until_certain_element = True
if args.until:
    that_certain_element = args.until
else:
    that_certain_element = "https://twitter.com/***/status/***"
if args.output:
    final_file_path = args.output
else:
    final_file_path = "final.txt"
tmp_file_path = "tmp.txt"
if args.fast:
    how_fast = args.fast  # choose between 1 and 10, 10 being the fastest, default=2
else:
    how_fast = 2
if args.err:
    max_errors_expected = args.err  # choose between 1 and 20, default = 8
else:
    max_errors_expected = 20

if new_lines_or_spaces != "new_lines":
    if new_lines_or_spaces != "spaces":
        print("wrong registration type")
        exit()
if 1 > how_fast > 10:
    print("fast must be between 1 and 10")
    exit()
if 1 > max_errors_expected > 20:
    print("max expected error must be between 1 and 20")
    exit()
#-------------------- login and navigate to liked posts

start_login = time.time()
browser.get("https://twitter.com/i/flow/login")
browser.maximize_window()
check_custom = True
while check_custom == True:
    try:
        browser.find_element_by_tag_name("input").send_keys(f"{username}")
        check_custom = False
    except:
        continue
browser.find_element_by_xpath(
    "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div").click()
time.sleep(3)
try:
    browser.find_element_by_xpath(
        "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(f"{password}")
except:
    print("wrong username")
    exit()
browser.find_element_by_xpath(
    "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div").click()
time.sleep(2)
if str(browser.current_url) == "https://twitter.com/home":
    print("login successful")
    browser.get(f"https://twitter.com/{which_accounts_liked_posts}/likes")
else:
    print("wrong password or username")
    exit()
time.sleep(2)
end_login = time.time()

#------------------ tmp file exists check

if os.path.exists(f"{tmp_file_path}"):
    with open(tmp_file_path, "w", encoding="utf-8") as f:
        f.write(" ")

#-------------------- capture

start_capture = time.time()
print("capture started")
if not that_certain_element == 'https://twitter.com/***/status/***':
    print(
        f"capture will go until {that_certain_element} is reached; if not, capture will go until the end")
if quit_with_key_stroke:
    print("to end capturing please press and hold 'esc'")
if ss_with_key_stroke:
    print("to see a screenshot please press and hold 'ctrl'")
end_check = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
cer_ele = False
with open(tmp_file_path, "a", encoding="utf-8") as file:
    file.write(f"START url: {which_accounts_liked_posts}\n")
err_count = 0
err_break = False
while True:
    try:
        browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]").click()
    except:
        pass
    ele = browser.find_elements_by_css_selector(
        "a.css-4rbku5.css-18t94o4.css-901oao.r-14j79pv.r-1loqt21.r-1q142lx.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-3s2u2q.r-qvutc0")
    for i in ele:
        with open(tmp_file_path, "a", encoding="utf-8") as file:
            try:
                file.write(i.get_attribute('href'))
                file.write("\n")
            except:
                err_count = err_count+1
                if err_count == max_errors_expected:
                    err_break = True
                    break
                continue
        if until_certain_element:
            try:
                if i.get_attribute("href") == that_certain_element:
                    cer_ele = True
            except:
                continue
    if err_break == True:
        print(
            f"more than {max_errors_expected} errors occured, please lower fast (currently={how_fast}) and/or increase max errors expected (currently={max_errors_expected}) ")
        break
    if cer_ele == True:
        print("element reached")
        break
    with open(tmp_file_path, "r", encoding="utf-8") as file:
        last_line = file.readlines()[-1]
        end_check.append(last_line)
    if end_check[-1] == end_check[-10]:
        print("End of the page")
        break
    browser.execute_script("window.scrollBy(0,600)")
    time.sleep(1/how_fast)
    if quit_with_key_stroke:
        if keyboard.is_pressed("esc"):
            print("capture stopped, calculating")
            break
    if ss_with_key_stroke:
        if keyboard.is_pressed("ctrl"):
            browser.save_screenshot("screenshot.png")
            os.startfile("screenshot.png")
            time.sleep(1)
            if auto_del_ss:
                if os.path.exists("screenshot.png"):
                    os.remove("screenshot.png")
                else:
                    continue
end_capture = time.time()
browser.quit()

#-------------------- final file control

check_3 = True
while check_3 == True:
    if os.path.exists(f"{final_file_path}"):
        final_exists = input(
            f"'{final_file_path}' exists. to override=o, to write a new file name=n: ")
        if final_exists == "o":
            check_3 = False
            with open(final_file_path, "w", encoding="utf-8") as f:
                f.write(" ")
        elif final_exists == "n":
            check_3 = False
            final_file_path = input(
                "write new file name (ex. file_name.txt)(note that if the file exists, it will be overwritten): ")
        else:
            print("choice doesn't exists")
    else:
        check_3 = False

#---------------------- purging tmp file from duplicate lines and writing into final file --> new lines

reg_start = time.time()
completed_lines_hash = set()
output_file = open(final_file_path, "w", encoding="utf-8")
for line in open(tmp_file_path, "r", encoding="utf-8"):
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
os.remove("tmp.txt")
reg_end = time.time()

count = len(open(final_file_path).readlines())-1
if new_lines_or_spaces == "new_lines":
    if count == 0:
        print("0 posts have been detected. The tweets are either protected or not existent")
    else:
        print(
            f"{count} urls registered in file '{final_file_path}' in form of '{new_lines_or_spaces}'")

#-------------------- --> spaces

elif new_lines_or_spaces == "spaces":
    with open(final_file_path, 'r', encoding="utf-8") as f:
        filedata = f.read()
        filedata = filedata.replace('\n', ' ')
    with open(final_file_path, 'w', encoding="utf-8") as f:
        f.write(filedata)
    reg_end = time.time()
    if count == 0:
        print("0 posts have been detected. The tweets are either protected or not existent")
    else:
        print(
            f"{count} urls registered in file '{final_file_path}' in form of '{new_lines_or_spaces}'")

#--------------------- dev infos

if dev_infos == True:
    print(f"logged in in {end_login-start_login} seconds")
    print(f"capture in {end_capture-start_capture} seconds")
    print(f"registiration in {reg_end-reg_start} seconds")
    print(f"total of {err_count} errors occured")
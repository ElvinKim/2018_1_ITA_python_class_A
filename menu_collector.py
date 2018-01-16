import re
import urllib.request

req = urllib.request.Request("https://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=emp&dvs_cd=emp&stt_dt=2018-01-17&site_dvs=")
data = urllib.request.urlopen(req).read().decode("utf-8")

tbody_pattern_obj = re.compile('<tbody>(.*?)</tbody>', re.DOTALL)
tbody = tbody_pattern_obj.findall(data)[0]

menu_pattern_obj = re.compile('<td.*?>(.*?)</td>', re.DOTALL)
menu_result = menu_pattern_obj.findall(tbody)

for menu in menu_result:
    print(menu.replace("<br />", "").replace("&quot;", "").replace("&amp;", ""))
    print("-" * 30)



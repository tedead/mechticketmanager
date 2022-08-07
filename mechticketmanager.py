from time import sleep
import mechanize
import re

userName = ""
password = ""
url = "https://ia.itic.occinc.com/ialogin/iSiteLogin.jsp?isite=y&db=mo&disttrans=n&basetrans=n&trans_id=0&district_code=0&record_id=0&trans_state="
br = mechanize.Browser()

#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
response = br.open(url)
#print(response.read())      # the text of the page

br.select_form("myform")         # works when form has a name

for control in br.form.controls:
    if control.name == "iSiteUserName":
        control.value = userName
    if control.name == "iSitePassword":
        control.value = password
    #controlInfo = "type=%s, name=%s, value=%s" % (control.type, control.name, control.value)
    #print(controlInfo)

br.submit()
sleep(1)
response = br.open("https://ia.itic.occinc.com/ialogin/iSiteMenu.jsp")
sleep(1)

for link in br.links():
    dicAttrs = dict(link.attrs)  # First create a dict

    try:
        if str(dicAttrs["id"]) == "linkETM":
            request = br.click_link(link)
            response = br.follow_link(link)
            sleep(1)
            #print(response.geturl())
            #print(response.read())
            br.select_form("multiSelectForm")
            for control in br.form.controls:
                print(control.type)
                #print("Control Type: " + control.type + " | Control Name: " + control.name + " | Control Value: " + control.value)
    except:
        print("")

    #print(link.attrs[1]['id'])
    #for atr in link.attrs[1]:
    #    print(atr[0] + atr[1])
    #if link.attrs[1] == "linkETM":
    #    print("LINK FOUND!")
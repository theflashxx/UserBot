from googlesearch import search
from requests import get
from urllib.parse import quote_plus
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from userbot.events import register
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, CHROME_DRIVER, GOOGLE_CHROME_BIN


@register(outgoing=True, pattern=r"^.google (.*)")
async def gsearch(q_event):
    """ For .google command, Do a Google search. """
    if not q_event.text[0].isalpha() and q_event.text[0] not in (
            "/", "#", "@", "!"):
        match_ = q_event.pattern_match.group(1)
        match = quote_plus(match_)
        result = ""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = GOOGLE_CHROME_BIN
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
        await q_event.edit("`UserBot is Getting Information From Google Please Wait...` 🙇✍️")
        for i in search(match, stop=10):
            driver.get(i)
            title = driver.title
            result += f"📍**{title}**\n{i}\n\n"
        await q_event.edit(
            "**Google Search Query:**\n\n" + match_ + "\n\n**Results:**\n\n" + result,
            link_preview = False
            )
        if BOTLOG:
            await q_event.client.send_message(
                BOTLOG_CHATID,
                "Google Search query " + match_ + " was executed successfully",
            )


CMD_HELP.update({
    'google': '.google <query>\
        \nUsage: Do a Google search.'
})

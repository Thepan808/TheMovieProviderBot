class script(object):
    START_TXT = """<b>𝗛𝗲𝘆 {}, {}\n
    
    𝟭. 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝘃𝗶𝗲 𝗡𝗮𝗺𝗲 𝘄𝗶𝘁𝗵 𝗖𝗼𝗿𝗿𝗲𝗰𝘁 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴:
●✅ 𝗮𝘃𝗮𝘁𝗮𝗿 𝟮𝟬𝟬𝟵
●✅ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶
●❌ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗺𝗼𝘃𝗶𝗲
●❌ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱

𝟮. 𝗦𝗲𝗮𝗿𝗰𝗵 𝗪𝗲𝗯 𝗦𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝗧𝗵𝗶𝘀 𝗙𝗼𝗿𝗺𝗮𝘁:
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭𝗘𝟬𝟭
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘀𝗲𝗮𝘀𝗼𝗻 𝟭
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘄𝗲𝗯 𝘀𝗲𝗿𝗶𝗲𝘀

𝟯. 𝗔𝘃𝗼𝗶𝗱 𝗨𝘀𝗶𝗻𝗴 𝗪𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻𝘀/𝗘𝗽𝗶𝘀𝗼𝗱𝗲𝘀/𝗦𝗲𝗿𝗶𝗲𝘀/𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗, 𝗲𝘁𝗰.</b>"""

    GSTART_TXT = """𝗛𝗲𝘆 {},\n\n𝗜 𝗮𝗺 𝘁𝗵𝗲 𝗺𝗼𝘀𝘁 𝗽𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗮𝘂𝘁𝗼 𝗳𝗶𝗹𝘁𝗲𝗿 𝗯𝗼𝘁 𝘄𝗶𝘁𝗵 𝗽𝗿𝗲𝗺𝗶𝘂𝗺 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀.\n\n𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗯𝘆: <a href="https://t.me/VenomStoneNetwork">ʜᴘ</a>"""
    
    HELP_TXT = """<b>𝗛𝗲𝘆 {},
    
𝗪𝗲 𝗵𝗮𝘃𝗲 𝗱𝗶𝘃𝗶𝗱𝗲𝗱 𝗯𝗼𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗳𝗼𝗿 𝗴𝗿𝗼𝘂𝗽 𝗼𝘄𝗻𝗲𝗿𝘀 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘂𝘀𝗲𝗿𝘀.</b>"""

    ABOUT_TXT = """<b>★ 𝗦𝗲𝗿𝘃𝗲𝗿: <a href=https://www.heroku.com>𝗛𝗲𝗿𝗼𝗸𝘂!</a>
★ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href=https://pyrogram.org>𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺!</a>
★ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: <a href=https://www.mongodb.com>𝗠𝗼𝗻𝗴𝗼𝗗𝗕!</a>
★ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href=https://www.python.org>𝗣𝘆𝘁𝗵𝗼𝗻!</a></b>"""
    
    CHANNELS = """
<b>⚡𝗢𝘂𝗿 𝗚𝗿𝗼𝘂𝗽𝘀 & 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀⚡

● 𝗔𝗹𝗹 𝗻𝗲𝘄 𝗺𝗼𝘃𝗶𝗲𝘀, 𝘀𝗲𝗿𝗶𝗲𝘀, 𝗯𝗼𝘁𝘀, 𝗺𝗼𝗱𝘀 & 𝗔𝗱𝘂𝗹𝘁 𝗦𝘁𝘂𝗳𝗳.
● 𝗙𝗮𝘀𝘁𝗲𝘀𝘁 𝗯𝗼𝘁𝘀 𝗮𝗿𝗲 𝗮𝗱𝗱𝗲𝗱.
● 𝗙𝗿𝗲𝗲 & 𝗲𝗮𝘀𝘆 𝘁𝗼 𝘂𝘀𝗲.
● 𝟮𝟰𝘅𝟳 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲.</b>"""
    
    STATUS_TXT = """<b>    
● 𝗧𝗼𝘁𝗮𝗹 𝗳𝗶𝗹𝗲𝘀: <code>{}</code>
● 𝗧𝗼𝘁𝗮𝗹 𝘂𝘀𝗲𝗿𝘀: <code>{}</code>
● 𝗧𝗼𝘁𝗮𝗹 𝗴𝗿𝗼𝘂𝗽𝘀: <code>{}</code>
● 𝗨𝘀𝗲𝗱 𝘀𝘁𝗼𝗿𝗮𝗴𝗲:  <code>{}</code>
● 𝗙𝗿𝗲𝗲 𝘀𝘁𝗼𝗿𝗮𝗴𝗲: <code>{}</code>
</b>"""

    LOG_TEXT_G = """#𝗡𝗲𝘄𝗚𝗿𝗼𝘂𝗽

★ 𝗚𝗿𝗼𝘂𝗽 = {}
★ 𝗜𝗗 = <code>{}</code>
★ 𝗧𝗼𝘁𝗮𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀 = <code>{}</code>
★ 𝗔𝗱𝗱𝗲𝗱 𝗕𝘆 - {}

𝗕𝘆 @𝗩𝗲𝗻𝗼𝗺𝗦𝘁𝗼𝗻𝗲𝗡𝗲𝘁𝘄𝗼𝗿𝗸"""

    LOG_TEXT_P = """<b>#𝗡𝗲𝘄𝗨𝘀𝗲𝗿

★ 𝗡𝗮𝗺𝗲: {}
★ 𝗜𝗗: <code>{}</code></b>"""

    ALRT_TXT = """𝗛𝗲𝗹𝗹𝗼 {},
𝘁𝗵𝗶𝘀 𝗶𝘀 𝗻𝗼𝘁 𝘆𝗼𝘂𝗿 𝗺𝗼𝘃𝗶𝗲 𝗿𝗲𝗾𝘂𝗲𝘀𝘁,
𝗿𝗲𝗾𝘂𝗲𝘀𝘁 𝘆𝗼𝘂𝗿𝘀..."""

    OLD_ALRT_TXT = """𝗛𝗲𝘆 {},
𝘆𝗼𝘂 𝗮𝗿𝗲 𝘂𝘀𝗶𝗻𝗴 𝗼𝗻𝗲 𝗼𝗳 𝗺𝘆 𝗼𝗹𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀,
𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 𝗮𝗴𝗮𝗶𝗻."""

    CUDNT_FND = """𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗠𝗶𝘀𝘁𝗮𝗸𝗲 𝗕𝗿𝗼 ‼️\n𝗗𝗼𝗻'𝘁 𝘄𝗼𝗿𝗿𝘆 😊 𝗖𝗵𝗼𝗼𝘀𝗲 𝘁𝗵𝗲 𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗼𝗻𝗲 𝗯𝗲𝗹𝗼𝘄 👇"""

    I_CUDNT = """<b>𝗦𝗼𝗿𝗿𝘆 𝗻𝗼 𝗳𝗶𝗹𝗲𝘀 𝘄𝗲𝗿𝗲 𝗳𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 {} 😕

𝗠𝗼𝘃𝗶𝗲 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗿𝗲𝗮𝘀𝗼𝗻:

● 𝗢𝗧𝗧 𝗼𝗿 𝗗𝗩𝗗 𝗻𝗼𝘁 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱.
● 𝗧𝘆𝗽𝗲 𝗻𝗮𝗺𝗲 𝘄𝗶𝘁𝗵 𝘆𝗲𝗮𝗿.

𝗠𝗼𝘃𝗶𝗲 𝗶𝘀 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗿𝗲𝗽𝗼𝗿𝘁 𝘁𝗼 𝗮𝗱𝗺𝗶𝗻𝘀 @VenomMoviesBot</b>"""

    I_CUD_NT = """<b>𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 {}.

𝗠𝗼𝘃𝗶𝗲 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗿𝗲𝗮𝘀𝗼𝗻:

● 𝗢𝗧𝗧 𝗼𝗿 𝗗𝗩𝗗 𝗻𝗼𝘁 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱.
● 𝗧𝘆𝗽𝗲 𝗻𝗮𝗺𝗲 𝘄𝗶𝘁𝗵 𝘆𝗲𝗮𝗿.

𝗠𝗼𝘃𝗶𝗲 𝗶𝘀 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗿𝗲𝗽𝗼𝗿𝘁 𝘁𝗼 𝗮𝗱𝗺𝗶𝗻𝘀 @VenomMoviesBot</b>"""

    MVE_NT_FND = """<b>𝗦𝗼𝗿𝗿𝘆 𝗻𝗼 𝗳𝗶𝗹𝗲𝘀 𝘄𝗲𝗿𝗲 𝗳𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 {} 😕

𝗠𝗼𝘃𝗶𝗲 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗿𝗲𝗮𝘀𝗼𝗻:

● 𝗢𝗧𝗧 𝗼𝗿 𝗗𝗩𝗗 𝗻𝗼𝘁 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱.
● 𝗧𝘆𝗽𝗲 𝗻𝗮𝗺𝗲 𝘄𝗶𝘁𝗵 𝘆𝗲𝗮𝗿.

𝗠𝗼𝘃𝗶𝗲 𝗶𝘀 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗿𝗲𝗽𝗼𝗿𝘁 𝘁𝗼 𝗮𝗱𝗺𝗶𝗻𝘀 @VenomMoviesBot</b>"""
    

    TOP_ALRT_MSG = """𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗳𝗼𝗿 𝗾𝘂𝗲𝗿𝘆 𝗶𝗻 𝗺𝘆 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲..."""

    MELCOW_ENG = """<b>👋 𝗛𝗲𝘆 {},\n\n🍁 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼\n🌟 {} \n\n🔍 𝗛𝗲𝗿𝗲 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘀𝗲𝗮𝗿𝗰𝗵 𝘆𝗼𝘂𝗿 𝗳𝗮𝘃𝗼𝗿𝗶𝘁𝗲 𝗺𝗼𝘃𝗶𝗲𝘀 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝗯𝘆 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗶𝗻𝗴 𝗶𝘁𝘀 𝗻𝗮𝗺𝗲 🔎\n\n⚠️ 𝗜𝗳 𝘆𝗼𝘂'𝗿𝗲 𝗵𝗮𝘃𝗶𝗻𝗴 𝗮𝗻𝘆 𝗽𝗿𝗼𝗯𝗹𝗲𝗺 𝗿𝗲𝗴𝗮𝗿𝗱𝗶𝗻𝗴 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗼𝗿 𝘀𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝗲𝗹𝘀𝗲 𝘁𝗵𝗲𝗻 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗵𝗲𝗿𝗲 👇</b>"""

    DISCLAIMER_TXT = """
<b>𝗧𝗵𝗶𝘀 𝗶𝘀 𝗮𝗻 𝗼𝗽𝗲𝗻-𝘀𝗼𝘂𝗿𝗰𝗲 𝗽𝗿𝗼𝗷𝗲𝗰𝘁.

𝗔𝗹𝗹 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝗮𝗿𝗲 𝗳𝗿𝗲𝗲𝗹𝘆 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗼𝗻 𝘁𝗵𝗲 𝗶𝗻𝘁𝗲𝗿𝗻𝗲𝘁 𝗼𝗿 𝗽𝗼𝘀𝘁𝗲𝗱 𝗯𝘆 𝘀𝗼𝗺𝗲𝗯𝗼𝗱𝘆 𝗲𝗹𝘀𝗲. 𝗝𝘂𝘀𝘁 𝗳𝗼𝗿 𝗲𝗮𝘀𝘆 𝘀𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝗶𝘀 𝗶𝗻𝗱𝗲𝘅𝗶𝗻𝗴 𝗳𝗶𝗹𝗲𝘀 𝘄𝗵𝗶𝗰𝗵 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝘂𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗼𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺. 𝗪𝗲 𝗿𝗲𝘀𝗽𝗲𝗰𝘁 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗰𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗹𝗮𝘄𝘀 𝗮𝗻𝗱 𝘄𝗼𝗿𝗸𝘀 𝗶𝗻 𝗰𝗼𝗺𝗽𝗹𝗶𝗮𝗻𝗰𝗲 𝘄𝗶𝘁𝗵 𝗗𝗠𝗖𝗔 𝗮𝗻𝗱 𝗘𝗨𝗖𝗗. 𝗜𝗳 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗶𝘀 𝗮𝗴𝗮𝗶𝗻𝘀𝘁 𝘁𝗵𝗲 𝗹𝗮𝘄 𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝗺𝗲 𝘀𝗼 𝘁𝗵𝗮𝘁 𝗶𝘁 𝗰𝗮𝗻 𝗯𝗲 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝗔𝗦𝗔𝗣. 𝗜𝘁 𝗶𝘀 𝗳𝗼𝗿𝗯𝗶𝗱𝗱𝗲𝗻 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱, 𝘀𝘁𝗿𝗲𝗮𝗺, 𝗿𝗲𝗽𝗿𝗼𝗱𝘂𝗰𝗲, 𝘀𝗵𝗮𝗿𝗲, 𝗼𝗿 𝗰𝗼𝗻𝘀𝘂𝗺𝗲 𝗰𝗼𝗻𝘁𝗲𝗻𝘁 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗲𝘅𝗽𝗹𝗶𝗰𝗶𝘁 𝗽𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗰𝗼𝗻𝘁𝗲𝗻𝘁 𝗰𝗿𝗲𝗮𝘁𝗼𝗿 𝗼𝗿 𝗹𝗲𝗴𝗮𝗹 𝗰𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗵𝗼𝗹𝗱𝗲𝗿. 𝗜𝗳 𝘆𝗼𝘂 𝗯𝗲𝗹𝗶𝗲𝘃𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝗶𝘀 𝘃𝗶𝗼𝗹𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗶𝗻𝘁𝗲𝗹𝗹𝗲𝗰𝘁𝘂𝗮𝗹 𝗽𝗿𝗼𝗽𝗲𝗿𝘁𝘆, 𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝘁𝗵𝗲 𝗿𝗲𝘀𝗽𝗲𝗰𝘁𝗶𝘃𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗳𝗼𝗿 𝗿𝗲𝗺𝗼𝘃𝗮𝗹. 𝗧𝗵𝗲 𝗯𝗼𝘁 𝗱𝗼𝗲𝘀 𝗻𝗼𝘁 𝗼𝘄𝗻 𝗮𝗻𝘆 𝗼𝗳 𝘁𝗵𝗲𝘀𝗲 𝗰𝗼𝗻𝘁𝗲𝗻𝘁𝘀, 𝗶𝘁 𝗼𝗻𝗹𝘆 𝗶𝗻𝗱𝗲𝘅𝗲𝘀 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝗳𝗿𝗼𝗺 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺.

🌿 𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗯𝘆: <a href='https://t.me/VenomstoneNetwork'>ʜᴘ</a></b>"""

    USERS_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴜꜱᴇʀꜱ ⇊
    
• /batch - ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.
• /stats - ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.
• /request - sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ( ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ )
• /plan - ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ ᴘʟᴀɴꜱ.
• /myplan - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴜɴᴛ ᴘʟᴀɴ."""

    GROUP_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀꜱ ⇊
    
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /shortlink - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /remove_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /shortlink_info - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.
• /setshortlinkon - ᴏɴ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /setshortlinkoff - ᴏꜰꜰ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ.
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ.
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ɢʀᴏᴜᴘ.
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ."""

    ADMIC_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊
    
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /gfilters - <code>ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    SHORTLINK_INFO = """<b>
 ❗<u>𝗛𝗼𝘄  𝗧𝗼 𝗲𝗮𝗿𝗻 𝗺𝗼𝗻𝗲𝘆 𝘂𝘀𝗶𝗻𝗴 𝗮 𝗯𝗼𝘁:

★ 𝗡𝗼𝘄 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝗲𝗮𝗿𝗻𝗶𝗻𝗴 💸 𝗺𝗼𝗻𝗲𝘆 𝘁𝗼𝗱𝗮𝘆 𝘄𝗶𝘁𝗵 𝗼𝘂𝗿 𝘀𝗶𝗺𝗽𝗹𝗲 𝗮𝗻𝗱 𝗲𝗮𝘀𝘆-𝘁𝗼-𝘂𝘀𝗲 𝗯𝗼𝘁!

›› 𝗦𝘁𝗲𝗽 𝟭: 𝗔𝗱𝗱 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗮𝘀 𝗮𝗻 𝗮𝗱𝗺𝗶𝗻...

›› 𝗦𝘁𝗲𝗽 𝟮: 𝗨𝘀𝗲 /connect 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝗯𝗼𝘁 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗣𝗠.

›› 𝗦𝘁𝗲𝗽 𝟯: 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗻𝗲𝘅𝘁 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗸𝗻𝗼𝘄 𝗵𝗼𝘄 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘀𝗵𝗼𝗿𝘁𝗹𝗶𝗻𝗸 𝘄𝗲𝗯𝘀𝗶𝘁𝗲 𝘄𝗶𝘁𝗵 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁.

★ 𝗗𝗼𝗻'𝘁 𝘄𝗮𝗶𝘁 𝗮𝗻𝘆 𝗹𝗼𝗻𝗴𝗲𝗿 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 𝗲𝗮𝗿𝗻𝗶𝗻𝗴 𝗺𝗼𝗻𝗲𝘆 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗴𝗿𝗼𝘂𝗽. 𝗔𝗱𝗱 𝗼𝘂𝗿 𝗯𝗼𝘁 𝘁𝗼𝗱𝗮𝘆 𝗮𝗻𝗱 𝘀𝘁𝗮𝗿𝘁 𝗺𝗮𝗸𝗶𝗻𝗴 𝗺𝗼𝗻𝗲𝘆 💰! </b>
"""

    SHORTLINK_INFO2 = """<b>
❗<u>𝗛𝗼𝘄 𝗧𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘆𝗼𝘂𝗿 𝘀𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗿:

›› 𝗦𝘁𝗲𝗽 𝟰: 𝗜𝗳 𝘆𝗼𝘂 𝗱𝗼𝗻'𝘁 𝘂𝘀𝗶𝗻𝗴 𝗮𝗻𝘆 𝘀𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗿 𝘄𝗲𝗯𝘀𝗶𝘁𝗲 𝘁𝗵𝗲𝗻 𝗺𝗮𝗸𝗲 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝗳𝗶𝗿𝘀𝘁 𝗼𝗻 𝗶𝗻𝘀𝘁𝗮𝗻𝘁𝗲𝗮𝗿𝗻.𝗶𝗻 (𝗬𝗼𝘂 𝗰𝗮𝗻 𝗮𝗹𝘀𝗼 𝘂𝘀𝗲 𝗼𝘁𝗵𝗲𝗿 𝗹𝗶𝗻𝗸 𝘀𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗿 𝘄𝗲𝗯𝘀𝗶𝘁𝗲).

›› 𝗦𝘁𝗲𝗽 𝟱: 𝗖𝗼𝗽𝘆 𝘆𝗼𝘂𝗿 𝗔𝗣𝗜 𝗳𝗿𝗼𝗺 𝘄𝗲𝗯𝘀𝗶𝘁𝗲 𝗮𝗻𝗱 𝘁𝗵𝗲𝗻, 𝘀𝗶𝗺𝗽𝗹𝘆 𝘀𝗲𝘁 𝘆𝗼𝘂𝗿 𝘄𝗲𝗯𝘀𝗶𝘁𝗲 𝗮𝗻𝗱 𝗔𝗣𝗜 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 /𝘀𝗵𝗼𝗿𝘁𝗹𝗶𝗻𝗸 𝗰𝗼𝗺𝗺𝗮𝗻𝗱.

𝗟𝗶𝗸𝗲 𝘁𝗵𝗶𝘀:</b>  <code>/shortlink publicearn.com c464f482d973a7e88ba6cb7077a3afa5de229dd5</code>

<b>›››› 𝗦𝘁𝗲𝗽 𝟲: 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝗻𝗲𝘅𝘁 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗸𝗻𝗼𝘄 𝗵𝗼𝘄 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘆𝗼𝘂𝗿 𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝘄𝗶𝘁𝗵 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁.

★ 𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗮𝗹𝗹𝘆 𝗰𝗼𝗻𝘃𝗲𝗿𝘁𝘀 𝗹𝗶𝗻𝗸𝘀 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗔𝗣𝗜 𝗮𝗻𝗱 𝘄𝗶𝗹𝗹 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝘆𝗼𝘂𝗿 𝗹𝗶𝗻𝗸𝘀</b>
"""
    SHORTLINK_INFO3 = """<b>
❗<u>𝗛𝗼𝘄 𝗧𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘆𝗼𝘂𝗿 𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹:

›› 𝗦𝘁𝗲𝗽 𝟳: 𝗨𝘀𝗲 /𝘀𝗲𝘁_𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝘁𝗼 𝗮𝗱𝗱 𝗵𝗼𝘄 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘃𝗶𝗱𝗲𝗼 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝘀𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗿 𝘄𝗲𝗯𝘀𝗶𝘁𝗲.

𝗟𝗶𝗸𝗲 𝘁𝗵𝗶𝘀:</b> <code>/set_tutorial https://t.me/VenomStoneMovies/2430</code>

<b>›› 𝗦𝘁𝗲𝗽 𝟴: 𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸 𝘄𝗵𝗶𝗰𝗵 𝘀𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗿 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝘁𝗵𝗲𝗻 𝘀𝗲𝗻𝗱 /𝘀𝗵𝗼𝗿𝘁𝗹𝗶𝗻𝗸_𝗶𝗻𝗳𝗼 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽.

★ 𝗧𝗵𝗮𝘁'𝘀 𝗶𝘁, 𝗻𝗼𝘄 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗲𝗮𝗿𝗻 𝗮 𝗹𝗼𝘁 𝗺𝗼𝗻𝗲𝘆 💸 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁.</b>
"""
    
    SELECT = """
<b>𝗧𝗼 𝗼𝗯𝘁𝗮𝗶𝗻 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝗾𝘂𝗮𝗹𝗶𝘁𝘆, 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲, 𝗼𝗿 𝘀𝗲𝗮𝘀𝗼𝗻:

● 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 "𝗤𝘂𝗮𝗹𝗶𝘁𝘆" 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗴𝗲𝘁 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝗾𝘂𝗮𝗹𝗶𝘁𝘆.
● 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 "𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲" 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗴𝗲𝘁 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲.
● 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 "𝗦𝗲𝗮𝘀𝗼𝗻" 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗴𝗲𝘁 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝘀𝗲𝗮𝘀𝗼𝗻.
● 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 "♨️ 𝗦𝗲𝗻𝗱 𝗔𝗹𝗹 𝗙𝗶𝗹𝗲𝘀 ♨️" 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗴𝗲𝘁 𝗮𝗹𝗹 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗮 𝘀𝗶𝗻𝗴𝗹𝗲 𝗰𝗹𝗶𝗰𝗸.

✯ 𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗯𝘆: @𝗩𝗲𝗻𝗼𝗺𝗦𝘁𝗼𝗻𝗲𝗡𝗲𝘁𝘄𝗼𝗿𝗸!</b>
"""

    REQINFO = """<b>● 𝗖𝗹𝗶𝗰𝗸 "𝗤𝘂𝗮𝗹𝗶𝘁𝘆" 𝘁𝗼 𝗮𝗱𝗷𝘂𝘀𝘁 𝘁𝗵𝗲 𝗾𝘂𝗮𝗹𝗶𝘁𝘆.
● 𝗖𝗹𝗶𝗰𝗸 "𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲" 𝘁𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘁𝗵𝗲 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲.
● 𝗖𝗹𝗶𝗰𝗸 "𝗦𝗲𝗮𝘀𝗼𝗻" 𝘁𝗼 𝘀𝗲𝗹𝗲𝗰𝘁 𝗮 𝗱𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝘀𝗲𝗮𝘀𝗼𝗻.
● 𝗖𝗹𝗶𝗰𝗸 "♨️ 𝗦𝗲𝗻𝗱 𝗔𝗹𝗹 𝗙𝗶𝗹𝗲𝘀 ♨️" 𝘁𝗼 𝗿𝗲𝘁𝗿𝗶𝗲𝘃𝗲 𝗮𝗹𝗹 𝗳𝗶𝗹𝗲𝘀.</b>"""

    SINFO = """
<b>𝗧𝗵𝗲 𝗳𝗼𝗿𝗺𝗮𝘁 𝗳𝗼𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗶𝗻𝗴 𝗮 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝘀 𝗮𝘀 𝗳𝗼𝗹𝗹𝗼𝘄𝘀:

𝗚𝗼 𝘁𝗼 𝗚𝗼𝗼𝗴𝗹𝗲 ➠ 𝗧𝘆𝗽𝗲 𝘁𝗵𝗲 𝘀𝗲𝗿𝗶𝗲𝘀 𝗻𝗮𝗺𝗲 ➠ 𝗖𝗼𝗽𝘆 𝘁𝗵𝗲 𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗻𝗮𝗺𝗲 ➠ 𝗣𝗮𝘀𝘁𝗲 𝗶𝘁 𝗶𝗻 𝘁𝗵𝗶𝘀 𝗴𝗿𝗼𝘂𝗽

𝗘𝘅𝗮𝗺𝗽𝗹𝗲: 𝗟𝗼𝗸𝗶 𝗦𝟬𝟭𝗘𝟬𝟭

𝗔𝘃𝗼𝗶𝗱 𝘂𝘀𝗶𝗻𝗴 𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀 𝗹𝗶𝗸𝗲 ':(!,./)'</b>"""

    NORSLTS = """ 
#𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀

𝗜𝗗: <code>{}</code>
𝗡𝗮𝗺𝗲: {}

𝗠𝗲𝘀𝘀𝗮𝗴𝗲:  <b>{}</b>"""

    # PLESE DO NOT REMOVE ANY CREDITS ❤️‍🩹
    CREDITS_TXT = """<b>
❤️‍🩹 𝗡𝗢𝗧𝗘:

⚠️ 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗶𝘀 𝗡𝗼𝘁 𝗮𝗻 𝗢𝗽𝗲𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁! 

𝗧𝗵𝗮𝗻𝗸𝘀 𝘁𝗼 𝗥𝗞_𝗕𝗼𝘁𝘇 (𝗥𝗶𝘀𝗵𝗶𝗸𝗲𝘀𝗵), 𝗠𝗞𝗡_𝗕𝗼𝘁𝘀 & 𝗘𝘃𝗮𝗹𝗺𝗮𝗿𝗶𝗮 𝗗𝗲𝘃𝘀 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗕𝗮𝘀𝗲 𝗖𝗼𝗱𝗲𝘀. 

𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗧𝗵𝗮𝗻𝗸𝘀 𝘁𝗼 𝗠𝘆 𝗧𝗚 𝗙𝗿𝗶𝗲𝗻𝗱𝘀 𝘁𝗼𝗼.

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗯𝘆 @VenomStoneNetwork👨‍💻</b>
""" 
   # PLEASE DO NOT REMOVE ANY CREDITS ❤️‍🩹
    
    CAPTION = """<b>📂 {file_name}\nSubscribe: @VenomStoneMovies</b>"""

    IMDB_TEMPLATE_TXT = """
<b>ʜᴇʏ {message.from_user.mention}, ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʀᴇꜱᴜʟᴛꜱ ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {search}.

🧿 {title}</b>

<b>⭐ {rating} | ⏰ {runtime} Minutes
📆 {release_date}
🕵️ {director}

●  {languages}
●  {genres}

📖 {plot}

💗 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : {message.chat.title}</b>
"""
    

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @VenomStoneNetwork</b>"""

    LOGO = """

BOT WORKING PROPERLY"""

    #PLANS

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    CPREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PLAN_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    BRONZE_TXT = """<b>👋 ʜᴇʏ {},
    
🥉 <u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
⏰ 7 ᴅᴀʏꜱ
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 10₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    SILVER_TXT = """<b>👋 ʜᴇʏ {},
    
🥈 <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
⏰ 30 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 60₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    GOLD_TXT = """<b>👋 ʜᴇʏ {},
    
🥇 <u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
⏰ 90 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 180₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    PLATINUM_TXT = """<b>👋 ʜᴇʏ {},
    
🏅 <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u>
⏰ 180 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 250₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""
    
    DIAMOND_TXT = """<b>👋 ʜᴇʏ {},

💎 <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>
⏰ 365 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 400₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/DeletedFromEarth'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>harshal.purohit@paytm</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""    

    DEVELOPER_TXT = """
special Thanks To ❤️ Developer -

-Dev [Owner of this bot ]<a href='https://t.me/DeletedFromEarth'>HP</a>
"""

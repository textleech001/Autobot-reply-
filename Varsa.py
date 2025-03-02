{
    "name": "Nursing Nation Bot",
    "description": "Conversation Bot.",
    "logo": "",
    "keywords": [
        "telegram",
        "Conversation Bot",
        "bot"
    ],
    "repository": "https://github.com/Arjunji001",
    "website": "",
    "success_url": "https://t.me/Nursing_Nation_bot",
    "env": {
        "API_HASH": {
            "description": "Your API HASH from my.telegram.org",
            "value": "0c58f3e3fecefc4a9d8e5bcf6968a106"
        },
        "API_ID": {
            "description": "Your API ID from my.telegram.org",
            "value": "23680771"
        },
        "BOT_TOKEN": {
            "description": "Bot token, get it from @BotFather.",
            "value": "7905988252:AAHNtoSq76j5cQaMfvtioiailGfEaqfz_qM"
        },
        "SESSION": {
            "description": "Pyrogram string session.",
            "value": ""
        },
        "AUTH": {
            "description": "User ID of Bot owner.",
            "value": "7609672518"
        },
        "FORCESUB": {
            "description": "Username name of public channel without using '@'.",
            "value": "https://t.me/testbotdrive"
        }
    },
    "buildpacks": [
        {
            "url": "heroku/python"
        },
        {
            "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git"
        }
    ]
}

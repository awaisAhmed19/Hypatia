from discord.ext.commands import check, CheckFailure

ANNOUNCEMENT_CHANNEL = 1365689373407969482
INTRODUCTION_CHANNEL = 1365689759330074747
GENERAL_CHANNEL = 1365689682557407252
PROJECT_SHOWCASE_CHANNEL = 1365689854108897456
PROJECT_FEEDBACK_CHANNEL = 1365689893510189228
DSA_CHALLENGE_CHANNEL = 1365690174381756619
CODING_CHALLENGE_CHANNEL = 1365690220925943840
RESOURCES_CHANNEL = 1365690265494356029
SCROLL_REQUEST_CHANNEL = 1365690335245635676
BOT_COMMANDS_CHANNEL = 1365690377075556352

OutPut_Blocked_Channels = {1365689373407969482, 1366034400248332328}


def output_blocked_channels():
    async def predicate(ctx):
        return ctx.channel.id not in OutPut_Blocked_Channels

    return check(predicate)


# Greetings list
GREETINGS = (
    "yo",
    "sup",
    "what's poppin'",
    "hey bestie",
    "howdy",
    "heyyy",
    "wassup",
    "yooo",
    "ayoo",
    "hiii",
    "what’s good",
    "sheeesh",
    "top of the morning",
    "yo fam",
    "my slime",
    "greetings earthling",
    "what it do",
    "wagwan",
    "hola",
    "eyy",
    "hey hey hey",
)

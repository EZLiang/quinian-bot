import discord, sys, random


client = discord.Client(status="Ping me for a quine")
user = client.user


quined = []


quines = [
    ("a='a=%s%s%s;print(a%%(chr(39),a,chr(39)))';print(a%(chr(39),a,chr(39)))", "python"),
    ("b='b={}{}{};print(b.format(chr(39),b,chr(39)))';print(b.format(chr(39),b,chr(39)))", "python"),
    ("c='c=%r;print(c%%c)';print(c%c)", "python"),
    ("exec(s='print(\"exec(s=%r)\"\\%s)')", "python"),
    ("public class Quine {\n  public static void main(String[] args) {\n    char q = 34;\n    String[] l = {\n    "
     "\"public class Quine {\",\n    \"  public static void main(String[] args) {\",\n    \"    char q = 34;\","
     "\n    \"    String[] l = {\",\n    \"    \",\n    \"    };\",\n    \"    for(int i = 0; i < 6; i++)\","
     "\n    \"        System.out.println(l[i]);\",\n    \"    for(int i = 0; i < l.length; i++)\",\n    \"        "
     "System.out.println(l[6] + q + l[i] + q + ',');\",\n    \"    for(int i = 7; i < l.length; i++)\",\n    \"       "
     " System.out.println(l[i]);\",\n    \"  }\",\n    \"}\",\n    };\n    for(int i = 0; i < 6; i++)\n        "
     "System.out.println(l[i]);\n    for(int i = 0; i < l.length; i++)\n        System.out.println(l[6] + q + l[i] + "
     "q + ',');\n    for(int i = 7; i < l.length; i++)\n        System.out.println(l[i]);\n  }\n}", "java"),
    ("eval s=\"print 'eval s=';p s\"", "ruby")
]


def get_channel(name):
    for channel in client.get_all_channels():
        if channel.name == name:
            return channel
    return None


@client.event
async def on_message(msg):
    mention = client.user.mention.replace("@", "@!")
    if mention in msg.content:
        m = msg.content.split(mention + " ")[-1]
        if m.lower().startswith("what are you "):
            q = m.lower()[13:].split("?")[0]
            await msg.channel.send("What am I " + q + "? What are _you_ " + q + "?!?")
            return
        if m[:7] == "random ":
            query = m[7:]
            if query.startswith("quined"):
                if len(quined) == 0:
                    await msg.channel.send(":slight_frown: We don't have any quined phrases now. Try again a little "
                                           "later!")
                    return
                await msg.channel.send(random.choice(quined))
                return
            elif query.startswith("quine"):
                quine = random.choice(quines)
                await msg.channel.send("```" + quine[1] + "\n" + quine[0] + "\n```")
            elif query.startswith("diceroll"):
                await msg.channel.send(":game_die: :" + random.choice(["one", "two", "three", "four", "five", "six"]) +
                                       ":")
            else:
                await msg.channel.send("Hey! I don't know how to do that!")
                return
            await msg.channel.send("Happy? :smirk:")
            return
        quine = "\"" + m[0].upper() + m[1:] + " when preceded by its quotation\" " + m + " when preceded by its " \
                                                                                         "quotation "
        await msg.channel.send(quine)
        quined.append(quine)
    if "wtf" in msg.content or "fuck" in msg.content or "hell" in msg.content or "damn" in msg.content or "shut up" in\
            msg.content:
        await msg.channel.send("Watch your language " + msg.author.mention + ". If I had mod permission I would ban "
                                                                             "you. :b: :a: :regional_indicator_n:")
        return


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def main():
    client.run(sys.argv[1])


if __name__ == "__main__":
    main()

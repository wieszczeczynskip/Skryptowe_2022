from collections import Counter

txt1 = "#love #tumblr #memes #quotes #funnytexts #texting #funny #tweets #textpost #texture #frasi #tweegram #tweet /" \
       "#tweetext #tweetexts #texgram #tweedride #instapage #tweembler #frasier #frasitumblr #tweeter #tweemblers \
       #tweeters #frasista #textmessage #frasistas #bhfyp"

txt1 = txt1.replace("#", " ")
txt1 = txt1.strip()
txt1 = txt1.replace("  ", " ")
words = txt1.split()

print(txt1)
print(words)

wordsDict = dict()
for i in words:
    wordsDict[i] = len(i)

print(wordsDict)

print("Word            Letters")
message = "%-15s %7s"
for i in range(len(wordsDict)):
    print(message % (list(wordsDict.keys())[i], list(wordsDict.values())[i]))

txt2 = "A hashtag is a metadata tag that is prefaced by the pound sign or hash symbol, # (not to be confused with the pound currency sign). Hashtags are used on microblogging and photo-sharing services such as Twitter, Instagram and WeChat as a form of user-generated tagging that enables cross-referencing of content; that is, sharing a topic or theme. For example, a search within Instagram for the hashtag #bluesky returns all posts that have been tagged with that hashtag. After the initial hash symbol, a hashtag may include letters, digits, and underscores.] The use of hashtags was first proposed by American blogger, product consultant and speaker Chris Messina in a 2007 tweet. Messina made no attempt to patent the use because he felt \"they were born of the internet, and owned by no one\". In 2013, Twitter purportedly told the Wall Street Journal that \"these things are for nerds\" and their use \"wouldn't be adopted widely.\"] By the end of the decade, though, hashtags were entrenched in the culture of the platform, and they soon emerged across Instagram, Facebook, and YouTube. In June 2014, hashtag was added to the Oxford English Dictionary, as \"a word or phrase with the symbol # in front of it, used on social media websites and apps so that you can search for all messages with the same subject\". "

print(txt2)

txt2 = txt2.replace(",", ";")

print(txt2)

words = txt2.split()

counter = 0
for i in words:
    if i == "in" or i == "In":
        counter += 1;

print("\"in\" appears in the text " + str(counter) + " times.")

letters = list("".join(words))

print(letters)

lettersCounter = Counter(letters)

print(lettersCounter)

sentences = txt2.split(".")

sentences[0] = sentences[0].capitalize()
sentences[1] = sentences[1].upper()
sentences[2] = sentences[2].lower()
sentences[3] = sentences[3].title()
sentences[4] = sentences[4].replace("]", " ")
temp = ""
for i in sentences[4]:
    if i == "a" or i == "e" or i == "o" or i == "u" or i == "y" or i == "i":
        temp = temp + i.swapcase()
    else:
        temp = temp + i
sentences[4] = temp

sentence = sentences[0] + "." + sentences[1] + "." + sentences[2] + "." + sentences[3] + "." + sentences[4] + "."
print(sentence)

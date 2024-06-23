import aiohttp
import discord
import firebase_admin
from firebase_admin import db


#---------------------variables---------------------




#---------------------user tools---------------------

def user_exists(user):
    ref = db.reference(f"/users/{user.id}")
    return ref.get() != None

def create_user(user):
    ref = db.reference(f"/users/{user.id}")
    ref.set({
        "name": f"{user.name}",
        "lemons": 0,
        "bank": 0,
        "level": 1,
        "xp": 0,
        "streak": 0,
    })

def update_user_list(users):
    ref = db.reference(f"/users")
    ref.set(users)

def is_developer(user):

    devs = [322164128280215564]

    if user.id in devs:
        return True
    else:
        return False
#---------------------economy tools---------------------

def get_user_lemons(user):

    if not user_exists(user):
        create_user(user)

    ref = db.reference(f"/users/{user.id}/lemons")
    return ref.get()

def set_user_lemons(user,lemons):
    ref = db.reference(f"/users/{user.id}/lemons")
    ref.set(lemons)

def getUserBank (user):
    ref = db.reference(f"/users/{user.id}/bank")
    return ref.get()

def setUserBank (user,bank):
    ref = db.reference(f"/users/{user.id}/bank")
    ref.set(bank)

def right_amount(ctx , amount):

    user_lem = get_user_lemons(ctx.author)

    """turn amounts with k or m into numbers"""
    try :
        if amount.endswith("k") or amount.endswith("K"):
            amount = amount[:-1]
            amount = int(amount)
            amount = amount * 1000
            return amount
        elif amount.endswith("m") or amount.endswith("M"):
            amount = amount[:-1]
            amount = int(amount)
            amount = amount * 1000000
            return amount
    except :
        print("error")
    
    if amount == None :
        amount = 1
        return amount

    elif amount == "all" or amount == "max":
                
        if user_lem <= 100000 :
            amount = user_lem
            return amount
        else :
            amount = 100000
            return amount
    elif amount == "half" :
                    
        if (user_lem//2) <= 100000 :
            amount = user_lem//2
            return amount
        else :
            amount = 100000
            return amount
        

    else :
        amount = int(amount)
        return amount
    
def update_server_fine_box(server,fine):
    ref = db.reference(f"/servers/{server.id}/fine_box")
    ref.set(fine)

def get_server_fine_box(server):
    ref = db.reference(f"/servers/{server.id}/fine_box")
    return ref.get()

def get_user_streak(user):
    ref = db.reference(f"/users/{user.id}/streak")
    return ref.get()

def set_user_streak(user,streaks):
    ref = db.reference(f"/users/{user.id}/streak")
    ref.set(streaks)

#---------------------server tools---------------------

def set_server_prefix(server,prefix = None):
    
    if prefix == None:
        prefix = "l "

    ref = db.reference(f"/servers/{server.id}/prefix")
    ref.set(prefix)

    def right_amount(delf, ctx , amount):

        user_lem = get_user_lemons(ctx.author)
        
        if amount == None :
            amount = 1
            return amount

        elif amount == "all" or amount == "max":
                    
            if user_lem <= 100000 :
                amount = user_lem
                return amount
            else :
                amount = 100000
                return amount
        elif amount == "half" :
                        
            if (user_lem//2) <= 100000 :
                amount = user_lem//2
                return amount
            else :
                amount = 100000
                return amount

        else :
            amount = int(amount)
            return amount

def server_exists(server):
    ref = db.reference(f"/servers/{server.id}")
    return ref.get() != None

def create_server(server):
    ref = db.reference(f"/servers/{server.id}")
    ref.set({
        "name": f"{server.name}",
        "prefix": "l ",
        "fine_box": 0,
    })

def delete_server(server):
    ref = db.reference(f"/servers/{server.id}")
    ref.delete()
#---------------------level tools---------------------

def level_up(user):
    ref = db.reference(f"/users/{user.id}/level")
    ref.set(ref.get() + 1)

def get_user_level(user):
    ref = db.reference(f"/users/{user.id}/level")
    return ref.get()

def set_user_level(user,level):
    ref = db.reference(f"/users/{user.id}/level")
    ref.set(level)

def get_user_xp(user):
    ref = db.reference(f"/users/{user.id}/xp")
    return ref.get()

def set_user_xp(user,xp):
    ref = db.reference(f"/users/{user.id}/xp")
    ref.set(xp)
        
def server_member_list(server):
    ref = db.reference(f"/servers/{server.id}/members")
    return ref.get()

#---------------------other tools---------------------

def get_feedback_number():
    ref = db.reference(f"/feedback/number_of_feedbacks")
    return ref.get()

def add_feedback(ctx,feedback):
    """adds a feedback to the feedback list precising the user , the feedback and the server"""
    feedback_id = get_feedback_number()+1
    num = db.reference(f"/feedback/number_of_feedbacks")
    num.set(feedback_id)
    feedback = str(feedback)

    ref = db.reference(f"/feedback/{feedback_id}/user/id")
    ref.set(ctx.author.id)
    ref = db.reference(f"/feedback/{feedback_id}/user/name")
    ref.set(ctx.author.name)
    ref = db.reference(f"/feedback/{feedback_id}/server/id")
    ref.set(ctx.guild.id)
    ref = db.reference(f"/feedback/{feedback_id}/server/name")
    ref.set(ctx.guild.name)
    ref = db.reference(f"/feedback/{feedback_id}/feedback content")
    ref.set(feedback)
    reviewd = db.reference(f"/feedback/{feedback_id}/reviewed")
    reviewd.set(False)

def time_handler(time):
    """takes a time in seconds and returns a string of the time in days , hours , minutes and seconds"""
    time = int(time)
    days = time // 86400
    hours = (time - (days*86400)) // 3600
    minutes = (time - (days*86400) - (hours*3600)) // 60
    seconds = time - (days*86400) - (hours*3600) - (minutes*60)
    if days == 0:
        if hours == 0:
            if minutes == 0:
                return f"{seconds} seconds"
            else:
                return f"{minutes} minutes and {seconds} seconds"
        else:
            return f"{hours} hours , {minutes} minutes and {seconds} seconds"
    else:
        return f"{days} days , {hours} hours , {minutes} minutes and {seconds} seconds"
    
def bad_words(text):
    """returns a list of all the bad words in the text"""
    
    banned_words = ["anal", "anus", "arse", "ass","asshole", "balls", "ballsack", "bastard", "biatch", "bitch", "blow job", "blowjob", "bollock", "bollok", "boner", "boob", "bugger", "bum", "butt", "buttplug", "clitoris", "cock", "coon", "condom", "cunt", "damn", "dick", "dildo", "dyke", "f u c k", "fag", "feck", "felching", "fellate", "fellatio", "flange", "fuck", "fucking", "fudge packer", "fudgepacker", "homo", "jerk", "jizz", "knob end", "knobend", "labia", "muff","naked", "nigga", "nigger", "penis", "piss", "poop", "prick", "pube", "pussy", "queer", "scrotum", "sex", "slut", "smegma", "spunk", "tit", "tosser", "turd", "twat", "vagina", "wank", "whore"]


    text = text.lower()
    text = text.split(" ")
    #check every word in the text and if it's in the bad words return true
    for i in text:
        if i in banned_words:
            return True
        
    return False
    


#--------------------- nasa embeds ---------------------
    
def nasa_apod_embed(data):
    #get the data from the api and make an embed out of it

    embed = discord.Embed(title = f"Astronomy picture of the day", description = f"here's what laymouna found :")
    embed.add_field(name = "title :", value = data['title'], inline = False)
    embed.add_field(name = "copyright :", value = data["copyright"], inline = False)
    embed.add_field(name = "date :", value = data["date"] , inline = False)

    explanation = data["explanation"]

    #split into paragraphs and send each one in a different field (every paragraph ends with a dot)
    paragraphs = explanation.split(".")
    k = 0

    for i in paragraphs:
        if k == 0:
            title = "explanation :"
            k += 1
        else:
            title = ""
        embed.add_field(name = title, value = i, inline = False)

    embed.set_image(url = data["hdurl"])

    return embed

def nasa_earth_embed (data,img):

    embed = discord.Embed(title = f"Earth picture of the day", description = f"here's what laymouna found :")
    embed.add_field(name = "identifier :", value = data['identifier'], inline = False)
    embed.add_field(name = "caption :", value = data["caption"], inline = False)
    embed.add_field(name = "date :", value = data["date"] , inline = False)
    embed.add_field(name = "image :", value = data["image"] , inline = False)
    if img != None:
        embed.set_image(url = img)
    
    return embed

def nasa_moon_embed (data):
    
        embed = discord.Embed(title = f"here's a random picture from the moon", description = f"")
        embed.set_image(url = data["img_src"])
        
        return embed
    
def nasa_epic_embed (data):
    
        embed = discord.Embed(title = f"here's a random picture from the earth", description = f"date : {data['date']}")
        embed.set_image(url = data["url"])
        
        return embed

def l3a3a3out():
    embed = discord.Embed(title = f"l3a3a3out", description = f"miw")
    embed.set_image(url = "https://yt3.googleusercontent.com/I7Pq6tV0OnfkWSCKoG6tuc3FBp8ETUK446eq3DcgVi1r_Yd6XrK5RyVFp4e4Twj3lJsgTqd4RQ=s900-c-k-c0x00ffffff-no-rj")
    return embed























































































#---------------------tool test---------------------

def get_homework_count(user):
    ref = db.reference(f"/{user.id}/homework")
    """returns the number of homeworks in the homework list"""
    a=ref.get()
    if a == None:
        return 0
    else:
        return len(a)

def get_user_homework(user):
    ref = db.reference(f"/{user.id}/homework")
    return ref.get()

def add_homework(user,module,homework,dateDue):
    """adds a homework to the homework list precising the server , the module , the homework and the date due"""
    homework_id = get_homework_count(user)+1
    homework = str(homework)
    module = str(module)
    dateDue = str(dateDue)


    ref = db.reference(f"/{user.id}/homework/{homework_id}/module")
    ref.set(module)
    ref = db.reference(f"/{user.id}/homework/{homework_id}/homework")
    ref.set(homework)
    ref = db.reference(f"/{user.id}/homework/{homework_id}/date due")
    ref.set(dateDue)
    ref = db.reference(f"/{user.id}/homework/{homework_id}/done")
    ref.set(False)

def get_homework_list(user):
    """returns a list of all the homeworks"""
    homework_list = []
    for i in range(get_homework_count(user)):
        homework_list.append(get_user_homework(user)[f"{i+1}"])
    return homework_list

    



def get_feedback_count():
    ref = db.reference(f"/feedback/number_of_feedbacks")
    return ref.get()

def get_feedback(feedback_id):
    ref = db.reference(f"/feedback/{feedback_id}/feedback content")
    return ref.get()

def get_feedback_status(feedback_id):
    ref = db.reference(f"/feedback/{feedback_id}/reviewed")
    return ref.get()

def set_feedback_status(feedback_id,status):
    ref = db.reference(f"/feedback/{feedback_id}/reviewed")
    ref.set(status)








    
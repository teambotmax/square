# -*- coding: utf-8 -*-
# Kuroku Square Bots
# Creator : Dzin
# ID LINE : adzin.zh
# https://github.com/dzingans
# Thanks to Fadhiilrachman ( github.com/fadhiilrachman ) dan teman teman
# Tolong jangan edit bagian ini, hargai creator dan pengembang

from linepy import *
import time

line = LINE() #untuk login qr
#line = LINE('EMAIL', 'PASSWORD') #untuk login menggunakan email dan password
#line = LINE('AUTHTOKEN') #untuk login token

line.log("Auth Token : " + str(line.authToken))
squareChatMid='(YOUR_SQUARE_MID)' # Get manual from line.getJoinableSquareChats('YOUR_SQUARE_MID')

helpMessage = """Kuroku Bots
Type : Square Bots

Hi
Kuroku help
Kuroku speed
Kuroku creator
Kuroku mymid
Kuroku me

github.com/dzingans"""

# Initialize OEPoll with LINE instance
oepoll = OEPoll(line)

while True:
    try:
        eventsSquareChat=oepoll.singleFetchSquareChat(squareChatMid=squareChatMid)
        for e in eventsSquareChat:
            if e.createdTime is not 0:
                ts_old = int(e.createdTime) / 1000
                ts_now = int(time.time())
                line.log('[FETCH_TIME] ' + str(int(e.createdTime)))
                if ts_old >= ts_now:
                    '''
                        This is sample for implement BOT in LINE square
                        BOT will noticed who leave square chat
                        Command availabe :
                        > hi
                        > /author
                    '''
                    # Receive messages
                    if e.payload.receiveMessage != None:
                        payload=e.payload.receiveMessage
                        line.log('[RECEIVE_MESSAGE]')
                        msg=payload.squareMessage.message
                        msg_id=msg.id
                        receiver_id=msg._from
                        sender_id=msg.to
                        if msg.contentType == 0:
                            text=msg.text
                            if text.lower() == 'hi':
                                line.log('%s' % text)
                                line.sendSquareMessage(squareChatMid, 'Hi too! How are you?')                            
                            elif text.lower() == 'kuroku help':
                                line.log('%s' % text)
                                line.sendSquareMessage(squareChatMid, helpMessage)
                            elif text.lower() == 'kuroku speed':
                                start = time.time()
                                line.sendSquareMessage(squareChatMid, 'speed starting...') 
                                elapsed_time = time.time() - start
                                line.sendSquareMessage(squareChatMid, '%s' % (elapsed_time))
                            elif text.lower() == 'kuroku creator':     
                                line.log('%s' % text) 
                                line.sendSquareContact(squareChatMid, 'uc7d319b7d2d38c35ef2b808e3a2aeed9') 
                            elif text.lower() == 'kuroku mymid':
                                line.log('%s' % text)
                                line.sendSquareMessage(squareChatMid, receiver_id)
                            elif text.lower() == 'kuroku me':
                                line.log('%s' % text)
                                line.sendSquareContact(squareChatMid, receiver_id)         
                    # Notified leave Square Chat
                    elif e.payload.notifiedLeaveSquareChat != None:
                        payload=e.payload.notifiedLeaveSquareChat
                        line.log('[NOTIFIED_LEAVE_SQUARE_CHAT]')
                        squareMemberMid=payload.squareChatMid
                        squareMemberMid=payload.squareMemberMid
                        squareMember=payload.squareMember
                        line.sendSquareMessage(squareChatMid, 'Kuroku melihat ada yang kabur, kejar tuh kali aja maling :v')
                    else:
                        pass
            
    except Exception as e:
        line.log("[FETCH_SQUARE] Fetch square chat error: " + str(e))

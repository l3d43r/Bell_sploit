import os
import sys
import time


os.system("clear")
print (("""
 _
(_)  <---Bell   Exploit--->
 |______________________________________
 |&&&&&&&                        &&&&&&&|
 |&&&&&&&                        &&&&&&&|
 |&&&&&&&                        &&&&&&&|   QUEBEC IS LIKE
 |&&&&&&&         .\^/.          &&&&&&&|
 |&&&&&&&       . |&&&| .        &&&&&&&|   THE CANADA
 |&&&&&&&       |\|&&&|/|        &&&&&&&|
 |&&&&&&&    .--'&&&&&&&'--.     &&&&&&&|   OF CANADA
 |&&&&&&&     \&&&&&&&&&&&/      &&&&&&&|
 |&&&&&&&      >&&&&&&&&&<       &&&&&&&|
 |&&&&&&&     '~|/~~|~~\|~'      &&&&&&&|
 |&&&&&&&           |            &&&&&&&|
 |&&&&&&&                        &&&&&&&|
 |&&&&&&&                        &&&&&&&|
 |&BELL&&________________________&ROOT&&|
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 """).encode('utf-8'))


def spinning_cursor():
  while True:
    for cursor in '\\|/-':
      time.sleep( 0.2 )
      sys.stdout.write('\r{}'.format(cursor))
      sys.stdout.flush()



def mac():

    gtw  = "ipconfig getifaddr en0"
    gtw1 = "route get default | grep gateway | sed 's/^.*: //' "
    print ("GETING IP ADDRESS .....")
    time.sleep(0.3)
    print ("---> ip address:  " )
    sys.stdout.flush ( )
    os.system ( gtw )

    print ("GETTING GATEWAY....")
    print ("---> Router Ip Address : " )
    sys.stdout.flush ( )
    os.system ( gtw1 )
    time.sleep(0.2)

    print("Some times in Canada they use strings...")  ,
    time.sleep(0.3)
    print ("\n")

    print ("exploiting Comming soon....baby....")
spinning_cursor()
if os.name == "posix":
    print ("------------> YOU ARE USING  MAC OSX<---------")
    time.sleep(7)
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line
    print ("...OK geting environment... GET ready")
    time.sleep(7)
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line
    mac()
elif os.name == "nt":
    print ("lol not yet")



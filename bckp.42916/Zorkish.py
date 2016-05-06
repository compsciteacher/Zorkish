import sys,os,time,textwrap

## Zorkish v .20
##
##MIT License
##
##Copyright (c) [2016] [Howard C Davis]
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.

##
##This will be a simple text based game like the old Zork games. It is an interactive fiction game
##using text based commands. Due to the large amount of storytelling that will be added
##v .10 through .50 will be purely command based with skeleton story.




def main():
    class User(object):
        def __init__(self, hp, inventory,loc):
            self.hp = hp
            self.inv = inventory
            self.loc=loc

        def __str__(self):
            return '%s %r' % (self.hp, self.inv)

        def hpcheck(self, hp):
            if hp < 1:
                print('Your character has died!')
                pause(3)
                sys.exit(0)
            else:
                return hp


    def save(u):#save current state to sv.txt file
        sv=open("sv.txt","w")
        sv.write(str(u.hp)+'\n')
        sv.write(u.loc+'\n')
        for x in u.inv:
            sv.write(x+"\n")
        sv.close()
        choice(u)
    def load():
        sv=open("sv.txt","r")
        full=sv.read().split('\n')
        ni=[]
        for x in full[2:]:
            ni.append(x)
        del ni[-1]
        user=User(full[0],ni,full[1])
        choice(user)



    class Room(object):
        def __init__(self, num):
            self.layout = ''
            self.npc = ''
            self.items = []
            self.desc = ''
            num += '.txt'
            room = open(num, 'r')

            l = int(room.readline().rstrip())
            for x in range(l):
                self.layout += room.readline()
            self.npc += room.readline().rstrip()
            l = int(room.readline().rstrip())
            for x in range(l):
                self.items.append(room.readline().rstrip())
            for line in room.readlines():
                self.desc += line
            room.close()

                #         if num==1:
                #             items=['sword','shield','book']
                #             layout='''
                # xxxxxxxx
                # x      x
                # x      x
                # x      x
                # xx[]xxxx
                #
                # '''
                #             npc='No one else'
                #         self.items=items
                #         self.layout=layout
                #         self.npc=npc
                #         self.desc="""You wake up in a room with random items scattered around.
                # You can't even remember how you got here, but you know you must get out.
                # It is unbelievably dark in the room as well. The faster you get out this room,
                # the faster you can get out of this terrible place."""

        def __str__(self):
            return '%s\n%s is here \n\n%s' % (self.layout, self.npc, self.desc)

    def choice(u,r): ##user makes choice of what to do, sends to compare if not stop
        c=input("What do you do? ")
        if c=='stop':
            sys.exit(0)
        compare(c,u,r)

    def compare(c,u,r):##compare user entry to given functions based on analysis, which is checking for words and stripping whitespace

        if "pickup" in c or "get" in c:
            i=c.replace("pickup",'').replace("get",'').strip()
            pickup(i,u)
        elif "go" in c or "walk" in c:
            i = c.replace("go", '').replace("walk", '').strip()
            go(i,u,r)
        elif c=="inventory":#prints inventory
            print(u.inv)
        elif c=="diagnostic":
            print(u.hpcheck(u.hp))
        elif c=="save":
            save(u)
        elif c=="restore":
            load()
        elif "look" in c:
            i=c.replace("look",'').strip()
            look(u,r)
        else:
            print('huh?')
            choice(u,r)

    def pickup(ask,u):#check to see if ask is in the rm item list, if it is add to inv, or tell not there
        room=Room(u.loc)
        if ask=="":
            print("What do you want??")
            choice(u,room)
        if ask in room.items:
            u.inv.append(ask)
            removei(ask,u)
            choice(u,room)
        else:
            print('%s is not here!' %ask)

            choice(u,room)
    def removei(i,u):
        r=open(u.loc+".txt","r")
        f=r.read()
        r.close()
        n=open(u.loc+".txt","w")
        n.write(f.replace(i,""))
        n.close()

    def go(dir,u,r):#get direction user wants to move, check map to see if that is possible

        map=open('map.txt','r')
        for line in map:

            l=line.rstrip().split(' ')
            if u.loc==l[0]:
                if dir in l:
                    try:
                        way=l.index(dir)+1
                        u.loc = l[way+1]
                        print('You have gone %s through the %s' % (dir, l[way]))
                        print(u.loc)
                        r=Room(u.loc)
                        print(r)
                        break


                    except:
                        print("hmm... that's weird, can't do that")
                        break
            else:
                print("You can't go that way")


        map.close()
        choice(u,r)
    def look(u,r):
        options=open("interactions.txt","r")
        for line in options:
            l=line.rstrip().split("/")
            if u.loc==l[0]:
                if "look" in l:
                    print(l[(l.index("look")+1)])
                    choice(u,r)
        choice(u,r)
    def clearit():
        os.system('cls' if os.name == 'nt' else 'clear')

    def teststart():
        
        starter=User(100,[],'rm1')
        print(starter)
        rm=Room(starter.loc)
        while(True):
            pause(4)
            clearit()
            print(rm)
            choice(starter,rm)





        
    def pause(x):
        time.sleep(x)
    print("THIS IS THE BEGINNING")
    teststart()

main()
            
        


## Zorkish v .10
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

class User(object):
    def __init__(self, hp, inventory):
        self.hp=hp
        self.inventory=inventory
    def __str__(self):
        return '%s %r' %(self.hp,self.inventory)
    def hpcheck(self,hp):
        if hp<1:
            print('Your character has died!')
            pause(3)
            sys.exit(0)
        else:
            return hp
def main():
    def teststart():
        
        starter=User(100,[])
        print(starter)
        print(starter.hp)
        print(starter.hpcheck(starter.hp))
    def pause(x):
        time.sleep(x)
    teststart()
main()
        
            
            
        

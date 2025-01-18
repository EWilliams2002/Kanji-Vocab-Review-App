from graphics import *
import random


class Node:

    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None

class Kanji:

    def __init__(self, char, kun_yomi, on_yomi, kun_sentence, on_sentence):
        # Initialize a kanji object with both readings and their example sentence
        self.char = char
        self.kun_yomi = kun_yomi
        self.on_yomi = on_yomi

        self.kun_sentence = kun_sentence
        self.on_sentence = on_sentence

class Vocab:

    def __init__(self, word, sentence):
        self.word = word
        self.sentence = sentence
        
class Card:

    def __init__(self, subject):
        # Initialize a card object that 
        if type(subject) == Kanji:
            self.char = subject.char
            self.kun_yomi = subject.kun_yomi
            self.on_yomi = subject.on_yomi
            self.kun_sentence = subject.kun_sentence
            self.on_sentence = subject.on_sentence

        elif type(subject) == Vocab:
            self.word = subject




def get_kanji_list(num, kanji_dict):

    ran_index = random.sample(range(0,len(kanji_dict)), len(kanji_dict))

    kanji_list_dlinked = Node(Card(kanji_dict[list(kanji_dict.keys())[ran_index[0]]]))

    curr = kanji_list_dlinked

    for ind in range(1,len(ran_index)):
        
        key = list(kanji_dict.keys())[ran_index[ind]]

        

        curr.next = Node(Card(kanji_dict[key]))

        curr.next.prev = curr

        curr = curr.next
        
    return kanji_list_dlinked




def change_card(curr, direction, extras, win, rect1, rect12):


    # [char, kun, on, kun_sentence, on_sentence]
    char = extras[0]
    kun = extras[1]
    on = extras[2]
    kun_sentence = extras[3]
    on_sentence = extras[4]

    if direction == 'r':
        kanji = curr.next.data

    if direction == 'l':
        kanji = curr.prev.data

    char.undraw()
    kun.undraw()
    on.undraw()
    kun_sentence.undraw()
    on_sentence.undraw()

    # The kanji char
    char = Text(Point(1000, 300), kanji.char)
    char.setSize(36)
    char.draw(win)

    # kun yomi
    kun = Text(Point(725, 530),kanji.kun_yomi)
    kun.setSize(15)
    kun.draw(win)

    # on yomi
    on = Text(Point(1275, 530),kanji.on_yomi)
    on.setSize(15)
    on.draw(win)

    # kun sentence
    kun_sentence = Text(Point(725, 630),kanji.kun_sentence)
    kun_sentence.setSize(15)
    kun_sentence.draw(win)

    # on sentence
    on_sentence = Text(Point(1275, 630),kanji.on_sentence)
    on_sentence.setSize(15)
    on_sentence.draw(win)

    rect1_, rect12_ = draw_blinders(win, rect1, rect12)

    if direction == 'r':
        return curr.next, [char, kun, on, kun_sentence, on_sentence], rect1_, rect12_

    if direction == 'l':
        return curr.prev, [char, kun, on, kun_sentence, on_sentence], rect1_, rect12_
    
def draw_card(win, curr):

    kanji = curr.data

    # The card
    rect = Rectangle(Point(450,100), Point(1550,900))
    rect.setOutline(color_rgb(0, 0, 0))
    rect.setFill(color_rgb(200, 200, 200))
    rect.draw(win)

    # divider line
    divider = Line(Point(1000, 430), Point(1000, 830))
    divider.draw(win)

    # The kanji char
    char = Text(Point(1000, 300), kanji.char)
    char.setSize(36)
    char.draw(win)

    # kun yomi
    kun = Text(Point(725, 530),kanji.kun_yomi)
    kun.setSize(15)
    kun.draw(win)

    # on yomi
    on = Text(Point(1275, 530),kanji.on_yomi)
    on.setSize(15)
    on.draw(win)

    # kun sentence
    kun_sentence = Text(Point(725, 630),kanji.kun_sentence)
    kun_sentence.setSize(15)
    kun_sentence.draw(win)

    # on sentence
    on_sentence = Text(Point(1275, 630),kanji.on_sentence)
    on_sentence.setSize(15)
    on_sentence.draw(win)

    rect1_ = Rectangle(Point(575,410), Point(910,810))
    rect1_.setOutline(color_rgb(0, 0, 0))
    rect1_.setFill(color_rgb(150, 200, 150))
    rect1_.draw(win)

    rect12_ = Rectangle(Point(1075,410), Point(1410,810))
    rect12_.setOutline(color_rgb(0, 0, 0))
    rect12_.setFill(color_rgb(150, 200, 150))
    rect12_.draw(win)

    return [char, kun, on, kun_sentence, on_sentence], rect1_, rect12_




def draw_blinders(win, rect1, rect12):
    
    undraw_blinders('l', rect1, rect12)
    undraw_blinders('r', rect1, rect12)

    rect1_ = Rectangle(Point(575,410), Point(910,810))
    rect1_.setOutline(color_rgb(0, 0, 0))
    rect1_.setFill(color_rgb(150, 200, 150))
    rect1_.draw(win)

    rect12_ = Rectangle(Point(1075,410), Point(1410,810))
    rect12_.setOutline(color_rgb(0, 0, 0))
    rect12_.setFill(color_rgb(150, 200, 150))
    rect12_.draw(win)

    return rect1_, rect12_

def undraw_blinders(direction, rect1, rect12):
    if direction == 'l':
        rect1.undraw()
    if direction == 'r':
        rect12.undraw()




def add_kanji(kanji_dict):
    pass




def traverse(head):
    # Traverse the doubly linked list and print its elements
    current = head
    while current:
      # Print current node's data
        print(current.data.char, end=" <-> ")
        # Move to the next node
        current = current.next
    print("None")




def program_loop(kanji_dict):

    # draws window
    win = GraphWin("yerr", 2000, 1000)

    # arrows
    arrow_left = Image(Point(300, 500), 'images\\arrow.png')
    arrow_right = Image(Point(1700, 500), 'images\\arrowright.png')
    arrow_left.draw(win)
    arrow_right.draw(win)

    # exit Button
    exit_b = Rectangle(Point(1900,950), Point(2000,1000))
    exit_b.setOutline(color_rgb(0, 0, 0))
    exit_b.setFill(color_rgb(200, 255, 200))
    exit_b.draw(win)

    exit_t = Text(exit_b.getCenter(), 'E X I T')
    exit_t.setSize(10)
    exit_t.draw(win)

    kanji_list = get_kanji_list(len(kanji_dict), kanji_dict)
    curr = kanji_list
    closed = False
    extras, rect1, rect12 = draw_card(win, curr)

    # program loop
    while not closed:
    
        mouse = win.getMouse()  

        # Pressed left
        if (mouse.getX() >= 0 and mouse.getX() <= 449) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.prev is not None:

            curr, extras, rect1, rect12 = change_card(curr, 'l', extras, win, rect1, rect12)

            print('clicked left', mouse.getX(), mouse.getY())
                
        # Pressed right
        if (mouse.getX() >= 1551 and mouse.getX() <= 2000) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.next is not None:

            curr, extras, rect1, rect12 = change_card(curr, 'r', extras, win, rect1, rect12)

            print('clicked right', mouse.getX(), mouse.getY())

        # Pressed exit
        if (mouse.getX() >= 1900 and mouse.getX() <= 2000) and (mouse.getY() >= 950 and mouse.getY() <= 1000):

            print('clicked exit', mouse.getX(), mouse.getY())
            win.close()
            closed = True
                
        # Pressed card left
        if (mouse.getX() >= 450 and mouse.getX() <= 1000) and (mouse.getY() >= 100 and mouse.getY() <= 900):

            undraw_blinders('l', rect1, rect12)
            print('clicked card left', mouse.getX(), mouse.getY())

        # Pressed card right
        if (mouse.getX() >= 1001 and mouse.getX() <= 1550) and (mouse.getY() >= 100 and mouse.getY() <= 900):

            undraw_blinders('r', rect1, rect12)
            print('clicked card right', mouse.getX(), mouse.getY())
        

def main():

    kanji_dict = {} # key - char/symbol     val - kanji_object
    kanji_dict['中'] = Kanji('中', 'naka', 'chu', 'fefef', 'klkl')
    kanji_dict['G'] = Kanji('G', 'tanpa', 'olo', 'trtr', 'asas')
    kanji_dict['f'] = Kanji('f', 'fff', 'ttwt', 'uuu', 'hgh')
    kanji_dict['h'] = Kanji('h', 'vvv', 'iii', 'ooo', 'bbb')
    kanji_dict['j'] = Kanji('j', 'xxxxx', 'zzz', 'lll', 'mmm')
    
    print(' __  _   ____  ____   ____  ____      ____     ___ __ __  ____    ___ __    __       ____  ____  ____  ')
    print('|  |/ ] /    ||    \ |    ||    |    |    \   /  _]  |  ||    |  /  _]  |__|  |     /    ||    \|    \ ')
    print("|  ' / |  o  ||  _  ||__  | |  |     |  D  ) /  [_|  |  | |  |  /  [_|  |  |  |    |  o  ||  o  )  o  )")
    print('|    \ |     ||  |  |__|  | |  |     |    / |    _]  |  | |  | |    _]  |  |  |    |     ||   _/|   _/ ')
    print("|     ||  _  ||  |  /  |  | |  |     |    \ |   [_|  :  | |  | |   [_|  `  '  |    |  _  ||  |  |  |   ")
    print('|  .  ||  |  ||  |  \  `  | |  |     |  .  \|     |\   /  |  | |     |\      /     |  |  ||  |  |  |   ')
    print('|__|\_||__|__||__|__|\____||____|    |__|\_||_____| \_/  |____||_____| \_/\_/      |__|__||__|  |__|   ')
    print('                                                                                                       ')
    print()
    




    print("Hello Welcome to Kanji Review App !! \n\n\n\n\n" + "Would you like to add new Kanji? [Y/N]")
    res = input()
    print('\n\n')
    
    if res.lower() in ['y','yes']:

        # Starts adding kanji sequence then after it is done, it returns to asking if you want to play
        add_kanji(kanji_dict)

    
    print("Would you like to play? [Y/N]")
    res = input()
    print('\n\n')


    if res.lower() in ['y','yes']:

        # Add code here to add check whether or not you want to go kanji or vocab

        # Starts the program loop and the window. Upon exit, the window closes and you are brought
        # back to the goodbye prompt below
        program_loop(kanji_dict)

    input("Goodbye !!\n\nPress enter to exit . . .")


if __name__ == "__main__":
    main()
from graphics import *
import random
# import keyboard

class Node:
    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None

class Kanji:

    def __init__(self, char, kun_yomi, on_yomi, kun_sentence, on_sentence):
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


def change_card(curr, direction, extras, win):
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

    if direction == 'r':
        return curr.next, [char, kun, on, kun_sentence, on_sentence]

    if direction == 'l':
        return curr.prev, [char, kun, on, kun_sentence, on_sentence]

    

    

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

    return [char, kun, on, kun_sentence, on_sentence]




def draw_blinders(win):
    pass




def add_kanji(kanji_dict):
    pass






# def traverse(head):
#     # Traverse the doubly linked list and print its elements
#     current = head
#     while current:
#       # Print current node's data
#         print(current.data.char, end=" <-> ")
#         # Move to the next node
#         current = current.next
#     print("None")


def program_loop(kanji_dict):

    # draws window
    win = GraphWin("yerr", 2000, 1000)

    # arrows
    arrow_left = Image(Point(300, 500), 'images\\arrow.png')
    arrow_right = Image(Point(1700, 500), 'images\\arrowright.png')
    arrow_left.draw(win)
    arrow_right.draw(win)


    # num is the amount of kanji in kanji_dict and will keep track of how many kanji left
    # in shuffle. This num will decrease until it loops the number of times of kanji in
    # the dict
    kanji_length = len(kanji_dict)
    num = kanji_length

    kanji_list = get_kanji_list(num, kanji_dict)
        

    curr = kanji_list

    # program loop
    while num >= 1:
        print(num)
        draw_blinders(win)

        extras = draw_card(win, curr)
        

        action = False

        while not action:
            mouse = win.getMouse()

            # Pressed left
            if (mouse.getX() >= 0 and mouse.getX() <= 449) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.prev is not None:

                curr, extras = change_card(curr, 'l', extras, win)

                print('clicked left', mouse.getX(), mouse.getY())

                # instead of action = true use num += 1 so that it negates progress towards outer loop
                num += 1
                

            # Pressed right
            if (mouse.getX() >= 1551 and mouse.getX() <= 2000) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.next is not None:

                curr, extras = change_card(curr, 'r', extras, win)

                print('clicked right', mouse.getX(), mouse.getY())
                action = True

            # Pressed exit
            if (mouse.getX() >= 1900 and mouse.getX() <= 2000) and (mouse.getY() >= 950 and mouse.getY() <= 1000):
                print('clicked exit', mouse.getX(), mouse.getY())
                action = True
        
        num -= 1
    
    win.close()

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

    else:
        print("Would you like to play? [Y/N]")
        res = input()
        print('\n\n')


        if res.lower() in ['y','yes']:

            # Add code here to add check whether or not yuo want to go visual or not

            # Starts the program loop and the window, upon completion the window closes and you are brought
            # back to the goodbye prompt below
            program_loop(kanji_dict)

        input("Goodbye !!\n\nPress enter to exit . . .")


    

    



if __name__ == "__main__":
    main()



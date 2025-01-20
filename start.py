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

    def __init__(self, word, translation, sentence_jpn, sentence_eng, verb=False):
        self.word = word
        self.translation = translation
        self.sentence_jpn = sentence_jpn
        self.sentence_eng = sentence_eng

        if verb:
            self.present_aff = verb[0]
            self.present_neg = verb[1]
        else:
            self.present_aff = None
            self.present_neg = None




def get_dlinked_list(choice_dict):
    """
    Converts the given card dictionary to 
    a doubly linked list

    :param choice_dict: Dictionary of cards
    :return: A doubly linked list with card objects as the values
            each node has a next and prev and the ends are approiatley
            missing either prev or next
    """

    # Gets a list of shuffled indexes to match the card list
    ran_index = random.sample(range(0,len(choice_dict)), len(choice_dict))

    # Uses the first card to create the head of the doubly linked list
    dlinked_list = Node(choice_dict[list(choice_dict.keys())[ran_index[0]]])

    # Sets the current node to the head of the list
    curr = dlinked_list

    # Iterates through the shuffled indexes
    for ind in range(1,len(ran_index)):
        
        key = list(choice_dict.keys())[ran_index[ind]]
        
        # Sets the next node from the node set to curr then replace curr with the next node
        # Also sets the node set to curr as prev to the next node
        curr.next = Node(choice_dict[key])
        curr.next.prev = curr
        curr = curr.next
        
    return dlinked_list




def change_card(curr, direction, extras, win, rect1, rect12, choice):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    if choice == 'kanji':

        # kanji - extras = [char, kun, on, kun_sentence, on_sentence]
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

        rect1_, rect12_ = draw_blinders(win, rect1, rect12, choice)

        if direction == 'r':
            return curr.next, [char, kun, on, kun_sentence, on_sentence], rect1_, rect12_

        if direction == 'l':
            return curr.prev, [char, kun, on, kun_sentence, on_sentence], rect1_, rect12_
        
    if choice == 'vocab':

        word = extras[0]
        translation = extras[1]
        sentence_jpn = extras[2]
        sentence_eng = extras[3]

        if direction == 'r':
            card = curr.next.data

        if direction == 'l':
            card = curr.prev.data

        word.undraw()
        translation.undraw()
        sentence_jpn.undraw()
        sentence_eng.undraw()
        

        # The kanji char
        word = Text(Point(1000, 250), card.word)
        word.setSize(36)
        word.draw(win)

        # translation
        translation = Text(Point(1000, 365),card.translation)
        translation.setSize(20)
        translation.draw(win)

        # divider line
        divider = Line(Point(1000, 450), Point(1000, 650))
        divider.draw(win)

        # sentence_jpn
        sentence_jpn = Text(Point(800, 475),card.sentence_jpn)
        sentence_jpn.setSize(20)
        sentence_jpn.draw(win)

        # sentence_eng
        sentence_eng = Text(Point(1200, 475),card.sentence_eng)
        sentence_eng.setSize(20)
        sentence_eng.draw(win)
        
        try:
            present_aff = extras[4]
            present_neg = extras[5]

            present_aff.undraw()
            present_neg.undraw()

            # verb label
            verb_label = Text(Point(800, 575),'Verb Tenses')
            verb_label.setSize(20)
            verb_label.draw(win)

            # present_aff
            present_aff = Text(Point(1200, 575),card.present_aff)
            present_aff.setSize(20)
            present_aff.draw(win)

            # present_neg
            present_neg = Text(Point(1200, 625),card.present_neg)
            present_neg.setSize(20)
            present_neg.draw(win)
            
            rect1_, rect12_ = draw_blinders(win, rect1, rect12, choice)
            
            if direction == 'r':
                return curr.next, [word, translation, sentence_jpn, sentence_eng, present_aff, present_neg], rect1_, rect12_

            if direction == 'l':
                return curr.prev, [word, translation, sentence_jpn, sentence_eng, present_aff, present_neg], rect1_, rect12_
            
        except IndexError:

            rect1_, rect12_ = draw_blinders(win, rect1, rect12, choice)

            if direction == 'r':
                return curr.next, [word, translation, sentence_jpn, sentence_eng], rect1_, rect12_

            if direction == 'l':
                return curr.prev, [word, translation, sentence_jpn, sentence_eng], rect1_, rect12_

    
    
def draw_card(win, curr, choice):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    
    card = curr.data

    # The card
    rect = Rectangle(Point(450,100), Point(1550,900))
    rect.setOutline(color_rgb(0, 0, 0))
    rect.setFill(color_rgb(200, 200, 200))
    rect.draw(win)

    if choice == 'kanji':
        # divider line
        divider = Line(Point(1000, 430), Point(1000, 830))
        divider.draw(win)

        # The kanji char
        char = Text(Point(1000, 300), card.char)
        char.setSize(36)
        char.draw(win)

        # kun yomi
        kun = Text(Point(725, 530),card.kun_yomi)
        kun.setSize(15)
        kun.draw(win)

        # on yomi
        on = Text(Point(1275, 530),card.on_yomi)
        on.setSize(15)
        on.draw(win)

        # kun sentence
        kun_sentence = Text(Point(725, 630),card.kun_sentence)
        kun_sentence.setSize(15)
        kun_sentence.draw(win)

        # on sentence
        on_sentence = Text(Point(1275, 630),card.on_sentence)
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
    
    if choice == 'vocab':

        # The kanji char
        word = Text(Point(1000, 250), card.word)
        word.setSize(36)
        word.draw(win)

        # translation
        translation = Text(Point(1000, 365),card.translation)
        translation.setSize(20)
        translation.draw(win)

        # divider line
        divider = Line(Point(1000, 450), Point(1000, 650))
        divider.draw(win)

        # sentence_jpn
        sentence_jpn = Text(Point(800, 475),card.sentence_jpn)
        sentence_jpn.setSize(20)
        sentence_jpn.draw(win)

        # sentence_eng
        sentence_eng = Text(Point(1200, 475),card.sentence_eng)
        sentence_eng.setSize(20)
        sentence_eng.draw(win)

        if card.present_aff is not None:

            # verb label
            verb_label = Text(Point(800, 575), 'Verb Tenses')
            verb_label.setSize(20)
            verb_label.draw(win)

            # present_aff
            present_aff = Text(Point(1200, 575),card.present_aff)
            present_aff.setSize(20)
            present_aff.draw(win)

            # present_neg
            present_neg = Text(Point(1200, 625),card.present_neg)
            present_neg.setSize(20)
            present_neg.draw(win)

            rect1_ = Rectangle(Point(600,340), Point(1400,380))
            rect1_.setOutline(color_rgb(0, 0, 0))
            rect1_.setFill(color_rgb(150, 200, 150))
            rect1_.draw(win)

            rect12_ = Rectangle(Point(600,440), Point(1400,670))
            rect12_.setOutline(color_rgb(0, 0, 0))
            rect12_.setFill(color_rgb(150, 200, 150))
            rect12_.draw(win)

            return [word, translation, sentence_jpn, sentence_eng, present_aff, present_neg], rect1_, rect12_
    
        rect1_ = Rectangle(Point(600,340), Point(1400,380))
        rect1_.setOutline(color_rgb(0, 0, 0))
        rect1_.setFill(color_rgb(150, 200, 150))
        rect1_.draw(win)

        rect12_ = Rectangle(Point(600,440), Point(1400,670))
        rect12_.setOutline(color_rgb(0, 0, 0))
        rect12_.setFill(color_rgb(150, 200, 150))
        rect12_.draw(win)

        return [word, translation, sentence_jpn, sentence_eng], rect1_, rect12_


def draw_blinders(win, rect1, rect12, choice):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    
    undraw_blinders('l', rect1, rect12)
    undraw_blinders('r', rect1, rect12)
    
    if choice == 'kanji':
        rect1_ = Rectangle(Point(575,410), Point(910,810))
        rect1_.setOutline(color_rgb(0, 0, 0))
        rect1_.setFill(color_rgb(150, 200, 150))
        rect1_.draw(win)

        rect12_ = Rectangle(Point(1075,410), Point(1410,810))
        rect12_.setOutline(color_rgb(0, 0, 0))
        rect12_.setFill(color_rgb(150, 200, 150))
        rect12_.draw(win)

        return rect1_, rect12_
    
    if choice == 'vocab':
        rect1_ = Rectangle(Point(600,340), Point(1400,380))
        rect1_.setOutline(color_rgb(0, 0, 0))
        rect1_.setFill(color_rgb(150, 200, 150))
        rect1_.draw(win)

        rect12_ = Rectangle(Point(600,440), Point(1400,670))
        rect12_.setOutline(color_rgb(0, 0, 0))
        rect12_.setFill(color_rgb(150, 200, 150))
        rect12_.draw(win)

        return rect1_, rect12_

def undraw_blinders(direction, rect1, rect12):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    if direction == 'l':
        rect1.undraw()
    if direction == 'r':
        rect12.undraw()




def add_kanji(kanji_dict):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """

    # This is what you would use to make sure the kanji is readable

    # new_kanji = 'h,vvv,iii,ooo,bbb'
    # with open(filename,'a',encoding='utf8') as f:
    #     f.write(new_kanji)

    pass




def traverse(head):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    # Traverse the doubly linked list and print its elements
    current = head
    while current:
      # Print current node's data
        print(current.data.word, end=" <-> ")
        # Move to the next node
        current = current.next
    print("None")




def program_loop(choice):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """

    if choice == 'kanji':
        choice_dict = read_to_dictionary('Dictionaries\kanji.txt', 'kanji')
        
    if choice == 'vocab':
        choice_dict = read_to_dictionary('Dictionaries\\vocab.txt', 'vocab')

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

    curr = get_dlinked_list(choice_dict)
    closed = False

    if choice == 'kanji':
        extras, rect1, rect12 = draw_card(win, curr, 'kanji')
        
    if choice == 'vocab':
        extras, rect1, rect12 = draw_card(win, curr, 'vocab')
    

    # program loop
    while not closed:
    
        mouse = win.getMouse()  

        # Pressed left
        if (mouse.getX() >= 0 and mouse.getX() <= 449) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.prev is not None:

            curr, extras, rect1, rect12 = change_card(curr, 'l', extras, win, rect1, rect12, choice)

            # print('clicked left', mouse.getX(), mouse.getY())
                
        # Pressed right
        if (mouse.getX() >= 1551 and mouse.getX() <= 2000) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.next is not None:

            curr, extras, rect1, rect12 = change_card(curr, 'r', extras, win, rect1, rect12, choice)

            # print('clicked right', mouse.getX(), mouse.getY())

        # Pressed exit
        if (mouse.getX() >= 1900 and mouse.getX() <= 2000) and (mouse.getY() >= 950 and mouse.getY() <= 1000):

            win.close()
            closed = True

            # print('clicked exit', mouse.getX(), mouse.getY())
                


        # Pressed card left (kanji)
        if (mouse.getX() >= 450 and mouse.getX() <= 1000) and (mouse.getY() >= 100 and mouse.getY() <= 900) and choice == 'kanji':

            undraw_blinders('l', rect1, rect12)

            # print('clicked card left', mouse.getX(), mouse.getY())

        # Pressed card right (kanji)
        if (mouse.getX() >= 1001 and mouse.getX() <= 1550) and (mouse.getY() >= 100 and mouse.getY() <= 900) and choice == 'kanji':

            undraw_blinders('r', rect1, rect12)

            # print('clicked card right', mouse.getX(), mouse.getY())
        


        # Pressed card upper (vocab)
        if (mouse.getX() >= 450 and mouse.getX() <= 1550) and (mouse.getY() >= 100 and mouse.getY() <= 400) and choice == 'vocab':

            undraw_blinders('l', rect1, rect12)

            # print('clicked card left', mouse.getX(), mouse.getY())

        # Pressed card lower (vocab)
        if (mouse.getX() >= 450 and mouse.getX() <= 1550) and (mouse.getY() >= 401 and mouse.getY() <= 900) and choice == 'vocab':

            undraw_blinders('r', rect1, rect12)

            # print('clicked card right', mouse.getX(), mouse.getY())

def read_to_dictionary(filename, choice):
    
    ret_dict = {}

    byte_string = open(filename, 'r', encoding='utf8').read()
    unicode_text = byte_string.encode('UTF-8')
    file = unicode_text.decode('UTF-8').splitlines()

    for line in file:
        temp = line.split(',')

        if choice == 'kanji':
            char = temp[0]
            kun_yomi = temp[1]
            on_yomi = temp[2]
            kun_sent = temp[3]
            on_sent = temp[4]
            
            ret_dict[char] = Kanji(char, kun_yomi, on_yomi, kun_sent, on_sent)
        
        if choice == 'vocab':
            
            word = temp[0]
            translation = temp[1]
            sentence_jpn = temp[2]
            sentence_eng = temp[3]

            try:
                verb = temp[4].split(';')
                ret_dict[word] = Vocab(word, translation, sentence_jpn, sentence_eng, verb)

            except IndexError:
                ret_dict[word] = Vocab(word, translation, sentence_jpn, sentence_eng)
    
    return ret_dict


def main():

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
        add_kanji()

    print("Would you like to play? [Y/N]")
    loop_res = input()

    if loop_res.lower() in ['y','yes']:

        while loop_res.lower() not in ['e','exit']:

            if loop_res.lower() in ['y','yes']:
                print('\n\n')
                
            print("Kanji review, Vocab review, or exit? [K/V/E]")
            loop_res = input()
            print('\n\n')

            if loop_res.lower() in ['k','kanji']:

                # Starts the program loop and the window. Upon exit, the window closes and you are brought
                # back to the goodbye prompt below
                program_loop('kanji')

            if loop_res.lower() in ['v','vocab']:
                program_loop('vocab')
            
            if loop_res.lower() in ['e','exit']:
                break
    else:
        print('\n\n')

    input("Goodbye !!\n\nPress enter to exit . . .")

if __name__ == "__main__":
    main()
from graphics import *
import random

class Node:

    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None

class Kanji:

    def __init__(self, char, translation, kun_yomi, on_yomi, kun_sentence, on_sentence):
        # Initialize a kanji object with both readings and their example sentence
        self.char = char
        self.translation = translation
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




def change_card(curr, direction, extras, win, rect1, rect12, choice, rect3=False):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    if choice == 'kanji':

        # kanji - extras = [char, kun, on, kun_sentence, on_sentence]
        char = extras[0]
        translation = extras[1]
        kun = extras[2]
        on = extras[3]
        kun_sentence = extras[4]
        on_sentence = extras[5]

        if direction == 'r':
            card = curr.next.data

        if direction == 'l':
            card = curr.prev.data

        char.undraw()
        translation.undraw()
        kun.undraw()
        on.undraw()
        kun_sentence.undraw()
        on_sentence.undraw()

        # The kanji char
        char = Text(Point(1000, 250), card.char)
        char.setSize(36)
        char.draw(win)

        # translation
        translation = Text(Point(1000, 355),card.translation.replace(';', ', '))
        translation.setSize(20)
        translation.draw(win)

        # kun yomi
        kun = Text(Point(725, 550),card.kun_yomi.replace(';', '  -  '))
        kun.setSize(15)
        kun.setStyle('bold')
        kun.draw(win)

        # on yomi
        on = Text(Point(1275, 550),card.on_yomi.replace(';', '  -  '))
        on.setSize(15)
        on.setStyle('bold')
        on.draw(win)

        # kun sentence
        kun_sentence = Text(Point(725, 650),card.kun_sentence.replace(';', ' -> '))
        kun_sentence.setSize(15)
        kun_sentence.setStyle('bold')
        kun_sentence.draw(win)

        # on sentence
        on_sentence = Text(Point(1275, 650),card.on_sentence.replace(';', ' -> '))
        on_sentence.setSize(15)
        on_sentence.setStyle('bold')
        on_sentence.draw(win)

        rect1_, rect12_, rect3_ = draw_blinders(win, rect1, rect12, choice, rect3)

        if direction == 'r':
            return curr.next, [char, translation, kun, on, kun_sentence, on_sentence], rect1_, rect12_, rect3_

        if direction == 'l':
            return curr.prev, [char, translation, kun, on, kun_sentence, on_sentence], rect1_, rect12_, rect3_
        
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
        

        # The kanji char
        char = Text(Point(1000, 250), card.char)
        char.setSize(36)
        char.draw(win)  

        # translation
        translation = Text(Point(1000, 355),card.translation.replace(';', ', '))
        translation.setSize(20)
        translation.draw(win)

        # divider line
        divider = Line(Point(1000, 450), Point(1000, 850))
        divider.draw(win)
        
        # kun yomi
        kun = Text(Point(725, 550),card.kun_yomi.replace(';', '  -  '))
        kun.setSize(15)
        kun.setStyle('bold')
        kun.draw(win)

        # on yomi
        on = Text(Point(1275, 550),card.on_yomi.replace(';', '  -  '))
        on.setSize(15)
        on.setStyle('bold')
        on.draw(win)

        # kun sentence
        kun_sentence = Text(Point(725, 650),card.kun_sentence.replace(';', ' -> '))
        kun_sentence.setSize(15)
        kun_sentence.setStyle('bold')
        kun_sentence.draw(win)

        # on sentence
        on_sentence = Text(Point(1275, 650),card.on_sentence.replace(';', ' -> '))
        on_sentence.setSize(15)
        on_sentence.setStyle('bold')
        on_sentence.draw(win)

        rect1_ = Rectangle(Point(450,450), Point(1000,850))
        rect1_.setOutline(color_rgb(0, 0, 0))
        rect1_.setFill(color_rgb(150, 200, 150))
        rect1_.draw(win)

        rect12_ = Rectangle(Point(1000,450), Point(1550,850))
        rect12_.setOutline(color_rgb(0, 0, 0))
        rect12_.setFill(color_rgb(150, 200, 150))
        rect12_.draw(win)

        rect3_ = Rectangle(Point(600,340), Point(1400,380))
        rect3_.setOutline(color_rgb(0, 0, 0))
        rect3_.setFill(color_rgb(150, 200, 150))
        rect3_.draw(win)

        return [char, translation, kun, on, kun_sentence, on_sentence], rect1_, rect12_, rect3_
    
    if choice == 'vocab':

        # The kanji char
        word = Text(Point(1000, 250), card.word)
        word.setSize(36)
        word.draw(win)

        # translation
        translation = Text(Point(1000, 365),card.translation)
        translation.setSize(20)
        translation.draw(win)

        #arrow one
        arrow_one = Line(Point(980, 475), Point(1020, 475))
        arrow_one.setArrow('last')
        arrow_one.draw(win)

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

            #arrow two
            arrow_one = Line(Point(980, 575), Point(1020, 575))
            arrow_one.setArrow('last')
            arrow_one.draw(win)

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


def draw_blinders(win, rect1, rect12, choice, rect3=False):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    
    undraw_blinders('l', rect1, rect12)
    undraw_blinders('r', rect1, rect12)
    
    if choice == 'kanji':

        undraw_blinders('m', rect1, rect12, rect3)

        rect1_ = Rectangle(Point(450,450), Point(1000,850))
        rect1_.setOutline(color_rgb(0, 0, 0))
        rect1_.setFill(color_rgb(150, 200, 150))
        rect1_.draw(win)

        rect12_ = Rectangle(Point(1000,450), Point(1550,850))
        rect12_.setOutline(color_rgb(0, 0, 0))
        rect12_.setFill(color_rgb(150, 200, 150))
        rect12_.draw(win)

        rect3_ = Rectangle(Point(600,340), Point(1400,380))
        rect3_.setOutline(color_rgb(0, 0, 0))
        rect3_.setFill(color_rgb(150, 200, 150))
        rect3_.draw(win)

        return rect1_, rect12_, rect3_
    
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

def undraw_blinders(direction, rect1, rect12, rect3=False):
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
    if direction == 'm':
        rect3.undraw()


def comma_check(res):

    if ',' in res:
        return False
    
    return True


def repeat_check(new_ent, res, end=False):

    if res in ['', None, 'None']:
        print('\n\n')
        
        if end:
            return new_ent + '-'
        else:
            return new_ent + '-' + ','
        

    cond_met = False

    if comma_check(res):
        cond_met = True
        print('\n\n')

        if end:
            return new_ent + res
        else:
            return new_ent + res + ','
    
    while not cond_met:
        print('ERROR: Please check your entry')

        res = input()

        cond_met = False

        if comma_check(res):
            cond_met = True
            print('\n\n')

            if end:
                return new_ent + res
            else:
                return new_ent + res + ','

    
def check_exists(res, choice):
    
    if choice == 'kanji':
        choice_dict = read_to_dictionary('Dictionaries\\kanji.txt', 'kanji')

        if res in choice_dict:
            return False
        
    if choice == 'vocab':
        choice_dict = read_to_dictionary('Dictionaries\\vocab.txt', 'vocab')

        if res in choice_dict:
            return False
        
    return True



def add_kanji(filename, choice):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """

    # print("New Kanji, New Vocab, or exit? [K/V/E]")
    # loop_res = input()
    # print('\n\n')

    if choice == 'kanji':

        new_kanji = ''

        # Character
        print("What is the character?")
        res = input()

        ret = check_exists(res, choice)

        cond_met = False

        if comma_check(res) and len(res) == 1 and ret:
            cond_met = True
            new_kanji += res + ','
     
        while not cond_met:

            if not ret:
                print('ERROR: Character already exists')
            else:
                print('ERROR: Please check your entry')

            res = input()

            ret = check_exists(res, choice)
            cond_met = False

            if comma_check(res) and len(res) == 1 and ret:
                cond_met = True
                new_kanji += res + ','

        print('\n\n')

        # translation
        print("What is the translation?  * seperate multiple by semicolons * ")
        res = input()
        new_kanji = repeat_check(new_kanji, res)
        
        # kun yomi
        print("What is the kun yomi reading?  * seperate multiple by semicolons * ")
        res = input()
        new_kanji = repeat_check(new_kanji, res)

        # on yomi
        print("What is the on yomi reading?  * seperate multiple by semicolons * ")
        res = input()
        new_kanji = repeat_check(new_kanji, res)

        # kun yomi sentence
        print("What is the kun yomi sentence?  * seperate multiple by semicolons * ")
        res = input()
        new_kanji = repeat_check(new_kanji, res)

        # on yomi sentence
        print("What is the on yomi sentence?  * seperate multiple by semicolons * ")
        res = input()
        new_kanji = repeat_check(new_kanji, res, True)
        print('\n\n')


        with open(filename,'a',encoding='utf8') as f:
            f.write('\n' + new_kanji)
        
        f.close()

    if choice == 'vocab':

        new_vocab = ''

        # Character
        print("What is the Word?")
        res = input()

        ret = check_exists(res, choice)

        cond_met = False

        if comma_check(res) and ret:
            cond_met = True
            new_vocab += res + ','
     
        while not cond_met:

            if not ret:
                print('ERROR: Word already exists')
            else:
                print('ERROR: Please check your entry')

            res = input()

            ret = check_exists(res, choice)
            cond_met = False

            if comma_check(res) and ret:
                cond_met = True
                new_vocab += res + ','

        print('\n\n')

        
        # translation
        print("What is the translation?")
        res = input()
        new_vocab = repeat_check(new_vocab, res)

        # sentence_jpn
        print("What is the example japanese sentence?")
        res = input()
        new_vocab = repeat_check(new_vocab, res)

        # sentence_eng
        print("What is that sentence's translation?")
        res = input()
        new_vocab = repeat_check(new_vocab, res, True)

        # verb_check
        print("Is your word a verb?")
        res = input()
        print('\n\n')

        if res.lower() in ['y','yes']:

            new_vocab += ','

            # present_aff
            print("What is the present affirmative tense?")
            res = input()
            new_vocab = repeat_check(new_vocab, res, True)
            new_vocab += ';'

            # present_neg
            print("What is the present negative tense?")
            res = input()
            new_vocab = repeat_check(new_vocab, res, True)

        with open(filename,'a',encoding='utf8') as f:
            f.write('\n' + new_vocab)
        
        f.close()



def program_loop(choice):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """

    if choice == 'kanji':
        choice_dict = read_to_dictionary('Dictionaries\\kanji.txt', 'kanji')
        
    if choice == 'vocab':
        choice_dict = read_to_dictionary('Dictionaries\\vocab.txt', 'vocab')

    # draws window
    win = GraphWin("Kanji 'N' Vocab Review App", 2000, 1000)

    bg = Image(Point(1000, 500), 'images\\bg.png')
    
    bg.draw(win)

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
        extras, rect1, rect12, rect3 = draw_card(win, curr, 'kanji')
        
    if choice == 'vocab':
        extras, rect1, rect12 = draw_card(win, curr, 'vocab')
    

    # program loop
    while not closed:
    
        mouse = win.getMouse()  

        # Pressed left
        if (mouse.getX() >= 0 and mouse.getX() <= 449) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.prev is not None:

            if choice == 'kanji':
                curr, extras, rect1, rect12, rect3 = change_card(curr, 'l', extras, win, rect1, rect12, choice, rect3)
            else:

                curr, extras, rect1, rect12 = change_card(curr, 'l', extras, win, rect1, rect12, choice)

            # print('clicked left', mouse.getX(), mouse.getY())
                
        # Pressed right
        if (mouse.getX() >= 1551 and mouse.getX() <= 2000) and (mouse.getY() >= 100 and mouse.getY() <= 900) and curr.next is not None:

            if choice == 'kanji':
                curr, extras, rect1, rect12, rect3 = change_card(curr, 'r', extras, win, rect1, rect12, choice, rect3)
            else:

                curr, extras, rect1, rect12 = change_card(curr, 'r', extras, win, rect1, rect12, choice)

            # print('clicked right', mouse.getX(), mouse.getY())

        # Pressed exit
        if (mouse.getX() >= 1900 and mouse.getX() <= 2000) and (mouse.getY() >= 950 and mouse.getY() <= 1000):

            win.close()
            closed = True

            # print('clicked exit', mouse.getX(), mouse.getY())
                


        # Pressed card left (kanji)
        if (mouse.getX() >= 450 and mouse.getX() <= 1000) and (mouse.getY() >= 381 and mouse.getY() <= 900) and choice == 'kanji':

            undraw_blinders('l', rect1, rect12)

            # print('clicked card left', mouse.getX(), mouse.getY())

        # Pressed card translation (kanji)
        if (mouse.getX() >= 450 and mouse.getX() <= 1550) and (mouse.getY() >= 100 and mouse.getY() <= 380) and choice == 'kanji':

            undraw_blinders('m', rect1, rect12, rect3)

            # print('clicked card left', mouse.getX(), mouse.getY())

        # Pressed card right (kanji)
        if (mouse.getX() >= 1001 and mouse.getX() <= 1550) and (mouse.getY() >= 381 and mouse.getY() <= 900) and choice == 'kanji':

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
            translation = temp[1]
            kun_yomi = temp[2]
            on_yomi = temp[3]
            kun_sent = temp[4]
            on_sent = temp[5]
            
            ret_dict[char] = Kanji(char, translation, kun_yomi, on_yomi, kun_sent, on_sent)
        
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

    print(' __  _   ____  ____   ____  ____      __  ____   __      __ __   ___     __   ____  ____       ____     ___ __ __  ____    ___ __    __       ____  ____  ____  ')
    print('|  |/ ] /    ||    \\ |    ||    |    |  ||    \\ |  |    |  |  | /   \\   /  ] /    ||    \\     |    \\   /  _]  |  ||    |  /  _]  |__|  |     /    ||    \\|    \\ ')
    print("|  ' / |  o  ||  _  ||__  | |  |     |_ ||  _  ||_ |    |  |  ||     | /  / |  o  ||  o  )    |  D  ) /  [_|  |  | |  |  /  [_|  |  |  |    |  o  ||  o  )  o  )")
    print('|    \\ |     ||  |  |__|  | |  |       \\||  |  |  \\|    |  |  ||  O  |/  /  |     ||     |    |    / |    _]  |  | |  | |    _]  |  |  |    |     ||   _/|   _/ ')
    print("|     ||  _  ||  |  /  |  | |  |         |  |  |        |  :  ||     /   \\_ |  _  ||  O  |    |    \\ |   [_|  :  | |  | |   [_|  `  '  |    |  _  ||  |  |  |   ")
    print('|  .  ||  |  ||  |  \\  `  | |  |         |  |  |         \\   / |     \\     ||  |  ||     |    |  .  \\|     |\\   /  |  | |     |\\      /     |  |  ||  |  |  |   ')
    print('|__|\\_||__|__||__|__|\\____j|____|        |__|__|          \\_/   \\___/ \\____||__|__||_____|    |__|\\_||_____| \\_/  |____||_____| \\_/\\_/      |__|__||__|  |__|   ')
    print('                                                                                                       ')
    print()

    print("Hello, welcome to Kanji Review App !! \n\n\n\n")
    print("Would you like to add a new Kanji or Vocab Word? [Y/N - K/V]")
    res = input()
    print('\n\n')

    # Adding new kanji or vocab
    while res.lower() in ['y','yes','k','kanji','v','vocab']:

        # Choice whether kanji or vocab
        if res.lower() not in ['k','kanji','v','vocab']:
            print("New Kanji, New Vocab, or skip? [K/V/S]")
            res = input()
            print('\n\n')
    
        if res.lower() in ['k','kanji']:
            add_kanji('Dictionaries\\kanji.txt', 'kanji')
            res = 'y'

        if res.lower() in ['v','vocab']:
            add_kanji('Dictionaries\\vocab.txt', 'vocab')
            res = 'y'
        
        if res.lower() in ['s','skip']:
            break


    print("Would you like to play? [Y/N]")
    loop_res = input()

    if loop_res.lower() in ['y','yes','']:

        while loop_res.lower() not in ['e','exit']:

            if loop_res.lower() in ['y','yes','']:
                print('\n\n')

            print("Kanji review, Vocab review, or exit? [K/V/E]")
            loop_res = input()
            print('\n\n')

            if loop_res.lower() in ['k','kanji']:
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



# def traverse(head):
#     """
#     Add two numbers.

#     :param x: First number
#     :param y: Second number
#     :return: Sum of x and y
#     """
#     # Traverse the doubly linked list and print its elements
#     current = head
#     while current:
#       # Print current node's data
#         print(current.data.word, end=" <-> ")
#         # Move to the next node
#         current = current.next
#     print("None")
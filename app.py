from graphics import *
import random

class Kanji:

    def __init__(self, char, kun_yomi, on_yomi):
        self.char = char
        self.kun_yomi = kun_yomi
        self.on_yomi = on_yomi
    
def add_kanji():
    pass

def program_loop(kanji_dict):

    # draws window
    win = GraphWin("yerr", 2000, 1000)

    

    # SHAPE TEST
    rect = Rectangle(Point(250,250), Point(350,350))
    rect.setOutline(color_rgb(0, 0, 0))
    rect.setFill(color_rgb(200, 200, 200))
    rect.draw(win)

    # # # TEXT TEST
    # text = Text(Point(300, 300),'中')
    # text.draw(win)
    

    kanji_length = len(kanji_dict)
    ran_index = random.sample(range(0,kanji_length), kanji_length)

    # num is the amount of kanji in kanji_dict and will keep track of how many kanji left
    # in shuffle. This num will decrease until it loops the number of times of kanji in
    # the dict
    num = kanji_length

    # program loop
    while num >= 1:
        ran_index = random.sample(range(0,num), 1)[0]
        kanji_key = list(kanji_dict.keys())[ran_index]
        
        kanji = kanji_dict[kanji_key]

        text = Text(Point(300, 300),kanji.char)
        text.draw(win)

        # used to stop to recience input and not just skip and close
        input()

        num -= 1
    
    win.close()

def main():
    
    
    kanji_dict = {} # key - char/symbol     val - kanji_object
    kanji_dict['中'] = Kanji('中', 'naka', 'chu')
    
    
    
    
    
    
    
    
    
    
    
    print("Hello Welcome to Kanji Reviewer App !! \n\n" + "Would you like to add new Kanji? [Y/N]")
    res = input()
    print('\n\n\n')
    
    if res.lower() in ['y','yes']:

        # Starts adding kanji sequence then after it is done, it returns to asking if you want to play
        add_kanji(kanji_dict)

    else:
        print("Would you like to play? [Y/N]")
        res = input()
        print('\n\n\n')


        if res.lower() in ['y','yes']:

            # Starts the program loop and the window, upon completion the window closes and you are brought
            # back to the goodbye prompt below
            program_loop(kanji_dict)

        input("Goodbye !!\n\nPress enter to exit . . .")


    

    



if __name__ == "__main__":
    main()



# Document string 

class screen:
    '''The world biggest tevevision show'''
    def __init__(self,basic,second,HD,High):
        self.basic = basic
        self.second = second
        self.HD = HD
        self.High = High
    def screen_clarity(self):
        print('This Tv is Model is',self.basic)
        print('This Tv is model is',self.second)
        print('This Tv is model is',self.HD)
        print('This Tv is model is',self.High)
    def screen_clarity2(self):
        print('This Tv is Model is',self.basic)
        print('This Tv is model is',self.second)

tv=screen(15,25,45,60)
tv.screen_clarity()
tv.screen_clarity2()
print(tv.__doc__)
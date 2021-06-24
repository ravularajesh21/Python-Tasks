# Overriding

class cricket:
    print('Welcome to World cup matches')
    def __init__(sachin,player_name,runs,wickets,catches):
        sachin.player_name = player_name
        sachin.runs = runs
        sachin.wickets = wickets
        sachin.catches = catches
    def ODI(sachin):
        print('Best opener',sachin.player_name)
        print('Runs',sachin.runs)
        print('Wickets',sachin.wickets)
    def ODI(sachin):
        print('Best opener',sachin.player_name)
        print('Runs',sachin.runs)
        
        
Ind = cricket('Rohit Sharma',8605,651,203)
Ind.ODI()


# Overloading
# but python  does not supports with overloading

class cricket:
    print('Welcome to World cup matches')
    def __init__(sachin,player_name,runs,wickets,catches,matches):
        sachin.player_name = player_name
        sachin.runs = runs
        sachin.wickets = wickets
        sachin.catches = catches
        sachin.matches = matches
    def ODI(sachin,rajesh):
        print('Best opener',sachin.player_name)
        print('Runs',sachin.runs)
        print('Wickets',sachin.wickets)
    def ODI(sachin):
        print('Total catches',sachin.catches)
        print('Total matches is',sachin.matches)
        
        
        
Ind = cricket('Rohit Sharma',8605,651,203,50)
Ind.ODI('money')

        
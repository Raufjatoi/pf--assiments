#. Movie Recommendation System: Create a program that recommends movies based on user 
#preferences. Use variables to store genre, rating, and release year. Write expressions to 
#compare movies and suggest matches.
genre = input ('enter genre : ')
ratin  = float (input('enter rating out of 1/10 : '))
release = int(input('enter release year : '))
def rec (genre,ratin,release):
    if genre in ['action','drama','sitcom'] or ratin in [1,2,3,4,5,6] or release in [2010,2011,2012,2013,2014,2015,2016,]:
        return ['Ironman','inception','thor','train to busan']
    elif genre in ['sci fic', 'comedy' ,'horror'] or ratin in [7,8,9,10] or release in [2017,2018,2019,2020]:
        return ['interstellar', 'bladerunner','everythin everyone all at once']
    else:
        return ['the mask','Ironman2','kunfu panda', 'three idiots']
print('movies recommendations are : ')

for i in rec(genre,ratin,release):
    print(i)
         
    
##Sorry, it was not enough time for me to finish task properly, so i'll try to show the way i think it should be done )

#First of all I would create database with all attributes, smth like:
# |AUTHOR|NOTES|RATING
#
# After that:

class Book:
    'Book information'
    pln = 0
    def __init__(self, nm, nt, rt):
        self.name = nm
        self.note = nt

        #rating can't be modified
        self.__rating = rt

        Book.pln += 1
        def info(self):
            print('Author:{} notes{} rated{}'.format(self.name, self.note, self.__rating))


#Read notes from file
        getattr(books, 'notes')

#Add notes to file
        setattr(books, 'notes', 'some value')

#Print notes to console
       print(books.__getattribute__(self, nt))

#Get author with the lowest rating
    def is_lowest(x):
        if x == 0:
            return True
        else:
            return False

        f = filter(is_lowest, [books[rating]])
        for i in f:
            print(i)

#Get author with the highest rating
    def is_highest(x):
        if x == 1:
            return True
        else:
            return False

        f = filter(is_highest, [books[rating]])
        for i in f:
            print(i)

#Get average rating among all authors
        avg = sum(rating) / len(rating)
        print("The average rating among all authors is ", round(avg, 2))
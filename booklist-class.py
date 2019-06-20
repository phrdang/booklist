class Book(object):
    id = 0
    def __init__(self, title, author, rating, genres, tags, series):
        '''
        Initializes the book object. 
        title, author, series: str
        genres, tags: list of str
        rating: int from 1-5
        '''
        self.title = title
        self.author = author
        self.rating = rating
        self.genres = genres
        self.tags = tags
        self.series = series

        Book.id += 1
        self.id = Book.id
    def __str__(self):
        # First line of info prints the title, author, and rating
        first = 'Title: %s | Author: %s | Rating: %s' % (self.title, self.author, self.rating)
        
        # Converts the self.genres list to a readable str
        genres_str = ''
        for genre in self.genres:
            if self.genres[-1] == genre:
                genres_str += genre
            else:
                genres_str += genre + ', '

        # Converts the self.tags list to a readable str
        tags_str = ''
        for tag in self.tags:
            if tags[-1] == tag:
                tags_str += tag
            else:
                tags_str += tag + ', '

        # Second line of info prints the genres and tags
        second = '\nGenre(s): %s | Tag(s): %s' % (genres_str, tags_str)
        
        # Third line of info prints the book ID
        third = '\nID: ' + str(self.id)
        
        return first + second + third


title = 'Six of Crows'
author = 'Leigh Bardugo'
rating = '5'
genres = ['YA', 'Fantasy']
tags = ['kaz brekker', 'inej ghafa', 'ketterdam']
series = 'Six of Crows Duology'
soc_obj = Book(title, author, rating, genres, tags, series)
print(soc_obj)
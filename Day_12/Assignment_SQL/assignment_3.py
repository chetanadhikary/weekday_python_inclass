import sqlite3

def get_table(table_name):
    '''
        Function takes table name as argument
        Returns table and column header (column names) which exists in chinook database
    '''
    with sqlite3.connect('chinook.db') as conn:
        sql_get = 'SELECT * FROM '+ table_name
        cur = conn.execute(sql_get)
        cols_header = [desc[0] for desc in cur.description]
        return cur.fetchall(),cols_header
    
tbl_artists,artists_cols = get_table('artists')
tbl_albums,albums_cols = get_table('albums')


def get_dict_table(tbl_name,col_header):
    '''
        Takes a table and column header as arguments
        
        Returns a list containing column header as key and row elements as value
        
        Expected output for artist table
        
        >>> get_dict_table(tbl_artists,artists_col)
        [{'ArtistId': 1, 'Name': 'AC/DC'},
         {'ArtistId': 2, 'Name': 'Accept'},
         {'ArtistId': 3, 'Name': 'Aerosmith'},
         ...
         ...
         {'ArtistId': 274, 'Name': 'Nash Ensemble'},
         {'ArtistId': 275, 'Name': 'Philip Glass Ensemble'}]
         
    '''
    ## Write your code within Begin and End.
    ## Begin
    
    
    ## End
    return dict_tbl

    

def get_Album_Artist(artist_tbl,album_tbl):
    '''
        Takes two arguments : Artist table and Album table
        
        Returns a list containg the album title and name of the artist
        
        Expected output
        
        >>>get_Album_Artist(dict_artist_tbl,dict_album_tbl)
        ['For Those About To Rock We Salute You was composed by "AC/DC"',
         'Let There Be Rock was composed by "AC/DC"',
         'Balls to the Wall was composed by "Accept"',
         'Restless and Wild was composed by "Accept"',
         ...
         ...
         'Mozart: Chamber Music was composed by "Nash Ensemble"',
         'Koyaanisqatsi (Soundtrack from the Motion Picture) was composed by "Philip Glass Ensemble"']
         
    '''
    ## Write your code within Begin and End 
    ## Begin
    
    
    ## End
    return lst_Album_Artist
    

def get_Artist_max_count(artist_tbl,album_tbl):
    '''
        Function takes two arguments Artist table and Album table
        
        Returns the name of artist who has composed most number of albums and
        number of albums he has created
        
        Expected Output:
        
        >>> get_Artist_max_count(artist_tbl,album_tbl)
        ('Iron Maiden', 21)
        
    '''
    ## Write your code within Begin and End 
    ## Begin
    
    
    ## End
   
    return max_artist_name,max_artist_count
# Video Game Sales Dataset
video_game_sales = [
    [1, 'Wii Sports', 'Wii', 2006, 'Sports', 'Nintendo', 41.49, 29.02, 3.77, 82.74],
    [2, 'Super Mario Bros.', 'NES', 1985, 'Platform', 'Nintendo', 29.08, 3.58, 6.81, 40.24],
    [3, 'Mario Kart Wii', 'Wii', 2008, 'Racing', 'Nintendo', 15.85, 12.88, 3.79, 35.82],
    [4, 'Wii Sports Resort', 'Wii', 2009, 'Sports', 'Nintendo', 15.75, 11.01, 3.28, 33.0],
    [5, 'Pokemon Red/Blue', 'GB', 1996, 'Role-Playing', 'Nintendo', 11.27, 8.89, 10.22, 31.37],
    [6, 'Tetris', 'GB', 1989, 'Puzzle', 'Nintendo', 23.2, 2.26, 4.22, 30.26],
    [7, 'New Super Mario Bros.', 'DS', 2006, 'Platform', 'Nintendo', 11.38, 9.23, 6.5, 30.01],
    [8, 'Wii Play', 'Wii', 2006, 'Misc', 'Nintendo', 14.03, 9.2, 2.93, 29.02],
    [9, 'New Super Mario Bros. Wii', 'Wii', 2009, 'Platform', 'Nintendo', 14.59, 7.06, 4.7, 28.62],
    [10, 'Duck Hunt', 'NES', 1984, 'Shooter', 'Nintendo', 26.93, 0.63, 0.28, 28.31],
    [11, 'Nintendogs', 'DS', 2005, 'Simulation', 'Nintendo', 9.07, 11.0, 1.93, 24.76],
    [12, 'Mario Kart DS', 'DS', 2005, 'Racing', 'Nintendo', 9.81, 7.57, 4.13, 23.42],
    [13, 'Pokemon Gold/Silver', 'GB', 1999, 'Role-Playing', 'Nintendo', 9.0, 6.18, 7.2, 23.1],
    [14, 'Wii Fit', 'Wii', 2007, 'Sports', 'Nintendo', 8.94, 8.03, 3.6, 22.72],
    [15, 'Kinect Adventures!', 'X360', 2010, 'Misc', 'Microsoft', 14.97, 4.94, 0.24, 21.82],
    [16, 'Grand Theft Auto V', 'PS3', 2013, 'Action', 'Take-Two', 7.01, 9.27, 0.97, 21.4],
    [17, 'Grand Theft Auto: San Andreas', 'PS2', 2004, 'Action', 'Take-Two', 9.43, 0.4, 0.41, 20.81],
    [18, 'Super Mario World', 'SNES', 1990, 'Platform', 'Nintendo', 12.78, 3.75, 3.54, 20.61],
    [19, 'Brain Age', 'DS', 2005, 'Puzzle', 'Nintendo', 4.75, 9.26, 4.16, 20.22],
    [20, 'Pokemon Diamond/Pearl', 'DS', 2006, 'Role-Playing', 'Nintendo', 6.42, 4.52, 6.04, 18.36],
]

RANK = 0
NAME = 1
PLATFORM = 2
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9

#a) Write a function called calculate_total_sales(game) that takes a single game row (a list) as input and returns the sum of NA, EU, and JP sales. Test it by calling it on the first game in the dataset and printing the result. use return to send back the sum of game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

def calculate_total_sales(game):
    total_sales = game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
    return total_sales
    
total_sales = calculate_total_sales(video_game_sales[0])

print (total_sales)

#b) Write a function called filter_by_genre(data, genre) that takes the full dataset and a genre string as inputs, and returns a new list containing only the games that match that genre. Give the genre parameter a default value of 'Platform'. Test it with and without specifying a genre. set the default value in the function definition: def filter_by_genre(data, genre='Platform'). Build a result list inside the function and return it. 

def filter_by_genre(data, genre='Platform'):
    empty_list = []
    for game in data:
        if game[GENRE] == genre:
            empty_list.append(game)
    return empty_list
    
platform_name = filter_by_genre(video_game_sales, genre='Platform')
platform_genre_name = filter_by_genre(video_game_sales)

print(platform_name)    
print(platform_genre_name)

# c) Write a function called get_summary(game) that takes a game row and returns a formatted string like: "Wii Sports (2006) - Sports - $82.74M". Use this function inside a loop to print a summary of every game in the dataset. use an f-string inside the function and return the string (don't print inside the function).
    
def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}"
    
for game in video_game_sales:
    print(get_summary(game))
        
    

    

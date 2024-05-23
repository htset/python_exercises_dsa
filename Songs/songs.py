class Song:
    def __init__(self, title, artist, album, release_year):
        self.title = title
        self.artist = artist
        self.album = album
        self.release_year = release_year

#Compare songs based on artist
def compare_by_artist(a, b):
    return (a.artist > b.artist) - (a.artist < b.artist)

#Compare songs based on album
def compare_by_album(a, b):
    return (a.album > b.album) - (a.album < b.album)

#Compare songs based on release date
def compare_by_release_date(a, b):
    return a.release_year - b.release_year

def insertion_sort(arr, comparator):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and comparator(arr[j], key) > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    songs = [
        Song("Song1", "Artist2", "Album1", 2010),
        Song("Song2", "Artist1", "Album2", 2005),
        Song("Song3", "Artist3", "Album1", 2015),
        Song("Song4", "Artist4", "Album3", 2008),
        Song("Song5", "Artist1", "Album2", 2003),
        Song("Song6", "Artist3", "Album4", 2019),
        Song("Song7", "Artist2", "Album3", 2012),
        Song("Song8", "Artist4", "Album4", 2017),
        Song("Song9", "Artist5", "Album5", 2014),
        Song("Song10", "Artist5", "Album5", 2011)
    ]

    #Sort by artist
    insertion_sort(songs, compare_by_artist)
    print("Sorted by Artist:")
    for song in songs:
        print(f"{song.title} from {song.artist}")
    print()

    #Sort by album
    insertion_sort(songs, compare_by_album)
    print("Sorted by Album:")
    for song in songs:
        print(f"{song.title} from {song.album}")
    print()

    #Sort by release date
    insertion_sort(songs, compare_by_release_date)
    print("Sorted by Release Date:")
    for song in songs:
        print(f"{song.title} released in {song.release_year}")

if __name__ == "__main__":
    main()

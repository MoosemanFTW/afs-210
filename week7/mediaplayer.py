import doubly_linked_list as dll
        
class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.data) 

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

class song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def __str__(self):
        return self.title + " by " + self.artist 
        
    # This private def just returns variable data
    def __repr__(self):
         return "%s %s" % (self.artist, self.title)

class musicplayer():
    def __init__(self):
        self.playlist = dll.DoublyLinkedList()
        self.currentSong = None


    def add(self,songTitle,songArtist):
        newSong = song(songTitle,songArtist)        
        self.playlist.add(newSong)

    def remove(self, index) -> int:
        if (index < 0) or (index > self.playlist.size()-1):
            return 0
        self.playlist.deleteAtIndex(index)
        return True

    def playCurrent(self, song=None):
        if song:
            self.currentSong = song
        if not self.currentSong:
            self.currentSong = self.playlist.getStart()
        print("Title: ", self.currentSong.data.getTitle())
        print("Artist: ", self.currentSong.data.getArtist())

    def skip(self):
        self.currentSong = self.currentSong.next

        if not self.currentSong:
            # We reached the end of the playlist, loop back to the beginning
            self.currentSong = self.playlist.getStart()

        self.playCurrent(self.currentSong)

    def goBack(self):
        self.currentSong = self.currentSong.prev
        if not self.currentSong:
            # We reached the end of the playlist, loop back to the end
            self.currentSong = self.playlist.getEnd()
        self.playCurrent(self.currentSong)     

    def showCurrentSong(self):
        if self.currentSong:
            print(self.currentSong.data) 
        else:
            print("No song is currently being playCurrented")

    def shuffle(self):
        self.playlist.shuffleList()

newPlaylist = musicplayer()
newPlaylist.add('Welcome To the Internet', 'Bo Burnham')
newPlaylist.add('The Author', 'Livingston')
newPlaylist.add('Kill the Lights', 'Set It Off')
newPlaylist.add('Bad Company', 'Five Finger Death Punch')
newPlaylist.add('Hail To the King', 'Avenged Sevenfold')
newPlaylist.add('The Last Stand', 'Sabaton')

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())

    if choice == 1:  #add song
        songTitle = input("Enter song name: ")
        songArtist = input("Enter songs artist: ")
        newPlaylist.add(songTitle, songArtist)
        print(f"The new song {songTitle} has been added")
    elif choice == 2:  #remove song
        print(newPlaylist.playlist)
        ind = int(input("Enter number for song you would like to remove: "))
        newPlaylist.remove(ind)
        print("Song Removed from Playlist")
    elif choice == 3:  #play current song
        newPlaylist.playCurrent()
        print("Playing....")        
    elif choice == 4:  #skip
        print("Next song... ")
        newPlaylist.skip()                    
    elif choice == 5:  #previous
        print("Previous song... ")
        newPlaylist.goBack() 
    elif choice == 6:  #shuffle
        print("Shuffling....") 
        newPlaylist.shuffle()
        print(newPlaylist.playlist)         
    elif choice == 7:  #show song
        print("Currently playing: ", end=" ")
        newPlaylist.showCurrentSong()  
    elif choice == 8:  #playslist order
        print("\nSong list:\n")
        print(newPlaylist.playlist)
    elif choice == 0:  #exit
        print("Goodbye.")
        break

            
list = DoublyLinkedList()
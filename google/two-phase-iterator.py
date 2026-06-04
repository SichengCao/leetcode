class PhotoIterator:
    def __init__(self,album,favorites):
        self.album = album
        self.favorites = favorites

        self.favorite_set = set(favorites)
        self.phase = 1
        self.i = 0
        self.j = 0


    def getNextPhoto(self):
        if self.phase ==1:
            if self.i < len(self.favorites):
                res = self.favorites[self.i]
                self.i +=1
                return res
            else:
                self.phase = 2


        while self.j < len(self.album):
            photo = self.album[self.j]
            self.j += 1
            if photo not in self.favorite_set:
                return photo


        return None


def main():
    album = [1, 2, 3, 4]
    favorites = [3, 1]

    it = PhotoIterator(album, favorites)
    print(it.getNextPhoto())


if __name__ == "__main__":
    main()
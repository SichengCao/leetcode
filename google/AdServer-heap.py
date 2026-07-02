import heapq


class AdServer:

    def __init__(self):

        self.heap = []
        self.prev = None

    def insertAd(self, content, score):

        heapq.heappush(self.heap,(-score,content))

    def getAd(self):

        if not self.heap:
            return None

        firstscore, firstContent = heapq.heappop(self.heap)

        if firstContent != self.prev:

            firstscore +=1

            if firstscore <0:
                heapq.heappush(self.heap,(firstscore,firstContent))

            self.prev = firstContent

            return firstContent

        if not self.heap:
            heapq.heappush(self.heap,(firstscore,firstContent))
            return None

        secondScore, secondContent = heapq.heappop(self.heap)
        secondScore +=1
        if secondScore < 0:
            heapq.heappush(self.heap,(secondScore,secondContent))


        heapq.heappush(self.heap,(firstscore,firstContent))

        self.prev = secondContent
        return secondContent




server = AdServer()

server.insertAd("A", 3)
server.insertAd("B", 2)
server.insertAd("C", 2)

for _ in range(10):
    print(server.getAd())
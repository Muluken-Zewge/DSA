class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # create counter hashmap: word -> count
        counter = Counter(words)
        # use max heap
        max_heap = []

        # heappush the negative of the count and the word itself
        for word, count in counter.items():
            heappush(max_heap, (-count,word))

        res = []
        # extract the top k
        for _ in range(k):
            _, word = heappop(max_heap)
            res.append(word)
        
        return res
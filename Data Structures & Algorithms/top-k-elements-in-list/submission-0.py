class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topic = {}

        for i in nums:

            if i not in topic:
                topic[i] = 1
            
            topic[i] += 1

        sorted_items = sorted(topic, key=topic.get, reverse=True)
        return sorted_items[:k]
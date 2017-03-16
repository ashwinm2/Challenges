# Top k frequent numbers
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    queue = []
    frequency_map = {}
    for i in nums:
        if i not in frequency_map:
            frequency_map[i] = 1
        else:
            frequency_map[i] += 1
    
    print "Freq map", frequency_map
    answer = {}
    max_val = 0
    for key in frequency_map:
        if frequency_map[key] not in answer:
            answer[frequency_map[key]] = [key]
            if max_val < frequency_map[key]:
                max_val = frequency_map[key]
        else:
            answer[frequency_map[key]].append(key)
            
    
    print "Answer map", answer
    print "Max", max_val
    
    final = []
    while len(final) < k:
        if max_val in answer:
            print "val", max_val
            t = answer[max_val]
            final.extend(t)
            del answer[max_val]
        else:
            max_val -= 1
            
    print final[:k]
    return final[:k]
        
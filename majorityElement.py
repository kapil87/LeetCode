def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        print "count: %s  candidate: %s"%(count, candidate)
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

from typing import List


class Solution:

    def minMeetingRoomsBruteForce(self, intervals: List[List[int]]) -> int:
        requiredHours = []
        roomsNeeded = 1
        for req in intervals:
            hrs = [hr for hr in range(req[0], req[1])]
            requiredHours.extend(hrs)
        for i in requiredHours:
            _ocr = requiredHours.count(i)
            if _ocr > roomsNeeded:
                roomsNeeded = _ocr
        return roomsNeeded

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = len(intervals)
        neededRooms = 0
        meetStarts = sorted([i[0] for i in intervals])
        meetEnds = sorted([i[1] for i in intervals])

        spt = 0
        ept = 0
        while spt < meetings:
            if meetStarts[spt] >= meetEnds[ept]:
                neededRooms -= 1
                ept += 1

            neededRooms += 1
            spt += 1
        return neededRooms


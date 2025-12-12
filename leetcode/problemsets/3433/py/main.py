# Solution to leetcode problem 3433
"""
Docstring for problemsets.3433.py.main
You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.

Each events[i] can be either of the following two types:

Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
This event indicates that a set of users was mentioned in a message at timestampi.
The mentions_stringi string can contain one of the following tokens:
id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
ALL: mentions all users.
HERE: mentions all online users.
Offline Event: ["OFFLINE", "timestampi", "idi"]
This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.

Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.
"""

from typing import List
import dataclasses

@dataclasses.dataclass
class Event:
    event_type: str
    timestamp: int
    mentions_direct: List[int]
    mentions_all: bool
    mentions_here: bool
    precedence: int

def ez_event(e):
    event_type: str = e[0]
    if event_type == "MESSAGE":
        timestamp: int = int(e[1])
        mentions_str: str = e[2]
        precedence = 2
        if mentions_str == "ALL":
            mentions_direct = []
            mentions_all = True
            mentions_here = False
        elif mentions_str == "HERE":
            mentions_direct = []
            mentions_all = False
            mentions_here = True
        else:
            mentions_direct = [int(m[2:]) for m in mentions_str.split(" ")]
            mentions_all = False
            mentions_here = False
        return Event(
            event_type=event_type,
            timestamp=timestamp,
            mentions_direct=mentions_direct,
            mentions_all=mentions_all,
            mentions_here=mentions_here,
            precedence=precedence
        )
    elif event_type == "OFFLINE":
        timestamp: int = int(e[1])
        user_id: int = int(e[2])
        return Event(
            event_type=event_type,
            timestamp=timestamp,
            mentions_direct=[user_id],
            mentions_all=False,
            mentions_here=False,
            precedence=1
        )
    else:
        raise ValueError(f"Unknown event type: {event_type}")



class Solution(object):
 
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # process events to make it more ergonomic
        ergo_events = [ez_event(e) for e in events]
        # Insert ONLINE events
        online_events = []
        for e in ergo_events:
            if e.event_type == "OFFLINE":
                online_events.append(Event(
                    event_type="ONLINE",
                    timestamp=e.timestamp + 60,
                    mentions_direct=e.mentions_direct,
                    mentions_all=False,
                    mentions_here=False,
                    precedence=0
                ))
        ergo_events.extend(online_events)
        # Sort events by timestamp.  If events have the same timestamp, they
        # are processed in type order: OFFLINE, ONLINE, MESSAGE.
        ergo_events.sort(
            key=lambda e: (
                e.timestamp,  # Lower timestamp first.
                e.precedence),
            reverse=False)
        msg_count = [0] * numberOfUsers
        is_online = [True] * numberOfUsers
        for ee in ergo_events:
            # print(f"ts: {ee.timestamp} {ee.event_type}")
            if ee.event_type == "OFFLINE":
                is_online[ee.mentions_direct[0]] = False
            elif ee.event_type == "ONLINE":
                is_online[ee.mentions_direct[0]] = True
            elif ee.event_type == "MESSAGE":
                if ee.mentions_all:
                    msg_count = [msg_count[i] + 1 for i in range(numberOfUsers)]
                elif ee.mentions_here:
                    msg_count = [msg_count[i] + 1 if is_online[i] else msg_count[i] for i in range(numberOfUsers)]
                else:
                    for i in ee.mentions_direct:
                        msg_count[i] += 1
            else:
                raise ValueError(f"Unknown event type: {ee.event_type}")

        return msg_count
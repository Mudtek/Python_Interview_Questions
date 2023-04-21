"""The example given on https://devguide.python.org/internals/garbage-collector/"""

import gc

class Link:
   def __init__(self, next_link: 'Link'=None) -> None:
       self.next_link = next_link

link_3 = Link()
link_2 = Link(link_3)
link_1 = Link(link_2)
link_3.next_link = link_1
A = link_1
del link_1, link_2, link_3

link_4 = Link()
link_4.next_link = link_4
del link_4

# Collect the unreachable Link object (and its .__dict__ dict).
gc.collect()
from pprint import pprint
import re
from typing import  TypedDict

"""
findall
find
finditer
// return none or match obj.
match
search
sub

compile
split
"""
#Return a list containing every occurrence of "ai":
"""
__all__ = [
    "match", "fullmatch", "search", "sub", "subn", "split",
    "findall", "finditer", "compile", "purge", "template", "escape",
    "error", "Pattern", "Match", "A", "I", "L", "M", "S", "X", "U",
    "ASCII", "IGNORECASE", "LOCALE", "MULTILINE", "DOTALL", "VERBOSE",
    "UNICODE",
]
"""
txt = "The rain in Spain"
x = re.search("\s", txt)
x = {
    'end': x.end(),
    'endpos': x.endpos,
    'group': x.group(), 'groupdict': x.groupdict(),
    'groups': x.groups(), 
    'pos': x.pos, 
    're': x.re, 
    'regs': x.regs,
    'span': x.span(), 
    'start': x.start(), 
    'string': x.string
}
pprint(x,indent=4)
print()
# x.update({
#  'expand': x.expand(), 
# 'lastgroup': x.lastgroup(), 
# 'lastindex': x.lastindex(), 
# }
import re
s = "asa"
x = re.sub(r"(\w)(?:?R|\w?)\1", "", s)
print(x)


class Movie(TypedDict):
   title: str
   year: int

m1: Movie = {"title": "Black Panther", "year": 2018}  # OK
m2: Movie = {"title": "Star Wars"}  # OK (year is not required)
m3: Movie = {"year": 2022}
print(type(m1))
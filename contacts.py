import re

#--------------------------- FormatContactName ---------------------------------
# Description: returns the contact name in First Last format. removes any
#   non-whitelist characters which are: 0-9a-zA-Z.-
# Examples: input: first = "Tim", last = "Pei" returns "Tim Pei"
#   input: first = "$Hello$" last = "#Kiss&My&App#" returns "Hello KissMyApp"

def FormatContactName(first, last):
    if IsValidContactName(first, last):
        return first + ' ' + last
    else:
        pattern = re.compile('([0-9a-zA-Z.-]+)')
        newFirst = pattern.findall(first)   #extracts all whitelist characters
        newFirst = ''.join(newFirst)
        #if newFirst > 12:            #possible concatenation if >12 characters
            #newFirst = newFirst[:12]
        newLast = pattern.findall(last)
        newLast = ''.join(newLast)
        #if newLast > 12:
            #newLast = newLast[:12]
        return newFirst + ' ' + newLast

#--------------------------- IsValidContactName ---------------------------------
# Description: checks if the first and last name are in valid format. Returns
#   false when there are non-whitelist characters and if either length is > 12
#   or < 2
# Examples: input: first = "Tim", last = "Pei" returns True
#   input: first = "$Hello$" last = "#Kiss&My&App#" returns False
def IsValidContactName(first, last):
    pattern = re.compile('(^[0-9a-zA-Z.-]+$)')
    if pattern.match(first) and pattern.match(last):
        if 13 > len(first) > 1 and 13 > len(last) > 1:
            return True
    return False

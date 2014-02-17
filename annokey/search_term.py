import re

# how many characters either side of the match do
# we keep as context
context_width = 50

class SearchTerm(object):
    pass

class Regex(SearchTerm):
    def __init__(self, term):
        self.term = term
        self.match = re.compile(term)

    def search(self, args, string):
        """find the pattern in the string and
        return the context around the match"""
        spans = []
        for match in self.match.finditer(string):
            spans.append(match.span())
            #low, high = match.span()
            #low_bound = max(0, low - context_width)
            #high_bound = min(len(string), high + context_width)
            #bottom = string[low_bound:low]
            #matched_term = string[low:high]
            #top = string[high:high_bound]
            #context = (bottom, matched_term, top)
            #result.append(context)
            #if not args.allmatches:
            #    # Return the first match only
            #    return result
        if len(spans) > 0:
            return TermMatch(string, spans)
        else:
            return None

    def __str__(self):
        return self.term

class TermMatch(object):
    def __init__(self, context, spans):
        self.context = context # string that was searched in
        self.spans = spans

def parse_search_term(string):
    search_term = string.strip()
    return Regex(search_term)

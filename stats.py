def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    letcount = {}
    for t in text:
        if( t.isalpha() and t.lower() in letcount ):
            letcount[t.lower()] += 1
        elif( t.isalpha() ):
            letcount[t.lower()] = 1
    return letcount
    
def sort_prio(dict):
    return dict["count"]

def sort_chars(letcount):
    sorted_count = []
    for k, v in letcount.items():
        sorted_count.append({"char": k, "count": v})
    sorted_count.sort(reverse=True, key=sort_prio)
    return sorted_count
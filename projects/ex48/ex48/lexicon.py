def scan(stuff):
    directions_list = ['north','south','east','west','down','up','left','right','back']
    verbs_list = ['go','stop','kill','eat']
    stops_list = ['the','in','of','from','at','it']
    nouns_list = ['door','bear','princess','cabinet']

    words = stuff.split()
    results = []

    for word in words:
        try:
            word = int(word)
            results.append( ('number', word) )
        except ValueError:
            if word in directions_list:
                results.append( ('direction', word) )
            elif word in verbs_list:
                results.append( ('verb', word) )
            elif word in stops_list:
                results.append( ('stop', word) )
            elif word in nouns_list:
                results.append( ('noun', word) )
            else:
                results.append( ('error', word) )

    return results
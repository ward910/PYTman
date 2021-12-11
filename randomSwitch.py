from randomText import exports


def randomSwitch():
    random = exports.get("random")
    title = exports.get("titleRandom")
    text = exports.get("textRandom")
    link = exports.get("linkRandom")

    if random == 0:
        ArticleContent = [title[0], text[0], link[0]]
    elif random == 1:
        ArticleContent = [title[1], text[1], link[1]]
    else:
        ArticleContent = [title[2], text[2], link[2]]
    
    return ArticleContent

from ngram import NGram
from jmbowordsuggest.models import AcceptedWord,AcceptedWordCategory 

def suggest_words(key, query):
    lower = lambda x: x.lower()
    
    ngram_index = NGram(iconv=lower, qconv=lower)
    
    if AcceptedWordCategory.objects.filter(name = key).exists():
        category = AcceptedWordCategory.objects.get(name = key)
        [ngram_index.add(x.word) for x in category.words.all()]
        words = ngram_index.search(query)
        return words[:2]
    return None
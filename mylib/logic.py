import wikipedia
#import googletrans
from deep_translator import GoogleTranslator



def wiki(name="Hunter", length=1):
    """ This is a wikipedia fetcher """
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """ Search Wikipedia for names """
    results = wikipedia.search(name)
    return results

def trans(name):
    """ Translation """
    page = wikipedia.summary(name)
    #trans = ts.google(query_text=page,to_language='fr')
    translated = GoogleTranslator(source='auto', target='fr').translate(page)
    return translated

#def wiki_page(page)
#    """ Search Wikipedia for page """
#    result_page = wikipedia.page(page)
#    return result_page


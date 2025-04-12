import wikipedia
from yake import KeywordExtractor

def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result     

def search(name="Microsoft"):
    result = wikipedia.search(name)
    return result
    

def get_wiki_page(name="Microsoft"):
    page = wikipedia.page(name)
    return page.content

#return the top 10 keywords of the wikipedia page
def get_keywords(name="Microsoft"):
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(get_wiki_page(name))
    return keywords[:10]



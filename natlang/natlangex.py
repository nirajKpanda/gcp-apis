import io
from google.cloud import language

def lang_analysis(text):
    l_c = language.Client()
    doc = l_c.document_from_text(text)
    sent_analysis = doc.analyze_sentiment()
    print dir(sent_analysis)
    sentiment = sent_analysis.sentiment
    ent_analysis = doc.analyze_entities()
    entities = ent_analysis.entities
    return sentiment, entities

print(lang_analysis('What separates the winners from the losers is how a person reacts to each new twist of fate.'))

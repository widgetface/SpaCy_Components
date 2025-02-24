import json
from data.labels import CLINICAL_ABBREVIATION
import spacy
from spacy.language import Language

ABBREV_FILE = "./data/abbreviations.json"
CLINICAL_NER_ABREV_FUNCTION_NAME = "clinical_ner_tagger"

abbreviations = {}
with open(ABBREV_FILE, "r") as file:
    abbreviations = json.load(file)


@Language.component(name="clinical_ner_tagger")
def clinical_ner_tagger(doc):
    for token in doc:
        lookup = abbreviations.get(token.text, None)
        if lookup:
            token.ent_type_ = CLINICAL_ABBREVIATION

    return doc

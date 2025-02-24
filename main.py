from components.clinical_abbreviation_tagger import (
    clinical_ner_tagger,
    CLINICAL_NER_ABREV_FUNCTION_NAME,
)
import spacy
from spacy.language import Language


ABBREV_FILE = "./data/abbreviations.json"

nlp = spacy.load("en_core_web_sm")


def main():
    nlp = spacy.load("en_core_web_sm")
    Language.component("clinical_ner_tagger")

    nlp.add_pipe(
        "clinical_ner_tagger",
        before="ner",
    )
    print(nlp.pipe_names)
    doc = nlp("The patient as suffering from two vessels disease (2VD).")

    for token in doc:
        print(f"LABEL {token.text} , abbrev = {token.ent_type_}")


if __name__ == "__main__":
    main()

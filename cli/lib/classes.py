from keyword_search import *

class InvertedIndex:
    def __init__(self):
        self.index = {}
        self.docmap = {}

    def __add_document(self, doc_id, text):
        tokens = tokenize_text(text)
        self.index[doc_id] = tokens

    def get_documents(self, term):

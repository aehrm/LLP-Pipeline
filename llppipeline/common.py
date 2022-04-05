from __future__ import annotations
from typing import TextIO, Iterable, Sequence

import more_itertools

class Token:
    fields = "doc id word sentence lemma pos morph".split()
    id: int
    doc: str
    word: str
    sentence: int
    lemma: str
    pos: str
    morph: str

    def __init__(self):
        self.fields = {}

    def get_field(self, key, module_name=None):
        if module_name is not None:
            return self.fields[(key, module_name)]

        candidates = [(field_key, field_module_name) for field_key, field_module_name in self.fields.keys() if
                      field_key == key]
        if len(candidates) == 0:
            raise TypeError(f'Field {key} not set')
        if len(candidates) > 1:
            raise TypeError(f'Field {key} set by multiple modules; call get_field(field, module_name)')
        return self.fields[candidates[0]]

    def set_field(self, field, module_name, value):
        self.fields[(field, module_name)] = value

    def __setattr__(self, key, value):
        if key in Token.fields:
            raise TypeError('Fields need to be set with set_field(field, module_name)')
        else:
            object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        if key in Token.fields:
            return self.get_field(key)
        else:
            return object.__getattribute__(self, key)

    def __str__(self):
        return self.fields.__str__()

    @staticmethod
    def get_sentences(tokens: Iterable[Token]) -> Iterable[Iterable[Token]]:
        return more_itertools.split_when(tokens, lambda a, b: a.sentence != b.sentence)

    @staticmethod
    def get_documents(tokens: Iterable[Token]) -> Iterable[Iterable[Token]]:
        return more_itertools.split_when(tokens, lambda a, b: a.doc != b.doc)


class Tokenizer:
    def tokenize(self, file: TextIO, filename: str) -> Iterable[Token]:
        raise NotImplementedError


class Module:
    def process(self, tokens: Sequence[Token], **kwargs) -> Iterable[Token]:
        raise NotImplementedError
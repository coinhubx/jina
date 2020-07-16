from typing import Iterable

from .. import BaseRecursiveDriver


class ReverseQL(BaseRecursiveDriver):
    def apply_all(self, docs: Iterable['jina_pb2.Document'], *args, **kwargs):
        docs.reverse()


class ReverseMatchesQL(BaseRecursiveDriver):
    def apply_all(self, docs: Iterable['jina_pb2.Document'], *args, **kwargs):
        docs.matches.reverse()

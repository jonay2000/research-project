from __future__ import annotations

from typing import Iterable

from mapfmclient import MarkedLocation

from python.agent import Agent


class Identifier:
    def __init__(self, partial: tuple[Agent, ...], actual: tuple[Agent, ...]):
        self.partial: tuple[Agent, ...] = partial
        self.actual: tuple[Agent, ...] = actual

    @classmethod
    def from_marked_locations(cls, starts: Iterable[MarkedLocation]) -> Identifier:
        agents = tuple(Agent.from_marked_location(start, 0) for start in starts)
        return cls(agents, agents)

    def __eq__(self, other: Identifier):
        return self.partial == other.partial and self.actual == other.actual

    def __hash__(self):
        return hash((self.partial, self.actual))

    def __repr__(self):
        if self.partial == self.actual:
            return f"actual: {self.actual}"
        else:
            return f"partial: {self.partial}, actual: {self.actual}"

from __future__ import annotations

import copy
from typing import Optional

from mapfmclient import MarkedLocation

from python.coord import Coord, UncalculatedCoord


class Agent:
    def __init__(self, location: Coord, color: int, accumulated_cost: Optional[int]):
        self.location = location
        self.accumulated_cost = accumulated_cost if accumulated_cost else 0
        self.color = color

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def __eq__(self, other: Agent):
        if other is self:
            return True
        return self.location == other and self.accumulated_cost == other.accumulated_cost

    def __hash__(self):
        return hash(self.location) ^ hash(self.accumulated_cost)

    def __repr__(self):
        if self == UncalculatedAgent:
            return "UncalculatedAgent    "
        else:
            return f"Agent({self.location}, {self.accumulated_cost})"

    @classmethod
    def from_marked_location(cls, location: MarkedLocation, accumulated_cost: int) -> Agent:
        return cls(Coord(location.x, location.y), location.color, accumulated_cost)

    def with_new_position(self, new_pos: Coord) -> Agent:
        return Agent(new_pos, self.color, self.accumulated_cost)


# An agent that has not yet been calculated. Stand in
# for agents in OD when states are only partially calculated
UncalculatedAgent = Agent(UncalculatedCoord, 0, 0)

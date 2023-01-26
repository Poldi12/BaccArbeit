from dataclasses import dataclass

@dataclass
class LocalViewC:
    MyColor: int = None
    NeighborColors = []

@dataclass
class BallC:
    MyLocalView: LocalViewC = None
    Adjacents = []
    
@dataclass
class VerticeC:
    Ball: BallC = None
    AF: int = None
    PositionInVerticeList: int = None

@dataclass
class NHGraphC:
    VerticeList = []
    SAT: int = None
    Solution = []
    Problem = []
    LaufzeitAusgabefärbung: int = None
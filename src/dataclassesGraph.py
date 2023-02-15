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
    Valid: bool = False
    Solution = []
    Problem = []
    MaxColorOutput: int = None
    LaufzeitAusgabefärbung: int = None
    LaufzeitGenerateGraph: int = None
    NOC: int = None
    TotAdj: int = 0

@dataclass
class InputC:
    m: int = None
    d: int = None
    q: int = None
    OutputFile = []
    PrintGraph = False
    Solver = []
    Output_Yes = True
#This file contains all datastructs used in this project

from dataclasses import dataclass

#dataclasses for the neighborhood graph

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
    MaxColorOutput: int = None
    LaufzeitAusgabefärbung: int = None
    LaufzeitGenerateGraph: int = None
    NOC: int = None
    TotAdj: int = 0

#Input dataclass
@dataclass
class InputC:
    m: int = None
    d: int = None
    q: int = None
    OutputFile = []
    PrintGraph = False
    Solver = []
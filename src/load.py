import pyenzyme as pe

from zntrack import Node, zn

import os

class LoadEnzymeML(Node):

    # Inputs
    path: str = zn.params()
    
    # Outputs
    enzmldoc: pe.EnzymeMLDocument = zn.outs()
    
    def run(self):
        """Loads an EnzymeML document"""
        
        self.enzmldoc = pe.EnzymeMLDocument.fromFile(self.path)
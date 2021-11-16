"""
Tree-Building Parser for Tiny programming language.
Returns the root of the parse tree. No attempt to optimize tree.

Myles Klapkowski, November 2021
"""

from tiny_scanner import *
from pt_node import *
import sys

import pickle

class TinyParser:

    def __init__(self, sourcepath):
        self.__scanner = TinyScanner(sourcepath, verbose = True)

    def parse_program(self):
        """Parse tokens matching the following production:
        <program> -> <stmtseq>
        """
        self.__scanner.log("Parsing <program> -> <stmtseq>")
        c = self.parse_stmtseq()
        return PTNode("program", [c])
        
    def parse_stmtseq(self):
        """Parse tokens matching the following production:
        <stmtseq> -> <statement>
        """

        self.__scanner.log("Parsing <stmtseq> -> <statement>")

        c = self.parse_statement()
        children = [c]

        while self.__scanner.current.kind in {"ID", "READ", "WRITE", 
        "IF", "REPEAT", "UNTIL"}:
            children.append(self.parse_statement())

        return PTNode("stmtseq", children)
    
    def parse_statement(self):
        """ Parse tokens matching following production:
                <statement> -> 
                    <ifstmt>
                    |  <repeatstmt>
                    |  <assignstmt>
                    |  <readstmt>
                    |  <writestmt>
        """

        self.__scanner.log("Parsing <statement>"
                        "<ifstmt>  |  <repeatstmt>"
                        "|  <assignstmt> |  <readstmt>" 
                        "|  <writestmt>")
        
        if self.__scanner.current.kind == "ID":
            c = self.parse_assignstmt
        elif self.__scanner.current.kind == "IF":
            c = self.parse_ifstmt()
        elif self.__scanner.current.kind in {"REPEAT", "UNTIL"}:
            c = self.parse_repeatstmt()
        elif self.__scanner.current.kind == "READ":
            c = self.parse_readstmt()
        elif self.__scanner.current.kind == "WRITE":
            c = self.parse_writestmt()
        return PTNode("statement", [c])

    def parse_assignstmt(self):
        return

    def parse_ifstmt(self):
        return
    
    def parse_repeatstmt(self):
        return

    def parse_readstmt(self):
        return
    
    def parse_writestmt(self):
        return

    def parse_exp(self):
        return

    def parse_simple_expr(self):
        return

    def parse_comp_expr(self):
        return
    
    def parse_addop(self):
        return
    
    def parse_term(self):
        return
    
    def parse_mulop(self):
        return
    
    def parse_factor(self):
        retunr
    

if __name__ == "main":

    fpath = "dangle.tny"

    parser = TinyParser(fpath)

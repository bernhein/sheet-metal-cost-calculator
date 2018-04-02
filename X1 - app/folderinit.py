#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 21:56:27 2018

@author: cricket
"""

import os

class FolderInit:
    def __init__(self, folderlist):
        self.folderlist = folderlist
        self.valid = True
        
    def projectverification(self):
        for path in self.folderlist:
            if not os.path.exists(os.path.join(os.getcwd(), *path)):
                self.createfolders(path)
                self.valid = False
        return self
    
    def createfolders(self, path):
        for index, folder in enumerate(path):
            if not os.path.exists(os.path.join(os.getcwd(), *path[:index+1])):
                os.makedirs(os.path.join(os.getcwd(), *path[:index+1]))
                
                
            
    
if __name__ == "__main__":
    folderinit = FolderInit([('..', 'A1 - Estimate', ),
                             ('..', 'B1 - Reports', ),
                             ('..', 'C1 - Train', 'Dxf'),
                             ('..', 'C1 - Train', 'Targets'),
                             ])
    folderinit.projectverification()
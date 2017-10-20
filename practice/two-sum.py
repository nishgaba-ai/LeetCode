#!/usr/bin/env/python
import sys
import math
from sys import stdin, stdout
import argparse

class Solution(object):
    def twoSum(self,nums,target):
        seen={}   
        for i,num in enumerate(nums):
                 
           if(target-num) in seen:
                return [seen[target-num],i]
           seen[num] = i

"""testing calculations for math.py"""

import math
import friendly_computing_machine as fcm
import pytest

def test_add():
	assert fcm.add(2,3) == 5 
	assert fcm.add(1,2) == 3
	assert fcm.add(3,4) == 7

def test_mult():
	assert fcm.mult(3,5) == 15
	assert fcm.mult(1,2) == 2

def test_squre():
	assert fcm.square(3) == 9
	assert fcm.square(-3) == 9



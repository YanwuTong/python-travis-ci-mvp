import pytest

from temp import cToF, fToC

def test_cToF_10():
   assert cToF(10.0) == pytest.approx(50.0)
   
def test_cToF_20():
   assert cToF(20.0) == pytest.approx(68.0)
   
def test_fToC_32():
   assert fToC(32.0) == pytest.approx(0.0)
   
def test_fToC_212():
   assert fToC(212.0) == pytest.approx(100.0)
   
def test_fToC_n40():
   assert fToC(-40.0) == pytest.approx(-40.0)

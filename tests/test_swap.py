import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_sswap(lib)->bool:
    name="cblas_sswap"
    fn=getattr(lib,name)
    x=(c_float*1)(0.0)
    y=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,x,1,y,1],expects_return=False)

def test_dswap(lib)->bool:
    name="cblas_dswap"
    fn=getattr(lib,name)
    x=(c_double*1)(0.0)
    y=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,x,1,y,1],expects_return=False)

def run_tests(lib):
    ok=True
    ok&=test_sswap(lib)
    ok&=test_dswap(lib)
    return ok
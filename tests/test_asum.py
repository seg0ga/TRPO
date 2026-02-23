import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_sasum(lib)->bool:
    name="cblas_sasum"
    fn=getattr(lib,name)
    x=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,x,1],expects_return=True)

def test_dasum(lib)->bool:
    name="cblas_dasum"
    fn=getattr(lib,name)
    x=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,x,1], expects_return=True)

def run_tests(lib):
    ok=True
    ok&=test_sasum(lib)
    ok&=test_dasum(lib)
    return ok
import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_scopy(lib)->bool:
    name="cblas_scopy"
    fn=getattr(lib,name)
    x=(c_float*1)(0.0)
    y=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,x,1,y,1],expects_return=False)

def test_dcopy(lib)->bool:
    name="cblas_dcopy"
    fn= getattr(lib, name)
    x=(c_double*1)(0.0)
    y=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,x,1,y,1],expects_return=False)

def run_tests(lib):
    ok=True
    ok&=test_scopy(lib)
    ok&=test_dcopy(lib)
    return ok
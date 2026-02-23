import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_isamax(lib)->bool:
    name="cblas_isamax"
    fn=getattr(lib, name)
    x=(c_float*1)(0.0)
    return call_or_fail(name,fn,[1,x,1],expects_return=True)

def test_idamax(lib)->bool:
    name="cblas_idamax"
    fn=getattr(lib,name)
    x=(c_double*1)(0.0)
    return call_or_fail(name,fn,[1,x,1],expects_return=True)

def run_tests(lib):
    ok=True
    ok&=test_isamax(lib)
    ok&=test_idamax(lib)
    return ok
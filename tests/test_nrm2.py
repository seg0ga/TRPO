import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_snrm2(lib)->bool:
    name="cblas_snrm2"
    fn=getattr(lib, name)
    x=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,x,1],expects_return=True)

def test_dnrm2(lib)->bool:
    name="cblas_dnrm2"
    fn=getattr(lib,name)
    x=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,x,1],expects_return=True)

def run_tests(lib):
    ok=True
    ok&=test_snrm2(lib)
    ok&=test_dnrm2(lib)
    return ok
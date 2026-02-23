import ctypes
from ctypes import c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_ddot(lib)->bool:
    name="cblas_ddot"
    fn=getattr(lib,name)
    x=(c_double*1)(0.0)
    y=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,x,1,y,1],expects_return=True)

def run_tests(lib):return test_ddot(lib)
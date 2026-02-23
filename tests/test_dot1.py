import ctypes
from ctypes import c_float
from .test_utils import call_or_fail, PASS, FAIL

def test_sdot(lib)->bool:
    name="cblas_sdot"
    fn=getattr(lib, name)
    x=(c_float*1)(0.0)
    y=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,x,1,y,1],expects_return=True)

def run_tests(lib):return test_sdot(lib)
import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_saxpy(lib)->bool:
    name="cblas_saxpy"
    fn=getattr(lib, name)
    x=(c_float*1)(0.0)
    y=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,c_float(1.0),x,1,y,1],expects_return=False)

def test_daxpy(lib)->bool:
    name="cblas_daxpy"
    fn= getattr(lib, name)
    x=(c_double*1)(0.0)
    y=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,c_double(1.0),x,1,y,1],expects_return=False)

def run_tests(lib):
    ok=True
    ok&=test_saxpy(lib)
    ok&=test_daxpy(lib)
    return ok
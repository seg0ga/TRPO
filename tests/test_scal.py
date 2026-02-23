import ctypes
from ctypes import c_float, c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_sscal(lib)->bool:
    name="cblas_sscal"
    fn=getattr(lib,name)
    x=(c_float*1)(0.0)
    return call_or_fail(name,fn,[0,c_float(2.0),x,1],expects_return=False)

def test_dscal(lib)->bool:
    name="cblas_dscal"
    fn=getattr(lib,name)
    x=(c_double*1)(0.0)
    return call_or_fail(name,fn,[0,c_double(2.0),x,1],expects_return=False)

def run_tests(lib):
    ok=True
    ok&=test_sscal(lib)
    ok&=test_dscal(lib)
    return ok
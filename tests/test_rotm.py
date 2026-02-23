import ctypes
from ctypes import c_float
from .test_utils import call_or_fail, PASS, FAIL

def test_srotm(lib)->bool:
    name="cblas_srotm"
    try:
        fn=getattr(lib,name)
        x=(c_float*1)(0.0)
        y=(c_float*1)(0.0)
        param=(c_float*5)(0.0,0.0,0.0,0.0,0.0)
        return call_or_fail(name,fn,[0,x,1,y,1,param],expects_return=False)
    except AttributeError:
        FAIL(f"{name}: функция не найдена")
        return False

def run_tests(lib):return test_srotm(lib)
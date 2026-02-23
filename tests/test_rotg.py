import ctypes
from ctypes import c_float, POINTER
from .test_utils import call_or_fail, PASS, FAIL

def test_srotg(lib)->bool:
    name="cblas_srotg"
    try:
        fn=getattr(lib,name)
        a=(c_float*1)(1.0)
        b=(c_float*1)(1.0)
        c=(c_float*1)(0.0)
        s=(c_float*1)(0.0)
        return call_or_fail(name,fn,[a,b,c,s],expects_return=False)
    except AttributeError:
        FAIL(f"{name}: функция не найдена")
        return False

def run_tests(lib):return test_srotg(lib)
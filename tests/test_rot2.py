import ctypes
from ctypes import c_double
from .test_utils import call_or_fail, PASS, FAIL

def test_drot(lib)->bool:
    name="cblas_drot"
    try:
        fn=getattr(lib,name)
        x=(c_double*1)(0.0)
        y=(c_double*1)(0.0)
        c=c_double(0.0)
        s=c_double(1.0)
        return call_or_fail(name,fn,[0,x,1,y,1,c,s],expects_return=False)
    except AttributeError:
        FAIL(f"{name}: функция не найдена")
        return False

def run_tests(lib):return test_drot(lib)
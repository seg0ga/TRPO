import ctypes
from ctypes import c_float, POINTER
from .test_utils import call_or_fail, PASS, FAIL

def test_srotmg(lib)->bool:
    name="cblas_srotmg"
    try:
        fn=getattr(lib,name)
        d1=(c_float*1)(1.0)
        d2=(c_float*1)(1.0)
        x1=(c_float*1)(1.0)
        y1=c_float(1.0)
        param=(c_float*5)(0.0,0.0,0.0,0.0,0.0)
        return call_or_fail(name,fn,[d1,d2,x1,y1,param],expects_return=False)
    except AttributeError:
        FAIL(f"{name}: функция не найдена")
        return False

def run_tests(lib):return test_srotmg(lib)
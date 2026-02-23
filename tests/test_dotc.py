import ctypes
from ctypes import c_float, POINTER
from .test_utils import call_or_fail, PASS, FAIL

class complex_float(ctypes.Structure):
    _fields_=[("real",c_float),("imag",c_float)]


def test_cdotc(lib)->bool:
    name="cblas_cdotc_sub"
    try:
        fn=getattr(lib,name)
        x=(complex_float*1)()
        x[0].real=1.0
        x[0].imag=2.0
        y=(complex_float*1)()
        y[0].real=3.0
        y[0].imag=4.0
        result=complex_float()
        fn(1,x,1,y,1,ctypes.byref(result))

        if abs(result.real-11.0)<0.0001 and abs(result.imag-(-2.0))<0.0001:
            PASS(f"{name}: call OK")
            return True
        else:
            FAIL(f"{name}: ERROR")
            return False

    except AttributeError:
        FAIL(f"{name}: функция не найдена")
        return False
    except Exception as e:
        FAIL(f"{name}: ошибка - {e}")
        return False

def run_tests(lib):return test_cdotc(lib)
def PASS(msg):print(f"[PASS] {msg}")

def FAIL(msg):print(f"[FAIL] {msg}")

def call_or_fail(name:str,fn,args,expects_return:bool)->bool:
    try:
        r=fn(*args)
        if expects_return:PASS(f"{name}: call OK (return={r})")
        else:PASS(f"{name}: call OK")
        return True
    except Exception as e:
        FAIL(f"{name}: call ERROR -> {type(e).__name__}: {e}")
        return False
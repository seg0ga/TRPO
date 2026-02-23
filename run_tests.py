import ctypes, importlib, sys
from pathlib import Path

lib=ctypes.CDLL("/usr/lib/x86_64-linux-gnu/libopenblas.so")
tests=[f.stem for f in Path("tests").glob("test_*.py") if f.stem != 'test_utils']

def run(t):
    try:
        m=importlib.import_module(f'tests.{t}')
        return m.run_tests(lib) if hasattr(m, 'run_tests') else False
    except: return False

def main():
    results={t:run(t) for t in tests}
    print("\n\nТЕСТЫ\n")

    failed=[t for t, p in results.items() if not p]
    for t,p in results.items():print(f"{'✅' if p else '❌'} {t}")

    if not failed:print("\n✅ Все тесты пройдены успешно!")
    else: print(f"\n❌ Ошибка: {', '.join(failed)}")
    return 0 if not failed else 1

if __name__ == "__main__":
    exit(main())
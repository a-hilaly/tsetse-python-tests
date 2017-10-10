#
class SkipTest(Exception):
    pass

class TestFail(Exception):
    pass

class SkipModule(Exception):
    pass

class Fatal(Exception):
    pass



SUCCEEDED_TEST = "[ OK ] ... {0} succeeded with a total run time of : {1} [seconds]"
FAILED_TEST = "[FAIL] ... {0} failed after runing : {1} [seconds]"
SKIPPED_TEST = "[SKIP] ... {0} Skipped by controll"


SKIPPED_MODULE = "[SKIP] ... Skipped module {0}"
IMPORTED_MODULE = "[IMPR] ... Imported module {0}"


def test_function(func, verbose=False):
    t1 = time.time()
    try:
        es, t2 = func(), time.time()
        if verbose:
            print(SUCCEEDED_TEST.format(func.__name__, t2 - t1))
        return True
    except SkipTest:
        if verbose:
            print(SKIPPED_TEST.format(func.__name__))
    except:
        t2 = time.time()
        if verbose:
            print(FAILED_TEST.format(func.__name__, t2 - t1))
        return False


def import_module_tests_functions(module):
    try:
        mod = __import__(module, globals(), locals(), [''])
        functions = getattr(mod, '__all__')
        print(IMPORTED_MODULE.format(module))
        return functions
    except SkipModule:
        print(SKIPPED_MODULE.format(module))
        return -1
    except:
        return -2


def run_pytests_modules(*test_modules):
    tfunction, tsuccess, c = 0, 0, None
    t1 = time.time()
    for module in test_modules:
        functions = import_module_tests_functions(module)
        print("[INFO] ... Runing {0} tests : [{1} functions]".format(module, len(functions)))
        if not functions:
            print("       ====> Skipped [NO FUNCTIONS]")
            print("")
            continue
        k1 = time.time()
        for func in functions:
            c = _test_function(func)
            tfunction += 1
            if c:
                tsuccess += 1
        k2 = time.time()
        print("        ====> Module tests total run time : {0} ms".format(k2 - k1))
        print("        ====> end module test")
        print("")
    t2 = time.time()
    sr = tsuccess/tfunction * 100
    print('[INFO] ... --- end test ---')
    print('       ====> Total runtime : {0} ms'.format(t2 - t1))
    print('       ====> Success rate : {0}  [ {1}/{2} ]'.format(sr, tsuccess, tfunction))
    # proc test error (for CI)
    if sr < 100:
        raise TestFail()


def run_all_tests():
    run_pytests_modules(*test_modules)

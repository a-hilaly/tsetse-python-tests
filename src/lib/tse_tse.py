#
class SkipTest(Exception):
    pass

class TestFail(Exception):
    pass

class ReportTest(Exception):
    pass

class SkipModule(Exception):
    pass




SUCCEEDED_TEST = "[ OK ] ... {0} succeeded ES:{1} with a total run time of : {2} ms"
FAILED_TEST = "[WARN] ... {0} failed after runing : {1} ms"
SKIPPED_TEST = "[SKIP] ... {0} Skipped before running ES:{1} [ {2} ]"



test_modules = []

def parse_tests():
    pass


def test_function(func):
    t1 = time.time()
    try:
        es, t2 = func(), time.time()
        print(SUCCEEDED_TEST.format(func.__name__, es, t2 - t1))
        return True
    except SkipTest:
        pass
    except SkipTest:
        pass
    except:
        t2 = time.time()
        print(FAILED_TEST.format(func.__name__, t2 - t1))
        return False


def import_module_tests_functions(module):
    mod = __import__(module, globals(), locals(), [''])
    functions = getattr(mod, '__all__')         #XXX: Python need this usless arguments
    return functions                            # to import all objects in a module


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

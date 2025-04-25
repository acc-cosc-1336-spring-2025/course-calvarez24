import unittest


from tests.examples.f_files_exception import tests_files_exception

suite = unittest.TestLoader().loadTestsFromModule(tests_files_exception)
unittest.TextTestRunner(verbosity=2).run(suite)  

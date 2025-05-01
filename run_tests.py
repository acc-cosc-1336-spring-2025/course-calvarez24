import unittest


from tests.examples.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)  

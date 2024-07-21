import unittest
from mainpkg.sub.module_zzz import module_zzz

class super_test(unittest.TestCase):
    def setUp(self):
        self.module = module_zzz()
    
    def test_func(self):
        expected = 'Hello, world!'  
        actual = self.module.func()
        self.assertEqual (expected, actual)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
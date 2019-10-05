import unittest, unittest.mock
import sys, logging
sys.path.insert(0,'../..')
import LTspyce.core.sim as LTS_sim

class TestSim(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('os.path.isfile')
    def test_constructorSuccess(self, os_path_isfile):
        os_path_isfile.return_value = True
        test_sim = LTS_sim.Sim('Test.asc');
        os_path_isfile.assert_called_once_with('Test.asc')
        self.assertEqual('Test.asc',test_sim.getPath())

    @unittest.mock.patch('os.path.isfile')
    def test_constructorFail(self, os_path_isfile):
        os_path_isfile.return_value = False
        with self.assertRaises(FileNotFoundError):
            test_sim = LTS_sim.Sim('Test.asc');
            os_path_isfile.assert_called_once_with('Test.asc')

        
if __name__ == '__main__':
    unittest.main()




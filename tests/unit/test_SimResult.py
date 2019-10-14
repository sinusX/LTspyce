import unittest, unittest.mock
import sys
import logging

sys.path.insert(0, '../..')
import LTspyce.core.SimResults as SimRes


# constructor Test
class TestSimResults_Constructor(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    @unittest.mock.patch('os.path.isfile')
    def test_constructorSuccess(self, os_path_isfile):
        os_path_isfile.return_value = True
        testObj = SimRes.SimResult('Test.raw')
        os_path_isfile.assert_called_once_with('Test.raw')
        self.assertEqual('Test.raw', testObj.getPath())

    @unittest.mock.patch('os.path.isfile')
    def test_constructorFail(self, os_path_isfile):
        os_path_isfile.return_value = False
        with self.assertRaises(FileNotFoundError):
            testObj = SimRes.SimResult('Test.raw')
            os_path_isfile.assert_called_once_with('Test.raw')


# readMetaData Tests
class TestSimResults_readMetaData(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_readMetaDataSuccess(self):
        testObj = SimRes.SimResult('res/Test.raw')
        testObj.readMetadata()
        self.assertEqual(6,testObj.getNoVars())
        self.assertEqual(1101,testObj.getNoPoints())
        self.assertEqual('Sat Oct 05 22:56:39 2019',testObj.getSimDate())

    def test_invalidMetaData(self):
        testObj = SimRes.SimResult('res/TestINvalidMeta.raw')
        with self.assertRaises(ValueError):
            testObj.readMetadata()


    # TODO cannot open file
    # TODO decode line failed


# TODO read getNoVars before available
# TODO read getNoPoints before available
# TODO read getSimDate before available


if __name__ == '__main__':
    unittest.main()
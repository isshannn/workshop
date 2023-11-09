import unittest
import control_flow_01
import sys

class LearnUnitTest(unittest.TestCase):
    def test_check_operator_input(self): 
        # Check for Invalid decimal Input
        result = control_flow_01.check_operator_input(10)
        self.assertIsNone(result)
        # Check Valid Input(between 1 and 4)
        valid_input = 4
        result = control_flow_01.check_operator_input(valid_input)
        self.assertEqual(result,valid_input)
        # Check for String Test
        result= control_flow_01.check_operator_input("Hello")
        self.assertIsNone(result)
        # Check for Floating Value
        result = control_flow_01.check_operator_input(1.43)
        self.assertIsNone(result)
        # Check for NULL Input
        result = control_flow_01.check_operator_input(None)
        self.assertIsNone(result)

    def test_check_operand_input(self):
        #Check for Strings    
        result = control_flow_01.check_operand_input("Hello")
        self.assertIsNone(result)
        #Check for Integers
        valid_input = 10
        result = control_flow_01.check_operand_input(valid_input)
        self.assertEqual(result,valid_input)
        #Check for Floating point
        valid_float_input = 1.0
        result = control_flow_01.check_operand_input(valid_float_input)
        self.assertEqual(result,valid_float_input)
        #Check for Bounds (Limits of computation)
        result1 = control_flow_01.check_operand_input(sys.float_info.max)
        result2 = control_flow_01.check_operand_input(sys.float_info.min)
        self.assertIsNone(result1)
        self.assertIsNone(result2)
        #Check for NULL input
        result = control_flow_01.check_operand_input(None)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()

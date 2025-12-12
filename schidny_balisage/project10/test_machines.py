#!/usr/bin/env python3
"""
Test suite for Turing Machine Simulator
Validates all three machines with comprehensive test cases
"""

from turing_machine import TuringMachineLibrary


def test_machine(machine, machine_name, test_cases):
    """Test a machine with given test cases"""
    print(f"\n{'=' * 80}")
    print(f"Testing: {machine_name}")
    print('=' * 80)
    
    total = 0
    passed = 0
    
    for test_input, expected_accept in test_cases:
        total += 1
        accepted, _, _ = machine.run(test_input)
        
        status = "✓ PASS" if accepted == expected_accept else "✗ FAIL"
        display_input = f"'{test_input}'" if test_input else "ε"
        expected = "ACCEPT" if expected_accept else "REJECT"
        actual = "ACCEPT" if accepted else "REJECT"
        
        print(f"  {display_input:15} Expected: {expected:8} Got: {actual:8} {status}")
        
        if accepted == expected_accept:
            passed += 1
    
    print(f"\n  Result: {passed}/{total} tests passed")
    return passed, total


def main():
    """Run all tests"""
    print("=" * 80)
    print(" " * 25 + "TURING MACHINE TEST SUITE")
    print("=" * 80)
    
    machines = TuringMachineLibrary.get_all_machines()
    
    test_suites = {
        'binary_palindrome': [
            ('', True),
            ('0', True),
            ('1', True),
            ('00', True),
            ('11', True),
            ('01', False),
            ('10', False),
            ('010', True),
            ('101', True),
            ('001', False),
            ('110', False),
            ('0110', True),
            ('1001', True),
            ('0101', False),
            ('1100', False),
            ('11011', True),
        ],
        'balanced_parentheses': [
            ('', True),
            ('()', True),
            ('(())', True),
            ('()()', True),
            ('((()))', True),
            ('(()())', True),
            ('(', False),
            (')', False),
            ('(()', False),
            ('())', False),
            (')(', False),
            ('(()()', False),
        ],
        'a_n_b_n': [
            ('', True),
            ('ab', True),
            ('aabb', True),
            ('aaabbb', True),
            ('aaaabbbb', True),
            ('a', False),
            ('b', False),
            ('ba', False),
            ('aab', False),
            ('abb', False),
            ('aaabb', False),
            ('aabbb', False),
        ]
    }
    
    machine_names = {
        'binary_palindrome': 'Binary Palindrome Checker',
        'balanced_parentheses': 'Balanced Parentheses Checker',
        'a_n_b_n': 'a^n b^n Checker'
    }
    
    total_passed = 0
    total_tests = 0
    
    for machine_key, test_cases in test_suites.items():
        machine = machines[machine_key]
        machine_name = machine_names[machine_key]
        passed, total = test_machine(machine, machine_name, test_cases)
        total_passed += passed
        total_tests += total
    
    print("\n" + "=" * 80)
    print(f"OVERALL RESULTS: {total_passed}/{total_tests} tests passed")
    if total_passed == total_tests:
        print("🎉 ALL TESTS PASSED! 🎉")
    else:
        print(f"⚠️  {total_tests - total_passed} test(s) failed")
    print("=" * 80)
    print()
    
    return total_passed == total_tests


if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)

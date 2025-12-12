#!/usr/bin/env python3
"""
Command-line interface for Turing Machine Simulator
"""

import sys
from turing_machine import TuringMachineLibrary


def print_banner():
    """Print welcome banner"""
    print("=" * 80)
    print(" " * 25 + "TURING MACHINE SIMULATOR")
    print("=" * 80)
    print()


def print_menu():
    """Print machine selection menu"""
    print("Available Turing Machines:")
    print()
    print("1. Binary Palindrome Checker")
    print("   Language: {w | w ∈ {0,1}* and w = w^R}")
    print("   Examples: ε, 0, 1, 00, 11, 010, 101")
    print()
    print("2. Balanced Parentheses Checker")
    print("   Language: {w | w has balanced parentheses}")
    print("   Examples: ε, (), (()), ()(), (()())")
    print()
    print("3. a^n b^n Checker")
    print("   Language: {a^n b^n | n ≥ 0}")
    print("   Examples: ε, ab, aabb, aaabbb")
    print()
    print("4. Run all example tests")
    print("5. Exit")
    print()


def get_machine_choice():
    """Get user's machine selection"""
    while True:
        try:
            choice = input("Select a machine (1-5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            sys.exit(0)


def get_input_string():
    """Get input string from user"""
    print()
    print("Enter input string (press Enter for empty string ε):")
    try:
        return input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")
        sys.exit(0)


def run_machine(machine, input_string, machine_name):
    """Run machine and display results"""
    print()
    print("=" * 80)
    print(f"Running: {machine_name}")
    print(f"Input: '{input_string}' " + ("(empty string ε)" if not input_string else ""))
    print("=" * 80)
    print()
    
    # Run the machine
    accepted, trace, final_tape = machine.run(input_string)
    
    # Print trace
    print(machine.get_trace_summary())
    
    # Print result
    print()
    if accepted:
        print("🎉 RESULT: ACCEPTED ✓")
    else:
        print("❌ RESULT: REJECTED ✗")
    print()
    print(f"Final tape: {final_tape}")
    print(f"Total steps: {len(trace) - 1}")
    print("=" * 80)


def run_all_tests():
    """Run comprehensive test suite"""
    print()
    print("=" * 80)
    print(" " * 25 + "RUNNING ALL TESTS")
    print("=" * 80)
    print()
    
    machines = TuringMachineLibrary.get_all_machines()
    
    test_cases = {
        "binary_palindrome": {
            "name": "Binary Palindrome Checker",
            "accept": ["", "0", "1", "00", "11", "010", "101"],
            "reject": ["01", "10", "001", "110"]
        },
        "balanced_parentheses": {
            "name": "Balanced Parentheses Checker",
            "accept": ["", "()", "(())", "()()"],
            "reject": ["(", ")", "(()", "())"]
        },
        "a_n_b_n": {
            "name": "a^n b^n Checker",
            "accept": ["", "ab", "aabb", "aaabbb"],
            "reject": ["a", "b", "ba", "aab"]
        }
    }
    
    total_tests = 0
    passed_tests = 0
    
    for machine_key, test_data in test_cases.items():
        print(f"\nTesting: {test_data['name']}")
        print('=' * 80)
        
        machine = machines[machine_key]
        
        print("\nAccept cases:")
        for test_input in test_data['accept']:
            total_tests += 1
            accepted, _, _ = machine.run(test_input)
            status = "✓ PASS" if accepted else "✗ FAIL"
            display_input = f"'{test_input}'" if test_input else "ε"
            print(f"  {display_input:20} -> {status}")
            if accepted:
                passed_tests += 1
        
        print("\nReject cases:")
        for test_input in test_data['reject']:
            total_tests += 1
            accepted, _, _ = machine.run(test_input)
            status = "✓ PASS" if not accepted else "✗ FAIL"
            print(f"  '{test_input}':20 -> {status}")
            if not accepted:
                passed_tests += 1
    
    print()
    print("=" * 80)
    print(f"TEST SUMMARY: {passed_tests}/{total_tests} tests passed")
    print("=" * 80)
    print()


def main():
    """Main CLI loop"""
    print_banner()
    
    machines = TuringMachineLibrary.get_all_machines()
    machine_map = {
        '1': ('binary_palindrome', 'Binary Palindrome Checker'),
        '2': ('balanced_parentheses', 'Balanced Parentheses Checker'),
        '3': ('a_n_b_n', 'a^n b^n Checker')
    }
    
    while True:
        print_menu()
        choice = get_machine_choice()
        
        if choice == '5':
            print("\nThank you for using the Turing Machine Simulator!")
            sys.exit(0)
        
        if choice == '4':
            run_all_tests()
            input("\nPress Enter to continue...")
            continue
        
        machine_key, machine_name = machine_map[choice]
        machine = machines[machine_key]
        
        while True:
            input_string = get_input_string()
            run_machine(machine, input_string, machine_name)
            
            print()
            again = input("Test another string with this machine? (y/n): ").strip().lower()
            if again != 'y':
                break
        
        print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)

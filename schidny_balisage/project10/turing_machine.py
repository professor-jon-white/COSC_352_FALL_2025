"""
Turing Machine Simulator
A comprehensive implementation of a Turing Machine with configurable states,
transitions, and tape operations.
"""

from enum import Enum


class Direction(Enum):
    """Tape head movement directions"""
    LEFT = "L"
    RIGHT = "R"
    STAY = "S"


class TuringMachine:
    """
    A configurable Turing Machine simulator.
    """
    
    def __init__(self, states, input_alphabet, tape_alphabet, transitions,
                 start_state, accept_state, reject_state, blank_symbol="_"):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol
        
        # Execution tracking
        self.current_state = start_state
        self.tape = []
        self.head_position = 0
        self.execution_trace = []
        self.step_count = 0
        self.max_steps = 10000
        
    def initialize_tape(self, input_string):
        """Initialize the tape with input string"""
        self.tape = list(input_string) if input_string else [self.blank_symbol]
        self.head_position = 0
        self.current_state = self.start_state
        self.execution_trace = []
        self.step_count = 0
        self._record_state()
    
    def _record_state(self):
        """Record current machine configuration for trace"""
        tape_str = ''.join(self.tape)
        config = {
            'step': self.step_count,
            'state': self.current_state,
            'tape': tape_str,
            'head_position': self.head_position,
            'current_symbol': self.tape[self.head_position] if 0 <= self.head_position < len(self.tape) else self.blank_symbol
        }
        self.execution_trace.append(config)
    
    def _extend_tape_if_needed(self):
        """Extend tape with blank symbols if head moves beyond current bounds"""
        if self.head_position < 0:
            self.tape.insert(0, self.blank_symbol)
            self.head_position = 0
        elif self.head_position >= len(self.tape):
            self.tape.append(self.blank_symbol)
    
    def step(self):
        """Execute one step of the Turing Machine."""
        if self.current_state in [self.accept_state, self.reject_state]:
            return False
        
        if self.step_count >= self.max_steps:
            self.current_state = self.reject_state
            self._record_state()
            return False
        
        self._extend_tape_if_needed()
        current_symbol = self.tape[self.head_position]
        
        transition_key = (self.current_state, current_symbol)
        
        if transition_key not in self.transitions:
            self.current_state = self.reject_state
            self._record_state()
            return False
        
        new_state, write_symbol, direction = self.transitions[transition_key]
        
        self.tape[self.head_position] = write_symbol
        
        if direction == Direction.LEFT:
            self.head_position -= 1
        elif direction == Direction.RIGHT:
            self.head_position += 1
        
        self.current_state = new_state
        self.step_count += 1
        self._record_state()
        
        return True
    
    def run(self, input_string):
        """Run the Turing Machine on input string."""
        self.initialize_tape(input_string)
        
        while self.step():
            pass
        
        accepted = self.current_state == self.accept_state
        final_tape = ''.join(self.tape)
        
        return accepted, self.execution_trace, final_tape
    
    def get_trace_summary(self):
        """Generate a human-readable trace summary"""
        lines = []
        lines.append("=" * 80)
        lines.append("TURING MACHINE EXECUTION TRACE")
        lines.append("=" * 80)
        
        for config in self.execution_trace:
            step = config['step']
            state = config['state']
            tape = config['tape']
            pos = config['head_position']
            symbol = config['current_symbol']
            
            pointer = ' ' * pos + '^'
            
            lines.append(f"\nStep {step}: State = {state}, Symbol = '{symbol}'")
            lines.append(f"Tape: {tape}")
            lines.append(f"      {pointer}")
        
        lines.append("\n" + "=" * 80)
        final_state = self.execution_trace[-1]['state'] if self.execution_trace else "NONE"
        lines.append(f"FINAL STATE: {final_state}")
        lines.append(f"TOTAL STEPS: {self.step_count}")
        lines.append("=" * 80)
        
        return '\n'.join(lines)


class TuringMachineLibrary:
    """Library of pre-configured Turing Machines for common languages"""
    
    @staticmethod
    def binary_palindrome_checker():
        """Turing Machine that accepts binary palindromes."""
        states = {"q0", "q1", "q2", "q3", "q4", "q5", "q_accept", "q_reject"}
        input_alphabet = {"0", "1"}
        tape_alphabet = {"0", "1", "X", "_"}
        blank = "_"
        
        transitions = {
            ("q0", "0"): ("q1", "X", Direction.RIGHT),
            ("q0", "1"): ("q2", "X", Direction.RIGHT),
            ("q0", "X"): ("q0", "X", Direction.RIGHT),
            ("q0", "_"): ("q_accept", "_", Direction.STAY),
            
            ("q1", "0"): ("q1", "0", Direction.RIGHT),
            ("q1", "1"): ("q1", "1", Direction.RIGHT),
            ("q1", "X"): ("q1", "X", Direction.RIGHT),
            ("q1", "_"): ("q3", "_", Direction.LEFT),
            
            ("q2", "0"): ("q2", "0", Direction.RIGHT),
            ("q2", "1"): ("q2", "1", Direction.RIGHT),
            ("q2", "X"): ("q2", "X", Direction.RIGHT),
            ("q2", "_"): ("q4", "_", Direction.LEFT),
            
            ("q3", "0"): ("q5", "X", Direction.LEFT),
            ("q3", "1"): ("q_reject", "1", Direction.STAY),
            ("q3", "X"): ("q_accept", "X", Direction.STAY),
            
            ("q4", "1"): ("q5", "X", Direction.LEFT),
            ("q4", "0"): ("q_reject", "0", Direction.STAY),
            ("q4", "X"): ("q_accept", "X", Direction.STAY),
            
            ("q5", "0"): ("q5", "0", Direction.LEFT),
            ("q5", "1"): ("q5", "1", Direction.LEFT),
            ("q5", "X"): ("q5", "X", Direction.LEFT),
            ("q5", "_"): ("q0", "_", Direction.RIGHT),
        }
        
        return TuringMachine(states, input_alphabet, tape_alphabet, transitions,
                           "q0", "q_accept", "q_reject", blank)
    
    @staticmethod
    def balanced_parentheses_checker():
        """Turing Machine that accepts strings with balanced parentheses."""
        states = {"q0", "q1", "q2", "q3", "q_accept", "q_reject"}
        input_alphabet = {"(", ")"}
        tape_alphabet = {"(", ")", "X", "Y", "_"}
        blank = "_"
        
        transitions = {
            ("q0", "("): ("q1", "X", Direction.RIGHT),
            ("q0", "X"): ("q0", "X", Direction.RIGHT),
            ("q0", "Y"): ("q0", "Y", Direction.RIGHT),
            ("q0", ")"): ("q_reject", ")", Direction.STAY),
            ("q0", "_"): ("q_accept", "_", Direction.STAY),
            
            ("q1", "("): ("q1", "(", Direction.RIGHT),
            ("q1", ")"): ("q2", "Y", Direction.LEFT),
            ("q1", "X"): ("q1", "X", Direction.RIGHT),
            ("q1", "Y"): ("q1", "Y", Direction.RIGHT),
            ("q1", "_"): ("q_reject", "_", Direction.STAY),
            
            ("q2", "("): ("q2", "(", Direction.LEFT),
            ("q2", ")"): ("q2", ")", Direction.LEFT),
            ("q2", "X"): ("q2", "X", Direction.LEFT),
            ("q2", "Y"): ("q2", "Y", Direction.LEFT),
            ("q2", "_"): ("q3", "_", Direction.RIGHT),
            
            ("q3", "X"): ("q3", "X", Direction.RIGHT),
            ("q3", "Y"): ("q3", "Y", Direction.RIGHT),
            ("q3", "("): ("q0", "(", Direction.STAY),
            ("q3", "_"): ("q_accept", "_", Direction.STAY),
            ("q3", ")"): ("q_reject", ")", Direction.STAY),
        }
        
        return TuringMachine(states, input_alphabet, tape_alphabet, transitions,
                           "q0", "q_accept", "q_reject", blank)
    
    @staticmethod
    def a_n_b_n_checker():
        """Turing Machine that accepts strings of form a^n b^n."""
        states = {"q0", "q1", "q2", "q3", "q_accept", "q_reject"}
        input_alphabet = {"a", "b"}
        tape_alphabet = {"a", "b", "X", "Y", "_"}
        blank = "_"
        
        transitions = {
            ("q0", "a"): ("q1", "X", Direction.RIGHT),
            ("q0", "Y"): ("q0", "Y", Direction.RIGHT),
            ("q0", "_"): ("q_accept", "_", Direction.STAY),
            ("q0", "b"): ("q_reject", "b", Direction.STAY),
            
            ("q1", "a"): ("q1", "a", Direction.RIGHT),
            ("q1", "Y"): ("q1", "Y", Direction.RIGHT),
            ("q1", "b"): ("q2", "Y", Direction.LEFT),
            ("q1", "_"): ("q_reject", "_", Direction.STAY),
            
            ("q2", "a"): ("q2", "a", Direction.LEFT),
            ("q2", "X"): ("q2", "X", Direction.LEFT),
            ("q2", "Y"): ("q2", "Y", Direction.LEFT),
            ("q2", "_"): ("q3", "_", Direction.RIGHT),
            
            ("q3", "X"): ("q3", "X", Direction.RIGHT),
            ("q3", "Y"): ("q3", "Y", Direction.RIGHT),
            ("q3", "_"): ("q_accept", "_", Direction.STAY),
            ("q3", "a"): ("q0", "a", Direction.STAY),
            ("q3", "b"): ("q_reject", "b", Direction.STAY),
        }
        
        return TuringMachine(states, input_alphabet, tape_alphabet, transitions,
                           "q0", "q_accept", "q_reject", blank)

    @staticmethod
    def get_all_machines():
        """Get all pre-configured machines"""
        return {
            "binary_palindrome": TuringMachineLibrary.binary_palindrome_checker(),
            "balanced_parentheses": TuringMachineLibrary.balanced_parentheses_checker(),
            "a_n_b_n": TuringMachineLibrary.a_n_b_n_checker()
        }

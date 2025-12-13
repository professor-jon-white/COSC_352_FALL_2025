# Turing Machine Simulator for a^n b^n c^n

## Overview
This project implements a Turing Machine (TM) simulator in Python that recognizes the language **a^n b^n c^n** where **n ≥ 1**. This is a classic example of a context-sensitive language, requiring a TM with marking and backtracking logic, making it more complex than simulators for regular or context-free languages.

The program is CLI-based, takes an input string, simulates the TM step-by-step, prints the state trace, and evaluates whether the input is accepted (pass) or rejected (fail). It is dockerized for easy deployment.

## Complexity
The language a^n b^n c^n is **context-sensitive** and cannot be recognized by a pushdown automaton (context-free). This demonstrates the computational power of Turing Machines beyond traditional finite automata. The TM implementation features:
- **6 states**: q0 (start), q1 (after backtrack), q2 (find/mark b), q3 (find/mark c), q4 (backtrack left), q5 (accept)
- **~18 transitions**: Handles marking, skipping marked symbols, and detecting mismatches
- **Time Complexity**: O(n²) due to multiple passes over the tape
- **Space Complexity**: O(n) tape cells with dynamic extension

## Approach

### Turing Machine Design
The TM uses a single tape and marks symbols to count and match occurrences:
- **Marking Strategy**: 'a' → 'X', 'b' → 'Y', 'c' → 'Z'
- **Algorithm**:
  1. Mark the first `a` with `X`
  2. Scan right to find and mark the first `b` with `Y`
  3. Continue right to find and mark the first `c` with `Z`
  4. Return to the beginning (state q4 → q1) and repeat
  5. Accept if only marked symbols remain; reject if mismatch detected

### State Diagram
- **q0**: Initial state - mark first `a`
- **q1**: After backtracking, check if done or continue marking
- **q2**: Find and mark first unmarked `b`
- **q3**: Find and mark first unmarked `c`
- **q4**: Backtrack to beginning
- **q5**: Accept state (all symbols matched)
- **q_reject**: Reject state (no valid transition)

### Transition Table
```
(q0, a) → (q2, X, R)  # Mark first a
(q1, a) → (q2, X, R)  # Mark next a
(q1, X) → (q1, X, R)  # Skip marked X's
(q1, Y) → (q1, Y, R)  # Skip marked Y's
(q1, Z) → (q1, Z, R)  # Skip marked Z's
(q1, ' ') → (q5, ' ', N)  # All marked - accept!
(q2, a) → (q2, a, R)  # Skip unmarked a's
(q2, Y) → (q2, Y, R)  # Skip marked Y's
(q2, Z) → (q2, Z, R)  # Skip marked Z's
(q2, b) → (q3, Y, R)  # Found b - mark it
(q3, b) → (q3, b, R)  # Skip unmarked b's
(q3, Z) → (q3, Z, R)  # Skip marked Z's
(q3, c) → (q4, Z, L)  # Found c - mark and return
(q4, a) → (q4, a, L)  # Move left
(q4, b) → (q4, b, L)  # Move left
(q4, Y) → (q4, Y, L)  # Move left
(q4, Z) → (q4, Z, L)  # Move left
(q4, X) → (q1, X, R)  # Back at marked area - continue
```

### Simulator Implementation
- Adapted from standard Python TM templates
- **Tape**: Dynamic list that extends infinitely in both directions using blanks (' ')
- **Tracing**: Prints state, tape contents, and head position at each step
- **Safety**: Max steps limit (10,000) prevents infinite loops
- **Evaluation**: Accepts if reaches q5; rejects if no transition exists or max steps exceeded

## Requirements
- Docker installed on your machine
- Git (for cloning from GitHub)

## Run Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/project10.git
cd project10
```

### 2. Build the Docker Image
```bash
docker build -t turing-machine .
```

### 3. Run the Simulator
Pass your input string as a command-line argument:

#### Accepting Inputs (Pass)
```bash
# n=1: abc
docker run --rm turing-machine abc

# n=2: aabbcc
docker run --rm turing-machine aabbcc

# n=3: aaabbbccc
docker run --rm turing-machine aaabbbccc
```

#### Rejecting Inputs (Fail)
```bash
# Unequal counts
docker run --rm turing-machine aabbc

# Wrong order
docker run --rm turing-machine abcabc

# Missing symbol
docker run --rm turing-machine aabb
```

## Example Output

### Input: `abc` (Should Accept - n=1)
```
State: q0
Tape: abc
Head: ^
----------------------------------------
State: q2
Tape: Xbc
Head:  ^
----------------------------------------
State: q3
Tape: XYc
Head:   ^
----------------------------------------
State: q4
Tape: XYZ
Head:  ^
----------------------------------------
State: q1
Tape: XYZ
Head:  ^
----------------------------------------
State: q1
Tape: XYZ
Head:   ^
----------------------------------------
State: q1
Tape: XYZ
Head:    ^
----------------------------------------
State: q5
Tape: XYZ
Head:     ^
----------------------------------------
Evaluation: Passed (reached accept state q5)
```

### Input: `aabbcc` (Should Accept - n=2)
```
State: q0
Tape: aabbcc
Head: ^
----------------------------------------
State: q2
Tape: Xabbcc
Head:  ^
----------------------------------------
[... intermediate steps showing marking process ...]
State: q5
Tape: XXYYZZ
Head:       ^
----------------------------------------
Evaluation: Passed (reached accept state q5)
```

### Input: `aabbc` (Should Reject - Unequal counts)
```
State: q0
Tape: aabbc
Head: ^
----------------------------------------
[... steps ...]
State: q_reject
Tape: XXYYZ
Head:      ^
----------------------------------------
Evaluation: Failed (reached reject state: q_reject)
```

## Use of Generative AI

### Tools Used
This project was developed with assistance from **Grok** (built by xAI), a generative AI model. The AI was leveraged throughout the development process to accelerate implementation while ensuring accuracy.

### How AI Was Used
1. **Language Selection**: Queried Grok for programming language recommendations. Python was selected for its expressiveness and ease of use for educational implementations. Claude AI was used for final polish.

2. **Code Generation**: Grok generated:
   - Initial code structure and class design
   - Transition table for the a^n b^n c^n language
   - State tracing and output formatting logic
   - Docker configuration

4. **Refinement**: I used Claude AI and my notes from my class on Theory of Formal Languages, Grammars and Automata to ensure
   - Transition completeness (ensuring all edge cases handled)
   - Tracing output for better readability
   - Docker ENTRYPOINT configuration based on Grok's suggestions
   - Documentation and examples

### Specific Contributions
- **Algorithm Design**: AI helped design the marking strategy (X, Y, Z) and state transitions
- **Transition Table**: Generated the ~18 transitions needed for correct operation
- **Error Handling**: Suggested max_steps limit and reject state logic
- **Documentation**: Assisted in creating clear explanations, state diagrams, and usage examples
- **Docker Setup**: Recommended using Python 3.12-slim and proper ENTRYPOINT configuration

## Project Structure
```
project10/
├── tm_simulator.py    # Main Turing Machine implementation
├── Dockerfile         # Container configuration
└── README.md          # This file
```

## Technical Details

### Files
- **tm_simulator.py**: Contains the `TuringMachine` class and CLI interface
  - `__init__`: Initializes tape, head position, states, and transition table
  - `step()`: Executes one transition step
  - `run()`: Main execution loop with tracing
  - `print_trace()`: Displays current state, tape, and head position
  - `main()`: Handles command-line arguments using argparse

- **Dockerfile**: Uses Python 3.12-slim base image with ENTRYPOINT for argument passing

### Transition Logic
- Tape extends dynamically when head moves beyond boundaries
- No transition = automatic rejection
- Max 10,000 steps to prevent infinite loops
- Blank symbol ' ' (space) marks tape ends

## Future Enhancements
- Add `--no-trace` flag for quiet output (final result only)
- Web-based interface for visual step-by-step execution
- Support for custom transition tables (user-configurable TM)
- Performance metrics (steps taken, execution time)
- Export trace to file for analysis

## Author
Justice Thomson  
COSC 352 - Fall 2025

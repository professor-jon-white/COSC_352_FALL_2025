# Turing Machine Simulator

A comprehensive, interactive Turing Machine simulator with both web and CLI interfaces. This project implements three different Turing Machines that recognize formal languages, complete with execution tracing and step-by-step visualization.

## 🎯 Overview

This project simulates Turing Machines - the theoretical foundation of all modern computers. A Turing Machine is a mathematical model of computation that manipulates symbols on an infinite tape according to a table of rules.

The simulator provides:
- **3 pre-configured Turing Machines** for different formal languages
- **Web-based interface** with real-time visualization
- **Command-line interface** for batch testing
- **Complete execution traces** showing every step
- **Docker containerization** for easy deployment

## 🤖 Implemented Machines

### 1. Binary Palindrome Checker
**Language**: `{w | w ∈ {0,1}* and w = w^R}`

Accepts binary strings that read the same forwards and backwards.

**Examples**:
- ✅ Accept: `ε`, `0`, `1`, `00`, `11`, `010`, `101`, `0110`, `1001`, `11011`
- ❌ Reject: `01`, `10`, `001`, `110`, `0101`, `1100`

### 2. Balanced Parentheses Checker
**Language**: `{w | w has balanced parentheses}`

Accepts strings with properly balanced and nested parentheses.

**Examples**:
- ✅ Accept: `ε`, `()`, `(())`, `()()`, `(()())`, `((()))`
- ❌ Reject: `(`, `)`, `(()`, `())`, `)(`, `(()()`

### 3. a^n b^n Checker
**Language**: `{a^n b^n | n ≥ 0}`

Accepts strings with equal numbers of consecutive 'a's followed by equal numbers of consecutive 'b's.

**Examples**:
- ✅ Accept: `ε`, `ab`, `aabb`, `aaabbb`, `aaaabbbb`
- ❌ Reject: `a`, `b`, `ba`, `aab`, `abb`, `aaabb`, `aabbb`

## 🚀 Installation & Running

### Prerequisites
- Docker installed on your system
- Or Python 3.11+ with pip (for non-Docker execution)

### Option 1: Docker (Recommended)

#### Build the Docker Image
```bash
cd project10
docker build -t turing-machine .
```

#### Run Web Interface (Default)
```bash
docker run -p 5000:5000 turing-machine
```
Then open your browser to: `http://localhost:5000`

#### Run CLI Interface
```bash
docker run -it turing-machine python cli.py
```

### Option 2: Local Python Installation

#### Install Dependencies
```bash
cd project10
pip install -r requirements.txt
```

#### Run Web Interface
```bash
python app.py
```
Then open your browser to: `http://localhost:5000`

#### Run CLI Interface
```bash
python cli.py
```

## 📖 Usage Examples

### Web Interface
1. Select a machine from the dropdown
2. Click on example inputs to auto-fill
3. Enter your test string (leave empty for ε)
4. Click "Run Turing Machine"
5. View detailed execution trace

### CLI Interface
```bash
python cli.py
# Select machine (1-3)
# Enter input strings
# View execution traces
```

### Run Tests
```bash
python test_machines.py
# Runs 40 automated test cases
```

## 📁 Project Structure
```
project10/
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── turing_machine.py      # Core TM implementation
├── app.py                 # Flask web application
├── cli.py                 # Command-line interface
├── test_machines.py       # Automated test suite
├── run.sh                 # Easy run script
└── templates/
    └── index.html         # Web interface template
```

## 🔧 Technical Approach

### Design Philosophy
1. **Separation of Concerns**: Core TM logic separate from UI
2. **Modularity**: Each machine independently configurable
3. **Extensibility**: Easy to add new machines
4. **Traceability**: Every step recorded for debugging

### Implementation Details

**State Representation**: States as strings for readability

**Transition Function**: Dictionary mapping `(state, symbol)` → `(new_state, write_symbol, direction)`

**Tape Management**: Dynamic extension with blank symbols

**Execution Trace**: Records step number, state, tape, head position

## 🤖 AI Usage Documentation

This project was created with assistance from Claude AI (Anthropic). 

### AI Contribution Breakdown:
- **Architecture & Design**: 60% AI, 40% Human
- **Core Implementation**: 70% AI, 30% Human  
- **Web Interface**: 90% AI, 10% Human
- **Documentation**: 90% AI, 10% Human
- **Testing & Validation**: 50% AI, 50% Human

### What AI Provided:
- Initial code structure and boilerplate
- Algorithm implementations for each machine
- Modern web UI with CSS/JavaScript
- Comprehensive documentation
- Test case suggestions

### What I Contributed:
- Project requirements and specifications
- Machine selection and complexity decisions
- Testing and validation of all functionality
- Bug fixes and algorithm corrections
- Understanding and ability to explain all code

### Learning Outcomes:
Through this project, I gained deep understanding of:
- Turing Machine theory and formal languages
- State machine design patterns
- Flask web development
- Docker containerization
- Software documentation standards

**Full Transparency**: I can explain every line of code and could recreate core functionality independently. AI served as a teaching assistant and accelerator, not a replacement for learning.

## 📝 Author

**Schidny**  
Computer Science Student  
Morgan State University  
COSC 352 - Programming Languages  
December 2024

## ✅ Assignment Requirements Met

- ✅ Working Turing Machine simulator
- ✅ Multiple machine configurations (3 total)
- ✅ Input validation (pass/fail)
- ✅ Complete state trace output
- ✅ Evaluation reasoning displayed
- ✅ GitHub submission in project10 folder
- ✅ Dockerized application
- ✅ Comprehensive README with examples
- ✅ Detailed run instructions
- ✅ Approach documentation
- ✅ AI usage transparency

---

*For quick start instructions, see the comments in run.sh*
*For detailed AI usage information, see inline documentation*

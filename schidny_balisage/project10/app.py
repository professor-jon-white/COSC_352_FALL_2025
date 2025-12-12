"""
Web interface for Turing Machine Simulator
Flask application with interactive UI
"""

from flask import Flask, render_template, request, jsonify
from turing_machine import TuringMachineLibrary, Direction
import json

app = Flask(__name__)

# Machine descriptions for UI
MACHINE_DESCRIPTIONS = {
    "binary_palindrome": {
        "name": "Binary Palindrome Checker",
        "description": "Accepts binary strings that read the same forwards and backwards",
        "language": "{w | w ∈ {0,1}* and w = w^R}",
        "examples": {
            "accept": ["", "0", "1", "00", "11", "010", "101", "0110", "1001", "11011"],
            "reject": ["01", "10", "001", "110", "0101", "1100"]
        }
    },
    "balanced_parentheses": {
        "name": "Balanced Parentheses Checker",
        "description": "Accepts strings with properly balanced and nested parentheses",
        "language": "{w | w has balanced parentheses}",
        "examples": {
            "accept": ["", "()", "(())", "()()", "(()())", "((()))"],
            "reject": ["(", ")", "(()", "())", ")(", "(()("]
        }
    },
    "a_n_b_n": {
        "name": "a^n b^n Checker",
        "description": "Accepts strings with equal numbers of a's followed by equal numbers of b's",
        "language": "{a^n b^n | n ≥ 0}",
        "examples": {
            "accept": ["", "ab", "aabb", "aaabbb", "aaaabbbb"],
            "reject": ["a", "b", "ba", "aab", "abb", "aaabb", "aabbb"]
        }
    }
}


@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html', machines=MACHINE_DESCRIPTIONS)


@app.route('/run', methods=['POST'])
def run_machine():
    """Run Turing Machine on input"""
    try:
        data = request.get_json()
        machine_type = data.get('machine_type')
        input_string = data.get('input_string', '')
        
        # Get the appropriate machine
        machines = TuringMachineLibrary.get_all_machines()
        if machine_type not in machines:
            return jsonify({'error': 'Invalid machine type'}), 400
        
        tm = machines[machine_type]
        
        # Run the machine
        accepted, trace, final_tape = tm.run(input_string)
        
        # Format response
        response = {
            'accepted': accepted,
            'result': 'ACCEPTED ✓' if accepted else 'REJECTED ✗',
            'steps': len(trace),
            'trace': trace,
            'final_tape': final_tape,
            'trace_summary': tm.get_trace_summary()
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/machine_info/<machine_type>')
def machine_info(machine_type):
    """Get information about a specific machine"""
    if machine_type in MACHINE_DESCRIPTIONS:
        return jsonify(MACHINE_DESCRIPTIONS[machine_type])
    return jsonify({'error': 'Machine not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

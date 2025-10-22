Calculator MCP

A Model Context Protocol (MCP) implementation of a calculator in Python, supporting standard input/output (stdio) and HTTP streaming for remote usage. This project demonstrates basic MCP integration and how to expose a simple calculator over multiple interfaces.

Features

Basic arithmetic operations: addition, subtraction, multiplication, division.

Works via standard input/output (stdio) for local use.

Supports HTTP streaming for remote requests.

Minimal dependencies, designed for easy extension into MCP workflows.

Requirements

Python 3.8+

requests (for HTTP streaming demo)

flask (optional, if using HTTP server)

Install dependencies:

pip install requests flask

Usage
1. Using STDIO

Run the calculator locally:

python fastmcp_calc.py


Then follow prompts in the terminal:

Enter first number: 5
Enter operator (+, -, *, /): *
Enter second number: 3
Result: 15

2. Using HTTP Stream

Start the HTTP server (if included):

python fastmcp_calc_server.py


Send a calculation request using HTTP streaming:

curl -X POST http://localhost:5000/calc -d '{"a":5,"op":"*","b":3}'


The server responds with a JSON payload:

{"result":15}

Project Structure
calculator-mcp/
│
├─ fastmcp_calc.py         # Main calculator script (stdio)
├─ fastmcp_calc_server.py  # Optional HTTP streaming server
├─ README.md               # This documentation
└─ requirements.txt        # Python dependencies

Contributing

Feel free to fork, suggest improvements, or extend functionality with:

Additional operators (exponentiation, modulus)

Error handling for invalid inputs

Integration with other MCP-compatible systems

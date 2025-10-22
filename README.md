# Calculator MCP

A **Model Context Protocol (MCP)** implementation of a calculator in **Python**, supporting standard input/output (`stdio`) and HTTP streaming for remote usage. This project demonstrates basic MCP integration and exposing a simple calculator over multiple interfaces.

## Features

* Basic arithmetic operations: addition, subtraction, multiplication, division
* Works via **standard input/output (stdio)** for local use
* Supports **HTTP streaming** for remote requests
* Minimal dependencies, designed for easy extension into MCP workflows

## Requirements

* Python 3.8+
* `requests` (for HTTP streaming demo)
* `flask` (optional, if using HTTP server)
* **Node.js** (required for MCP integration)

Install dependencies:

```bash
pip install requests flask
```

You also need to install and set up Node.js: [https://nodejs.org/](https://nodejs.org/)

## Usage

### 1. Using STDIO

Run the calculator locally:

```bash
python fastmcp_calc.py
```

Follow the prompts in the terminal:

```
Enter first number: 5
Enter operator (+, -, *, /): *
Enter second number: 3
Result: 15
```

### 2. Using HTTP Stream

Start the HTTP server (if included):

```bash
python fastmcp_calc_server.py
```

Send a calculation request using HTTP streaming:

```bash
curl -X POST http://localhost:5000/calc -d '{"a":5,"op":"*","b":3}'
```

The server responds with a JSON payload:

```json
{"result":15}
```

## Demo

Include a screenshot or GIF of the calculator working via STDIO and HTTP streaming for better visualization.

## Project Structure

```
calculator-mcp/
│
├─ fastmcp_calc.py         # Main calculator script (stdio)
├─ fastmcp_calc_server.py  # Optional HTTP streaming server
├─ README.md               # This documentation
└─ requirements.txt        # Python dependencies
```

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/yourusername/calculator-mcp.git
cd calculator-mcp
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure Node.js is installed and set up.

4. Run via STDIO or start the HTTP server as described in the Usage section.

## Contributing

Feel free to fork, suggest improvements, or extend functionality with:

* Additional operators (exponentiation, modulus)
* Error handling for invalid inputs
* Integration with other MCP-compatible systems

## License

MIT License © [Yo

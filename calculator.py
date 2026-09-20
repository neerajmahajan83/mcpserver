from mcp.server import MCPServer


mcp = MCPServer("Calculator MCP Server")


@mcp.tool()
def calculate(a: float, operation: str, b: float) -> float:
	"""Perform a basic arithmetic calculation."""
	if operation == "+":
		return a + b
	if operation == "-":
		return a - b
	if operation == "*":
		return a * b
	if operation == "/":
		if b == 0:
			raise ValueError("Cannot divide by zero")
		return a / b
	raise ValueError("Supported operations are +, -, *, and /")


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
	"""Return a greeting for a named user."""
	return f"Hello, {name}!"


if __name__ == "__main__":
	mcp.run()
# (c) Danit Consultancy and Development, January-2026, danittech@yahoo.com

""" Example MCP server for math operations """

from fastmcp import FastMCP

mcp = FastMCP("Math Server")

# ----------------------------------------------------------------------------------------

@mcp.tool()
def add(a: int, b: int) -> int:
    """ Add two numbers """
    return a + b

# ----------------------------------------------------------------------------------------

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """ Multiply two numbers """
    return a * b

# ========================================================================================

if __name__ == "__main__":

    mcp.run(transport="stdio")

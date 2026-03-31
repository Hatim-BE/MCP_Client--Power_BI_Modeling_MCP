# PowerBI MCP Client

---

## Requirements

- Python 3.10+
- Windows MCP server executable (`.exe`)
- `uv` package manager (or `pip` alternative)
- Dependencies:
  - [`mcp`](https://pypi.org/project/mcp/)
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/powerbi-mcp-client.git
cd powerbi-mcp-client
```

2. Install dependencies with `uv`:

```bash
uv install mcp python-dotenv
```

~~3. Create a `.env` file in the project root (optional):~~

~~```env~~
~~# Example .env~~
~~API_KEY=your_api_key_here~~
~~```~~

4. Ensure your MCP server executable is accessible:

```
PowerBI.MCP.Server.exe
```

---

## Usage

Run the client with the path to your MCP server:

```bash
python client.py path/to/PowerBI.MCP.Server.exe
```

Example output:

```
Connected to server with tools: ['Tool1', 'Tool2', 'Tool3']
```

---

## Project Structure

```
client.py          # Main MCP client script
README.md          # Project documentation
```

- `MCPClient` class: Manages connection, initialization, and cleanup
- `connect_to_server()`: Connects and lists available tools
- `cleanup()`: Closes connections gracefully
- `main()`: Async entry point for running the client

---

## Development

- Extend `MCPClient` to implement custom workflows with your MCP tools
- Use `asyncio` for asynchronous interactions
- Only Windows `.exe` server scripts are supported for now!
- Compatible with Visual Studio Code for development and debugging

---

## References

- [Power BI Modeling MCP GitHub](https://github.com/microsoft/powerbi-modeling-mcp)
- [MCP Python SDK Documentation](https://pypi.org/project/mcp/)
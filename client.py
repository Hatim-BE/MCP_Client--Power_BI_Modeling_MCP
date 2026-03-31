import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
    # methods will go here

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.exe for windows)
        """
        is_win_exe = server_script_path.endswith('.exe')
        if not (is_win_exe):
            raise ValueError("Server script must be a .exe (windows executable) file")

        command = server_script_path
        server_params = StdioServerParameters(
            command=command,
            args=["--start"],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    
async def main():
    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        # await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
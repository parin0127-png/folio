import asyncio
import threading
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os, sys

cwd = os.path.dirname(__file__)
server_path = os.path.join(os.path.dirname(__file__), "server.py")
_loop = None
_session = None
ready = threading.Event()

async def _start():
    try:
        global _session, _loop
        _loop = asyncio.get_event_loop()
        params = StdioServerParameters(command = sys.executable, args = [server_path], cwd = cwd)
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                _session = session
                await _session.initialize()
                print("> MCP Connected !")
                ready.set()
                await asyncio.Future()
    except Exception as e:
        print(f"> [Error]: {e}")
        os._exit(0)
threading.Thread(target = lambda: asyncio.run(_start()), daemon = True).start()

def call_tools(tool_name, args):
    ready.wait()
    fut = asyncio.run_coroutine_threadsafe(_session.call_tool(tool_name, args), _loop)
    result = fut.result()

    # print("> MCP RESULT:", result)
    return result.content[0].text

def list_tools():
    ready.wait()
    fut = asyncio.run_coroutine_threadsafe(_session.list_tools(), _loop)
    return {t.name: t.description for t in fut.result().tools}

def get_tool_dict():
    ready.wait()
    fut = asyncio.run_coroutine_threadsafe(_session.list_tools(), _loop)
    return {t.name: t.description for t in fut.result().tools}

def get_schema(tool_name):
    ready.wait()
    fut = asyncio.run_coroutine_threadsafe(_session.list_tools(), _loop)
    tools = fut.result().tools
    for t in tools:
        if t.name == tool_name:
            return{
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.inputSchema
                }
            }
    return None
#todo mcp
from fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP(name="Todoist")

API_TOKEN = os.getenv("TODOIST_API_TOKEN")
BASE_URL = "https://api.todoist.com/rest/v2"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

@mcp.tool()
def get_today_tasks() -> list:
    """Get all tasks due today.
    
    returns: list: List of tasks with their names and IDs.
    """
    response = requests.get(f"{BASE_URL}/tasks", headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    
    tasks = response.json()
    return [{"id": t["id"], "content": t["content"], "due": t.get("due")} for t in tasks]

@mcp.tool()
def add_task(content: str, due_string: str = None) -> dict:
    """Add a new task to Todoist.
    
    args: 
        content (str): The task description.
        due_string (str): When it's due (e.g., "today", "tomorrow", "next monday").
    
    returns: dict: The created task details.
    """
    data = {"content": content}
    if due_string:
        data["due_string"] = due_string
    
    response = requests.post(f"{BASE_URL}/tasks", headers=HEADERS, json=data)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    
    return response.json()

@mcp.tool()
def complete_task(task_id: str) -> bool:
    """Mark a task as complete.
    
    args:
        task_id (str): The ID of the task to complete.
    
    returns: bool: True if successful.
    """
    response = requests.post(f"{BASE_URL}/tasks/{task_id}/close", headers=HEADERS)
    return response.status_code == 204

@mcp.tool()
def search_tasks(query: str) -> list:
    """Search for tasks by keyword.
    
    args:
        query (str): The search term.
    
    returns: list: Matching tasks.
    """
    response = requests.get(f"{BASE_URL}/tasks", headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    
    tasks = response.json()
    return [t for t in tasks if query.lower() in t["content"].lower()]

if __name__ == "__main__":
    mcp.run()
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

class ToolInfo:

    name:str
    func: callable
    descriptions: str
    category:str="general"

    def __post_init__(self):
        if self.params is None:
            import inspect
            sig = inspect.signature(self.func)
            self.parameters=list(sig.parameters.keys())


class MetadataRegistry:
    def __init__(self):
        self.tools:Dict[str,ToolInfo]={}

    def register_tool(self, name: str, func: Callable, description: str, category: str = "general"):
        tool_info = ToolInfo(name=name, func=func, descriptions=description, category=category)
        self.tools[name] = tool_info
        print(f"Tool registered: {name}")

    def run_tool(self, name: str, *args, **kwargs) -> Any:
        if name in self.tools:
            tool_info = self.tools[name]
            return tool_info.func(*args, **kwargs)
        else:
            raise ValueError(f"Tool '{name}' NOT FOUND")
        
    def list_tools(self)->list:
        return list(self.tools.keys())
    
    def get_tool_info(self, name: str) -> ToolInfo:
        return self.tools.get(name)
    
registry=MetadataRegistry()

@registry.register_tool(name="multiply", description="Multiplies two numbers", category="math")
def multiply(a,b):
    """ Multiply two numbers"""
    return a*b


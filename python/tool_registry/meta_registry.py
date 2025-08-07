from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

@dataclass
class ToolInfo:

    name:str
    description: str
    func: Callable 
    category:str="general" 
    parameters: Optional[List[str]] = None


    def __post_init__(self):
        if self.parameters is None:
            import inspect
            sig = inspect.signature(self.func)
            self.parameters=list(sig.parameters.keys())


class MetadataRegistry:
    def __init__(self):
        self.tools:Dict[str,ToolInfo]={}

    def tool(self, name: str, description: str, category: str = "general"):
        def decorator(func: Callable) -> Callable:
             tool_info = ToolInfo(name=name,func=func,description=description, category=category)
             self.tools[name] = tool_info
             print(f"Tool registered: {name}")
             return func
        return decorator

       

    def execute(self, name: str, *args, **kwargs) -> Any:
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

@registry.tool(name="multiply", description="Multiplies two numbers", category="math")
def multiply(a,b):
    """ Multiply two numbers"""
    return a*b

registry.execute("multiply", 5, 7)


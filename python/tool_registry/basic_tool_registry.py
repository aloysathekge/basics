class SimpleRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, func):

        self.tools[name] = func
        print(f"registered a tool: {name}")

    def get_tool_name(self, name):

        return self.tools.get(name)

    def get_tool_list(self):

        return list(self.tools.keys())


registry = SimpleRegistry()


def multiply(a, b) -> int:
    return a * b


def greet(name):
    return f"Hi {name}"


registry.register("multiply", multiply)
registry.register("greet", greet)
add_tool = registry.get_tool_name("multiply")

print(add_tool(2, 6))

# print(registry.get_tool_list())


# def __init__(self):
#     self.tools = {}

# def register(self, name, func):
#     """Register a tool with a name"""

#     self.tools[name] = func
#     print(f"registered a tool:{name}")

# def get_tool(self, name):
#     """Get a too by name"""

#     return self.tools.get(name)

# def list_tools(self):
#     """List all registered tools"""

#     return list(self.tools.keys())


# registry = SimpleRegistry()


# def add_numbers(a, b):
#     return a + b


# def multiply_number(a, b):
#     return a * b


# def greet(name):
#     return f"Hello {name}"


# registry.register("add", add_numbers)
# registry.register("multiply", multiply_number)
# registry.register("greet", greet)

# get_all_tool = registry.list_tools()

# print(f"Tools available:{get_all_tool}")

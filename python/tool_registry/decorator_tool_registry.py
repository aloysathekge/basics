class Decorator_registry:

    def __init__(self):
        self.tools = {}

    def tool(self, name):
        """Decorator to register tool"""

        def decorator(func):
            self.tools[name] = func

            print(f"Tool registered: {name}")

            return func

        return decorator

    def run(self, tool_name, *args, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name](*args, **kwargs)
        else:
            raise ValueError(f"Tool '{tool_name} NOT FOUND")

    def list_tools(self):
        return list(self.tools.keys())


registry = Decorator_registry()


@registry.tool("multiply")
def multiply(a, b):
    return a * b


@registry.tool("power")
def power(base, exponent):
    return base**exponent


print(registry.run("multiply", 5, 7))

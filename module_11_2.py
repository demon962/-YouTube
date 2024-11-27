def introspection_info(obj):
    import inspect

    result = {}

    result['type'] = type(obj).__name__

    attributes = {attr: getattr(obj, attr) for attr in dir(obj)}
    result['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    result['methods'] = methods

    module_name = inspect.getmodule(obj).__name__ if inspect.ismodule(obj) else None
    result['module'] = module_name

    return result

class ExampleClass:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        pass


example_instance = ExampleClass("test")
info = introspection_info(example_instance)

for key, value in info.items():
    print(f"{key}: {value}")
def call_function(function_call, functions):
    function_name = function_call.name
    function_args = function_call.args
    return functions[function_name](**function_args)
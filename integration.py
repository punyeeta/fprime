import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Union, Dict, List, Any
import re
import math


def integrate_function(func: Callable[[float], float], lower_bound: float, upper_bound: float, **kwargs) -> Tuple[float, float]:
    """
    Numerically integrate a function using scipy.integrate.quad.
    
    Args:
        func: The function to integrate
        lower_bound: Lower limit of integration
        upper_bound: Upper limit of integration
        **kwargs: Additional parameters to pass to quad
        
    Returns:
        Tuple containing (integral value, estimated absolute error)
    """
    result = integrate.quad(func, lower_bound, upper_bound, **kwargs)
    return result


def cumulative_integral(func: Callable[[float], float], x_values: np.ndarray, lower_bound: float = None) -> np.ndarray:
    """
    Calculate the cumulative integral of a function over a range of x values.
    This is useful for plotting the integral function.
    
    Args:
        func: The function to integrate
        x_values: Array of x values to calculate the cumulative integral for
        lower_bound: Starting point for integration (defaults to min(x_values))
        
    Returns:
        Array of cumulative integral values corresponding to x_values
    """
    if lower_bound is None:
        lower_bound = np.min(x_values)
    
    integral_values = np.zeros_like(x_values, dtype=float)
    
    for i, x in enumerate(x_values):
        if x > lower_bound:
            integral_values[i], _ = integrate_function(func, lower_bound, x)
    
    return integral_values


def integrate_common_functions() -> Dict[str, Callable[[float], float]]:
    """
    Return a dictionary of common mathematical functions and their analytical integrals.
    Useful for testing and demonstration purposes.
    
    Returns:
        Dictionary mapping function names to their integral functions
    """
    # Define some common functions and their integrals
    # Note: These are analytical integrals for reference
    common_integrals = {
        "x^2": lambda x: x**3/3,  # Integral of x^2 is x^3/3
        "x^3": lambda x: x**4/4,  # Integral of x^3 is x^4/4
        "sin(x)": lambda x: -np.cos(x),  # Integral of sin(x) is -cos(x)
        "cos(x)": lambda x: np.sin(x),  # Integral of cos(x) is sin(x)
        "e^x": lambda x: np.exp(x),  # Integral of e^x is e^x
        "1/x": lambda x: np.log(abs(x)),  # Integral of 1/x is ln|x|
        "sqrt(x)": lambda x: 2/3 * x**(3/2),  # Integral of sqrt(x) is (2/3)x^(3/2)
        "tan(x)": lambda x: -np.log(abs(np.cos(x))),  # Integral of tan(x) is -ln|cos(x)|
    }
    
    return common_integrals


def get_integral_error(func: Callable[[float], float], analytical_integral: Callable[[float], float], 
                      lower_bound: float, upper_bound: float) -> float:
    """
    Calculate the error between numerical and analytical integration.
    
    Args:
        func: The function to integrate numerically
        analytical_integral: The analytical integral function
        lower_bound: Lower limit of integration
        upper_bound: Upper limit of integration
        
    Returns:
        Absolute error between numerical and analytical results
    """
    numerical_result, _ = integrate_function(func, lower_bound, upper_bound)
    analytical_result = analytical_integral(upper_bound) - analytical_integral(lower_bound)
    
    return abs(numerical_result - analytical_result)


def parse_user_function(func_str):
    """Parse user input function string into a callable function"""
    try:
        # Replace common mathematical notations with Python syntax
        func_str = func_str.replace('^', '**')  # Handle exponents
        
        # Handle pi and e
        func_str = func_str.replace('pi', 'np.pi')
        func_str = func_str.replace('e', 'np.e')
        
        # Handle implicit multiplication
        func_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', func_str)  # 2x -> 2*x
        func_str = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', func_str)  # x2 -> x*2
        func_str = re.sub(r'\)([a-zA-Z])', r')*\1', func_str)     # (x+1)x -> (x+1)*x
        func_str = re.sub(r'([a-zA-Z])\(', r'\1*(', func_str)     # x(x+1) -> x*(x+1)
        
        # Handle exponential function
        func_str = re.sub(r'e\^\((.*?)\)', r'np.exp(\1)', func_str)
        func_str = re.sub(r'e\^(.*?)(?=[+\-*/) ]|$)', r'np.exp(\1)', func_str)
        
        # Handle trigonometric functions with proper numpy syntax
        func_str = re.sub(r'sin\((.*?)\)', r'np.sin(\1)', func_str)
        func_str = re.sub(r'cos\((.*?)\)', r'np.cos(\1)', func_str)
        func_str = re.sub(r'tan\((.*?)\)', r'np.tan(\1)', func_str)
        func_str = re.sub(r'csc\((.*?)\)', r'1/np.sin(\1)', func_str)
        func_str = re.sub(r'sec\((.*?)\)', r'1/np.cos(\1)', func_str)
        func_str = re.sub(r'cot\((.*?)\)', r'1/np.tan(\1)', func_str)
        
        # Handle inverse trigonometric functions
        func_str = re.sub(r'arcsin\((.*?)\)', r'np.arcsin(\1)', func_str)
        func_str = re.sub(r'arccos\((.*?)\)', r'np.arccos(\1)', func_str)
        func_str = re.sub(r'arctan\((.*?)\)', r'np.arctan(\1)', func_str)
        
        # Handle exponential and logarithmic functions
        func_str = re.sub(r'exp\((.*?)\)', r'np.exp(\1)', func_str)
        func_str = re.sub(r'log\((.*?)\)', r'np.log(\1)', func_str)
        func_str = re.sub(r'ln\((.*?)\)', r'np.log(\1)', func_str)
        
        # Handle square root
        func_str = re.sub(r'sqrt\((.*?)\)', r'np.sqrt(\1)', func_str)
        
        # Create a safe dictionary with allowed mathematical functions
        safe_dict = {
            'np': np,
            'sin': lambda x: np.sin(x),
            'cos': lambda x: np.cos(x),
            'tan': lambda x: np.tan(x),
            'arcsin': lambda x: np.arcsin(x),
            'arccos': lambda x: np.arccos(x),
            'arctan': lambda x: np.arctan(x),
            'exp': lambda x: np.exp(x),
            'log': lambda x: np.log(x),
            'sqrt': lambda x: np.sqrt(x),
            'pi': np.pi,
            'e': np.e
        }
        
        # Create a lambda function that uses numpy for mathematical operations
        def func(x):
            try:
                # Convert x to numpy array if it's a scalar
                if not isinstance(x, np.ndarray):
                    x = np.array(x)
                return eval(func_str, {'x': x, **safe_dict})
            except Exception as e:
                raise ValueError(f"Error evaluating function: {str(e)}")
        
        return func
    except Exception as e:
        raise ValueError(f"Error parsing function: {str(e)}")


def process_user_integration(func_str: str, lower_bound: float, upper_bound: float) -> Dict[str, Any]:
    """
    Process user input for integration and return results in a structured format.
    Uses only the quad method for integration.
    
    Args:
        func_str: String representation of the function to integrate
        lower_bound: Lower limit of integration
        upper_bound: Upper limit of integration
        
    Returns:
        Dictionary containing integration results and metadata
    """
    try:
        # Parse the user function
        func = parse_user_function(func_str)
        
        # Perform the integration with the quad method
        result, error = integrate_function(func, lower_bound, upper_bound)
        
        # Simplify the result display
        if 'e^' in func_str or 'exp' in func_str:
            # For exponential functions, simplify the display
            result_str = f"{result:.6f}"
        else:
            result_str = f"{result:.6f}"
        
        return {
            "success": True,
            "function": func_str,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "result": result,
            "error": error,
            "message": "Integration successful using quad method."
        }
    except Exception as e:
        return {
            "success": False,
            "function": func_str,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "message": f"Integration failed: {str(e)}"
        }
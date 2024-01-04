#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets
from IPython.display import display

# Define widgets
num1_input = widgets.FloatText(value=0, description='Number 1:')
num2_input = widgets.FloatText(value=0, description='Number 2:')
operation_dropdown = widgets.Dropdown(
    options=['Add', 'Subtract', 'Multiply', 'Divide'],
    value='Add',
    description='Operation:'
)
result_output = widgets.Output()

# Define calculation function
def calculate_result(change):
    num1 = num1_input.value
    num2 = num2_input.value
    operation = operation_dropdown.value
    
    with result_output:
        result_output.clear_output()
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result_output.append_stdout("Error: Cannot divide by zero.")
                return
        result_output.append_stdout(f"Result of {num1} {operation} {num2} is: {result}")

# Attach the function to the widgets' change event
num1_input.observe(calculate_result, names='value')
num2_input.observe(calculate_result, names='value')
operation_dropdown.observe(calculate_result, names='value')

# Display widgets
display(num1_input, num2_input, operation_dropdown, result_output)


# In[ ]:





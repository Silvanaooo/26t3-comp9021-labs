def f5(integral_part, fractional_part):
    # Determine the number of digits in the fractional part
    precision = len(str(fractional_part))
    
    # Construct the floating point number by converting parts to strings
    a_float = float(str(integral_part) + '.' + str(fractional_part))
    
    # Format with original precision
    simple_precision = f'{a_float:.{precision}f}'
    
    # Create a version with expected trailing zeros (if number is exact)
    extended_simple_precision = simple_precision + '0' * precision
    
    # Format with double precision
    double_precision = f'{a_float:.{precision * 2}f}'
    
    # Start printing the output
    print('With', precision * 2, 'digits after the decimal point, ', end='')
    
    # Compare the extended simple precision with double precision
    if extended_simple_precision == double_precision:
        # If they match, it means the number can be represented exactly with trailing zeros
        print(simple_precision, 'prints with', precision, 'trailing',
              # Singular/plural form for "zero"/"zeroes"
              precision == 1 and 'zero,' or 'zeros,', 'namely',
              extended_simple_precision + "."
             )
    else:
        # If they don't match, it means floating point representation introduces rounding errors
        print(simple_precision, 'prints as', double_precision + ".")
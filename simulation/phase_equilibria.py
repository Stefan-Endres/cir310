class Raoult:
    """
    Modified Raoults law
    """
    def __init__(self, fugacity_coeff, activity_coeff):
        pass

class CubicEOS:
    def __init__(self):
        pass

    def roots(self):
        pass

class Fugacity:
    """

    """
    def __init__(self):
        pass

def V_root(state, parameters):
    """
    Calculates the volume roots of the van der Waals equation using the
    analytic solution at specified values of P (or Psat), T, a(T) and b. If
    an analytical solution does not exist a numerical estimate is used.

    Parameters
    ----------
    state : dictionary
        Contains the current temperature state variables 'T', pressure 'P'
        and the VdW coefficients 'a' and 'b'.

    parameters : dictionary
        Contains the critical paramters 'T_c', 'a_c', 'R'.

    Dependencies
    ------------
    numpy, math
    """
    import logging
    from math import sqrt, acos, cos, pi
    if state['P'] == 0:
        state['P'] = 3.0

    import numpy
    # Coefficients of (C_0)V^3 + (C_1)V^2 + (C_2)V + C_3 = 0
    C = [1.0,  # Coefficient C_0
         - (parameters['R'] * state['T'] / state['P'] + state['b']),  # Coefficient C_1
         state['a'] / state['P'],  # Coefficient C_2
         - state['a'] * state['b'] / state['P']  # Coefficient C_3
         ]

    V_roots = numpy.roots(C)
    state['V_v'], state['V_l']  = max(V_roots.real), min(V_roots.real)

    return state
"""
Contains the equilibrium stage and distillation column classes
"""
from parameters import *
from phase_equilibria import *
import numpy

class EquilibriumStage:
    def __init__(self, N, reactions=None):
        # Define if reactor stage or not
        # Return function representing the
        # mass balance around the reaction
        pass


class Column:
    """
    Reactive distillation column system
    """
    def __init__(self, T, P, N, F, R, z0=(0.47, 0.53, 0.0),
                 comps=('formaldehyde', 'trioxane', 'water'),
                 reactions=None):
        """
        :param T: Temperature (K) of the reactor
        :param P: Column pressure (kPa)
        :param N: Number of equilibrium stages
        :param F: Feed flow rate (mol / h)
        :param R: Reflux ratio
        :param z0: Initial composition (mol fr)
        :param comp: Number of components (int)
        :param reactions: Reaction equations (func)

        :return:
        """
        self.N = N
        self.F = F
        self.R = R
        self.T = T
        self.P = P
        self.z0 = z0
        self.comps = comps
        self.reactions = reactions

        # Initiate concentration stages:
        # Profiles representated as array with a
        # component index for rows and the columns
        # representing the equilibrium stage
        # N is the concentration in the reactor
        self.x = numpy.array([len(comps), N])
        self.y = numpy.array([len(comps), N])

    def __repr__(self):
        print("Column: TODO: Print profiles")

    def algebraic_equations(self):
        # Explicit algebraics:
        # Liquid entrainment (Note: D = F)
        self.L = self.R * self.V
        # Vapour flow rate
        self.V = self.F - self.L

        # Solve non-linear


def reaction_rate(x, V_l, L):
    """
    Reaction rates the trimerization reaction:

    C H_2 O --> C_3 H_6 O_3

    catalyzed by sulfuric acid

    :param x: Compositions in liquid phase
    :param V_l: Liquid reaction phase volume

    :return:
    """
    #TODO: x[#] should be total mol in liquid phase (unknown)
    return V_l * V_R * (k_1 * (x[0] / V_l)**2 - k_2 * (x[1] / V_l))
from typing import List
from .comrasion import Comprasion

class NonParameterEstmation:
    def __init__(self, 
                 sample_size:int, 
                 members_of_row:int, 
                 choose_distribution:int, 
                 choose_model:int) -> None:
        self.sample_size = sample_size
        self.members_of_row = members_of_row
        self.choose_distribution = choose_distribution
        self.choose_model = choose_model
        self.teoretical = []
        pass

    @property
    def message(self)->str:
        comprasion = Comprasion(self.teoretical, self.density_function)
        return 'X2 = {:3f}   | D = {:3f} \n'.format(comprasion.X2, comprasion.deviation)
    
    @property
    def density_function(self) -> List[int]:
        # nPoint = sampleSize
        # kMember = membersOfRow
        # viewLimits = getViewLimits(chooseDistribution)

        # randomVariables = getRandomVariables(nPoint, chooseDistribution)
        # fourierTransform = FourierTransform(randomVariables,
        #                                     nPoint,
        #                                     kMember,
        #                                     viewLimits)
        # return fourierTransform.getEstmation(chooseModel)
        return []
    
    def show(self):
        pass
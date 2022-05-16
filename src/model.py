import pyenzyme as pe

from zntrack import Node, zn

class Model(Node):
    
    # Dependencies
    data: pe.EnzymeMLDocument = zn.deps()
    
    # Inputs
    reaction: str = zn.params()
    equation: str = zn.params()
    config: dict = zn.params({})
    
    # Outputs
    enzmldoc: pe.EnzymeMLDocument = zn.outs()
    
    def run(self):
        """Adds the models to the according reactions"""
        
        # Fetch the reaction
        reaction = self.data.enzmldoc.reaction_dict[self.reaction]
        
        # Create the model
        equation = self._replace_names_with_ids(self.equation)
        model = pe.KineticModel.fromEquation(name=f"Model_{self.reaction}", equation=equation)
        
        # For demo, apply any init values
        for parameter in model.parameters:
            param_config = self.config.get(parameter.name)
            
            if param_config:
                parameter.value = param_config.get("value")
                parameter.initial_value = param_config.get("initial_value")
                parameter.lower = param_config.get("lower")
                parameter.upper = param_config.get("upper")
                parameter.unit = param_config.get("unit")
            else:
                raise ValueError(
                    f"Please specify at least an `initial value` for parameter `{parameter.name}`"
                )
        
        # Add model to reaction
        reaction.model = model
        
        self.enzmldoc = self.data.enzmldoc.copy(deep=True)
        
        
    def _replace_names_with_ids(self, equation):
        """Replaces names with IDs to maintain consistency"""
        
        all_species = {
            **self.data.enzmldoc.reactant_dict,
            **self.data.enzmldoc.protein_dict,
            **self.data.enzmldoc.complex_dict
        }.values()
        
        for species in all_species:
            equation = equation.replace(species.name, species.id)
            
        return equation
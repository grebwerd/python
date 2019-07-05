from builder import Builder

class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """
    def _build_part_a(self):
        pass
    
    def _build_part_b(self):
        pass
    
    def _build_part_c(self):
        pass

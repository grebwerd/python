from concrete_builder import ConcreteBuilder
from director import Director
from animal import Animal

def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product

if __name__ == "__main__":
    main()
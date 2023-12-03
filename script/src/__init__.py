from .MacroSelect import MacroSelect


def create_instance(c_instance):
    """Creates and returns Remote Script instance"""
    return MacroSelect(c_instance)

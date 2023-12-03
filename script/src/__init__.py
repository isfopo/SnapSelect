from .SnapSelect import SnapSelect


def create_instance(c_instance):
    """Creates and returns Remote Script instance"""
    return SnapSelect(c_instance)

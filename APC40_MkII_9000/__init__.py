from APC40_MkII import get_capabilities as parent_capabilities
from .APC40_MkII_9000 import APC40_MkII_Plus


def create_instance(c_instance):
    return APC40_MkII_Plus(c_instance)


def get_capabilities():
    return parent_capabilities()

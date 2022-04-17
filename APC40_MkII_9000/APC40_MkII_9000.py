import logging
import os

from _Framework.ControlSurface import logger

from APC40_MkII import APC40_MkII
from pushbase.step_seq_component import StepSeqComponent


class APC40_MkII_9000(APC40_MkII):
    """Extension of APC40 MkII remote control script
    """
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        with self.component_guard():
            self._init_step_sequencer()

    def _init_step_sequencer(self):
        pass

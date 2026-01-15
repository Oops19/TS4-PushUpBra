#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from push_up_bra.pie_ctrl.ctrl_sim import CtrlSim

from typing import Any

from interactions.context import InteractionContext
from sims.sim import Sim
from sims4.tuning.tunable import Tunable

from sims4communitylib.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from sims4communitylib.classes.testing.common_execution_result import CommonExecutionResult
from sims4communitylib.classes.testing.common_test_result import CommonTestResult


class PieSim(CommonImmediateSuperInteraction):
    INSTANCE_TUNABLES = {
        'slider_f_small': Tunable(tunable_type=int, default=8840277215316813897),
        'slider_m_small': Tunable(tunable_type=int, default=8840277215316813897),
        'value_small': Tunable(tunable_type=float, default=0.0),
        'slider_f_big': Tunable(tunable_type=int, default=8467641399601199718),
        'slider_m_big': Tunable(tunable_type=int, default=8467641399601199718),
        'value_big': Tunable(tunable_type=float, default=0.0),
    }

    __slots__ = {'slider_f_small', 'slider_m_small', 'value_small', 'slider_f_big', 'slider_m_big', 'value_big', }

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        return CtrlSim.on_test(cls, interaction_sim, interaction_target, interaction_context, **kwargs)

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> CommonExecutionResult:
        return CtrlSim().on_started(self, interaction_sim, interaction_target)

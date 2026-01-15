#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from push_up_bra.bra_main import BraMain

from typing import Any

from interactions.context import InteractionContext
from sims.outfits.outfit_enums import OutfitCategory, SpecialOutfitIndex

from sims.sim import Sim
from sims.sim_info import SimInfo
from sims4communitylib.classes.testing.common_execution_result import CommonExecutionResult
from sims4communitylib.classes.testing.common_test_result import CommonTestResult
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils


class CtrlSim:
    @classmethod
    def on_test(cls, caller, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        interaction_sim_info: SimInfo = CommonSimUtils.get_sim_info(interaction_sim)

        # don't show for other sims
        target_sim_info: SimInfo = CommonSimUtils.get_sim_info(interaction_target)
        if interaction_sim_info != target_sim_info:
            return CommonTestResult.FALSE

        # don't show foy BITCh
        if CommonAgeUtils.is_baby_infant_toddler_or_child(target_sim_info):
            return CommonTestResult.FALSE

        # don't show if the outfit can't be retrieved
        outfit_category_and_index = CommonOutfitUtils.get_current_outfit(interaction_sim_info)
        if not isinstance(outfit_category_and_index, tuple) or not len(outfit_category_and_index) == 2:
            return CommonTestResult.FALSE

        # don't show for bathing and towel
        outfit_category, outfit_index = outfit_category_and_index
        if isinstance(outfit_category, OutfitCategory):
            outfit_category = outfit_category.value
        if outfit_category == OutfitCategory.BATHING.value or outfit_category == OutfitCategory.SPECIAL.value and outfit_index == SpecialOutfitIndex.TOWEL:
            return CommonTestResult.FALSE

        return CommonTestResult.TRUE

    def on_started(self, caller, interaction_sim: Sim, interaction_target: Any) -> CommonTestResult:
        BraMain().process_interaction(caller, interaction_sim, interaction_target)
        return CommonExecutionResult.TRUE

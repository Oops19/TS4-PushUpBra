#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from caches import cached
from objects.script_object import ScriptObject
from sims.sim_info import SimInfo

from sims4communitylib.utils.common_type_utils import CommonTypeUtils
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils


class CtrlSimReg:
    @staticmethod
    @cached
    def should_add(caller, script_object: ScriptObject, *args, **kwargs) -> bool:
        if CommonTypeUtils.is_sim_or_sim_info(script_object) or CommonTypeUtils.is_sim_info_base_wrapper(script_object):
            sim_info: SimInfo = CommonSimUtils.get_sim_info(script_object)
            return CommonAgeUtils.is_teen_adult_or_elder(sim_info)
        return False

#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from push_up_bra.modinfo import ModInfo
from push_up_bra.bra_main import BraMain

from sims.sim_info_base_wrapper import SimInfoBaseWrapper

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'OutfitChangeListener')
log.enable()


class OutfitChangeListener:
    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfoBaseWrapper, SimInfoBaseWrapper._set_current_outfit_without_distribution.__name__, handle_exceptions=False)
    def bra_set_current_outfit_without_distribution(original, self, *args, **kwargs):
        try:
            BraMain().change_outfit(self, *args, **kwargs)
        except Exception as e:
            log.warn(f"Error occurred changing outfit '{e}'.")
        return original(self, *args, **kwargs)

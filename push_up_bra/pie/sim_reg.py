#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Tuple
from objects.script_object import ScriptObject
from push_up_bra.pie_ctrl.ctrl_sim_reg import CtrlSimReg
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class PieSimReg(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0x137EC274CF038747,  # 'None' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUp_Bra_PMA_PieSim_None')
            0x2F34948021192E44,  # 'Medium' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUp_Bra_PMA_PieSim_Medium')
            0x713965D4DEEB5209,  # 'Voluptuous' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUp_Bra_PMA_PieSim_Voluptuous')
            0x4CDB51CF2925224F,  # 'Extreme' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUp_Bra_PMA_PieSim_Extreme')
            0x7022C00E14B204B1,  # 'Overdrive' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUp_Bra_PMA_PieSim_Overdrive')
            0xA2D78DF85BCB65B1,  # 'Vanilla' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8re_PMA_PieSim_Vanilla')
            0x2C03BCFD558D37DD,  # 'Sports Bra' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8re_PMA_PieSim_Sports_Bra')
            0x77D207608E31A207,  # 'Über-Slim' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8re_PMA_PieSim_xDCberx2DSlim')
            0x368DCB653FB47A29,  # 'None' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Thighs_PMA_PieSim_None')
            0x7EF08D64D73889C4,  # 'Slim' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Thighs_PMA_PieSim_Slim')
            0xD42C5ADA88715F06,  # 'Mega-Slim' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Thighs_PMA_PieSim_Megax2DSlim')
            0xA8EDDA2FF28D0E8A,  # 'Thick' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Thighs_PMA_PieSim_Thick')
            0x62F9A321853FBB4F,  # 'Voluptuous' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Thighs_PMA_PieSim_Voluptuous')
            0xBE474E68DB0A5FF7,  # 'Vanilla Butt' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Panties_PMA_PieSim_Vanilla_Butt')
            0xDE15B5D763CAC004,  # 'Round Butt' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Panties_PMA_PieSim_Round_Butt')
            0xA713A2FEE46BF5BA,  # 'Tiny Butt' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Panties_PMA_PieSim_Tiny_Butt')
            0xF0D04C68F7410C16,  # 'Vanilla Hips' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Panties_PMA_PieSim_Vanilla_Hips')
            0x48A72F5C7DBBF5EE,  # 'Wide Hips' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Panties_PMA_PieSim_Wide_Hips')
        )
        return interactions


    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return CtrlSimReg().should_add(self, script_object)

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
            0xF922DA17125636E9,  # 'Vanilla Bra' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUps_PMA_PieSim_Vanilla_Bra')
            0xB2708F8CBBED7FDD,  # 'Curvy Charm' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUps_PMA_PieSim_Curvy_Charm')
            0x00C31FBFF9D21A6D,  # 'Wonder Bra' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUps_PMA_PieSim_Wonder_Bra')
            0x32E988A9D7022B2C,  # 'Double Dare' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUps_PMA_PieSim_Double_Dare')
            0x9DD4AD399FAD59C0,  # 'Voluptuous' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUps_PMA_PieSim_Voluptuous')
            0x728C33D407B7903A,  # 'Bombshell' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Pushx2DUps_PMA_PieSim_Bombshell')
            0x266CBC5FEA2BE1C4,  # 'Vanilla' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8res_PMA_PieSim_Vanilla')
            0xAB6E3582A541A942,  # 'Light Sport' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8res_PMA_PieSim_Light_Sport')
            0xC3D72B95CC835783,  # 'Sport' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8res_PMA_PieSim_Sport')
            0x1179E86B9F19CFC2,  # 'Über-Slim' - fnv('o19_PushUpBra_PMC__142150__Lingerie__BrassixE8res_PMA_PieSim_xDCberx2DSlim')
            0x7C07A322D51E2CE4,  # 'Vanilla Thighs' - fnv('o19_PushUpBra_PMC__142150__Lingerie__Thighs_PMA_PieSim_Vanilla_Thighs')
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

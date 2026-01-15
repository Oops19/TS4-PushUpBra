#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#
from push_up_bra.enums.pie_slider import PieSlider
from push_up_bra.modinfo import ModInfo

from ts4lib.custom_enums.custom_slider import CustomSlider
from ts4lib.enums.sim_modifier import SimModifier
from ts4lib.utils.singleton import Singleton
from ts4lib.utils.sliders.manage_sliders import ManageSliders

from typing import Any, Union, Dict, Set

from sims.outfits.outfit_enums import OutfitCategory, SpecialOutfitIndex
from sims.sim import Sim
from sims.sim_info import SimInfo
from sims.sim_info_base_wrapper import SimInfoBaseWrapper

from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
from sims4communitylib.utils.sims.common_gender_utils import CommonGenderUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'BraMain')
log.enable()


class BraMain(metaclass=Singleton):
    def __init__(self):
        self.ms = ManageSliders()
        self.modifier = CustomSlider.BLOB_SIM_BODY_MODIFIER
        self.slider_keys: Set[int] = set()

        # Register local sliders within TS4L
        _sliders: Dict[str, int] = {}
        for k, v in PieSlider.__members__.items():
            value = v.value
            self.slider_keys.add(value)
            _sliders.update({value: k})
        log.debug(f"{_sliders}")  # TODO
        SimModifier.MAP.update(_sliders)
        log.debug(f"{SimModifier.MAP}")  # TODO

    def process_interaction(self, caller, interaction_sim: Sim, interaction_target: Any):
        r"""
        :param caller:
        :param interaction_sim:
        :param interaction_target:
        :return:
        """
        slider_f_small: int = getattr(caller, 'slider_f_small', 0)
        slider_m_small: int = getattr(caller, 'slider_m_small', 0)
        value_small: float = getattr(caller, 'value_small', 0.0)
        slider_f_big: int = getattr(caller, 'slider_f_big', 0)
        slider_m_big: int = getattr(caller, 'slider_m_big', 0)
        value_big: float = getattr(caller, 'value_big', 0.0)
        log.debug(f"process_interaction({interaction_sim}, {interaction_target}: {type(interaction_target)}, s={value_small}, b={value_big}")

        sim_info = CommonSimUtils.get_sim_info(interaction_sim)
        if CommonGenderUtils.is_female(sim_info):
            slider_small = slider_f_small
            slider_big = slider_f_big
        else:
            slider_small = slider_m_small
            slider_big = slider_m_big
        self.ms.slide_to(sim_info, self.modifier, slider_small, value_small)
        self.ms.slide_to(sim_info, self.modifier, slider_big, value_big)
        log.debug(f"'{sim_info} slider {PieSlider(slider_small).name} = {value_small:.2f}")
        log.debug(f"'{sim_info} slider {PieSlider(slider_big).name} = {value_big:.2f}")

    def change_outfit(self, sim_info: Union[SimInfo, SimInfoBaseWrapper], *args, **kwargs):
        # log.debug(f"change_outfit({sim_info}: {type(sim_info)}; {args}; {kwargs})")

        outfit_category_and_index = args[0]
        if isinstance(sim_info, SimInfoBaseWrapper):
            sim_id = CommonSimUtils.get_sim_id(sim_info)
            sim_info: SimInfo = CommonSimUtils.get_sim_info(sim_id)
        if sim_info is None:
            log.debug(f"sim_info is None")
        if isinstance(sim_info, SimInfo):
            sim_id = CommonSimUtils.get_sim_id(sim_info)
        else:
            log.warn(f"Expected SimInfo/SimInfoBaseWrapper. Got: '{sim_info}: {type(sim_info)}'")
            return

        if not isinstance(outfit_category_and_index, tuple) or not len(outfit_category_and_index) == 2:
            log.warn(f"Expected Tuple(outfit_category, outfit_index). Got: '{outfit_category_and_index}: {type(outfit_category_and_index)}'")
            return

        outfit_category, outfit_index = outfit_category_and_index
        if isinstance(outfit_category, OutfitCategory):
            outfit_category = outfit_category.value
        outfit_id = outfit_category * 100 + outfit_index
        log.debug(f"change_outfit({sim_id}, {outfit_category}, {outfit_index}; {outfit_id})")

        if outfit_category == OutfitCategory.BATHING.value or outfit_category == OutfitCategory.SPECIAL.value and outfit_index == SpecialOutfitIndex.TOWEL:
            slider_value = 0
            for slider_key in self.slider_keys:
                self.ms.slide_to(sim_info, self.modifier, slider_key, slider_value)
            self.ms.slide_to(sim_info, self.modifier, slider_key, slider_value)
            log.info(f"'{sim_info}' removed all temporary body modifications")


r"""
o19_slider_b_push_up_bra
FF4D927BBBD4A00E 18396521113008250894

"Instance": "0x949E5305DB22495D", 10709088248550017373
"Name": "o19_slider_f_push_up_bra"
o19.ts4l.slider.set 2 10709088248550017373 1
o19.ts4l.slider.set 2 10709088248550017373 0

"Instance": "0x982FD3F9B5E13FE3", 10966216687122202595
"Name": "o19_slider_m_push_up_bra"
o19.ts4l.slider.set 2 10966216687122202595 1
o19.ts4l.slider.set 2 10966216687122202595 0

"""
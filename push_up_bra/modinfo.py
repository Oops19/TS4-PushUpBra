#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'PushUpBra'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'push_up_bra'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '0.0.6'


r"""
v0.0.6
    Rename the slider package from '_o19_/o19_slider_ts4.package' to '_o19_/pushupbra_slider.package' 
v0.0.5
    Update the icon
v0.0.4
    Remove push-up bra when changing into swimwear.
v0.0.3
    Double chest sliders
    Show 'Brassières > Sport' bra
v0.0.2
    Fix sim_info is None check
    Fix TOWEL check
v0.0.1 Initial version
"""
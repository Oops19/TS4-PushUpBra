
from ts4lib.custom_enums.enum_types.custom_enum import CustomIntEnum


class PieSlider(CustomIntEnum):
    NONE = 0

    o19_yfheadBelly_Small = 0x409BB05423A4E74A
    o19_yfheadButt_Big = 0x2288DCC35CB309F2
    o19_yfheadButt_Small = 0x4A107A70BE2411A5
    o19_yfheadHips_Narrow = 0xBDBC907224894732
    o19_yfheadHips_Wide = 0x7107D8C7701C84A2
    o19_yfheadThighs_Big = 0x247511C4477175C6
    o19_yfheadThighs_Small = 0xF392E53ACCCA48A9
    o19_ymheadBelly_Small = 0x255799F81CEA19BF
    o19_ymheadButt_Big = 0xB1290A22AC93CC59
    o19_ymheadButt_Small = 0x889A272D7308D626
    o19_ymheadHips_Narrow = 0xA92AE38C173EE873
    o19_ymheadHips_Wide = 0xE3A7279AC9ACD0C3
    o19_ymheadThighs_Small = 0xA861D34BA8CCAE86
    o19_ymheadThighs_Big = 0xC37D54EA731D76B9
    o19_yfheadChest_Small = 0x7AAEF94A1EF02849
    o19_yfheadChest_Big = 0x75831AFD4C9EFA66
    o19_yfheadChest_Small_2 = 0xE88F432E38C1AA8E
    o19_yfheadChest_Big_2 = 0x8FDEE5C0324A1725

    r"""
    @classmethod
    def _missing_(cls, value):
        return cls.NONE
    """
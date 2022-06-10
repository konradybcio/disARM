architecture_dict = {
        0b0000: "Unknown (0b0000)",
        0b0001: "Armv4",
        0b0010: "Armv4T",
        0b0011: "Armv5 (obsolete)", # you don't say, xD
        0b0100: "Armv5T",
        0b0101: "Armv5TE",
        0b0111: "Armv6",
        0b1111: "Unknown (0b1111)"
}

implementer_dict = {
        0x00: "QEMU",
        0x3e: "Nvidia Corp.",
        0x41: "ARM Ltd.",
        0x42: "Broadcom Corp.",
        0x43: "Cavium Inc.",
        0x44: "Digital Equipment Corp.",
        0x46: "Fujitsu Ltd.",
        0x48: "HiSilicon Technologies Inc.",
        0x51: "Qualcomm Inc.",
        0x53: "Samsung",
        0x54: "Texas Instruments",
        0x61: "Apple Inc."
}

partnum_doubledict = {
        "Apple Inc.": {
                0x01: "A7 Cyclone",
                0x02: "A8 Typhoon",
                0x03: "A8X Typhoon",
                0x04: "A9 Twister",
                0x05: "A9X Twister",
                0x06: "A10 Hurricane",
                0x07: "A10X Hurricane (Myst)",
                0x08: "A11 Monsoon [e-core]",
                0x09: "A11 Mistral [p-core]",
                # 0x0a is unknown apparently
                0x0b: "A12 Vortex [p-core]",
                0x0c: "A12 Tempest [e-core]",
                # 0x0d-0x0e are unknown apparently
                0x0f: "S4/S5 Tempest [yes, on the watch]",
                0x10: "A12X/A12Z Vortex [p-core]",
                0x11: "A12X/A12Z Tempest [e-core]",
                0x12: "A13 Lightning [p-core]",
                0x13: "A13 Thunder [e-core]",
                # Another big gap
                0x20: "A14 Icestorm [e-core]",
                0x21: "A14 Firestroem [p-core]",
                0x22: "M1 Icestorm [e-core]",
                0x23: "M1 Firestorm [p-core]",
                # Gaaap!
                0x26: "S6/S7 Thunder [yes, on the watch]"
        }
}

# Matrices for checking whether a feature is supported
# [feature_name, start_bit, stop_bit]
isar0_matrix = [
        # 0-3 reserved
        ["AES", 4, 7],
        ["SHA1", 8, 11],
        ["SHA2", 12, 15],
        ["CRC32", 16, 19],
        ["ATOMICS", 20, 23],
        # 24-27 reserved
        ["RDM", 28, 31],
        ["SHA3", 32, 35],
        ["SM3", 36, 39],
        ["SM4", 40, 43],
        ["DP", 44, 47],
        ["FHM", 48, 51],
        ["TS", 52, 55],
        # 56-59 reserved
        ["RNDR", 60, 63]
]

pfr0_matrix = [
        ["EL0", 0, 3],
        ["EL1", 4, 7],
        ["EL2", 8, 11],
        ["EL3", 12, 15],
        ["FP", 16, 19],
        ["AdvSIMD", 20, 23],
        ["GIC", 24, 27],
        # 28-31 reserved
        ["SVE", 32, 35],
        # 36-47 reserved
        ["DIT", 48, 51]
        # 52-63 reserved
]

pfr1_matrix = [
        ["BT", 0, 3],
        ["SSBS", 4, 7],
        ["MTE", 8, 11],
        # 12 - 63 reserved
]

# Matrices for features with >2 possibilities
# [name, dict with possible values, start_bit, stop_bit]
clidr_matrix = [
        [
                "CType1",
                {
                        0b011: "Separate instruction and data caches at L1."
                },
                0, 2
        ],
        [
                "CType2",
                {
                        0b100: "L2 cache is implemented as a unified cache."
                },
                3, 5
        ],
        [
                "Ctype3",
                {
                        0b000: "Both per-core L2 and cluster L3 caches are present.",
                        0b100: "It is not true that both per-core L2 and cluster L3 caches are present."
                },
                6, 8
        ],
        # 9 - 20 reserved
        [
                "LoUIS",
                {
                        0b000: "No cache level needs cleaning to Point of Unification."
                },
                21, 23
        ],
        [
                "LoC",
                {
                        0b010: "L3 cache is not implemented",
                        0b011: "L3 cache is implemented"
                },
                24, 26
        ],
        [
                "LoUU",
                {
                        0b000: "No levels of cache need to be cleaned or invalidated when cleaning or invalidating to the Point of Unification. This is the value if no caches are configured"
                },
                27, 29
        ],
        [
                "ICB",
                {
                        0b010: "L2 cache is the highest inner level",
                        0b011: "L3 cache is the highest inner level"
                },
                30, 32
        ]
]

midr_matrix = [
        [
                "Part number",
                partnum_doubledict,
                4, 15
        ],
        [
                "Architecture",
                architecture_dict,
                16, 19
        ],
        [
                "Implementer",
                implementer_dict,
                24, 31
        ]
]

mmfr0_matrix = [
        [
                "PARange",
                {
                        0b0000: "32-bit / 4G",
                        0b0001: "36-bit / 64GB",
                        0b0010: "40-bit / 1TB",
                        0b0011: "42-bit / 4TB",
                        0b0100: "44-bit / 16TB",
                        0b0101: "48-bit / 256TB",
                        0b0110: "52-bit / 4PB if FEAT_LPA, otherwise reserved"
                },
                0, 3
        ],
        [
                "ASIDbits",
                {
                        0b0000: "8 bits",
                        0b0001: "16 bits"
                },
                4, 7
        ],
        [
                "BigEnd",
                {
                        0b0000: "No mixed-endian support.",
                        0b0001: "Mixed-endian support."
                },
                8, 11
        ],
        [
                "SNSMem",
                {
                        0b0000: "Does not support a distinction between Secure and Non-secure Memory.",
                        0b0001: "Does support a distinction between Secure and Non-secure Memory."
                },
                12, 15
        ],
        [
                "BigEndEL0",
                {
                        0b0000: "No mixed-endian support at EL0",
                        0b0001: "Mixed-endian support at EL0"
                },
                16, 19
        ],
        [
                "TGran16",
                {
                        0b0000: "16KB granule not supported.",
                        0b0001: "16KB granule supported.",
                        0b0010: "16KB granule supports 52-bit input and output addresses. (When FEAT_LPA2 is implemented!)"
                },
                20, 23
        ],
        [
                "TGran64",
                {
                        0b0000: "64KB granule supported.",
                        0b0001: "64KB granule not supported."
                },
                24, 27
        ],
        [
                "TGran4",
                {
                        0b0000: "4KB granule supported.",
                        0b0001: "4KB granule supports 52-bit input and output addresses (When FEAT_LPA2 is implemented!)",
                        0b1111: "4KB granule not supported."
                },
                28, 31
        ],
        [
                "TGran16_2",
                {
                        0b0000: "Support for 16KB granule at stage 2 is identified in the ID_AA64MMFR0_EL1.TGran16 field.",
                        0b0001: "16KB granule not supported at stage 2.",
                        0b0010: "16KB granule supported at stage 2.",
                        0b0011: "16KB granule at stage 2 supports 52-bit input and output addresses. (When FEAT_LPA2 is implemented!)"
                },
                32, 35
        ],
        [
                "TGran64_2",
                {
                        0b0000: "Support for 64KB granule at stage 2 is identified in the ID_AA64MMFR0_EL1.TGran64 field.",
                        0b0001: "64KB granule not supported at stage 2.",
                        0b0010: "64KB granule supported at stage 2."
                },
                36, 39
        ],
        [
                "TGran4_2",
                {
                        0b0000: "Support for 4KB granule at stage 2 is identified in the ID_AA64MMFR0_EL1.TGran4 field.",
                        0b0001: "4KB granule not supported at stage 2.",
                        0b0010: "4KB granule supported at stage 2.",
                        0b0011: "4KB granule at stage 2 supports 52-bit input and output addresses. (When FEAT_LPA2 is implemented!)"
                },
                40, 43
        ],
        [
                "ExS",
                {
                        0b0000: "All exception entries and exits are context synchronization events.",
                        0b0001: "Non-context synchronizing exception entry and exit are supported."
                },
                44, 47
        ],
        # 48-55 reserved
        [
                "FGT",
                {
                        0b0000: "The fine-grained trap controls are not implemented.",
                        0b0001: "The fine-grained trap controls are implemented."
                },
                56, 59
        ],
        [
                "ECV",
                {
                        0b0000: "Enhanced Counter Virtualization is not implemented.",
                        0b0001: "Enhanced Counter Virtualization is implemented",
                        0b0010: "Enhanced Counter Virtualization is implemented and also includes support for CNTHCTL_EL2.ECV and CNTPOFF_EL2."
                },
                60, 63
        ]
]

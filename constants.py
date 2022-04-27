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
                0x03: "A8X Typhoon"
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

mmfr0_matrix = [
        # 0 - 59 reserved
        ["ECV", 60, 63]
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

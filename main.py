# SPDX-License-Identifier: GPL-2.0-only

import constants

def gen_bitmask(start, stop):
        i = 0
        ret = 0

        if start > stop:
                raise Exception(f"The start bit ({start}) is higher than stop ({stop})!")
        
        if start == stop:
                return 1 << start
        
        while i < (stop - start):
                ret |= 1 << (start+i)
                i += 1

        return ret

def get_nth_bits(val, start, stop):
        return (val & gen_bitmask(start, stop)) >> start

def dict_value_if_known(d: dict, key):
        return d[key] if key in d.keys() else f"Unknown ({bin(key)})"

def doubledict_value_if_known(dd: dict, key1, key2):
        if key1 in dd.keys():
                if key2 in dd[key1].keys():
                        return dd[key1][key2]
        return f"Unknown ({key1}, {bin(key2)})"

def supported_or_not(val, mask):
        return "√" if val & mask > 0 else "X"

def print_supported_features(val, mtx):
        for i in range(len(mtx)):
                print(f"{mtx[i][0]}: {supported_or_not(val, gen_bitmask(mtx[i][1], mtx[i][2]))}")

def print_features(val, mtx, implementer):
        for i in range(len(mtx)):
                # Yay, special case for partnum..
                if isinstance(list(mtx[i][1].values())[0], dict):
                        ret = doubledict_value_if_known(mtx[i][1], implementer, get_nth_bits(val, mtx[i][2], mtx[i][3]))
                        print(f"{mtx[i][0]}: {ret}")
                        continue
                ret = dict_value_if_known(mtx[i][1], get_nth_bits(val, mtx[i][2], mtx[i][3]))
                print(f"{mtx[i][0]}: {ret}")


# reg_name, corresponding_matrix, is_simple
supported_regs = [
        ["ID_AA64MMFR0_EL1", constants.mmfr0_matrix, True],
        ["ID_AA64ISAR0_EL1", constants.isar0_matrix, True],
        ["ID_AA64PFR0_EL1", constants.pfr0_matrix, True],
        ["ID_AA64PFR1_EL1", constants.pfr1_matrix, True],
        ["CLIDR_EL1", constants.clidr_matrix, False],
        ["MIDR_EL1", constants.midr_matrix, False]
]

def main():
        n_regs = len(supported_regs)
        input_arr = [None for _ in range(n_regs)]

        for i in range(n_regs):
                input_arr[i] = int(input(f"Please input the value of {supported_regs[i][0]}: "), base=16)

        print()
        print("------")
        print()

        # Hacky, but implementer value is needed for partnum, eh..
        implementer = constants.implementer_dict[get_nth_bits(input_arr[5], 24, 31)]

        for i in range(n_regs):
                print(f"* {supported_regs[i][0]}:")
                if supported_regs[i][2]:
                        print_supported_features(input_arr[i], supported_regs[i][1])
                else:
                        print_features(input_arr[i], supported_regs[i][1], implementer)
                print()


if __name__ == "__main__":
        main()
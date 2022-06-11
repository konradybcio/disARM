# SPDX-License-Identifier: GPL-2.0-only

import ast
import constants
import sys

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
supported_regs = {
        "ID_AA64MMFR0_EL1": [constants.mmfr0_matrix, False],
        "ID_AA64MMFR1_EL1": [constants.mmfr1_matrix, False],
        "ID_AA64ISAR0_EL1": [constants.isar0_matrix, True],
        "ID_AA64PFR0_EL1": [constants.pfr0_matrix, True],
        "ID_AA64PFR1_EL1": [constants.pfr1_matrix, True],
        "CLIDR_EL1": [constants.clidr_matrix, False],
        "MIDR_EL1": [constants.midr_matrix, False]
}

def main():
        implementer = None
        input_dict = {}

        if len(sys.argv) > 1:
                if sys.argv[1] != "main.py":
                        filename = sys.argv[1]
                if len(sys.argv) == 2:
                        filename = sys.argv[1]
                with open(filename, "r") as f:
                        file_data = f.readline()
                        try:
                                input_dict = ast.literal_eval(file_data)
                        except:
                                Exception("The file does not contain a valid dictionary.")
        else:
                for key in supported_regs.keys():
                        input_dict[key] = int(input(f"Please input the value of {key} (in hex): "), base=16)
                
                with open("output.dict", "w+") as f:
                        f.write(str(input_dict))

        print()
        print("------")
        print()

        for key in input_dict:
                if key == "MIDR_EL1":
                        implementer = constants.implementer_dict[get_nth_bits(input_dict[key], 24, 31)]

                print(f"* {key}:")
                if supported_regs[key][1]:
                        print_supported_features(input_dict[key], supported_regs[key][0])
                else:
                        print_features(input_dict[key], supported_regs[key][0], implementer)

                # Newline to make it look half-decent
                print()


if __name__ == "__main__":
        main()
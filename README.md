# disARM

Ever had to re-do the same janky bit extractions and then look it up in the arm docs over and over and over and over again? Fear no more!


For testing, you can use the values extracted from an Apple iPhone 5S (Apple A7 SoC):

```
"ID_AA64MMFR0_EL1":     0x11021
"ID_AA64MMFR1_EL1":     0x0
"ID_AA64ISAR0_EL1":	0x1110
"ID_AA64PFR0_EL1":	0x1012
"ID_AA64PFR1_EL1":	0x0
"CLIDR_EL1":            0x9200023
"MIDR_EL1":		0x611f0011
```

..or any other from the known_values directory, by simply providing the filename as an argument.


If you came here to help with Apple SoC mainlining, you may easily get these registers by running the `dump` command in [pongoOS from my fork](https://github.com/konradybcio/pongoOS):

```
[boot pongo blah blah, cd to pongo dir]

python3 scripts/issue_cmd.py dump

(or use pongoterm)
```
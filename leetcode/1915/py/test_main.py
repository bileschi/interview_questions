import main
import unittest


class TestMain(unittest.TestCase):
    def test_basic(self):
        s = main.Solution()
        self.assertEqual(4, s.wonderfulSubstrings(word="aba"))
        self.assertEqual(9, s.wonderfulSubstrings(word="aabb"))
        self.assertEqual(2, s.wonderfulSubstrings(word="he"))
        self.assertEqual(
            3614,
            s.wonderfulSubstrings(
                word="bibacdfehgbchbjicccecacbdeiggideciijgbahifjjhdeddeabbfihb"
                "egbagcgbidefijigabfjhbdjfiihggdbjacgjccidedajgaabdibcdfjfjfeif"
                "efdeachbcbdadggiagbdfigjadeaadfbadhfjgifeeaagiabddicdejcgaejcd"
                "gffggdddffideijchchaffgjhfeaffhbfahieggdahdbeijfjbeaciagfjjbcj"
                "dbjgdfeefbgjfhcbajbdghgeieiahadebeiabjedjhbfbhfhajcieibaejefbf"
                "eihebbjgciceibbabddcaeehdfdhbeeeffdijfghdfeedfcccfchjhdjddfgeh"
                "iccdggbdjjghicagdhceiaebfhjhbefghjjcbjbjbfbbdhhdbdbceejaffbdbi"
                "daefihcjagaibhihbebhjfggbddhedfcacagegfaiiaeheiggjhfaegffdicge"
                "babceaahjeegafgjgfejfeheafidabjbgafjcdgffdafcgecjdjefcbhefbfgh"
                "gsegfegdabjiicihfdbjjiehjfbjfhgaeacjgfbggggjegffgbabafdhbbiadg"
                "fcbfcicjagceeibhagieiddjjhcjdidccgjfbgihadhhjihgdaheibigihefac"
                "fbdgfiefehgjbbcggccfcibhbhhjjagjhehciejafbhjeicaieagjagdaaaddf"
                "giibgicgjghdjiddaeihbcbccbfjigdjcachhdcgfheaacfhfajefbccgjcdca"
                "ahjaaedcibbjgggajaceijababjafbaccfiffcbedjc"
            ),
        )


if __name__ == "__main__":
    unittest.main()

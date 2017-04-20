import unittest
from carpp import parse_pdf


class TestFunctions(unittest.TestCase):
    def test_merge_invalid_input(self):
        rows = [
                [u'2008', u'TL', u'', u'', u'3.2L 6CYL', u'4DR SDN', u'GREY',
                    u'142,904', u'$3,600', u'19UUA66208', u'Consignment', u'']]
        self.assertIsNone(parse_pdf.merge_rows(rows))

    def test_merged_rows(self):
        rows = [
                [u'2008', u'TL', u'', u'', u'3.2L 6CYL', u'4DR SDN', u'GREY',
                    u'142,904', u'$3,600', u'19UUA66208', u'Consignment', u''],
                [u'', u'', u'', u'', u'GASOLINE', u'AUTO', u'', u'', u'',
                    u'', u'Sale', u''],
                [u'', u'', u'', u'', u'FUEL', u'', u'', u'', u'', u'', u'',
                    u'']]

        hand_merged = [u'2008', u'TL', u'', u'',
                u'3.2L 6CYL GASOLINE FUEL', u'4DR SDN AUTO', u'GREY',
                u'142,904', u'$3,600', u'19UUA66208', u'Consignment Sale', u'']

        func_merged = parse_pdf.merge_rows(rows)
        self.assertEqual(func_merged, hand_merged)

if __name__ == '__main__':
    unittest.main()

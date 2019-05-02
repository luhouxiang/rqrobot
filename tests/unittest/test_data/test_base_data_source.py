from rqrobot.utils.testing import BaseDataSourceFixture, rqrobotTestCase, mock_instrument


class BaseDataSourceTestCase(BaseDataSourceFixture, rqrobotTestCase):
    def test_get_tick_size(self):
        self.assertEqual(self.base_data_source.get_tick_size(mock_instrument(exchange="XSHE")), 0.01)
        self.assertEqual(self.base_data_source.get_tick_size(mock_instrument(_type="FenjiA")), 0.001)
        self.assertEqual(self.base_data_source.get_tick_size(mock_instrument(_type="INDX")), 0.01)
        self.assertEqual(self.base_data_source.get_tick_size(
            mock_instrument(_type="Future", underlying_symbol="SM")
        ), 2)
        with self.assertRaises(RuntimeError):
            self.base_data_source.get_tick_size(mock_instrument(_type=None))

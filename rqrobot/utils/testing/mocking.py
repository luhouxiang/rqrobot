def mock_instrument(order_book_id="000001", _type="CS", exchange="XSHE", **kwargs):
    from rqrobot.model.instrument import Instrument

    ins_dict = {
        "order_book_id": order_book_id,
        "type": _type,
        "exchange": exchange,
    }
    ins_dict.update(kwargs)

    return Instrument(ins_dict)


def mock_bar(instrument, **kwargs):
    from rqrobot.model.bar import BarObject
    return BarObject(instrument, kwargs)


def mock_tick(instrumnet, **kwargs):
    from rqrobot.model.tick import TickObject
    return TickObject(instrumnet, kwargs)

#!/usr/local/meshtastic/bin/python3

from getnodes import buffertoprotobufs


def test():
    print("test start")
    td = []
    td.append(
        b'\x94\xc3\x00S"Q\x08\x80\xde\x96\xd3\r\x12&\n\t!da65af00\x12\x07M0OFC 0\x1a\x04OFC0"\x064\xb7\xdae\xaf\x00(+8\x03\x1a\x05%T\xee<f%\x00\x00TA-\xf2\x08=f2\x10\x08T\x15u\x93\x80@%P\xd9\xc1>(\xd7\xb1\x19\x94\xc3\x00i"g\x08\xfc\xe6\x94\x97\x0e\x12/\n\t!e2e5337c\x12\x11Wishing Tree Base\x1a\x03WTB"\x06H\'\xe2\xe53|(+0\x01\x1a\x11\r_\x9dQ\x1e\x15\xac;R\x00\x18U%\'Y<f%\x00\x00\x82\xc1-!d<f2\x11\x08Y\x15\xa4p\x81@\x1d\xaa\xaa\xea?%ea\x80?'
    )
    td.append(
        b'\x94\xc3\x001"/\x08\xe0\x85\x92\xa8\x02\x1a\x11\r\xa1"T\x1e\x15|yU\x00\x18g%<k<f%\x00\x00\x80\xc1-@k<f2\n\x1d\x03\x9d\xa6@%\xaf\x93;?\x94\xc3\x00%"#\x08\xbc\x83\xda\xd2\r\x1a\x11\r?IS\x1e\x15\xf1\xf37\x00\x18(%\x9eT<f%\x00\x00\x84\xc1-\xf3T<f\x94\xc3\x002"0\x08\xa4\xeb\xc9\x81\x03\x12(\n\t!303275a4\x12\x07M1EQB-5\x1a\x04EQB5"\x06\xc0N02u\xa4(+0\x018\x03'
    )
    td.append(
        b"\x94\xc3\x00\rR\x0b\x12\x07\x12\x01\x01:\x02\x08 \x18\x01\x94\xc3\x00\x06R\x04\x08\x01\x12\x00\x94\xc3\x00\x06R\x04\x08\x02\x12\x00"
    )
    td.append(
        b"\x94\xc3\x003R1\x08\x07\x12+\x12 \xa1\xf7&z\xc8{d^\xc4\x8byw,[\xb1\x97\x8c\xa8\x13\xf3\xab\xee\x1f\x06*\x1c\xfe\xc0Z\x87d^\x1a\x07ofcmesh\x18\x02\x94\xc3\x00\t*\x07\n\x05\x10\x018\xb0T"
    )
    td.append(b'\x94\xc3\x00\x04J\x02"\x00\x94\xc3\x00\x04J\x02*\x00')
    td.append(b"\x94\xc3\x00\x0eJ\x0cZ\n\x10\n\x18\xc8\x01 \xcf\x01(L\x94\xc3\x00\x08J\x06b\x04\x10-8\x01")
    td.append(b"\x94\xc3\x00\x04J\x02j\x00\x94\xc3\x00\x068\xa5\xdc\xbf\xfd\x08")
    td.append(b'\x94\xc3\x00Q"O\x08\xbc\x83\xda\xd2\r\x12*\n\t!da5681bc\x12\rBoreham Ridge\x1a')
    for d in td:
        print(buffertoprotobufs(d))
    print("test end")


if __name__ == "__main__":
    test()

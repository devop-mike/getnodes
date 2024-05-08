#!/usr/local/meshtastic/bin/python3

from sys import argv
import random
import socket
import time
from meshtastic import mesh_pb2
from google.protobuf.json_format import MessageToDict
import base64
import json

START1 = 0x94
START2 = 0xC3
START = bytearray([START1, START2])
HEADER_LEN = 4
MAX_TO_FROM_RADIO_SIZE = 512
RUNID = random.randint(0, 0xFFFFFFFF)


def doconnection(dest: str):
    sock = socket.create_connection((dest, 4403))
    # send wake up
    buf = bytearray([0xFF] * 8)
    sock.send(buf)
    time.sleep(0.1)

    # send request
    buf = makerequest()
    sock.send(buf)

    # create collection for nodes
    nodes = []

    # create deserialiserialiser
    deserialiser = mesh_pb2.FromRadio()

    # loop though recieved data
    while buf:
        buf = sock.recv(MAX_TO_FROM_RADIO_SIZE)
        # strip 4 byte header and deserialiserialise
        deserialiser.ParseFromString(buf[4:])

        if deserialiser.HasField("node_info"):
            # store node info. Note: deserialiser is a pointer and needs to be dereferenced to add to a list.
            node = MessageToDict(deserialiser.node_info)
            if "user" in node.keys() and "macaddr" in node["user"].keys():
                # fix mac address
                node["user"]["macaddr"] = base64.b64decode(node["user"]["macaddr"]).hex(sep=":")
            nodes.append(node)

        if deserialiser.config_complete_id:
            # stop loop when we get the complete signal
            break

    sock.close()

    print(json.dumps(nodes))


def makerequest():
    # make request packet
    wantconfig = mesh_pb2.ToRadio()
    wantconfig.want_config_id = RUNID
    # encode and get length
    reqdata = wantconfig.SerializeToString()
    reqlen = len(reqdata)
    # combine header(0x94c3), payload size and payload
    buf = START + bytearray([(reqlen >> 8) & 0xFF, reqlen & 0xFF]) + reqdata
    return buf


def test():
    print("test start")
    node = mesh_pb2.NodeInfo()
    print(json.dumps(MessageToDict(node,always_print_fields_with_no_presence=True,)))
    print("test end")


def main():
    if len(argv) > 1:
        doconnection(argv[1])
        # test()


if __name__ == "__main__":
    main()

#!/usr/local/meshtastic/bin/python3

from sys import argv
import random
from connector import connector
from connector.socket import socketconnector
from connector.serial import serialconnector
from meshtastic import mesh_pb2, admin_pb2
from google.protobuf.json_format import MessageToDict
import base64
import json

START1 = 0x94
START2 = 0xC3
START = bytearray([START1, START2])
HEADER_LEN = 4
MAX_TO_FROM_RADIO_SIZE = 512
RUNID = random.randint(0, 0xFFFFFFFF)


def doconnection(connector: connector):
    # send request
    connector.send(makerequest())
    # capture node list
    nodes = processmessagesfornodes(connector)
    connector.close()
    print(json.dumps(nodes))


def processmessagesfornodes(connector: connector):
    # create deserialiserialiser
    deserialiser = mesh_pb2.FromRadio()

    # loop though recieved data collecting nodes
    nodes = []
    buf = True
    while buf:
        buf = connector.recv(MAX_TO_FROM_RADIO_SIZE)
        protobufs = buffertoprotobufs(buf)
        for pb in protobufs:
            deserialiser.ParseFromString(pb)

            if deserialiser.HasField("node_info"):
                # store node info. Note: deserialiser is a pointer and needs to be dereferenced to add to a list.
                node = MessageToDict(deserialiser.node_info)
                if "user" in node.keys() and "macaddr" in node["user"].keys():
                    # fix mac address
                    node["user"]["macaddr"] = base64.b64decode(node["user"]["macaddr"]).hex(sep=":")
                nodes.append(node)
            if deserialiser.HasField("config_complete_id"):
                # stop loop when we get the complete signal
                return nodes
    # no more data
    return nodes


def buffertoprotobufs(buffer):
    protobufs = []
    buflen = len(buffer)
    pbend = 0
    while pbend < buflen:
        pblen = (buffer[pbend + 2] << 8) + buffer[pbend + 3]
        pbstart = pbend + 4
        pbend = pbstart + pblen
        protobufs.append(buffer[pbstart:pbend])
    return protobufs


def makerequest():
    # make request packet
    wantconfig = mesh_pb2.ToRadio(want_config_id=RUNID)
    # encode and get length
    reqdata = wantconfig.SerializeToString()
    reqlen = len(reqdata)
    # combine header(0x94c3), payload size and payload
    buf = START + bytearray([(reqlen >> 8) & 0xFF, reqlen & 0xFF]) + reqdata
    return buf


def test():
    admin = admin_pb2.AdminMessage(set_favorite_node=2747846476)
    # admin = admin_pb2.AdminMessage(set_favorite_node=3664097024)
    data = admin.SerializeToString()
    dlen = len(data)
    buf = START + bytearray([(dlen >> 8) & 0xFF, dlen & 0xFF]) + data
    connector = socketconnector("meshtastic.ofc0")
    # connector = socketconnector("meshtastic.ofc1")
    connector.send(buf)
    connector.close()


def main():
    if len(argv) > 1:
        doconnection(socketconnector(argv[1]))
        return
    doconnection(serialconnector())


if __name__ == "__main__":
    main()

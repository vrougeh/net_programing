import socket
import struct
import binascii

class udpHeader:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.src_port, self.dst_port)
        packed += struct.pack('!HH', self.length, self.checksum)
        return packed

    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!HHHH', buffer[:8])
        return unpacked

    def getSrcPort(unpacked):
        return unpacked[0]

    def getDstPort(unpacked):
        return unpacked[1]

    def getLength(unpacked):
        return unpacked[2]

    def getChecksum(unpacked):
        return unpacked[3]

udp = udpHeader(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = udpHeader.unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port: {} Destination Port: {} Length {} Checksum: {}'
        .format(udpHeader.getSrcPort(unpacked_udphdr), 
                udpHeader.getDstPort(unpacked_udphdr),
                udpHeader.getLength(unpacked_udphdr),
                udpHeader.getChecksum(unpacked_udphdr)))

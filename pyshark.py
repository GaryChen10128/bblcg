# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:06:42 2021

@author: DIAMO
"""
import socket

# AF_INET: internet协议簇
# SOCK_STREAM: stream类型的socket
# 0: 使用该socket类型的默认协议，即TCP协议
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
ETH_P_ALL = 0x3

ETH_P_IP = 0x0800
ETH_P_ARP = 0x0806
ETH_P_RARP = 0x8035
ETH_P_IPV6 = 0x086dd

raw_sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))

while True:
    packet, packet_info = raw_sock.recvfrom(1500)
    print(packet)
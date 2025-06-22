## Server info packet

Client sends:

- Byte `0x69`

Server sends:

- (nothing or closes socket if server doesn't support this feature)
- Protocol version:
    - Byte `0x01` for RACv1 
    - Byte `0x02` for RACv1.99
    - Byte `0x03` for RACv2
- Server name
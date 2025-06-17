# RAC protocol

Description of the Sugoma’s “IRC killer”, the so-called RAC (Real Address Chat) protocol. (The worst name for a protocol.)

Client sends a message consisting of a message type (single byte) and an argument, if required. Server ignores everything that comes afterwards, so the socket must be closed.

Known message types:

0x30: Server stores the argument to the message log. Server does not respond with anything.

Message cannot be longer than 4096 bytes (including the 0x30 byte and the newline at the end). Longer messages are stripped.
0x31 (argumentless): Server responds with the size of the message log in bytes as a decimal string which needs to be converted into a number. Clients are confused when it is incorrect.

0x32 (argumentless): Server responds with the raw contents of the message log stripped to the size of the answer to the previous ‘1’ message.

Server responds with garbage to a message of this type if the client have not previously sent a ‘1’ message.

Source: https://bedohswe.eu.org/text/rac/protocol.md.html

RAC Protocol

Message Retrieval
a. The client initiates a message retrieval session by sending the byte 0x00 to the server.

b. In response, the server transmits the size of the available messages as an ASCII-encoded string.

c. After receiving the size, the client must send one of the following bytes or close the connection:

i. Sending 0x01 instructs the server to transmit all messages in full.

ii. Sending 0x02 followed by the client’s cached messages length (as an ASCII string, e.g., 0x02"1024") instructs the server to transmit only new messages added since the cached length. The server sends messages starting from the cached length offset, and the client updates its cached length to the total size received in step 1b after processing the new messages.

Message Transmission
a. To send a message, the client issues a request in the following format:

The client sends the byte 0x01 followed immediately by the message content. The server does not send a response.
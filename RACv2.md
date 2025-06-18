# RAC Protocol
RAC v2.0 is backward compatible with older versions of RAC
## Message Retrieval

a. The client initiates a message retrieval session by sending the byte 0x00 to the server.

b. In response, the server transmits the size of the available messages as an ASCII-encoded string.

c. After receiving the size, the client must send one of the following bytes or close the connection:

i. Sending 0x01 instructs the server to transmit all messages in full.

ii. Sending 0x02 followed by the client’s cached messages length (as an ASCII string, e.g., 0x02"1024") instructs the server to transmit only new messages added since the cached length. The server sends messages starting from the cached length offset, and the client updates its cached length to the total size received in step 1b after processing the new messages.

## Message Transmission

a. To send a message, the client issues a request in one of the following formats:

i. Unauthenticated Message: The client sends the byte 0x01 followed immediately by the message content. The server does not send a response.

ii. Authenticated Message: The client sends the byte 0x02 followed by the username, a newline character (\n), the password, a newline character and the message content. The server responds with a single byte:

0x01 indicates the user does not exist.

0x02 indicates the password is incorrect.

A successful authentication results in the server accepting the message without sending a response.
## User Registration

a. To register a new user, the client sends a request formatted as:

The byte 0x03.

The username, followed by a newline character (\n).

The password.

b. The server processes the request and responds with a single byte:

0x01 if the username already exists.

A successful registration is assumed if no error byte (0x01) is received. The client should close the connection after handling the response.

Source: https://gitea.bedohswe.eu.org/pixtaded/crab#rac-protocol

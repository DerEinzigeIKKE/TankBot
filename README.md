# TankBot
Bot zur Benachrichtigung bei niedrigen Dieselpreisen


## Setup

### Filelayout
1234567890:AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQQ;bot_token
00000000-0000-0000-0000-000000000000;api_key
123456789;chat_id

## Functions

| Fumction | Parameters | Return | Description |
|:-------------:|:-------------:|:-------------:|:-------------:|
| getTokens | - | bot_token, api_key, chat_ids |  |
| getPrice | api_key | price | |
| sendMessage |bot_token, chat_id, msg | - | |
| saveToCsv | price | - | |

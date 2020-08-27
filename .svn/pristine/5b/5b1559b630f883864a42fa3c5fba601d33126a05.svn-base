"""
命令格式
命令由命令头、命令ID和若干字段组成，字段可以任意组合，字段组合存放于Payload Data区域，命令格式如下定义：
0	1	2	3	4	5	6	7
Start Of Message（0x0B）
0x1C
Sequence ID
Request/Response
Product ID（0x00~0xFE）0xFF表示此条命令不区分设备型号
0xFF indicates that this command does not distinguish between device models
Message ID(Low)
Message ID(High)
Timestamp(UTC)
Payload length （2 bytes）
Payload Data字段1 Field1
Payload Data字段2 Field2
………
Checksum(CRC)32位 32 bit
"""

# sent command
# 0B 1C 00 00 02 0A 20 13 0B 1B 0D 18 08 2B 00 02 15 00 01 00 11 00 10 66 66 E6 41 14 00 00 00 00 00 00 00 00 00 00 00 38 D1 2A CE
# 0B 1C       Start Of Message
# 00          Sequence ID
# 00          Request/Response
# 02          Product ID
# 0A 20         Message ID
# 13 0B 1B 0D 18 08 2B 00 02    Timestamp
# 15 00 01 00 11 00 10 66 66 E6 41 14 00 00 00 00 00 00 00 00 00 00 00                  Payload Data
# 38 D1 2A CE       Checksum


# 0B 1C 00 01 02 0A 20 00 00 00 00 00 00 00 00 00 00 00 94 EF 7E 62
# Start_of_message = '0B1C'
# Sequence_id = '00'
# Response = '01'
# Product_id = '02'
# Message_id = '0A20'


# c9lvp.getAlarmName(0)
# 2019-12-04 16:22:37  向泵发送的字节流：
# 0B 1C 00 00 02 23 01 13 0C 04 10 16 25 2B 00 02 05 00 01 00 01 00 00 44 FB 66 A4
# 2019-12-04 16:22:38  泵返回的字节流：
# 0B 1C 00 01 02 23 01 00 00 00 00 00 00 00 00 00 07 00 01 00 03 00 00 00 00 3E 12 A4 20
# c9lvp.getAlarmName(1)
# 2019-12-04 16:32:37  向泵发送的字节流：
# 0B 1C 00 00 02 23 01 13 0C 04 10 20 25 2B 00 02 05 00 01 00 01 00 01 36 58 75 28
# 2019-12-04 16:32:37  泵返回的字节流：
# 0B 1C 00 01 02 23 01 00 00 00 00 00 00 00 00 00 16 00 01 00 12 00 01 01 0F E9 80 9F E7 8E 87 E8 B6 85 E8 8C 83 E5 9B B4 64 22 74 3B
# c9lvp.getAlarmName(2)
# 2019-12-04 16:41:36  向泵发送的字节流：
# 0B 1C 00 00 02 23 01 13 0C 04 10 29 24 2B 00 02 05 00 01 00 01 00 02 DD EC 5B ED
# 2019-12-04 16:41:36  泵返回的字节流：
# 0B 1C 00 01 02 23 01 00 00 00 00 00 00 00 00 00 16 00 01 00 12 00 02 01 0F E5 8F 82 E6 95 B0 E6 9C AA E8 AE BE E7 BD AE 40 AC 1C B0


# 泵端当前版本不支持设置完成输注警报时间命令
# c9lvp.setCompleteInfusionAlarm(5)
# 2019-12-04 13:13:40  向泵发送的字节流：
# 0B 1C 00 00 02 0D 20 13 0C 04 0D 0D 28 2B 00 02 05 00 01 00 01 00 05 9A 9E 57 7C
# 2019-12-04 13:13:40  泵返回的字节流：
# 0B 1C 00 01 02 01 00 00 00 00 00 00 00 00 00 00 07 00 13 00 03 00 0D 20 01 61 BE 6E 3D

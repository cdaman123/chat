# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\x12\x03pbx\"\x08\n\x06Unused\",\n\x0e\x44\x65\x66\x61ultAcsMode\x12\x0c\n\x04\x61uth\x18\x01 \x01(\t\x12\x0c\n\x04\x61non\x18\x02 \x01(\t\")\n\nAccessMode\x12\x0c\n\x04want\x18\x01 \x01(\t\x12\r\n\x05given\x18\x02 \x01(\t\"\'\n\x06SetSub\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\t\"\x99\x01\n\nClientCred\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08response\x18\x03 \x01(\t\x12+\n\x06params\x18\x04 \x03(\x0b\x32\x1b.pbx.ClientCred.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"e\n\x07SetDesc\x12(\n\x0b\x64\x65\x66\x61ult_acs\x18\x01 \x01(\x0b\x32\x13.pbx.DefaultAcsMode\x12\x0e\n\x06public\x18\x02 \x01(\x0c\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12\x0f\n\x07trusted\x18\x04 \x01(\x0c\"u\n\x07GetOpts\x12\x19\n\x11if_modified_since\x18\x01 \x01(\x03\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x10\n\x08since_id\x18\x04 \x01(\x05\x12\x11\n\tbefore_id\x18\x05 \x01(\x05\x12\r\n\x05limit\x18\x06 \x01(\x05\"k\n\x08GetQuery\x12\x0c\n\x04what\x18\x01 \x01(\t\x12\x1a\n\x04\x64\x65sc\x18\x02 \x01(\x0b\x32\x0c.pbx.GetOpts\x12\x19\n\x03sub\x18\x03 \x01(\x0b\x32\x0c.pbx.GetOpts\x12\x1a\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0c.pbx.GetOpts\"m\n\x08SetQuery\x12\x1a\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32\x0c.pbx.SetDesc\x12\x18\n\x03sub\x18\x02 \x01(\x0b\x32\x0b.pbx.SetSub\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x1d\n\x04\x63red\x18\x04 \x01(\x0b\x32\x0f.pbx.ClientCred\"#\n\x08SeqRange\x12\x0b\n\x03low\x18\x01 \x01(\x05\x12\n\n\x02hi\x18\x02 \x01(\x05\"~\n\x08\x43lientHi\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nuser_agent\x18\x02 \x01(\t\x12\x0b\n\x03ver\x18\x03 \x01(\t\x12\x11\n\tdevice_id\x18\x04 \x01(\t\x12\x0c\n\x04lang\x18\x05 \x01(\t\x12\x10\n\x08platform\x18\x06 \x01(\t\x12\x12\n\nbackground\x18\x07 \x01(\x08\"\xbe\x01\n\tClientAcc\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0e\n\x06scheme\x18\x03 \x01(\t\x12\x0e\n\x06secret\x18\x04 \x01(\x0c\x12\r\n\x05login\x18\x05 \x01(\x08\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x1a\n\x04\x64\x65sc\x18\x07 \x01(\x0b\x32\x0c.pbx.SetDesc\x12\x1d\n\x04\x63red\x18\x08 \x03(\x0b\x32\x0f.pbx.ClientCred\x12\r\n\x05token\x18\t \x01(\x0c\x12\r\n\x05state\x18\n \x01(\t\"X\n\x0b\x43lientLogin\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06scheme\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\x0c\x12\x1d\n\x04\x63red\x18\x04 \x03(\x0b\x32\x0f.pbx.ClientCred\"j\n\tClientSub\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12 \n\tset_query\x18\x03 \x01(\x0b\x32\r.pbx.SetQuery\x12 \n\tget_query\x18\x04 \x01(\x0b\x32\r.pbx.GetQuery\"7\n\x0b\x43lientLeave\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\r\n\x05unsub\x18\x03 \x01(\x08\"\x9d\x01\n\tClientPub\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0f\n\x07no_echo\x18\x03 \x01(\x08\x12&\n\x04head\x18\x04 \x03(\x0b\x32\x18.pbx.ClientPub.HeadEntry\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\x0c\x1a+\n\tHeadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"D\n\tClientGet\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x1c\n\x05query\x18\x03 \x01(\x0b\x32\r.pbx.GetQuery\"D\n\tClientSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x1c\n\x05query\x18\x03 \x01(\x0b\x32\r.pbx.SetQuery\"\xe0\x01\n\tClientDel\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12!\n\x04what\x18\x03 \x01(\x0e\x32\x13.pbx.ClientDel.What\x12\x1e\n\x07\x64\x65l_seq\x18\x04 \x03(\x0b\x32\r.pbx.SeqRange\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12\x1d\n\x04\x63red\x18\x06 \x01(\x0b\x32\x0f.pbx.ClientCred\x12\x0c\n\x04hard\x18\x07 \x01(\x08\"7\n\x04What\x12\x07\n\x03MSG\x10\x00\x12\t\n\x05TOPIC\x10\x01\x12\x07\n\x03SUB\x10\x02\x12\x08\n\x04USER\x10\x03\x12\x08\n\x04\x43RED\x10\x04\"H\n\nClientNote\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x1b\n\x04what\x18\x02 \x01(\x0e\x32\r.pbx.InfoNote\x12\x0e\n\x06seq_id\x18\x03 \x01(\x05\"\\\n\x0b\x43lientExtra\x12\x13\n\x0b\x61ttachments\x18\x01 \x03(\t\x12\x14\n\x0con_behalf_of\x18\x02 \x01(\t\x12\"\n\nauth_level\x18\x03 \x01(\x0e\x32\x0e.pbx.AuthLevel\"\xf5\x02\n\tClientMsg\x12\x1b\n\x02hi\x18\x01 \x01(\x0b\x32\r.pbx.ClientHiH\x00\x12\x1d\n\x03\x61\x63\x63\x18\x02 \x01(\x0b\x32\x0e.pbx.ClientAccH\x00\x12!\n\x05login\x18\x03 \x01(\x0b\x32\x10.pbx.ClientLoginH\x00\x12\x1d\n\x03sub\x18\x04 \x01(\x0b\x32\x0e.pbx.ClientSubH\x00\x12!\n\x05leave\x18\x05 \x01(\x0b\x32\x10.pbx.ClientLeaveH\x00\x12\x1d\n\x03pub\x18\x06 \x01(\x0b\x32\x0e.pbx.ClientPubH\x00\x12\x1d\n\x03get\x18\x07 \x01(\x0b\x32\x0e.pbx.ClientGetH\x00\x12\x1d\n\x03set\x18\x08 \x01(\x0b\x32\x0e.pbx.ClientSetH\x00\x12\x1d\n\x03\x64\x65l\x18\t \x01(\x0b\x32\x0e.pbx.ClientDelH\x00\x12\x1f\n\x04note\x18\n \x01(\x0b\x32\x0f.pbx.ClientNoteH\x00\x12\x1f\n\x05\x65xtra\x18\r \x01(\x0b\x32\x10.pbx.ClientExtraB\t\n\x07Message\"9\n\nServerCred\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\"\xe6\x02\n\tTopicDesc\x12\x12\n\ncreated_at\x18\x01 \x01(\x03\x12\x12\n\nupdated_at\x18\x02 \x01(\x03\x12\x12\n\ntouched_at\x18\x03 \x01(\x03\x12#\n\x06\x64\x65\x66\x61\x63s\x18\x04 \x01(\x0b\x32\x13.pbx.DefaultAcsMode\x12\x1c\n\x03\x61\x63s\x18\x05 \x01(\x0b\x32\x0f.pbx.AccessMode\x12\x0e\n\x06seq_id\x18\x06 \x01(\x05\x12\x0f\n\x07read_id\x18\x07 \x01(\x05\x12\x0f\n\x07recv_id\x18\x08 \x01(\x05\x12\x0e\n\x06\x64\x65l_id\x18\t \x01(\x05\x12\x0e\n\x06public\x18\n \x01(\x0c\x12\x0f\n\x07private\x18\x0b \x01(\x0c\x12\r\n\x05state\x18\x0c \x01(\t\x12\x10\n\x08state_at\x18\r \x01(\x03\x12\x0f\n\x07trusted\x18\x0e \x01(\x0c\x12\x0f\n\x07is_chan\x18\x11 \x01(\x08\x12\x16\n\x0elast_seen_time\x18\x0f \x01(\x03\x12\x1c\n\x14last_seen_user_agent\x18\x10 \x01(\t\"\xbe\x02\n\x08TopicSub\x12\x12\n\nupdated_at\x18\x01 \x01(\x03\x12\x12\n\ndeleted_at\x18\x02 \x01(\x03\x12\x0e\n\x06online\x18\x03 \x01(\x08\x12\x1c\n\x03\x61\x63s\x18\x04 \x01(\x0b\x32\x0f.pbx.AccessMode\x12\x0f\n\x07read_id\x18\x05 \x01(\x05\x12\x0f\n\x07recv_id\x18\x06 \x01(\x05\x12\x0e\n\x06public\x18\x07 \x01(\x0c\x12\x0f\n\x07trusted\x18\x10 \x01(\x0c\x12\x0f\n\x07private\x18\x08 \x01(\x0c\x12\x0f\n\x07user_id\x18\t \x01(\t\x12\r\n\x05topic\x18\n \x01(\t\x12\x12\n\ntouched_at\x18\x0b \x01(\x03\x12\x0e\n\x06seq_id\x18\x0c \x01(\x05\x12\x0e\n\x06\x64\x65l_id\x18\r \x01(\x05\x12\x16\n\x0elast_seen_time\x18\x0e \x01(\x03\x12\x1c\n\x14last_seen_user_agent\x18\x0f \x01(\t\";\n\tDelValues\x12\x0e\n\x06\x64\x65l_id\x18\x01 \x01(\x05\x12\x1e\n\x07\x64\x65l_seq\x18\x02 \x03(\x0b\x32\r.pbx.SeqRange\"\x9f\x01\n\nServerCtrl\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12\x0c\n\x04text\x18\x04 \x01(\t\x12+\n\x06params\x18\x05 \x03(\x0b\x32\x1b.pbx.ServerCtrl.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xcf\x01\n\nServerData\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x07 \x01(\x03\x12\x12\n\ndeleted_at\x18\x03 \x01(\x03\x12\x0e\n\x06seq_id\x18\x04 \x01(\x05\x12\'\n\x04head\x18\x05 \x03(\x0b\x32\x19.pbx.ServerData.HeadEntry\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\x0c\x1a+\n\tHeadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xe4\x02\n\nServerPres\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\"\n\x04what\x18\x03 \x01(\x0e\x32\x14.pbx.ServerPres.What\x12\x12\n\nuser_agent\x18\x04 \x01(\t\x12\x0e\n\x06seq_id\x18\x05 \x01(\x05\x12\x0e\n\x06\x64\x65l_id\x18\x06 \x01(\x05\x12\x1e\n\x07\x64\x65l_seq\x18\x07 \x03(\x0b\x32\r.pbx.SeqRange\x12\x16\n\x0etarget_user_id\x18\x08 \x01(\t\x12\x15\n\ractor_user_id\x18\t \x01(\t\x12\x1c\n\x03\x61\x63s\x18\n \x01(\x0b\x32\x0f.pbx.AccessMode\"u\n\x04What\x12\x06\n\x02ON\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x06\n\x02UA\x10\x03\x12\x07\n\x03UPD\x10\x04\x12\x08\n\x04GONE\x10\x05\x12\x07\n\x03\x41\x43S\x10\x06\x12\x08\n\x04TERM\x10\x07\x12\x07\n\x03MSG\x10\x08\x12\x08\n\x04READ\x10\t\x12\x08\n\x04RECV\x10\n\x12\x07\n\x03\x44\x45L\x10\x0b\x12\x08\n\x04TAGS\x10\x0c\"\xab\x01\n\nServerMeta\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x1c\n\x04\x64\x65sc\x18\x03 \x01(\x0b\x32\x0e.pbx.TopicDesc\x12\x1a\n\x03sub\x18\x04 \x03(\x0b\x32\r.pbx.TopicSub\x12\x1b\n\x03\x64\x65l\x18\x05 \x01(\x0b\x32\x0e.pbx.DelValues\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x1d\n\x04\x63red\x18\x07 \x03(\x0b\x32\x0f.pbx.ServerCred\"k\n\nServerInfo\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x01(\t\x12\x1b\n\x04what\x18\x03 \x01(\x0e\x32\r.pbx.InfoNote\x12\x0e\n\x06seq_id\x18\x04 \x01(\x05\x12\x0b\n\x03src\x18\x05 \x01(\t\"\xca\x01\n\tServerMsg\x12\x1f\n\x04\x63trl\x18\x01 \x01(\x0b\x32\x0f.pbx.ServerCtrlH\x00\x12\x1f\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0f.pbx.ServerDataH\x00\x12\x1f\n\x04pres\x18\x03 \x01(\x0b\x32\x0f.pbx.ServerPresH\x00\x12\x1f\n\x04meta\x18\x04 \x01(\x0b\x32\x0f.pbx.ServerMetaH\x00\x12\x1f\n\x04info\x18\x05 \x01(\x0b\x32\x0f.pbx.ServerInfoH\x00\x12\r\n\x05topic\x18\x06 \x01(\tB\t\n\x07Message\"j\n\nServerResp\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.pbx.RespCode\x12\x1e\n\x06srvmsg\x18\x02 \x01(\x0b\x32\x0e.pbx.ServerMsg\x12\x1d\n\x05\x63lmsg\x18\x03 \x01(\x0b\x32\x0e.pbx.ClientMsg\"\xa0\x01\n\x07Session\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\"\n\nauth_level\x18\x03 \x01(\x0e\x32\x0e.pbx.AuthLevel\x12\x13\n\x0bremote_addr\x18\x04 \x01(\t\x12\x12\n\nuser_agent\x18\x05 \x01(\t\x12\x11\n\tdevice_id\x18\x06 \x01(\t\x12\x10\n\x08language\x18\x07 \x01(\t\"D\n\tClientReq\x12\x1b\n\x03msg\x18\x01 \x01(\x0b\x32\x0e.pbx.ClientMsg\x12\x1a\n\x04sess\x18\x02 \x01(\x0b\x32\x0c.pbx.Session\"-\n\x0bSearchQuery\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\"Z\n\x0bSearchFound\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.pbx.RespCode\x12\r\n\x05query\x18\x02 \x01(\t\x12\x1d\n\x06result\x18\x03 \x03(\x0b\x32\r.pbx.TopicSub\"S\n\nTopicEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x04\x64\x65sc\x18\x03 \x01(\x0b\x32\x0e.pbx.TopicDesc\"\x82\x01\n\x0c\x41\x63\x63ountEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12(\n\x0b\x64\x65\x66\x61ult_acs\x18\x03 \x01(\x0b\x32\x13.pbx.DefaultAcsMode\x12\x0e\n\x06public\x18\x04 \x01(\x0c\x12\x0c\n\x04tags\x18\x08 \x03(\t\"\xb0\x01\n\x11SubscriptionEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65l_id\x18\x04 \x01(\x05\x12\x0f\n\x07read_id\x18\x05 \x01(\x05\x12\x0f\n\x07recv_id\x18\x06 \x01(\x05\x12\x1d\n\x04mode\x18\x07 \x01(\x0b\x32\x0f.pbx.AccessMode\x12\x0f\n\x07private\x18\x08 \x01(\x0c\"G\n\x0cMessageEvent\x12\x19\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\t.pbx.Crud\x12\x1c\n\x03msg\x18\x02 \x01(\x0b\x32\x0f.pbx.ServerData*3\n\tAuthLevel\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04\x41NON\x10\n\x12\x08\n\x04\x41UTH\x10\x14\x12\x08\n\x04ROOT\x10\x1e*&\n\x08InfoNote\x12\x08\n\x04READ\x10\x00\x12\x08\n\x04RECV\x10\x01\x12\x06\n\x02KP\x10\x02*<\n\x08RespCode\x12\x0c\n\x08\x43ONTINUE\x10\x00\x12\x08\n\x04\x44ROP\x10\x01\x12\x0b\n\x07RESPOND\x10\x02\x12\x0b\n\x07REPLACE\x10\x03**\n\x04\x43rud\x12\n\n\x06\x43REATE\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x32;\n\x04Node\x12\x33\n\x0bMessageLoop\x12\x0e.pbx.ClientMsg\x1a\x0e.pbx.ServerMsg\"\x00(\x01\x30\x01\x32\x9f\x02\n\x06Plugin\x12-\n\x08\x46ireHose\x12\x0e.pbx.ClientReq\x1a\x0f.pbx.ServerResp\"\x00\x12,\n\x04\x46ind\x12\x10.pbx.SearchQuery\x1a\x10.pbx.SearchFound\"\x00\x12+\n\x07\x41\x63\x63ount\x12\x11.pbx.AccountEvent\x1a\x0b.pbx.Unused\"\x00\x12\'\n\x05Topic\x12\x0f.pbx.TopicEvent\x1a\x0b.pbx.Unused\"\x00\x12\x35\n\x0cSubscription\x12\x16.pbx.SubscriptionEvent\x1a\x0b.pbx.Unused\"\x00\x12+\n\x07Message\x12\x11.pbx.MessageEvent\x1a\x0b.pbx.Unused\"\x00\x42\x1cZ\x1agithub.com/cdaman123/chat/pbxb\x06proto3')

_AUTHLEVEL = DESCRIPTOR.enum_types_by_name['AuthLevel']
AuthLevel = enum_type_wrapper.EnumTypeWrapper(_AUTHLEVEL)
_INFONOTE = DESCRIPTOR.enum_types_by_name['InfoNote']
InfoNote = enum_type_wrapper.EnumTypeWrapper(_INFONOTE)
_RESPCODE = DESCRIPTOR.enum_types_by_name['RespCode']
RespCode = enum_type_wrapper.EnumTypeWrapper(_RESPCODE)
_CRUD = DESCRIPTOR.enum_types_by_name['Crud']
Crud = enum_type_wrapper.EnumTypeWrapper(_CRUD)
NONE = 0
ANON = 10
AUTH = 20
ROOT = 30
READ = 0
RECV = 1
KP = 2
CONTINUE = 0
DROP = 1
RESPOND = 2
REPLACE = 3
CREATE = 0
UPDATE = 1
DELETE = 2


_UNUSED = DESCRIPTOR.message_types_by_name['Unused']
_DEFAULTACSMODE = DESCRIPTOR.message_types_by_name['DefaultAcsMode']
_ACCESSMODE = DESCRIPTOR.message_types_by_name['AccessMode']
_SETSUB = DESCRIPTOR.message_types_by_name['SetSub']
_CLIENTCRED = DESCRIPTOR.message_types_by_name['ClientCred']
_CLIENTCRED_PARAMSENTRY = _CLIENTCRED.nested_types_by_name['ParamsEntry']
_SETDESC = DESCRIPTOR.message_types_by_name['SetDesc']
_GETOPTS = DESCRIPTOR.message_types_by_name['GetOpts']
_GETQUERY = DESCRIPTOR.message_types_by_name['GetQuery']
_SETQUERY = DESCRIPTOR.message_types_by_name['SetQuery']
_SEQRANGE = DESCRIPTOR.message_types_by_name['SeqRange']
_CLIENTHI = DESCRIPTOR.message_types_by_name['ClientHi']
_CLIENTACC = DESCRIPTOR.message_types_by_name['ClientAcc']
_CLIENTLOGIN = DESCRIPTOR.message_types_by_name['ClientLogin']
_CLIENTSUB = DESCRIPTOR.message_types_by_name['ClientSub']
_CLIENTLEAVE = DESCRIPTOR.message_types_by_name['ClientLeave']
_CLIENTPUB = DESCRIPTOR.message_types_by_name['ClientPub']
_CLIENTPUB_HEADENTRY = _CLIENTPUB.nested_types_by_name['HeadEntry']
_CLIENTGET = DESCRIPTOR.message_types_by_name['ClientGet']
_CLIENTSET = DESCRIPTOR.message_types_by_name['ClientSet']
_CLIENTDEL = DESCRIPTOR.message_types_by_name['ClientDel']
_CLIENTNOTE = DESCRIPTOR.message_types_by_name['ClientNote']
_CLIENTEXTRA = DESCRIPTOR.message_types_by_name['ClientExtra']
_CLIENTMSG = DESCRIPTOR.message_types_by_name['ClientMsg']
_SERVERCRED = DESCRIPTOR.message_types_by_name['ServerCred']
_TOPICDESC = DESCRIPTOR.message_types_by_name['TopicDesc']
_TOPICSUB = DESCRIPTOR.message_types_by_name['TopicSub']
_DELVALUES = DESCRIPTOR.message_types_by_name['DelValues']
_SERVERCTRL = DESCRIPTOR.message_types_by_name['ServerCtrl']
_SERVERCTRL_PARAMSENTRY = _SERVERCTRL.nested_types_by_name['ParamsEntry']
_SERVERDATA = DESCRIPTOR.message_types_by_name['ServerData']
_SERVERDATA_HEADENTRY = _SERVERDATA.nested_types_by_name['HeadEntry']
_SERVERPRES = DESCRIPTOR.message_types_by_name['ServerPres']
_SERVERMETA = DESCRIPTOR.message_types_by_name['ServerMeta']
_SERVERINFO = DESCRIPTOR.message_types_by_name['ServerInfo']
_SERVERMSG = DESCRIPTOR.message_types_by_name['ServerMsg']
_SERVERRESP = DESCRIPTOR.message_types_by_name['ServerResp']
_SESSION = DESCRIPTOR.message_types_by_name['Session']
_CLIENTREQ = DESCRIPTOR.message_types_by_name['ClientReq']
_SEARCHQUERY = DESCRIPTOR.message_types_by_name['SearchQuery']
_SEARCHFOUND = DESCRIPTOR.message_types_by_name['SearchFound']
_TOPICEVENT = DESCRIPTOR.message_types_by_name['TopicEvent']
_ACCOUNTEVENT = DESCRIPTOR.message_types_by_name['AccountEvent']
_SUBSCRIPTIONEVENT = DESCRIPTOR.message_types_by_name['SubscriptionEvent']
_MESSAGEEVENT = DESCRIPTOR.message_types_by_name['MessageEvent']
_CLIENTDEL_WHAT = _CLIENTDEL.enum_types_by_name['What']
_SERVERPRES_WHAT = _SERVERPRES.enum_types_by_name['What']
Unused = _reflection.GeneratedProtocolMessageType('Unused', (_message.Message,), {
  'DESCRIPTOR' : _UNUSED,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.Unused)
  })
_sym_db.RegisterMessage(Unused)

DefaultAcsMode = _reflection.GeneratedProtocolMessageType('DefaultAcsMode', (_message.Message,), {
  'DESCRIPTOR' : _DEFAULTACSMODE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.DefaultAcsMode)
  })
_sym_db.RegisterMessage(DefaultAcsMode)

AccessMode = _reflection.GeneratedProtocolMessageType('AccessMode', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSMODE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.AccessMode)
  })
_sym_db.RegisterMessage(AccessMode)

SetSub = _reflection.GeneratedProtocolMessageType('SetSub', (_message.Message,), {
  'DESCRIPTOR' : _SETSUB,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SetSub)
  })
_sym_db.RegisterMessage(SetSub)

ClientCred = _reflection.GeneratedProtocolMessageType('ClientCred', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLIENTCRED_PARAMSENTRY,
    '__module__' : 'model_pb2'
    # @@protoc_insertion_point(class_scope:pbx.ClientCred.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _CLIENTCRED,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientCred)
  })
_sym_db.RegisterMessage(ClientCred)
_sym_db.RegisterMessage(ClientCred.ParamsEntry)

SetDesc = _reflection.GeneratedProtocolMessageType('SetDesc', (_message.Message,), {
  'DESCRIPTOR' : _SETDESC,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SetDesc)
  })
_sym_db.RegisterMessage(SetDesc)

GetOpts = _reflection.GeneratedProtocolMessageType('GetOpts', (_message.Message,), {
  'DESCRIPTOR' : _GETOPTS,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.GetOpts)
  })
_sym_db.RegisterMessage(GetOpts)

GetQuery = _reflection.GeneratedProtocolMessageType('GetQuery', (_message.Message,), {
  'DESCRIPTOR' : _GETQUERY,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.GetQuery)
  })
_sym_db.RegisterMessage(GetQuery)

SetQuery = _reflection.GeneratedProtocolMessageType('SetQuery', (_message.Message,), {
  'DESCRIPTOR' : _SETQUERY,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SetQuery)
  })
_sym_db.RegisterMessage(SetQuery)

SeqRange = _reflection.GeneratedProtocolMessageType('SeqRange', (_message.Message,), {
  'DESCRIPTOR' : _SEQRANGE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SeqRange)
  })
_sym_db.RegisterMessage(SeqRange)

ClientHi = _reflection.GeneratedProtocolMessageType('ClientHi', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTHI,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientHi)
  })
_sym_db.RegisterMessage(ClientHi)

ClientAcc = _reflection.GeneratedProtocolMessageType('ClientAcc', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTACC,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientAcc)
  })
_sym_db.RegisterMessage(ClientAcc)

ClientLogin = _reflection.GeneratedProtocolMessageType('ClientLogin', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTLOGIN,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientLogin)
  })
_sym_db.RegisterMessage(ClientLogin)

ClientSub = _reflection.GeneratedProtocolMessageType('ClientSub', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSUB,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientSub)
  })
_sym_db.RegisterMessage(ClientSub)

ClientLeave = _reflection.GeneratedProtocolMessageType('ClientLeave', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTLEAVE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientLeave)
  })
_sym_db.RegisterMessage(ClientLeave)

ClientPub = _reflection.GeneratedProtocolMessageType('ClientPub', (_message.Message,), {

  'HeadEntry' : _reflection.GeneratedProtocolMessageType('HeadEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLIENTPUB_HEADENTRY,
    '__module__' : 'model_pb2'
    # @@protoc_insertion_point(class_scope:pbx.ClientPub.HeadEntry)
    })
  ,
  'DESCRIPTOR' : _CLIENTPUB,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientPub)
  })
_sym_db.RegisterMessage(ClientPub)
_sym_db.RegisterMessage(ClientPub.HeadEntry)

ClientGet = _reflection.GeneratedProtocolMessageType('ClientGet', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTGET,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientGet)
  })
_sym_db.RegisterMessage(ClientGet)

ClientSet = _reflection.GeneratedProtocolMessageType('ClientSet', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSET,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientSet)
  })
_sym_db.RegisterMessage(ClientSet)

ClientDel = _reflection.GeneratedProtocolMessageType('ClientDel', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTDEL,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientDel)
  })
_sym_db.RegisterMessage(ClientDel)

ClientNote = _reflection.GeneratedProtocolMessageType('ClientNote', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTNOTE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientNote)
  })
_sym_db.RegisterMessage(ClientNote)

ClientExtra = _reflection.GeneratedProtocolMessageType('ClientExtra', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTEXTRA,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientExtra)
  })
_sym_db.RegisterMessage(ClientExtra)

ClientMsg = _reflection.GeneratedProtocolMessageType('ClientMsg', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTMSG,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientMsg)
  })
_sym_db.RegisterMessage(ClientMsg)

ServerCred = _reflection.GeneratedProtocolMessageType('ServerCred', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCRED,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerCred)
  })
_sym_db.RegisterMessage(ServerCred)

TopicDesc = _reflection.GeneratedProtocolMessageType('TopicDesc', (_message.Message,), {
  'DESCRIPTOR' : _TOPICDESC,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.TopicDesc)
  })
_sym_db.RegisterMessage(TopicDesc)

TopicSub = _reflection.GeneratedProtocolMessageType('TopicSub', (_message.Message,), {
  'DESCRIPTOR' : _TOPICSUB,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.TopicSub)
  })
_sym_db.RegisterMessage(TopicSub)

DelValues = _reflection.GeneratedProtocolMessageType('DelValues', (_message.Message,), {
  'DESCRIPTOR' : _DELVALUES,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.DelValues)
  })
_sym_db.RegisterMessage(DelValues)

ServerCtrl = _reflection.GeneratedProtocolMessageType('ServerCtrl', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERCTRL_PARAMSENTRY,
    '__module__' : 'model_pb2'
    # @@protoc_insertion_point(class_scope:pbx.ServerCtrl.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERCTRL,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerCtrl)
  })
_sym_db.RegisterMessage(ServerCtrl)
_sym_db.RegisterMessage(ServerCtrl.ParamsEntry)

ServerData = _reflection.GeneratedProtocolMessageType('ServerData', (_message.Message,), {

  'HeadEntry' : _reflection.GeneratedProtocolMessageType('HeadEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERDATA_HEADENTRY,
    '__module__' : 'model_pb2'
    # @@protoc_insertion_point(class_scope:pbx.ServerData.HeadEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERDATA,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerData)
  })
_sym_db.RegisterMessage(ServerData)
_sym_db.RegisterMessage(ServerData.HeadEntry)

ServerPres = _reflection.GeneratedProtocolMessageType('ServerPres', (_message.Message,), {
  'DESCRIPTOR' : _SERVERPRES,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerPres)
  })
_sym_db.RegisterMessage(ServerPres)

ServerMeta = _reflection.GeneratedProtocolMessageType('ServerMeta', (_message.Message,), {
  'DESCRIPTOR' : _SERVERMETA,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerMeta)
  })
_sym_db.RegisterMessage(ServerMeta)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFO,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerInfo)
  })
_sym_db.RegisterMessage(ServerInfo)

ServerMsg = _reflection.GeneratedProtocolMessageType('ServerMsg', (_message.Message,), {
  'DESCRIPTOR' : _SERVERMSG,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerMsg)
  })
_sym_db.RegisterMessage(ServerMsg)

ServerResp = _reflection.GeneratedProtocolMessageType('ServerResp', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESP,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ServerResp)
  })
_sym_db.RegisterMessage(ServerResp)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.Session)
  })
_sym_db.RegisterMessage(Session)

ClientReq = _reflection.GeneratedProtocolMessageType('ClientReq', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQ,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.ClientReq)
  })
_sym_db.RegisterMessage(ClientReq)

SearchQuery = _reflection.GeneratedProtocolMessageType('SearchQuery', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHQUERY,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SearchQuery)
  })
_sym_db.RegisterMessage(SearchQuery)

SearchFound = _reflection.GeneratedProtocolMessageType('SearchFound', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHFOUND,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SearchFound)
  })
_sym_db.RegisterMessage(SearchFound)

TopicEvent = _reflection.GeneratedProtocolMessageType('TopicEvent', (_message.Message,), {
  'DESCRIPTOR' : _TOPICEVENT,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.TopicEvent)
  })
_sym_db.RegisterMessage(TopicEvent)

AccountEvent = _reflection.GeneratedProtocolMessageType('AccountEvent', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTEVENT,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.AccountEvent)
  })
_sym_db.RegisterMessage(AccountEvent)

SubscriptionEvent = _reflection.GeneratedProtocolMessageType('SubscriptionEvent', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONEVENT,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.SubscriptionEvent)
  })
_sym_db.RegisterMessage(SubscriptionEvent)

MessageEvent = _reflection.GeneratedProtocolMessageType('MessageEvent', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEEVENT,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:pbx.MessageEvent)
  })
_sym_db.RegisterMessage(MessageEvent)

_NODE = DESCRIPTOR.services_by_name['Node']
_PLUGIN = DESCRIPTOR.services_by_name['Plugin']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032github.com/cdaman123/chat/pbx'
  _CLIENTCRED_PARAMSENTRY._options = None
  _CLIENTCRED_PARAMSENTRY._serialized_options = b'8\001'
  _CLIENTPUB_HEADENTRY._options = None
  _CLIENTPUB_HEADENTRY._serialized_options = b'8\001'
  _SERVERCTRL_PARAMSENTRY._options = None
  _SERVERCTRL_PARAMSENTRY._serialized_options = b'8\001'
  _SERVERDATA_HEADENTRY._options = None
  _SERVERDATA_HEADENTRY._serialized_options = b'8\001'
  _AUTHLEVEL._serialized_start=5413
  _AUTHLEVEL._serialized_end=5464
  _INFONOTE._serialized_start=5466
  _INFONOTE._serialized_end=5504
  _RESPCODE._serialized_start=5506
  _RESPCODE._serialized_end=5566
  _CRUD._serialized_start=5568
  _CRUD._serialized_end=5610
  _UNUSED._serialized_start=20
  _UNUSED._serialized_end=28
  _DEFAULTACSMODE._serialized_start=30
  _DEFAULTACSMODE._serialized_end=74
  _ACCESSMODE._serialized_start=76
  _ACCESSMODE._serialized_end=117
  _SETSUB._serialized_start=119
  _SETSUB._serialized_end=158
  _CLIENTCRED._serialized_start=161
  _CLIENTCRED._serialized_end=314
  _CLIENTCRED_PARAMSENTRY._serialized_start=269
  _CLIENTCRED_PARAMSENTRY._serialized_end=314
  _SETDESC._serialized_start=316
  _SETDESC._serialized_end=417
  _GETOPTS._serialized_start=419
  _GETOPTS._serialized_end=536
  _GETQUERY._serialized_start=538
  _GETQUERY._serialized_end=645
  _SETQUERY._serialized_start=647
  _SETQUERY._serialized_end=756
  _SEQRANGE._serialized_start=758
  _SEQRANGE._serialized_end=793
  _CLIENTHI._serialized_start=795
  _CLIENTHI._serialized_end=921
  _CLIENTACC._serialized_start=924
  _CLIENTACC._serialized_end=1114
  _CLIENTLOGIN._serialized_start=1116
  _CLIENTLOGIN._serialized_end=1204
  _CLIENTSUB._serialized_start=1206
  _CLIENTSUB._serialized_end=1312
  _CLIENTLEAVE._serialized_start=1314
  _CLIENTLEAVE._serialized_end=1369
  _CLIENTPUB._serialized_start=1372
  _CLIENTPUB._serialized_end=1529
  _CLIENTPUB_HEADENTRY._serialized_start=1486
  _CLIENTPUB_HEADENTRY._serialized_end=1529
  _CLIENTGET._serialized_start=1531
  _CLIENTGET._serialized_end=1599
  _CLIENTSET._serialized_start=1601
  _CLIENTSET._serialized_end=1669
  _CLIENTDEL._serialized_start=1672
  _CLIENTDEL._serialized_end=1896
  _CLIENTDEL_WHAT._serialized_start=1841
  _CLIENTDEL_WHAT._serialized_end=1896
  _CLIENTNOTE._serialized_start=1898
  _CLIENTNOTE._serialized_end=1970
  _CLIENTEXTRA._serialized_start=1972
  _CLIENTEXTRA._serialized_end=2064
  _CLIENTMSG._serialized_start=2067
  _CLIENTMSG._serialized_end=2440
  _SERVERCRED._serialized_start=2442
  _SERVERCRED._serialized_end=2499
  _TOPICDESC._serialized_start=2502
  _TOPICDESC._serialized_end=2860
  _TOPICSUB._serialized_start=2863
  _TOPICSUB._serialized_end=3181
  _DELVALUES._serialized_start=3183
  _DELVALUES._serialized_end=3242
  _SERVERCTRL._serialized_start=3245
  _SERVERCTRL._serialized_end=3404
  _SERVERCTRL_PARAMSENTRY._serialized_start=269
  _SERVERCTRL_PARAMSENTRY._serialized_end=314
  _SERVERDATA._serialized_start=3407
  _SERVERDATA._serialized_end=3614
  _SERVERDATA_HEADENTRY._serialized_start=1486
  _SERVERDATA_HEADENTRY._serialized_end=1529
  _SERVERPRES._serialized_start=3617
  _SERVERPRES._serialized_end=3973
  _SERVERPRES_WHAT._serialized_start=3856
  _SERVERPRES_WHAT._serialized_end=3973
  _SERVERMETA._serialized_start=3976
  _SERVERMETA._serialized_end=4147
  _SERVERINFO._serialized_start=4149
  _SERVERINFO._serialized_end=4256
  _SERVERMSG._serialized_start=4259
  _SERVERMSG._serialized_end=4461
  _SERVERRESP._serialized_start=4463
  _SERVERRESP._serialized_end=4569
  _SESSION._serialized_start=4572
  _SESSION._serialized_end=4732
  _CLIENTREQ._serialized_start=4734
  _CLIENTREQ._serialized_end=4802
  _SEARCHQUERY._serialized_start=4804
  _SEARCHQUERY._serialized_end=4849
  _SEARCHFOUND._serialized_start=4851
  _SEARCHFOUND._serialized_end=4941
  _TOPICEVENT._serialized_start=4943
  _TOPICEVENT._serialized_end=5026
  _ACCOUNTEVENT._serialized_start=5029
  _ACCOUNTEVENT._serialized_end=5159
  _SUBSCRIPTIONEVENT._serialized_start=5162
  _SUBSCRIPTIONEVENT._serialized_end=5338
  _MESSAGEEVENT._serialized_start=5340
  _MESSAGEEVENT._serialized_end=5411
  _NODE._serialized_start=5612
  _NODE._serialized_end=5671
  _PLUGIN._serialized_start=5674
  _PLUGIN._serialized_end=5961
# @@protoc_insertion_point(module_scope)

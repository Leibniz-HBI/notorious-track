# still in need to be checked for bugs, the prelim schema
import string
from sqlalchemy import Boolean, Column, Date, Integer, Index, Sequence, SmallInteger, Text
from sqlalchemy.dialects.postgresql import ENUM, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import event
from sqlalchemy.schema import CreateSchema

Base = declarative_base()
metadata = Base.metadata

schema_name = 'telegram'
event.listen(metadata, 'before_create', CreateSchema(schema_name))

#class TelegramMeta(Base):
   # telegram = Column(VARCHAR)
  # telegram_post = Column(Text)


class TelegramMessage(Base):
    __tablename__ = 'telegram_messages'
    __tablename__ = {'schema' : schema_name}

    telegram_id = Column(VARCHAR,Sequence('telegram_id_seq', schema=schema_name))
    telegram_text = Column(Text, nullable=False)
    telegram_date = Column(Date, nullable=False, index=True)
    telegram_links = Column(VARCHAR, Sequence('telegram_links_seq', schema=schema_name))
    telegram_channelId = Column(VARCHAR, Sequence('telegram_id_seq', schema=schema_name))
    telegram_numViews = Column(VARCHAR)
    

class TelegramAccount(Base):
    __tablename__ = 'telegram_account'
    __tablename__ = {'schema': schema_name}

    telegram_channelID = Column(VARCHAR)
    telegram_channelAlias = Column(VARCHAR)
    telegram_channelName = Column(Text)
    


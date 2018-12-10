# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:database.py
@time:2018/12/10 001010:28
"""
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

link_address = ""
engine = create_engine(link_address)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class MusicResource(Base):
    ___tablename__ = "tb_music_res"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(63), nullable=False)
    url = Column(String(255), nullable=False)
    singer = Column(String(63), nullable=False)

    def __str__(self):
        return self.name


class SingerList(Base):
    __tablename__ = "tb_singer_name"
    id = Column(Integer, primary_key=True, autoincrement=True)
    singer = Column(String(63), nullable=False)
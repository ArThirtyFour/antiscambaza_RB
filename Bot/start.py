from osnova import botur
from pyrogram import filters

from add_del import add_bd, deletebd, addadmin, deladmin
from ostalnoe import started , help1
from check_info import check, check_you, about


@botur.on_message(filters.command('addbd'))
def da(bot,message):
    add_bd(botur,message)


@botur.on_message(filters.command('delbd'))
def da1(bot,message):
    deletebd(botur,message)


@botur.on_message(filters.command('addadmin'))
def da2(bot,message):
    addadmin(botur,message)


@botur.on_message(filters.command('deladmin'))
def da2(bot,message):
    deladmin(botur,message)


@botur.on_message(filters.command('check'))
def da3(bot,message):
    check(botur,message)


@botur.on_message(filters.command('me'))
def da4(bot,message):
    check_you(botur,message)

@botur.on_message(filters.command('status'))
def da5(bot,message):
    about(botur,message)

@botur.on_message(filters.command('start'))
def da6(bot,message):
    started(botur,message)


@botur.on_message(filters.command('help'))
def da7(bot,message):
    help1(botur,message)


botur.run()
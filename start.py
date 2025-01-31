#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 07:51:37 2025

@author: praid
"""

import asyncio
from aiohttp import web

import numpy as np
from numpy.random import random as randf
import time

users = {}
starship_ore = 10.
station_ore = 0.

async def ore_data(request):
    #data = await request.json()
    #print(request.query)
    username = request.query["username"]
    if username in users:
        return web.json_response({"starship_ore": users[username]["starship_ore"], "station_ore": station_ore})

async def mining(request):
    global starship_ore
    username = request.query["username"]
    await asyncio.sleep(0.1)
    if username in users:
        users[username]["starship_ore"] += randf() + 0.1
        #print(users)
    #starship_ore += randf() + 0.1

async def heartbeat(request):
    print(users)
    return web.Response(text="OK")

async def login(request):
    username = await request.text()
    if not username in users:
        users[username] = {"starship_ore": 0}
    users[username]["last_login"] = time.time()
    return web.Response(text="logged")


app = web.Application()
app.router.add_post('/login', login)
app.router.add_get("/ore_data", ore_data)
app.router.add_get("/mining", mining)
app.router.add_get("/heartbeat", heartbeat)

if __name__ == '__main__':
    web.run_app(app)
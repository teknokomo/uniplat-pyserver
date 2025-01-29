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

starship_ore = 10.
station_ore = 0.

async def handle(request): # Testing routines, to be deleted
    return web.Response(text="Hello, world")

async def root_post(request): # Testing routines, to be deleted
    text = await request.text()
    #print(text)
    return web.Response(text=text)

async def ore_data(request):
    #data = await request.json()
    return web.json_response({"starship_ore": starship_ore, "station_ore": station_ore})

async def mining(request):
    global starship_ore
    await asyncio.sleep(0.1)
    starship_ore += randf() + 0.1

async def heartbeat(request):
    return web.Response(text="OK")

app = web.Application()
app.router.add_get('/', handle)
app.router.add_post('/', root_post)
app.router.add_get("/ore_data", ore_data)
app.router.add_get("/mining", mining)
app.router.add_get("/heartbeat", heartbeat)

if __name__ == '__main__':
    web.run_app(app)
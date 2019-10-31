# -*- coding: utf-8 -*-

import logging
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import process

logger = logging.getLogger(__name__)


class EventLoggerPlugin(MachineBasePlugin):

    async def catch_all(self, event):
        logger.debug("Event received: %s", event)


class EchoPlugin(MachineBasePlugin):

    @process(slack_event_type='message')
    async def echo_message(self, event):
        logger.debug("Message received: %s", event)
        await self.say(event['channel'], event['text'])

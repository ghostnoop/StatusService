from datetime import datetime, timedelta
from typing import List

from models.main import Script

MINUTES = 10


async def check_status():
    scripts: List[Script] = await Script.all()
    now = datetime.now()
    minutes = now.timestamp() - (now - timedelta(minutes=10)).timestamp()
    for script in scripts:
        check = ((now.timestamp() - script.last_connection.timestamp()) > minutes)
        if check:
            script.alive = False
            await script.save(update_fields=['alive'])
        elif script.alive == False and (not check):
            script.alive = True
            await script.save(update_fields=['alive'])
        print(script.name, script.last_connection, script.alive)

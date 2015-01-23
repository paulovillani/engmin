#!/bin/bash
python manage.py dumpdata planilha | python -m json.tool > /home/photo/apps/engmin/planilha/fixtures/initial_data.json

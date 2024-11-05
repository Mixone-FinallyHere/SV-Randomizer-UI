@echo off
title SV Randomizer UI by Mixone using XLumas code
python -m venv importantCodeThings
call importantCodeThings\Scripts\activate.bat
python -m pip install -r requirements.txt
python RandomizerUI.py
:py RandomizerUI.py
Pause
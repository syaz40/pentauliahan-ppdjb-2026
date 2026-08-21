import re

# Read the previous merged file from git / backup or from the original template
# In the original merge, we had lines 1 to 1650 for the 6 modals
# Let's extract them from the backup or re-create Modals.html cleanly

# Let's check if 06_Arkib_Fail has any of the original html files or if we can extract from previous version
import os

with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\00_SEJARAH_PERBUALAN_LENGKAP_PROJECT.md", "r", encoding="utf-8") as f:
    history = f.read()

# Let's create a clean Modals.html with the 6 modals routed via <? if (page === ...) ?>
# Since Modals.html will ONLY have the 6 small Sheet dialogs (total ~40KB instead of 310KB),
# it will be super fast and never conflict with Index.html!

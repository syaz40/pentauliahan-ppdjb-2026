import json

with open(r'C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\steps\1212\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find goog.script.init
idx = content.find('goog.script.init(')
if idx != -1:
    print("Found goog.script.init!")
    # Find the string inside goog.script.init("...")
    start_quote = content.find('"', idx)
    end_quote = content.find('"', start_quote + 1)
    # Actually it's goog.script.init("...") where the argument is an escaped json string
    # Let's extract the userHtml part
    user_html_idx = content.find('userHtml', idx)
    print("userHtml found at:", user_html_idx)
    # Check if script tags are inside userHtml
    script_count = content.count('<script', idx)
    print("Script count after init:", script_count)
else:
    print("goog.script.init not found")

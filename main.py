"""Last Text at One Percent — make.fun entry.

Writes exactly one line (the phone's last text at 1% battery) to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os

TEXT = "I'm at 1%. If anyone asks, I died doing what I loved: judging your 2 a.m. searches. Delete the browser history. Goodbye."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)

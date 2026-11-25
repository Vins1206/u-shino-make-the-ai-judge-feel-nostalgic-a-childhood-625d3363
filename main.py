# One sentence, one childhood memory: written exactly as-is, no trailing newline.
from pathlib import Path

TEXT = "Every August evening my grandmother stood at the stove in her faded apron, frying rice while the cicadas sang outside, and I sat on the counter swinging my legs, not knowing those were the last summers I would ever taste."

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(TEXT, encoding="utf-8")

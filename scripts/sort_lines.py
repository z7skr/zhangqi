import pyperclip


text = pyperclip.paste()
lines = text.split("\n")
lines = [line.strip() for line in lines]
lines = [line + "\n" for line in lines if line]
lines.sort()
text = "".join(lines)
pyperclip.copy(text)

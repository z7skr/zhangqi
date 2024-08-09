import os
import glob
import re
import sys


def transform(file):
    import_first = True
    with open(file) as fr:
        origin_lines = fr.readlines()
        lines, inputs, outputs, funcs = [], [], [], []
        for line in origin_lines:
            line = line.rstrip()
            if line in ["#", "--", "//", "# algorithms"]:
                continue
            if (
                line.startswith("# Likes:")
                or line.startswith("# Dislikes:")
                or line.startswith("# Total ")
            ):
                continue
            if import_first and ") ->" in line or ")->" in line:
                impt = ", ".join(list(set(re.findall(r"List|Optional", line))))
                if impt:
                    lines.append(f"    from typing import {impt}")
                import_first = False
            if line[:5] in ["# 输入：", "# 输入:"]:
                x = list(map(str.strip, line[5:].split(", ")))
                x = line[5:].split(", ")
                x = list(map(lambda i: i.strip(), x))
                inputs.append("\n".join(x))
            if line[:5] in ["# 输出：", "# 输出:"]:
                outputs.append("# " + line[5:])
            if line[:7] == "    def":
                funcs.append(line)
            lines.append(line)

        func = re.findall(r"def (\w+)", funcs[0])[0]
        try:
            args = [re.findall(r"(.*?)=", i)[0].strip() for i in inputs[0].split("\n")]
            flag = 1
        except:
            args = []
            flag = 0

    with open(file, "w") as fw:
        text = "\n".join(lines)
        fw.write(text + "\n")
        fw.write(f"func = Solution().{func}" + "\n")
        if flag == 1:
            for i, o in zip(inputs, outputs):
                fw.write(i + "\n")
                fw.write(f"print(func({', '.join(args)}))" + "\n")
                fw.write(o + "\n\n")


def transform2(file):
    with open(file) as fr:
        origin_lines = fr.readlines()
        lines = []
        for line in origin_lines:
            line = line.rstrip()
            if line in ["#", "--", "//", "# algorithms"]:
                continue
            if (
                line.startswith("# Likes:")
                or line.startswith("# Dislikes:")
                or line.startswith("# Total ")
            ):
                continue
            lines.append(line)

    with open(file, "w") as fw:
        text = "\n".join(lines)
        fw.write(text + "\n")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lc_dir = os.path.abspath(os.path.join(base_dir, "../leetcode"))
    log_file = os.path.abspath(os.path.join(base_dir, "leetcode_delete.log"))
    if not os.path.exists(log_file):
        os.system(f"touch {log_file}")

    f_log = open(log_file)
    files_done = set(f_log.read().split("\n"))
    files_all = glob.glob(lc_dir + "/*.py")
    files_all = [f.split("/")[-1] for f in files_all]
    files_all = list(filter(lambda x: len(re.findall(r"\d+", x)) > 0, files_all))
    files_all.sort(key=lambda x: int(re.findall(r"\d+", x)[0]))
    files_todo = [f for f in files_all if f not in files_done]

    if len(sys.argv) == 2:
        specify = sys.argv[1].split(",")
        files_todo = [f for f in files_all if f.split(".")[0] in specify]

    with open(log_file, "a") as f_log:
        for file in files_todo:
            path = os.path.join(lc_dir, file)
            print(file)
            transform(path)
            f_log.write(file + "\n")

    with open(log_file, "rt") as f_log:
        lines = f_log.readlines()
    newlines = []
    for line in reversed(lines):
        if line not in newlines:
            newlines.append(line)
    with open(log_file, "wt") as f_log:
        f_log.write("".join(newlines[::-1]))

    # for file in files_all:
    #     path = os.path.join(lc_dir, file)
    #     print(file)
    #     transform2(path)


if __name__ == "__main__":
    main()

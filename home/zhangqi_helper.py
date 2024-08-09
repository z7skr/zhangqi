# 查看类的方法
def fir(var):
    """
    打印对象的属性和方法，按类型分组显示。

    参数:
    var: 要检查的对象

    功能:
    1. 获取对象的所有成员
    2. 按类型对成员进行分组
    3. 先打印基本类型的成员
    4. 再按字母顺序打印其他类型的成员
    """
    import re, itertools, inspect, importlib

    def pnt(name, ls):
        """打印类型名称和该类型的成员列表"""
        print("😳" + name + "😳", end=" ")
        if name in prior_print:
            print(sep.join(ls))
        else:
            print()
            for k, v in itertools.groupby(ls, key=lambda x: x[0].lower()):
                print(f"[{k}]", sep.join(v))
        return

    # 获取对象的类型名称
    tp = re.findall(r"'(.*?)'", str(type(var)))[0]
    types = {}
    try:
        # 尝试直接获取对象的成员
        member_list = inspect.getmembers(var)
    except:
        # 如果失败，尝试导入模块并获取成员
        pkg = importlib.import_module(tp.split(".")[0])
        pkg_rest = ".".join(tp.split(".")[1:])
        var = eval(f"pkg.{pkg_rest}")
        member_list = inspect.getmembers(var)

    # 对成员进行分类
    for i, j in member_list:
        if i.startswith("_"):
            continue
        obj = eval(f"var.{i}")
        t = re.findall(r"'(.*?)'", str(type(obj)))[0]
        types[t] = types.get(t, []) + [i]

    # 设置打印顺序和分隔符
    sep, prior_print = " ", [
        "int",
        "float",
        "str",
        "bytes",
        "bool",
        "list",
        "tuple",
        "dict",
        "NoneType",
    ]
    
    # 打印对象类型
    print("😂type =", {tp})
    
    # 先打印基本类型
    for tp in prior_print:
        if tp in types:
            pnt(tp, types[tp])
            del types[tp]
    
    # 按字母顺序打印其他类型
    types = list(types.items())
    types.sort(key=lambda x: x[0])
    for tp, members in types:
        pnt(tp, members)


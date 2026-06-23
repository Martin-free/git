"""
这是一个用来测试 Git 仓库的简单 Python 脚本
"""

def greet(name):
    """向用户问好"""
    return f"Hello, {name}! 你的 Git 仓库测试成功啦！🎉"

if __name__ == "__main__":
    # 打印测试信息
    print(greet("开发者"))
    print("当前状态：文件已创建，准备提交到 Git 仓库。")
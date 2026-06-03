import os
import shutil
import subprocess
import sys

def main():
    # 1. 定义源文件和目标路径
    src_filename = "global.gitignore"
    # os.path.expanduser("~") 会自动获取当前操作系统的用户主目录 (如 C:\Users\Username 或 /home/username)
    user_home = os.path.expanduser("~")
    dest_filepath = os.path.join(user_home, src_filename)

    # 检查当前目录下是否存在 global.gitignore
    if not os.path.exists(src_filename):
        print(f"❌ 错误: 当前目录下未找到 '{src_filename}' 文件，请检查。")
        sys.exit(1)

    # 2. 将文件复制到用户目录
    try:
        # copy2 会尽量保留文件的元数据 (如修改时间)
        shutil.copy2(src_filename, dest_filepath)
        print(f"✅ 成功: 已将 '{src_filename}' 复制到 '{dest_filepath}'")
    except Exception as e:
        print(f"❌ 复制文件失败: {e}")
        sys.exit(1)

    # 3. 自动等待用户输入
    print("\n--- Git 全局环境配置 ---")
    git_username = input("请输入您的 Git 用户名: ").strip()
    git_email = input("请输入您的 Git 邮箱: ").strip()

    if not git_username or not git_email:
        print("❌ 错误: 用户名和邮箱不能为空。")
        sys.exit(1)

    # 4. 准备 Git 配置命令
    # 针对 Windows 系统兼容性，将路径中的反斜杠 \ 替换为正斜杠 /，Git 对正斜杠解析更好
    git_excludesfile_path = dest_filepath.replace("\\", "/")

    git_configs = [
        ["git", "config", "--global", "user.name", git_username],
        ["git", "config", "--global", "user.email", git_email],
        ["git", "config", "--global", "core.excludesfile", git_excludesfile_path]
    ]

    # 5. 使用 subprocess 执行命令
    print("\n正在应用 Git 配置...")
    for cmd in git_configs:
        try:
            # check=True 表示如果命令执行返回非 0 状态码，将抛出 CalledProcessError 异常
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"   -> 已设置: {cmd[3]} = {cmd[4]}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Git 配置失败: 运行命令 '{' '.join(cmd)}' 时出错。")
            print(f"错误详情: {e.stderr.decode('utf-8', errors='ignore').strip()}")
            sys.exit(1)
        except FileNotFoundError:
             print("❌ 错误: 未找到 'git' 命令，请确认系统已安装 Git 并添加到了环境变量 (PATH) 中。")
             sys.exit(1)

    print("\n🎉 Git 全局配置已全部成功完成！")

if __name__ == "__main__":
    main()
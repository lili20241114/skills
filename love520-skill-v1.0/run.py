
#!/usr/bin/env python3
"""
520浪漫表白技能启动脚本
"""
import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from love520_skill.gui import main

if __name__ == "__main__":
    main()

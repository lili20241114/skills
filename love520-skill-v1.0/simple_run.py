
#!/usr/bin/env python3
"""
简化版启动脚本 - 直接在目录中运行
"""
import sys
import os
import webbrowser

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import LoveConfig
from generator import Love520Generator

print("💖 520 浪漫表白技能")
print("=" * 40)

# 尝试启动GUI
try:
    from PyQt5.QtWidgets import QApplication
    from gui import Love520GUI
    
    print("🎨 正在启动图形化界面...")
    app = QApplication(sys.argv)
    window = Love520GUI()
    window.show()
    sys.exit(app.exec_())
    
except ImportError:
    print("⚠️  PyQt5不可用，使用命令行模式")
    print()
    
    # 创建配置
    config = LoveConfig()
    
    # 简单的交互式配置
    print("📝 快速配置（直接回车使用默认值）:")
    
    title = input(f"主标题 [{config.title}]: ").strip()
    if title:
        config.title = title
    
    subtitle = input(f"副标题 [{config.subtitle}]: ").strip()
    if subtitle:
        config.subtitle = subtitle
    
    print()
    print("表白语（输入空行结束）:")
    print(f"[当前]: {config.love_message}")
    
    # 生成页面
    generator = Love520Generator(config)
    
    # 保存文件
    output_file = os.path.join(os.path.dirname(__file__), "love520.html")
    generator.save_to_file(output_file)
    
    print()
    print(f"✅ 页面已生成: {output_file}")
    print("💖 在浏览器中打开...")
    
    webbrowser.open(f'file:///{os.path.abspath(output_file)}')


"""
配置管理模块
"""
import json
import os
from dataclasses import dataclass, asdict, field
from typing import Dict, Any


@dataclass
class LoveConfig:
    """表白配置类"""
    
    # 标题配置
    title: str = "💖 520 我爱你 💖"
    subtitle: str = "用代码写下的浪漫"
    
    # 表白内容配置
    love_message: str = "在这个特别的日子里\n我想对你说：\n遇见你是我最美的意外\n愿意和我在一起吗？"
    highlight_text: str = "遇见你是我最美的意外"
    
    # 按钮配置
    yes_button_text: str = "💕 我愿意 💕"
    no_button_text: str = "😢 再想想"
    
    # 成功弹窗配置
    success_title: str = "🎉 太棒了！🎉"
    success_message: str = "从今天起\n我们的故事正式开始\n❤️ 永远在一起 ❤️"
    
    # 代码块配置
    code_block: str = """const love = true;
while (love) {
  // 每一天都更爱你
  let happiness = "you + me";
  if (you == "happy") {
    love++; // 无限循环
  }
}"""
    
    # 样式配置
    primary_color: str = "#ff6b9d"
    secondary_color: str = "#ff1493"
    accent_color: str = "#ffd700"
    background_color: str = "#1a0a2e"
    
    # 特效配置
    particle_count: int = 100
    show_particles: bool = True
    show_floating_hearts: bool = True
    
    # 预设模板
    @classmethod
    def get_preset_templates(cls) -&gt; Dict[str, Dict[str, Any]]:
        """获取预设模板"""
        return {
            "经典浪漫": {
                "title": "💖 520 我爱你 💖",
                "subtitle": "用代码写下的浪漫",
                "love_message": "在这个特别的日子里\n我想对你说：\n遇见你是我最美的意外\n愿意和我在一起吗？",
                "highlight_text": "遇见你是我最美的意外",
                "primary_color": "#ff6b9d",
                "secondary_color": "#ff1493"
            },
            "程序员的爱": {
                "title": "💻 Hello, My Love 💻",
                "subtitle": "我们的代码从此merge在一起",
                "love_message": "if (you == \"happy\") {\n  I will love you forever;\n} else {\n  I will make you happy first;\n}\n愿意做我的另一半吗？",
                "highlight_text": "愿意做我的另一半吗？",
                "primary_color": "#00ff88",
                "secondary_color": "#00cc6a"
            },
            "永恒约定": {
                "title": "✨ 永远在一起 ✨",
                "subtitle": "我们的故事才刚刚开始",
                "love_message": "无论未来怎样\n我都会陪在你身边\n一起经历所有的美好\n愿意和我永远在一起吗？",
                "highlight_text": "愿意和我永远在一起吗？",
                "primary_color": "#9d4edd",
                "secondary_color": "#7b2cbf"
            }
        }
    
    def to_dict(self) -&gt; Dict[str, Any]:
        """转换为字典"""
        return asdict(self)
    
    def from_dict(self, data: Dict[str, Any]) -&gt; None:
        """从字典加载配置"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def save(self, filepath: str) -&gt; None:
        """保存配置到文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
    
    @classmethod
    def load(cls, filepath: str) -&gt; 'LoveConfig':
        """从文件加载配置"""
        if not os.path.exists(filepath):
            return cls()
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        config = cls()
        config.from_dict(data)
        return config


"""
520浪漫表白技能
一个可自定义配置的浪漫表白页面生成器
"""

__version__ = "1.0.0"
__author__ = "520表白技能"

from .generator import Love520Generator
from .config import LoveConfig

__all__ = ['Love520Generator', 'LoveConfig']

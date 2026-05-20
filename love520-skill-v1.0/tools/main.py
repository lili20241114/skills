
"""
520表白技能 - 主入口文件
"""
import sys
import os
import json
import tempfile
from typing import Dict, Any, Optional

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import LoveConfig
from generator import Love520Generator

class Love520Skill:
    """520表白技能主类"""
    
    def __init__(self):
        self.config = LoveConfig()
        self.generator = Love520Generator(self.config)
        self.last_html_path: Optional[str] = None
        self.config_dir = os.path.join(tempfile.gettempdir(), 'love520_configs')
        os.makedirs(self.config_dir, exist_ok=True)
    
    def handle_tool(self, tool_name: str, params: Dict[str, Any]) -&gt; Dict[str, Any]:
        """处理工具调用"""
        
        try:
            if tool_name == "generate":
                return self._handle_generate(params)
            elif tool_name == "open_preview":
                return self._handle_open_preview(params)
            elif tool_name == "save_config":
                return self._handle_save_config(params)
            elif tool_name == "load_config":
                return self._handle_load_config(params)
            elif tool_name == "list_configs":
                return self._handle_list_configs(params)
            else:
                return {
                    "success": False,
                    "message": f"Unknown tool: {tool_name}"
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error: {str(e)}"
            }
    
    def _handle_generate(self, params: Dict[str, Any]) -&gt; Dict[str, Any]:
        """处理生成工具"""
        config_param = params.get("config", "default")
        
        # 处理配置
        if isinstance(config_param, str):
            # 预设模板
            if not self.config.apply_preset(config_param):
                return {
                    "success": False,
                    "message": f"Unknown preset: {config_param}"
                }
        elif isinstance(config_param, dict):
            # 自定义配置
            self.config.from_dict(config_param)
        
        # 生成HTML
        output_path = os.path.join(tempfile.gettempdir(), 'love520.html')
        self.generator.save_to_file(output_path)
        self.last_html_path = output_path
        
        return {
            "success": True,
            "html_path": output_path,
            "message": f"Generated successfully: {output_path}"
        }
    
    def _handle_open_preview(self, params: Dict[str, Any]) -&gt; Dict[str, Any]:
        """处理预览工具"""
        html_path = params.get("html_path")
        
        if html_path is None:
            html_path = self.last_html_path
        
        if html_path is None:
            return {
                "success": False,
                "message": "No HTML file to preview. Please generate one first."
            }
        
        if not os.path.exists(html_path):
            return {
                "success": False,
                "message": f"HTML file not found: {html_path}"
            }
        
        self.generator.open_in_browser(html_path)
        
        return {
            "success": True,
            "message": f"Opened preview: {html_path}"
        }
    
    def _handle_save_config(self, params: Dict[str, Any]) -&gt; Dict[str, Any]:
        """处理保存配置工具"""
        config_name = params.get("name")
        config_data = params.get("config")
        
        if not config_name:
            return {
                "success": False,
                "message": "Config name is required"
            }
        
        if config_data:
            self.config.from_dict(config_data)
        
        config_path = os.path.join(self.config_dir, f"{config_name}.json")
        self.config.save(config_path)
        
        return {
            "success": True,
            "config_path": config_path,
            "message": f"Config saved: {config_path}"
        }
    
    def _handle_load_config(self, params: Dict[str, Any]) -&gt; Dict[str, Any]:
        """处理加载配置工具"""
        config_name = params.get("name")
        
        if not config_name:
            return {
                "success": False,
                "message": "Config name is required"
            }
        
        config_path = os.path.join(self.config_dir, f"{config_name}.json")
        loaded_config = LoveConfig.load(config_path)
        
        if loaded_config is None:
            return {
                "success": False,
                "message": f"Config not found: {config_name}"
            }
        
        self.config = loaded_config
        self.generator.config = loaded_config
        
        return {
            "success": True,
            "config": loaded_config.to_dict(),
            "message": f"Config loaded: {config_name}"
        }
    
    def _handle_list_configs(self, params: Dict[str, Any]) -&gt; Dict[str, Any]:
        """处理列出配置工具"""
        config_files = []
        
        if os.path.exists(self.config_dir):
            for filename in os.listdir(self.config_dir):
                if filename.endswith('.json'):
                    config_files.append(filename[:-5])
        
        return {
            "success": True,
            "configs": config_files,
            "message": f"Found {len(config_files)} configs"
        }

def main():
    """命令行入口"""
    if len(sys.argv) &lt; 2:
        print("Usage: python main.py &lt;tool_name&gt; [json_params]")
        print("\nAvailable tools:")
        print("  generate - Generate love page")
        print("  open_preview - Open preview in browser")
        print("  save_config - Save config")
        print("  load_config - Load config")
        print("  list_configs - List saved configs")
        return
    
    tool_name = sys.argv[1]
    params = {}
    
    if len(sys.argv) &gt; 2:
        try:
            params = json.loads(sys.argv[2])
        except Exception:
            print("Warning: Failed to parse params, using empty params")
    
    skill = Love520Skill()
    result = skill.handle_tool(tool_name, params)
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

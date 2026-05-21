
"""
图形化配置界面
"""
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QTabWidget,
    QFileDialog, QMessageBox, QGroupBox, QFormLayout, QColorDialog,
    QSpinBox, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from .config import LoveConfig
from .generator import Love520Generator


class Love520GUI(QMainWindow):
    """520表白技能主界面"""
    
    def __init__(self):
        super().__init__()
        self.config = LoveConfig()
        self.generator = Love520Generator(self.config)
        self.current_config_path = None
        self.init_ui()
        
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle("💖 520 浪漫表白技能")
        self.setGeometry(100, 100, 900, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # 标题
        title_label = QLabel("💖 520 浪漫表白页面生成器")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ff6b9d; text-align: center;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 标签页
        tab_widget = QTabWidget()
        
        # 基础配置标签页
        basic_tab = self.create_basic_tab()
        tab_widget.addTab(basic_tab, "📝 基础配置")
        
        # 高级配置标签页
        advanced_tab = self.create_advanced_tab()
        tab_widget.addTab(advanced_tab, "⚙️ 高级配置")
        
        main_layout.addWidget(tab_widget)
        
        # 预设模板
        preset_layout = QHBoxLayout()
        preset_label = QLabel("选择预设模板:")
        preset_layout.addWidget(preset_label)
        
        self.preset_combo = QComboBox()
        self.preset_combo.addItems(list(LoveConfig.get_preset_templates().keys()))
        self.preset_combo.currentTextChanged.connect(self.apply_preset)
        preset_layout.addWidget(self.preset_combo)
        
        main_layout.addLayout(preset_layout)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        
        self.save_config_btn = QPushButton("💾 保存配置")
        self.save_config_btn.clicked.connect(self.save_config)
        button_layout.addWidget(self.save_config_btn)
        
        self.load_config_btn = QPushButton("📂 加载配置")
        self.load_config_btn.clicked.connect(self.load_config)
        button_layout.addWidget(self.load_config_btn)
        
        self.generate_btn = QPushButton("✨ 生成并预览")
        self.generate_btn.setStyleSheet("background: linear-gradient(135deg, #ff6b9d, #ff1493); color: white; font-weight: bold; padding: 15px;")
        self.generate_btn.clicked.connect(self.generate_and_preview)
        button_layout.addWidget(self.generate_btn)
        
        self.save_html_btn = QPushButton("📄 保存HTML")
        self.save_html_btn.clicked.connect(self.save_html)
        button_layout.addWidget(self.save_html_btn)
        
        main_layout.addLayout(button_layout)
        
    def create_basic_tab(self) -&gt; QWidget:
        """创建基础配置标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 标题配置
        title_group = QGroupBox("标题配置")
        title_layout = QFormLayout(title_group)
        
        self.title_edit = QLineEdit(self.config.title)
        self.title_edit.textChanged.connect(self.update_config)
        title_layout.addRow("主标题:", self.title_edit)
        
        self.subtitle_edit = QLineEdit(self.config.subtitle)
        self.subtitle_edit.textChanged.connect(self.update_config)
        title_layout.addRow("副标题:", self.subtitle_edit)
        
        layout.addWidget(title_group)
        
        # 表白内容
        message_group = QGroupBox("表白内容")
        message_layout = QFormLayout(message_group)
        
        self.love_message_edit = QTextEdit(self.config.love_message)
        self.love_message_edit.setMaximumHeight(150)
        self.love_message_edit.textChanged.connect(self.update_config)
        message_layout.addRow("表白语:", self.love_message_edit)
        
        self.highlight_edit = QLineEdit(self.config.highlight_text)
        self.highlight_edit.textChanged.connect(self.update_config)
        message_layout.addRow("高亮文字:", self.highlight_edit)
        
        layout.addWidget(message_group)
        
        # 按钮文字
        button_group = QGroupBox("按钮配置")
        button_layout = QFormLayout(button_group)
        
        self.yes_btn_edit = QLineEdit(self.config.yes_button_text)
        self.yes_btn_edit.textChanged.connect(self.update_config)
        button_layout.addRow("接受按钮:", self.yes_btn_edit)
        
        self.no_btn_edit = QLineEdit(self.config.no_button_text)
        self.no_btn_edit.textChanged.connect(self.update_config)
        button_layout.addRow("拒绝按钮:", self.no_btn_edit)
        
        layout.addWidget(button_group)
        
        # 成功弹窗
        success_group = QGroupBox("成功弹窗")
        success_layout = QFormLayout(success_group)
        
        self.success_title_edit = QLineEdit(self.config.success_title)
        self.success_title_edit.textChanged.connect(self.update_config)
        success_layout.addRow("弹窗标题:", self.success_title_edit)
        
        self.success_message_edit = QTextEdit(self.config.success_message)
        self.success_message_edit.setMaximumHeight(100)
        self.success_message_edit.textChanged.connect(self.update_config)
        success_layout.addRow("弹窗内容:", self.success_message_edit)
        
        layout.addWidget(success_group)
        
        return widget
    
    def create_advanced_tab(self) -&gt; QWidget:
        """创建高级配置标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 代码块
        code_group = QGroupBox("代码块")
        code_layout = QVBoxLayout(code_group)
        
        self.code_edit = QTextEdit(self.config.code_block)
        self.code_edit.setFontFamily("Courier New")
        self.code_edit.textChanged.connect(self.update_config)
        code_layout.addWidget(self.code_edit)
        
        layout.addWidget(code_group)
        
        # 颜色配置
        color_group = QGroupBox("颜色配置")
        color_layout = QFormLayout(color_group)
        
        self.primary_color_btn = QPushButton()
        self.primary_color_btn.setStyleSheet(f"background-color: {self.config.primary_color};")
        self.primary_color_btn.clicked.connect(lambda: self.choose_color('primary'))
        color_layout.addRow("主色调:", self.primary_color_btn)
        
        self.secondary_color_btn = QPushButton()
        self.secondary_color_btn.setStyleSheet(f"background-color: {self.config.secondary_color};")
        self.secondary_color_btn.clicked.connect(lambda: self.choose_color('secondary'))
        color_layout.addRow("次色调:", self.secondary_color_btn)
        
        self.accent_color_btn = QPushButton()
        self.accent_color_btn.setStyleSheet(f"background-color: {self.config.accent_color};")
        self.accent_color_btn.clicked.connect(lambda: self.choose_color('accent'))
        color_layout.addRow("强调色:", self.accent_color_btn)
        
        layout.addWidget(color_group)
        
        # 特效配置
        effect_group = QGroupBox("特效配置")
        effect_layout = QFormLayout(effect_group)
        
        self.particle_spin = QSpinBox()
        self.particle_spin.setRange(10, 500)
        self.particle_spin.setValue(self.config.particle_count)
        self.particle_spin.valueChanged.connect(self.update_config)
        effect_layout.addRow("粒子数量:", self.particle_spin)
        
        self.show_particles_check = QCheckBox("显示粒子动画")
        self.show_particles_check.setChecked(self.config.show_particles)
        self.show_particles_check.stateChanged.connect(self.update_config)
        effect_layout.addRow(self.show_particles_check)
        
        self.show_hearts_check = QCheckBox("显示浮动爱心")
        self.show_hearts_check.setChecked(self.config.show_floating_hearts)
        self.show_hearts_check.stateChanged.connect(self.update_config)
        effect_layout.addRow(self.show_hearts_check)
        
        layout.addWidget(effect_group)
        
        return widget
    
    def choose_color(self, color_type: str):
        """选择颜色"""
        current_color = getattr(self.config, f'{color_type}_color')
        color = QColorDialog.getColor(QColor(current_color), self, "选择颜色")
        
        if color.isValid():
            color_hex = color.name()
            setattr(self.config, f'{color_type}_color', color_hex)
            
            btn = getattr(self, f'{color_type}_color_btn')
            btn.setStyleSheet(f"background-color: {color_hex};")
    
    def update_config(self):
        """更新配置"""
        self.config.title = self.title_edit.text()
        self.config.subtitle = self.subtitle_edit.text()
        self.config.love_message = self.love_message_edit.toPlainText()
        self.config.highlight_text = self.highlight_edit.text()
        self.config.yes_button_text = self.yes_btn_edit.text()
        self.config.no_button_text = self.no_btn_edit.text()
        self.config.success_title = self.success_title_edit.text()
        self.config.success_message = self.success_message_edit.toPlainText()
        self.config.code_block = self.code_edit.toPlainText()
        self.config.particle_count = self.particle_spin.value()
        self.config.show_particles = self.show_particles_check.isChecked()
        self.config.show_floating_hearts = self.show_hearts_check.isChecked()
    
    def apply_preset(self, preset_name: str):
        """应用预设模板"""
        templates = LoveConfig.get_preset_templates()
        if preset_name in templates:
            template = templates[preset_name]
            
            # 更新配置
            for key, value in template.items():
                if hasattr(self.config, key):
                    setattr(self.config, key, value)
            
            # 更新界面
            self.title_edit.setText(self.config.title)
            self.subtitle_edit.setText(self.config.subtitle)
            self.love_message_edit.setText(self.config.love_message)
            self.highlight_edit.setText(self.config.highlight_text)
            
            # 更新颜色按钮
            self.primary_color_btn.setStyleSheet(f"background-color: {self.config.primary_color};")
            self.secondary_color_btn.setStyleSheet(f"background-color: {self.config.secondary_color};")
            
            QMessageBox.information(self, "成功", f"已应用模板: {preset_name}")
    
    def save_config(self):
        """保存配置"""
        filepath, _ = QFileDialog.getSaveFileName(
            self, "保存配置", "", "JSON Files (*.json)"
        )
        
        if filepath:
            self.config.save(filepath)
            self.current_config_path = filepath
            QMessageBox.information(self, "成功", "配置已保存!")
    
    def load_config(self):
        """加载配置"""
        filepath, _ = QFileDialog.getOpenFileName(
            self, "加载配置", "", "JSON Files (*.json)"
        )
        
        if filepath:
            self.config = LoveConfig.load(filepath)
            self.generator.config = self.config
            
            # 更新界面
            self.title_edit.setText(self.config.title)
            self.subtitle_edit.setText(self.config.subtitle)
            self.love_message_edit.setText(self.config.love_message)
            self.highlight_edit.setText(self.config.highlight_text)
            self.yes_btn_edit.setText(self.config.yes_button_text)
            self.no_btn_edit.setText(self.config.no_button_text)
            self.success_title_edit.setText(self.config.success_title)
            self.success_message_edit.setText(self.config.success_message)
            self.code_edit.setText(self.config.code_block)
            self.particle_spin.setValue(self.config.particle_count)
            self.show_particles_check.setChecked(self.config.show_particles)
            self.show_hearts_check.setChecked(self.config.show_floating_hearts)
            
            self.primary_color_btn.setStyleSheet(f"background-color: {self.config.primary_color};")
            self.secondary_color_btn.setStyleSheet(f"background-color: {self.config.secondary_color};")
            self.accent_color_btn.setStyleSheet(f"background-color: {self.config.accent_color};")
            
            QMessageBox.information(self, "成功", "配置已加载!")
    
    def generate_and_preview(self):
        """生成并预览"""
        try:
            self.generator.open_in_browser()
            QMessageBox.information(self, "成功", "页面已在浏览器中打开!")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成失败: {str(e)}")
    
    def save_html(self):
        """保存HTML"""
        filepath, _ = QFileDialog.getSaveFileName(
            self, "保存HTML", "love520.html", "HTML Files (*.html)"
        )
        
        if filepath:
            try:
                self.generator.save_to_file(filepath)
                QMessageBox.information(self, "成功", f"HTML已保存到:\n{filepath}")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存失败: {str(e)}")


def main():
    """主函数"""
    app = QApplication(sys.argv)
    window = Love520GUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

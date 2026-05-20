
---
name: 520浪漫表白技能
version: 1.0.0
description: 一个可自定义配置的浪漫表白页面生成器，包含炫酷的粒子动画、跳动爱心、互动按钮等功能，适合520、情人节、纪念日等场合。
author: 520表白团队
tags: ["表白", "情人节", "520", "浪漫", "HTML", "动画"]
homepage: https://github.com/love520/skill
---

# 520浪漫表白技能

## 功能介绍

一个强大的表白页面生成技能，可以帮助用户快速创建包含炫酷视觉效果的HTML表白页面。

### 核心功能
- 🎨 **粒子动画背景** - 100+彩色粒子在屏幕上自由飘动
- 💖 **跳动大爱心** - 中心有一个脉动的红色爱心
- 💕 **浮动爱心雨** - 各种爱心emoji从底部升起
- ✨ **霓虹发光效果** - 标题和文字有漂亮的光晕
- 🎯 **互动按钮** - "我愿意"弹出惊喜，"再想想"会躲起来
- ⚙️ **完全可自定义** - 所有内容、颜色、效果都能自定义

### 预设模板
- 经典浪漫 - 粉色系，温馨浪漫
- 程序员的爱 - 绿色系，科技感十足
- 永恒约定 - 紫色系，神秘浪漫

## 快速开始

### 1. 生成默认表白页面

调用工具生成默认的表白页面：

```json
{
  "action": "generate",
  "config": "default"
}
```

### 2. 自定义表白内容

你可以自定义所有内容：

```json
{
  "action": "generate",
  "config": {
    "title": "💕 亲爱的，我爱你 💕",
    "subtitle": "用代码写下的浪漫",
    "love_message": "从遇见你那一刻，我的世界变得不同...",
    "highlight_text": "遇见你是我最美的意外",
    "yes_button_text": "💕 我愿意 💕",
    "no_button_text": "😢 再想想",
    "success_title": "🎉 太棒了！🎉",
    "success_message": "从今天起，我们的故事正式开始！"
  }
}
```

### 3. 使用预设模板

```json
{
  "action": "generate",
  "config": "programmer" // 或 "classic", "eternal"
}
```

### 4. 保存和加载配置

保存你的配置：
```json
{
  "action": "save_config",
  "name": "my_love_config",
  "config": { /* 你的配置 */ }
}
```

加载配置：
```json
{
  "action": "load_config",
  "name": "my_love_config"
}
```

## 配置说明

### 完整配置选项

```typescript
interface LoveConfig {
  // 标题配置
  title: string;              // 主标题
  subtitle: string;           // 副标题
  
  // 表白内容
  love_message: string;       // 表白语
  highlight_text: string;     // 高亮文字
  
  // 按钮配置
  yes_button_text: string;    // "我愿意"按钮文字
  no_button_text: string;     // "再想想"按钮文字
  
  // 成功弹窗
  success_title: string;      // 成功弹窗标题
  success_message: string;    // 成功弹窗内容
  
  // 代码块
  code_block: string;         // 显示的代码块
  
  // 颜色配置
  primary_color: string;      // 主色调 (默认: #ff6b9d)
  secondary_color: string;    // 次色调 (默认: #ff1493)
  accent_color: string;       // 强调色 (默认: #ffd700)
  background_color: string;   // 背景色 (默认: #1a0a2e)
  
  // 特效配置
  particle_count: number;     // 粒子数量 (默认: 100)
  show_particles: boolean;    // 是否显示粒子 (默认: true)
  show_hearts: boolean;       // 是否显示浮动爱心 (默认: true)
}
```

## 使用示例

### 示例1：程序员的表白

```json
{
  "action": "generate",
  "config": {
    "title": "💻 Hello, My Love 💻",
    "subtitle": "我们的代码从此merge在一起",
    "love_message": "if (you == \"happy\") {\n  I will love you forever;\n} else {\n  I will make you happy first;\n}\n愿意做我的另一半吗？",
    "highlight_text": "愿意做我的另一半吗？",
    "code_block": "const love = true;\nwhile (love) {\n  // 每一天都更爱你\n  let happiness = \"you + me\";\n  if (you == \"happy\") {\n    love++;\n  }\n}",
    "primary_color": "#00ff88",
    "secondary_color": "#00cc6a"
  }
}
```

### 示例2：经典浪漫表白

```json
{
  "action": "generate",
  "config": {
    "title": "💕 520 我爱你 💕",
    "subtitle": "用代码写下的浪漫",
    "love_message": "亲爱的：\n\n在这个特别的520\n我想对你说\n遇见你是我最美的意外\n愿意和我永远在一起吗？",
    "highlight_text": "愿意和我永远在一起吗？"
  }
}
```

## 工具说明

本技能提供以下工具：

### 1. generate
生成表白页面

**参数：**
- `config` - 配置对象或预设名称 ("default", "classic", "programmer", "eternal")

**返回：**
- 生成的HTML文件路径

### 2. open_preview
在浏览器中预览生成的页面

**参数：**
- `html_path` - HTML文件路径（可选，默认使用最新生成的）

### 3. save_config
保存配置

**参数：**
- `name` - 配置名称
- `config` - 配置对象

### 4. load_config
加载已保存的配置

**参数：**
- `name` - 配置名称

**返回：**
- 配置对象

### 5. list_configs
列出所有已保存的配置

**返回：**
- 配置名称列表

## 注意事项

1. 生成的HTML文件是纯前端文件，不依赖任何后端
2. 可以直接将HTML文件发给对方，用浏览器打开即可
3. 建议使用Chrome、Firefox、Edge等现代浏览器
4. 所有内容都在本地处理，保护隐私

## 常见问题

**Q: 我可以修改生成的HTML吗？**
A: 可以！生成的HTML文件是纯文本，可以手动编辑。

**Q: 如何添加背景音乐？**
A: 生成HTML后，可以手动编辑添加`<audio>`标签。

**Q: 页面支持移动端吗？**
A: 支持！页面是响应式设计，在手机上也能完美显示。

---

**版本：1.0.0**
**最后更新：2026-05-20**
**Made with 💖 for Love**

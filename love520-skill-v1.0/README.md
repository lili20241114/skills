
# 520 浪漫表白技能 💖

一个功能强大的表白页面生成技能，帮助你用程序员的方式表达爱意。

## 功能特性

### 炫酷视觉效果
- 🎨 **粒子动画背景** - 100+彩色粒子在屏幕上自由飘动
- 💖 **跳动大爱心** - 中心有一个脉动的红色爱心
- 💕 **浮动爱心雨** - 各种爱心emoji从底部升起
- ✨ **霓虹发光效果** - 标题和文字有漂亮的光晕
- 🎯 **互动按钮** - "我愿意"弹出惊喜，"再想想"会躲来躲去

### 自定义配置
- ✅ 自定义标题和副标题
- ✅ 自定义表白内容
- ✅ 自定义代码块
- ✅ 自定义配色方案
- ✅ 自定义按钮文字
- ✅ 预设模板（经典浪漫、程序员的爱、永恒约定）
- ✅ 配置保存和加载

## 目录结构

```
love520-skill/
├── SKILL.md             # 技能文档
├── skill.json           # 技能配置
├── README.md            # 本文件
└── tools/
    ├── main.py          # 主入口
    ├── config.py        # 配置管理
    └── generator.py     # HTML生成器
```

## 快速开始

### 在 Trae Solo 中使用

1. **确保技能已正确放置**
   - 技能应该在 `.trae/skills/love520-skill/` 目录下

2. **启用技能**
   - 在 Trae Solo 的技能面板中找到 "520浪漫表白技能"
   - 启用该技能

3. **使用技能**
   - 直接对话调用技能，例如："使用520表白技能生成一个经典模板"

### 命令行使用

```bash
# 生成默认页面
python tools/main.py generate '{"config": "default"}'

# 生成程序员模板
python tools/main.py generate '{"config": "programmer"}'

# 自定义配置
python tools/main.py generate '{"config": {"title": "我爱你", "love_message": "遇见你是我最大的幸福"}}'

# 打开预览
python tools/main.py open_preview
```

## 工具说明

### generate
生成表白页面

**参数：**
- `config` - 配置对象或预设名称 ("default", "classic", "programmer", "eternal")

**返回：**
```json
{
  "success": true,
  "html_path": "/tmp/love520.html",
  "message": "Generated successfully"
}
```

### open_preview
在浏览器中预览生成的页面

**参数：**
- `html_path` - HTML文件路径（可选）

### save_config
保存配置

**参数：**
- `name` - 配置名称
- `config` - 配置对象

### load_config
加载已保存的配置

**参数：**
- `name` - 配置名称

### list_configs
列出所有已保存的配置

## 配置选项

完整的配置对象：

```javascript
{
  "title": "💖 520 我爱你 💖",
  "subtitle": "用代码写下的浪漫",
  "love_message": "在这个特别的日子里\n我想对你说：\n遇见你是我最美的意外\n愿意和我在一起吗？",
  "highlight_text": "遇见你是我最美的意外",
  "yes_button_text": "💕 我愿意 💕",
  "no_button_text": "😢 再想想",
  "success_title": "🎉 太棒了！🎉",
  "success_message": "从今天起\n我们的故事正式开始\n❤️ 永远在一起 ❤️",
  "code_block": "const love = true;\nwhile (love) {\n  // 每一天都更爱你\n  let happiness = \"you + me\";\n  if (you == \"happy\") {\n    love++;\n  }\n}",
  "primary_color": "#ff6b9d",
  "secondary_color": "#ff1493",
  "accent_color": "#ffd700",
  "background_color": "#1a0a2e",
  "particle_count": 100,
  "show_particles": true,
  "show_hearts": true
}
```

## 预设模板

### default / classic（经典浪漫）
- 粉色配色
- 温馨浪漫的文字

### programmer（程序员的爱）
- 绿色配色
- 代码风格的表白

### eternal（永恒约定）
- 紫色配色
- 永恒约定的主题

## 示例对话

### 示例1：使用预设模板
```
你：使用520表白技能生成一个程序员模板
AI：好的，正在生成程序员风格的表白页面...
```

### 示例2：自定义内容
```
你：帮我生成一个表白页面，标题是"亲爱的我爱你"，内容是"认识你是我这辈子最开心的事"
AI：正在生成你的专属表白页面...
```

### 示例3：保存配置
```
你：把这个配置保存为"我的表白"
AI：配置已保存为"我的表白"
```

## 注意事项

1. 生成的HTML文件是纯前端文件，不依赖任何后端
2. 可以直接将HTML文件发给对方，用浏览器打开即可
3. 建议使用Chrome、Firefox、Edge等现代浏览器
4. 所有内容都在本地处理，保护隐私

## 常见问题

**Q：我可以修改生成的HTML吗？**
A：可以！生成的HTML文件是纯文本，可以手动编辑。

**Q：如何添加背景音乐？**
A：生成HTML后，可以手动编辑添加`<audio>`标签。

**Q：页面支持移动端吗？**
A：支持！页面是响应式设计，在手机上也能完美显示。

## 版本信息

- **版本：** 1.0.0
- **作者：** 520表白团队
- **最后更新：** 2026-05-20

---

**Made with 💖 for Love**

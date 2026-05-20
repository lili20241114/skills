
"""
HTML生成器模块
"""
import os
import webbrowser
from typing import Optional
from .config import LoveConfig


class Love520Generator:
    """520表白HTML生成器"""
    
    def __init__(self, config: Optional[LoveConfig] = None):
        self.config = config or LoveConfig()
    
    def generate_html(self) -&gt; str:
        """生成完整的HTML页面"""
        
        # 处理换行符
        love_message_html = self.config.love_message.replace('\n', '&lt;br&gt;')
        
        html_template = f'''&lt;!DOCTYPE html&gt;
&lt;html lang="zh-CN"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;{self.config.title}&lt;/title&gt;
    &lt;style&gt;
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            min-height: 100vh;
            background: linear-gradient(135deg, {self.config.background_color} 0%, #2d1b4e 50%, #4a2c7a 100%);
            overflow: hidden;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}

        #canvas-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }}

        #main-canvas {{
            display: block;
        }}

        .content {{
            position: relative;
            z-index: 10;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .title {{
            font-size: 4rem;
            color: {self.config.primary_color};
            text-shadow: 0 0 20px {self.config.primary_color}, 0 0 40px {self.config.primary_color}, 0 0 60px {self.config.secondary_color};
            margin-bottom: 20px;
            animation: titlePulse 2s ease-in-out infinite;
            text-align: center;
        }}

        @keyframes titlePulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}

        .subtitle {{
            font-size: 1.5rem;
            color: {self.config.accent_color};
            text-shadow: 0 0 10px {self.config.accent_color};
            margin-bottom: 40px;
            animation: fadeInUp 1s ease-out 0.5s both;
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .love-container {{
            position: relative;
            margin: 40px 0;
        }}

        .big-heart {{
            font-size: 8rem;
            animation: heartbeat 1s ease-in-out infinite;
            filter: drop-shadow(0 0 30px {self.config.secondary_color});
        }}

        @keyframes heartbeat {{
            0%, 100% {{ transform: scale(1); }}
            14% {{ transform: scale(1.1); }}
            28% {{ transform: scale(1); }}
            42% {{ transform: scale(1.1); }}
            70% {{ transform: scale(1); }}
        }}

        .message-box {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 107, 157, 0.5);
            border-radius: 20px;
            padding: 30px;
            max-width: 600px;
            text-align: center;
            animation: fadeInUp 1s ease-out 1s both;
            box-shadow: 0 0 30px rgba(255, 107, 157, 0.3);
        }}

        .love-message {{
            font-size: 1.5rem;
            color: #fff;
            line-height: 2;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        }}

        .love-message .highlight {{
            color: {self.config.primary_color};
            font-weight: bold;
            font-size: 1.8rem;
        }}

        .buttons {{
            display: flex;
            gap: 20px;
            margin-top: 40px;
            animation: fadeInUp 1s ease-out 1.5s both;
        }}

        .btn {{
            padding: 15px 40px;
            font-size: 1.2rem;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
        }}

        .btn-yes {{
            background: linear-gradient(135deg, {self.config.primary_color}, {self.config.secondary_color});
            color: white;
            box-shadow: 0 5px 20px {self.config.secondary_color}66;
        }}

        .btn-yes:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 30px {self.config.secondary_color}99;
        }}

        .btn-no {{
            background: linear-gradient(135deg, #666, #444);
            color: white;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        }}

        .btn-no:hover {{
            transform: translate(calc(var(--tx, 0) * 1px), calc(var(--ty, 0) * 1px));
        }}

        .success-modal {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }}

        .success-content {{
            background: linear-gradient(135deg, #2d1b4e, #4a2c7a);
            padding: 60px;
            border-radius: 30px;
            text-align: center;
            border: 3px solid {self.config.primary_color};
            box-shadow: 0 0 50px {self.config.primary_color}80;
            animation: successPop 0.5s ease-out;
        }}

        @keyframes successPop {{
            0% {{ transform: scale(0); }}
            50% {{ transform: scale(1.1); }}
            100% {{ transform: scale(1); }}
        }}

        .success-title {{
            font-size: 3rem;
            color: {self.config.primary_color};
            margin-bottom: 20px;
        }}

        .success-text {{
            font-size: 1.5rem;
            color: #fff;
            line-height: 1.8;
        }}

        .floating-hearts {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 5;
        }}

        .floating-heart {{
            position: absolute;
            font-size: 2rem;
            animation: floatHeart 4s ease-in-out infinite;
            opacity: 0;
        }}

        @keyframes floatHeart {{
            0% {{
                opacity: 0;
                transform: translateY(100vh) rotate(0deg);
            }}
            10% {{
                opacity: 1;
            }}
            90% {{
                opacity: 1;
            }}
            100% {{
                opacity: 0;
                transform: translateY(-100px) rotate(360deg);
            }}
        }}

        .code-display {{
            background: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
            font-family: 'Courier New', monospace;
            text-align: left;
            max-width: 500px;
            animation: fadeInUp 1s ease-out 2s both;
        }}

        .code-line {{
            color: #0f0;
            margin: 5px 0;
            font-size: 0.9rem;
        }}

        .code-keyword {{
            color: {self.config.primary_color};
        }}

        .code-string {{
            color: {self.config.accent_color};
        }}

        .code-comment {{
            color: #888;
        }}

        @media (max-width: 768px) {{
            .title {{
                font-size: 2.5rem;
            }}
            .subtitle {{
                font-size: 1.2rem;
            }}
            .big-heart {{
                font-size: 5rem;
            }}
            .love-message {{
                font-size: 1.2rem;
            }}
            .buttons {{
                flex-direction: column;
            }}
        }}
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div id="canvas-container"&gt;
        &lt;canvas id="main-canvas"&gt;&lt;/canvas&gt;
    &lt;/div&gt;

    &lt;div class="floating-hearts" id="floating-hearts"&gt;&lt;/div&gt;

    &lt;div class="content"&gt;
        &lt;h1 class="title"&gt;{self.config.title}&lt;/h1&gt;
        &lt;p class="subtitle"&gt;{self.config.subtitle}&lt;/p&gt;
        
        &lt;div class="love-container"&gt;
            &lt;div class="big-heart"&gt;❤️&lt;/div&gt;
        &lt;/div&gt;

        &lt;div class="message-box"&gt;
            &lt;p class="love-message"&gt;
                {love_message_html.replace(self.config.highlight_text, f'&lt;span class="highlight"&gt;{self.config.highlight_text}&lt;/span&gt;')}
            &lt;/p&gt;
        &lt;/div&gt;

        &lt;div class="code-display"&gt;
            {self._format_code_block(self.config.code_block)}
        &lt;/div&gt;

        &lt;div class="buttons"&gt;
            &lt;button class="btn btn-yes" onclick="sayYes()"&gt;{self.config.yes_button_text}&lt;/button&gt;
            &lt;button class="btn btn-no" id="btn-no" onmouseover="moveNoButton()"&gt;{self.config.no_button_text}&lt;/button&gt;
        &lt;/div&gt;
    &lt;/div&gt;

    &lt;div class="success-modal" id="success-modal"&gt;
        &lt;div class="success-content"&gt;
            &lt;h2 class="success-title"&gt;{self.config.success_title}&lt;/h2&gt;
            &lt;p class="success-text"&gt;
                {self.config.success_message.replace('\\n', '&lt;br&gt;')}
            &lt;/p&gt;
        &lt;/div&gt;
    &lt;/div&gt;

    &lt;script&gt;
        // Canvas粒子动画
        const canvas = document.getElementById('main-canvas');
        const ctx = canvas.getContext('2d');
        
        function resizeCanvas() {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }}
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        // 粒子系统
        class Particle {{
            constructor() {{
                this.reset();
            }}

            reset() {{
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 3 + 1;
                this.speedX = (Math.random() - 0.5) * 2;
                this.speedY = (Math.random() - 0.5) * 2;
                this.opacity = Math.random() * 0.5 + 0.2;
                this.color = this.getRandomColor();
            }}

            getRandomColor() {{
                const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}', '{self.config.primary_color}', '{self.config.secondary_color}'];
                return colors[Math.floor(Math.random() * colors.length)];
            }}

            update() {{
                this.x += this.speedX;
                this.y += this.speedY;

                if (this.x &lt; 0 || this.x &gt; canvas.width) this.speedX *= -1;
                if (this.y &lt; 0 || this.y &gt; canvas.height) this.speedY *= -1;
            }}

            draw() {{
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.globalAlpha = this.opacity;
                ctx.fill();
                ctx.globalAlpha = 1;
            }}
        }}

        const particles = [];
        for (let i = 0; i &lt; {self.config.particle_count}; i++) {{
            particles.push(new Particle());
        }}

        // 绘制心形
        function drawHeart(x, y, size, color) {{
            ctx.save();
            ctx.translate(x, y);
            ctx.scale(size, size);
            ctx.fillStyle = color;
            ctx.globalAlpha = 0.3;
            ctx.beginPath();
            ctx.moveTo(0, -0.5);
            ctx.bezierCurveTo(-1, -1.5, -2, 0, 0, 1.5);
            ctx.bezierCurveTo(2, 0, 1, -1.5, 0, -0.5);
            ctx.fill();
            ctx.restore();
        }}

        // 动画循环
        let heartPhase = 0;
        function animate() {{
            ctx.fillStyle = 'rgba(26, 10, 46, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            particles.forEach(particle =&gt; {{
                particle.update();
                particle.draw();
            }});

            heartPhase += 0.02;
            const heartSize = 150 + Math.sin(heartPhase) * 20;
            drawHeart(canvas.width / 2, canvas.height / 2, heartSize, '{self.config.secondary_color}');

            requestAnimationFrame(animate);
        }}
        animate();

        // 浮动爱心
        function createFloatingHeart() {{
            const heart = document.createElement('div');
            heart.className = 'floating-heart';
            heart.innerHTML = ['❤️', '💕', '💖', '💗', '💓', '💝'][Math.floor(Math.random() * 6)];
            heart.style.left = Math.random() * 100 + '%';
            heart.style.animationDelay = Math.random() * 2 + 's';
            heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
            document.getElementById('floating-hearts').appendChild(heart);

            setTimeout(() =&gt; heart.remove(), 6000);
        }}

        setInterval(createFloatingHeart, 500);

        // "我愿意"按钮
        function sayYes() {{
            const modal = document.getElementById('success-modal');
            modal.style.display = 'flex';
            
            for (let i = 0; i &lt; 20; i++) {{
                setTimeout(createFloatingHeart, i * 100);
            }}
        }}

        // "再想想"按钮 - 会逃跑
        let moveCount = 0;
        function moveNoButton() {{
            const btn = document.getElementById('btn-no');
            moveCount++;
            
            const maxMove = Math.min(200, moveCount * 50);
            const tx = (Math.random() - 0.5) * maxMove;
            const ty = (Math.random() - 0.5) * maxMove;
            
            btn.style.setProperty('--tx', tx);
            btn.style.setProperty('--ty', ty);
            
            if (moveCount &gt; 5) {{
                btn.textContent = '求求了！';
            }}
            if (moveCount &gt; 10) {{
                btn.style.display = 'none';
            }}
        }}
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''
        
        return html_template
    
    def _format_code_block(self, code: str) -&gt; str:
        """格式化代码块，添加语法高亮"""
        lines = code.split('\n')
        formatted_lines = []
        
        keywords = ['const', 'let', 'var', 'function', 'if', 'else', 'for', 'while', 'true', 'false']
        
        for line in lines:
            formatted_line = line
            
            # 高亮关键字
            for keyword in keywords:
                formatted_line = formatted_line.replace(
                    f'{keyword} ', 
                    f'&lt;span class="code-keyword"&gt;{keyword}&lt;/span&gt; '
                )
            
            # 高亮字符串
            import re
            formatted_line = re.sub(
                r'"([^"]*)"',
                r'&lt;span class="code-string"&gt;"\1"&lt;/span&gt;',
                formatted_line
            )
            
            # 高亮注释
            if '//' in formatted_line:
                parts = formatted_line.split('//', 1)
                formatted_line = f'{parts[0]}&lt;span class="code-comment"&gt;//{parts[1]}&lt;/span&gt;'
            
            formatted_lines.append(f'&lt;div class="code-line"&gt;{formatted_line}&lt;/div&gt;')
        
        return '\n'.join(formatted_lines)
    
    def save_to_file(self, filepath: str) -&gt; str:
        """保存HTML到文件"""
        html_content = self.generate_html()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
    
    def open_in_browser(self, filepath: Optional[str] = None) -&gt; None:
        """在浏览器中打开"""
        if filepath is None:
            import tempfile
            filepath = os.path.join(tempfile.gettempdir(), 'love520.html')
            self.save_to_file(filepath)
        
        webbrowser.open(f'file:///{os.path.abspath(filepath)}')

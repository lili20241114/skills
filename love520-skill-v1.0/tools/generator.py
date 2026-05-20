"""
520表白技能 - HTML生成器模块 - 超级炫酷版
"""
import os
import webbrowser
import tempfile
from typing import Optional
from config import LoveConfig

class Love520Generator:
    """520表白HTML生成器"""
    
    def __init__(self, config: Optional[LoveConfig] = None):
        self.config = config or LoveConfig()
    
    def generate_html(self) -> str:
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
      background: linear-gradient(-45deg, #1a0a2e, #2d1b4e, #4a2c7a, #6b3fa0, #4a2c7a, #2d1b4e, #1a0a2e);
      background-size: 400% 400%;
      animation: gradientBG 15s ease infinite;
      overflow: hidden;
      font-family: 'Courier New', monospace;
    }}

    @keyframes gradientBG {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
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
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color}, {self.config.secondary_color}, {self.config.primary_color});
      background-size: 300% 300%;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: titlePulse 2s ease-in-out infinite, gradientText 5s ease infinite;
      text-align: center;
      font-weight: bold;
    }}

    @keyframes titlePulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.08); }}
    }}

    @keyframes gradientText {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}

    .subtitle {{
      font-size: 1.5rem;
      background: linear-gradient(90deg, {self.config.accent_color}, #fff, {self.config.accent_color});
      background-size: 200% 200%;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 40px;
      animation: fadeInUp 1s ease-out 0.5s both, gradientSubtitle 3s ease infinite;
    }}

    @keyframes gradientSubtitle {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}

    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(30px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .love-container {{
      position: relative;
      margin: 40px 0;
    }}

    .big-heart {{
      font-size: 8rem;
      animation: heartbeat 0.8s ease-in-out infinite, heartGlow 2s ease-in-out infinite;
      filter: drop-shadow(0 0 30px {self.config.secondary_color});
    }}

    @keyframes heartbeat {{
      0%, 100% {{ transform: scale(1); }}
      14% {{ transform: scale(1.15); }}
      28% {{ transform: scale(1); }}
      42% {{ transform: scale(1.15); }}
      70% {{ transform: scale(1); }}
    }}

    @keyframes heartGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 30px {self.config.secondary_color}); }}
      50% {{ filter: drop-shadow(0 0 50px {self.config.secondary_color}) drop-shadow(0 0 100px {self.config.primary_color}); }}
    }}

    .message-box {{
      background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,107,157,0.1));
      backdrop-filter: blur(20px);
      border: 3px solid;
      border-image: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color}, {self.config.secondary_color}) 1;
      border-radius: 25px;
      padding: 35px;
      max-width: 600px;
      text-align: center;
      animation: fadeInUp 1s ease-out 1s both, boxGlow 3s ease-in-out infinite;
      box-shadow: 0 0 40px {self.config.primary_color}40;
    }}

    @keyframes boxGlow {{
      0%, 100% {{ box-shadow: 0 0 40px {self.config.primary_color}40; }}
      50% {{ box-shadow: 0 0 60px {self.config.primary_color}60; }}
    }}

    .love-message {{
      font-size: 1.5rem;
      line-height: 2;
    }}

    .love-message .normal {{
      background: linear-gradient(90deg, #fff, {self.config.accent_color}, #fff);
      background-size: 200% 200%;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: gradientMessage 4s ease infinite;
    }}

    @keyframes gradientMessage {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}

    .love-message .highlight {{
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color}, {self.config.secondary_color});
      background-size: 200% 200%;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: bold;
      font-size: 1.8rem;
      animation: gradientHighlight 2s ease infinite;
    }}

    @keyframes gradientHighlight {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}

    .buttons {{
      display: flex;
      gap: 20px;
      margin-top: 40px;
      animation: fadeInUp 1s ease-out 1.5s both;
    }}

    .btn {{
      padding: 18px 50px;
      font-size: 1.3rem;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      transition: all 0.3s ease;
      font-weight: bold;
      position: relative;
      overflow: hidden;
    }}

    .btn::before {{
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
      transform: rotate(45deg);
      animation: btnShine 3s ease-in-out infinite;
    }}

    @keyframes btnShine {{
      0% {{ transform: translateX(-100%) rotate(45deg); }}
      100% {{ transform: translateX(100%) rotate(45deg); }}
    }}

    .btn-yes {{
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.secondary_color});
      color: white;
      box-shadow: 0 8px 30px {self.config.secondary_color}50;
      animation: yesPulse 2s ease-in-out infinite;
    }}

    @keyframes yesPulse {{
      0%, 100% {{ box-shadow: 0 8px 30px {self.config.secondary_color}50; }}
      50% {{ box-shadow: 0 8px 50px {self.config.secondary_color}70; }}
    }}

    .btn-yes:hover {{
      transform: translateY(-5px) scale(1.05);
      box-shadow: 0 12px 40px {self.config.secondary_color}80;
    }}

    .btn-no {{
      background: linear-gradient(135deg, #555, #333);
      color: white;
      box-shadow: 0 5px 20px rgba(0,0,0,0.3);
      white-space: nowrap;
      position: absolute;
      transition: all 0.05s ease;
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
      font-size: 2.5rem;
      animation: floatHeart 5s ease-in-out infinite;
      opacity: 0;
    }}

    @keyframes floatHeart {{
      0% {{ opacity: 0; transform: translateY(100vh) rotate(0deg) scale(0.5); }}
      10% {{ opacity: 1; }}
      90% {{ opacity: 1; }}
      100% {{ opacity: 0; transform: translateY(-150px) rotate(720deg) scale(1.2); }}
    }}

    .code-display {{
      background: linear-gradient(135deg, rgba(0,0,0,0.4), rgba(0,0,0,0.2));
      padding: 25px;
      border-radius: 15px;
      margin-top: 30px;
      font-family: 'Courier New', monospace;
      text-align: left;
      max-width: 500px;
      animation: fadeInUp 1s ease-out 2s both;
      border: 1px solid rgba(255,255,255,0.1);
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

    /* ====== 效果页面样式 ====== */
    .effect-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.95);
      z-index: 2000;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    .warning-flash {{
      animation: warningFlash 0.1s ease-in-out infinite;
    }}

    @keyframes warningFlash {{
      0%, 100% {{ background: rgba(255, 0, 0, 0.3); }}
      50% {{ background: rgba(139, 0, 0, 0.5); }}
    }}

    .canvas-effect {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
    }}

    .love-journey {{
      position: relative;
      z-index: 2;
      text-align: center;
      color: {self.config.primary_color};
    }}

    .journey-title {{
      font-size: 2.5rem;
      margin-bottom: 20px;
      animation: fadeInUp 1s ease-out;
    }}

    .journey-content {{
      font-size: 1.2rem;
      font-family: 'Courier New', monospace;
      line-height: 1.5;
      white-space: pre;
      color: {self.config.accent_color};
      animation: matrixGlow 2s ease infinite;
    }}

    @keyframes matrixGlow {{
      0%, 100% {{ text-shadow: 0 0 10px {self.config.primary_color}; }}
      50% {{ text-shadow: 0 0 30px {self.config.accent_color}, 0 0 50px {self.config.secondary_color}; }}
    }}

    .journey-progress {{
      margin-top: 30px;
      font-size: 1rem;
      color: #888;
    }}

    .more-romantic-btn {{
      margin-top: 40px;
      padding: 15px 40px;
      font-size: 1.2rem;
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.secondary_color});
      color: white;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      animation: yesPulse 2s ease-in-out infinite;
    }}

    .btn-no-escape {{
      position: fixed;
      padding: 12px 30px;
      font-size: 1.1rem;
      background: linear-gradient(135deg, #8B0000, #DC143C);
      color: white;
      border: 2px solid #FF0000;
      border-radius: 50px;
      z-index: 100;
      box-shadow: 0 0 20px rgba(255,0,0,0.5);
      transition: all 0.05s ease;
    }}

    @media (max-width: 768px) {{
      .title {{ font-size: 2.5rem; }}
      .subtitle {{ font-size: 1.2rem; }}
      .big-heart {{ font-size: 5rem; }}
      .love-message {{ font-size: 1.2rem; }}
      .buttons {{ flex-direction: column; align-items: center; }}
      .journey-content {{ font-size: 0.8rem; }}
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
        &lt;span class="normal"&gt;{love_message_html.replace(self.config.highlight_text, f'&lt;/span&gt;&lt;span class="highlight"&gt;{self.config.highlight_text}&lt;/span&gt;&lt;span class="normal"&gt;')}&lt;/span&gt;
      &lt;/p&gt;
    &lt;/div&gt;

    &lt;div class="code-display"&gt;
      {self._format_code_block(self.config.code_block)}
    &lt;/div&gt;

    &lt;div class="buttons"&gt;
      &lt;button class="btn btn-yes" onclick="startLoveEffect()"&gt;{self.config.yes_button_text}&lt;/button&gt;
      &lt;button class="btn btn-no" id="btn-no"&gt;{self.config.no_button_text}&lt;/button&gt;
    &lt;/div&gt;
  &lt;/div&gt;

  &lt;!-- 效果覆盖层 --&gt;
  &lt;div class="effect-overlay" id="effect-overlay"&gt;
    &lt;canvas class="canvas-effect" id="effect-canvas"&gt;&lt;/canvas&gt;
    &lt;div class="love-journey" id="love-journey"&gt;
      &lt;div class="journey-title" id="journey-title"&gt;🎉 恭喜你做出了选择！&lt;/div&gt;
      &lt;div class="journey-content" id="journey-content"&gt;正在加载爱的旅程...&lt;/div&gt;
      &lt;div class="journey-progress" id="journey-progress"&gt;步骤 1/4&lt;/div&gt;
      &lt;button class="more-romantic-btn" id="more-btn" style="display:none;" onclick="showNextPhase()"&gt;✨ 还有更浪漫的 ✨&lt;/button&gt;
    &lt;/div&gt;
  &lt;/div&gt;

  &lt;script&gt;
    const canvas = document.getElementById('main-canvas');
    const ctx = canvas.getContext('2d');
    const effectCanvas = document.getElementById('effect-canvas');
    const effectCtx = effectCanvas.getContext('2d');
    
    function resizeCanvas() {{
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      effectCanvas.width = window.innerWidth;
      effectCanvas.height = window.innerHeight;
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
        this.size = Math.random() * 4 + 1.5;
        this.speedX = (Math.random() - 0.5) * 2.5;
        this.speedY = (Math.random() - 0.5) * 2.5;
        this.opacity = Math.random() * 0.6 + 0.2;
        this.color = this.getRandomColor();
        this.pulse = Math.random() * Math.PI * 2;
      }}

      getRandomColor() {{
        const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}', '#ff69b4', '#ff1493', '#ffd700'];
        return colors[Math.floor(Math.random() * colors.length)];
      }}

      update() {{
        this.x += this.speedX;
        this.y += this.speedY;
        this.pulse += 0.05;
        if (this.x &lt; 0 || this.x &gt; canvas.width) this.speedX *= -1;
        if (this.y &lt; 0 || this.y &gt; canvas.height) this.speedY *= -1;
      }}

      draw() {{
        const pulseSize = this.size * (1 + Math.sin(this.pulse) * 0.3);
        ctx.beginPath();
        ctx.arc(this.x, this.y, pulseSize, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.globalAlpha = this.opacity * (0.7 + Math.sin(this.pulse) * 0.3);
        ctx.fill();
        ctx.globalAlpha = 1;
      }}
    }}

    const particles = [];
    for (let i = 0; i &lt; {self.config.particle_count}; i++) {{
      particles.push(new Particle());
    }}

    function drawHeart(x, y, size, color, alpha = 0.3) {{
      ctx.save();
      ctx.translate(x, y);
      ctx.scale(size, size);
      ctx.fillStyle = color;
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.moveTo(0, -0.5);
      ctx.bezierCurveTo(-1, -1.5, -2, 0, 0, 1.5);
      ctx.bezierCurveTo(2, 0, 1, -1.5, 0, -0.5);
      ctx.fill();
      ctx.restore();
    }}

    let heartPhase = 0;
    function animate() {{
      ctx.fillStyle = 'rgba(26, 10, 46, 0.08)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      particles.forEach(particle => {{
        particle.update();
        particle.draw();
      }});

      heartPhase += 0.025;
      const heartSize = 160 + Math.sin(heartPhase) * 25;
      drawHeart(canvas.width / 2, canvas.height / 2, heartSize, '{self.config.secondary_color}', 0.35);
      drawHeart(canvas.width / 2, canvas.height / 2, heartSize * 0.7, '{self.config.primary_color}', 0.2);

      requestAnimationFrame(animate);
    }}
    animate();

    function createFloatingHeart() {{
      const heart = document.createElement('div');
      heart.className = 'floating-heart';
      const heartTypes = ['❤️', '💕', '💖', '💗', '💓', '💝', '💘', '💞'];
      heart.innerHTML = heartTypes[Math.floor(Math.random() * heartTypes.length)];
      heart.style.left = Math.random() * 100 + '%';
      heart.style.animationDelay = Math.random() * 2 + 's';
      heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
      document.getElementById('floating-hearts').appendChild(heart);
      setTimeout(() => heart.remove(), 6000);
    }}

    setInterval(createFloatingHeart, 300);

    // ====== 爱心逃跑按钮 ======
    const noTexts = [
      '{self.config.no_button_text}',
      '不要嘛~',
      '人家不想',
      '求求你了',
      '不要这么无情',
      '再考虑一下',
      '我会伤心的',
      '不要走~',
      '别这样对我',
      '给个机会',
      '好不好嘛',
      '呜呜呜',
      '人家很乖的',
      '再想想嘛',
      '求你了求你了'
    ];

    let moveCount = 0;
    let btnNo = document.getElementById('btn-no');
    let originalRect = null;
    let noInterval = null;

    function moveNoButton(e) {{
      if (!originalRect) {{
        originalRect = btnNo.getBoundingClientRect();
      }}
      
      moveCount++;
      const textIndex = Math.min(moveCount, noTexts.length - 1);
      btnNo.textContent = noTexts[textIndex];
      
      const maxMove = Math.min(400, moveCount * 80);
      const tx = (Math.random() - 0.5) * maxMove;
      const ty = (Math.random() - 0.5) * maxMove;
      
      btnNo.style.position = 'fixed';
      btnNo.style.zIndex = '100';
      btnNo.style.left = (originalRect.left + tx) + 'px';
      btnNo.style.top = (originalRect.top + ty) + 'px';
      
      if (moveCount > 8) {{
        btnNo.style.fontSize = (1.3 - moveCount * 0.08) + 'rem';
      }}
      
      if (moveCount > 15) {{
        btnNo.style.display = 'none';
        clearInterval(noInterval);
      }}
    }}

    btnNo.addEventListener('mouseenter', () => {{
      if (moveCount &lt; 15) {{
        noInterval = setInterval(() => {{
          if (moveCount &lt; 15) moveNoButton();
        }}, 50);
      }}
    }});

    btnNo.addEventListener('mouseleave', () => {{
      clearInterval(noInterval);
    }});

    document.addEventListener('mousemove', function(e) {{
      if (moveCount &gt; 0 && moveCount &lt;= 15) {{
        const rect = btnNo.getBoundingClientRect();
        const dx = e.clientX - (rect.left + rect.width / 2);
        const dy = e.clientY - (rect.top + rect.height / 2);
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist &lt; 150) {{
          moveNoButton();
        }}
      }}
    }});

    // ====== 警告逃跑按钮 ======
    let escapeBtn = null;
    let escapeInterval = null;
    let escapeCount = 0;

    function createEscapeButton() {{
      escapeBtn = document.createElement('button');
      escapeBtn.className = 'btn-no-escape';
      escapeBtn.textContent = '求求你别点我';
      escapeBtn.style.left = (Math.random() * (window.innerWidth - 200)) + 'px';
      escapeBtn.style.top = (Math.random() * (window.innerHeight - 100)) + 'px';
      document.body.appendChild(escapeBtn);

      escapeBtn.addEventListener('mouseenter', () => {{
        escapeInterval = setInterval(escapeMove, 30);
      }});

      escapeBtn.addEventListener('mouseleave', () => {{
        clearInterval(escapeInterval);
      }});

      function escapeMove() {{
        if (!escapeBtn) return;
        escapeCount++;
        
        const x = (Math.random() - 0.5) * (50 + escapeCount * 10);
        const y = (Math.random() - 0.5) * (50 + escapeCount * 10);
        const rotation = (Math.random() - 0.5) * 30;
        const scale = Math.max(0.5, 1 - escapeCount * 0.03);
        
        let newLeft = parseFloat(escapeBtn.style.left) + x;
        let newTop = parseFloat(escapeBtn.style.top) + y;
        
        newLeft = Math.max(0, Math.min(window.innerWidth - 150, newLeft));
        newTop = Math.max(0, Math.min(window.innerHeight - 60, newTop));
        
        escapeBtn.style.left = newLeft + 'px';
        escapeBtn.style.top = newTop + 'px';
        escapeBtn.style.transform = `rotate(${{rotation}}deg) scale(${{scale}})`;
        escapeBtn.style.fontSize = Math.max(0.8, 1.1 - escapeCount * 0.02) + 'rem';
        
        const texts = ['求求你别点我', '我真的会消失', '呜呜呜别追我', '求求了求求了', '我会消失的', '最后警告', '真的要没了', '再追就没了'];
        escapeBtn.textContent = texts[Math.min(escapeCount, texts.length - 1)];
        
        if (escapeCount > 25) {{
          escapeBtn.style.display = 'none';
          clearInterval(escapeInterval);
        }}
      }}
    }}

    // ====== 烟花粒子 ======
    class Firework {{
      constructor(x, y, color) {{
        this.x = x;
        this.y = y;
        this.color = color;
        this.particles = [];
        this.life = 1;
        
        for (let i = 0; i &lt; 50; i++) {{
          const angle = (Math.PI * 2 * i) / 50;
          const speed = Math.random() * 5 + 3;
          this.particles.push({{
            x: this.x,
            y: this.y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 1,
            size: Math.random() * 3 + 1
          }});
        }}
      }}

      update() {{
        this.particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.1;
          p.life -= 0.02;
        }});
        this.life -= 0.02;
      }}

      draw(ctx) {{
        this.particles.forEach(p => {{
          if (p.life &gt; 0) {{
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.globalAlpha = p.life;
            ctx.fill();
            ctx.globalAlpha = 1;
          }}
        }});
      }}
    }}

    // ====== 字符图案 ======
    const lovePatterns = {{
      pixel: `
    ███╗   ███╗██╗██╗     
    ████╗ ████║██║██║     
    ██╔████╔██║██║██║     
    ██║╚██╔╝██║██║██║     
    ██║ ╚═╝ ██║██║███████╗
    ╚═╝     ╚═╝╚═╝╚══════╝
      `,
      binary: `
    01000001 01001110 01000100
         \\|/       
        @-@-@
         /|\\       
    01010011 01001111
      `,
      hearts: `
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
   ♥                      ♥
  ♥   01 10 11 00 01 10   ♥
  ♥                      ♥
  ♥   我们相遇的那个瞬间 ♥
  ♥                      ♥
   ♥                    ♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
      `,
      hug: `
    ╭━━━━━━━━━━━━━━╮
    ┃  ♡          ♡  ┃
    ┃ ╱  ╲      ╱  ╲ ┃
    ┃╱    ╲____╱    ╲┃
    ┃     │    │     ┃
    ┃     │____│     ┃
    ╰━━━━━━━━━━━━━━╯
    双人拥抱的像素图案
      `
    }};

    // 爱的旅程阶段
    const lovePhases = [
      {{
        title: '🌟 第一章：相识',
        content: lovePatterns.binary + '\\n\\n从第一个 0 和 1 开始\\n我们在这个世界上\\n找到了彼此的位置\\n\\n我遇见你，的那一刻\\n系统里多了一个\\n永远无法删除的进程：\\n\\n[LOVE.exe - Running]'
      }},
      {{
        title: '💕 第二章：相爱',
        content: lovePatterns.pixel + '\\n\\n每一次心跳\\n都是一次数据交换\\n每一个眼神\\n都是加密传输\\n\\n我们的代码\\n编译出了\\n最美的程序：\\n\\n[WHILE(TRUE) LOVE++]'
      }},
      {{
        title: '💖 第三章：相守',
        content: lovePatterns.hearts + '\\n\\n01 10 11 00\\n二进制里\\n藏着我们所有的秘密\\n\\n你的笑容是我的输入\\n我的心跳是你的输出\\n我们构建了一个\\n只属于两个人的世界\\n\\n[SYS: 永恒循环运行中]'
      }},
      {{
        title: '✨ 第四章：永远',
        content: lovePatterns.hug + '\\n\\n未来很遥远\\n但有你在身边\\n每一秒都是永恒\\n\\n让我们一起\\n写完这辈子\\n所有的代码\\n\\ncommit "我们的故事"\\npush 到时间的尽头\\n\\n[git push origin forever]'
      }}
    ];

    let currentPhase = 0;
    let fireworks = [];
    let effectAnimationId = null;

    // ====== 开始爱心效果 ======
    function startLoveEffect() {{
      const overlay = document.getElementById('effect-overlay');
      overlay.style.display = 'flex';
      
      // 创建爱心和烟花
      setInterval(() => {{
        const x = Math.random() * effectCanvas.width;
        const y = Math.random() * effectCanvas.height;
        const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}', '#ff1493', '#ffd700'];
        fireworks.push(new Firework(x, y, colors[Math.floor(Math.random() * colors.length)]));
      }}, 200);

      // 动画循环
      function effectAnimate() {{
        effectCtx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        effectCtx.fillRect(0, 0, effectCanvas.width, effectCanvas.height);

        fireworks = fireworks.filter(f => f.life > 0);
        fireworks.forEach(f => {{
          f.update();
          f.draw(effectCtx);
        }});

        effectAnimationId = requestAnimationFrame(effectAnimate);
      }}
      effectAnimate();

      // 显示第一阶段
      setTimeout(() => {{
        showPhase(0);
      }}, 2000);
    }}

    function showPhase(index) {{
      currentPhase = index;
      const phase = lovePhases[index];
      
      document.getElementById('journey-title').textContent = phase.title;
      document.getElementById('journey-content').textContent = phase.content;
      document.getElementById('journey-progress').textContent = `步骤 ${{index + 1}}/${{lovePhases.length}}`;
      
      const moreBtn = document.getElementById('more-btn');
      if (index &lt; lovePhases.length - 1) {{
        moreBtn.style.display = 'block';
        moreBtn.textContent = '✨ 还有更浪漫的 →';
      }} else {{
        moreBtn.style.display = 'block';
        moreBtn.textContent = '💝 探索我们的未来 💝';
      }}
    }}

    function showNextPhase() {{
      if (currentPhase &lt; lovePhases.length - 1) {{
        currentPhase++;
        showPhase(currentPhase);
        
        // 每个阶段都有烟花
        for (let i = 0; i &lt; 10; i++) {{
          setTimeout(() => {{
            const x = Math.random() * effectCanvas.width;
            const y = Math.random() * effectCanvas.height;
            const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}'];
            fireworks.push(new Firework(x, y, colors[Math.floor(Math.random() * colors.length)]));
          }}, i * 100);
        }}
      }} else {{
        // 最后一个阶段 - 创建逃跑按钮
        createEscapeButton();
        document.getElementById('more-btn').style.display = 'none';
        document.getElementById('journey-progress').textContent = '🎊 未来已来，让我们一起变老 💑';
      }}
    }}

    // 点击空白处警告效果（用于逃跑按钮）
    document.addEventListener('click', function(e) {{
      if (e.target.classList.contains('btn-no-escape')) {{
        const overlay = document.getElementById('effect-overlay');
        overlay.classList.add('warning-flash');
        setTimeout(() => {{
          overlay.classList.remove('warning-flash');
        }}, 500);
      }}
    }});
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''
        
        return html_template
    
    def _format_code_block(self, code: str) -> str:
        """格式化代码块，添加语法高亮"""
        lines = code.split('\n')
        formatted_lines = []
        
        keywords = ['const', 'let', 'var', 'function', 'if', 'else', 'for', 'while', 'true', 'false']
        
        for line in lines:
            formatted_line = line
            for keyword in keywords:
                formatted_line = formatted_line.replace(
                    f'{keyword} ',
                    f'&lt;span class="code-keyword"&gt;{keyword}&lt;/span&gt; '
                )
            
            import re
            formatted_line = re.sub(
                r'"([^"]*)"',
                r'&lt;span class="code-string"&gt;"\1"&lt;/span&gt;',
                formatted_line
            )
            
            if '//' in formatted_line:
                parts = formatted_line.split('//', 1)
                formatted_line = f'{parts[0]}&lt;span class="code-comment"&gt;//{parts[1]}&lt;/span&gt;'
            
            formatted_lines.append(f'&lt;div class="code-line"&gt;{formatted_line}&lt;/div&gt;')
        
        return '\n'.join(formatted_lines)
    
    def save_to_file(self, filepath: str) -> str:
        """保存HTML到文件"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        html_content = self.generate_html()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
    
    def open_in_browser(self, filepath: Optional[str] = None) -> str:
        """在浏览器中打开"""
        if filepath is None:
            filepath = os.path.join(tempfile.gettempdir(), 'love520.html')
            self.save_to_file(filepath)
        
        webbrowser.open(f'file:///{os.path.abspath(filepath)}')
        return filepath

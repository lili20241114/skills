"""
520表白技能 - HTML生成器模块 - 超级炫酷版 v2.0
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
      justify-content: flex-start;
      padding: 20px;
      padding-top: 5vh;
      overflow-y: auto;
    }}

    .title {{
      font-size: clamp(2rem, 6vw, 5rem);
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color}, {self.config.secondary_color}, {self.config.primary_color});
      background-size: 300% 300%;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: titlePulse 2s ease-in-out infinite, gradientText 5s ease infinite;
      text-align: center;
      font-weight: bold;
      max-width: 95vw;
      word-wrap: break-word;
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
      font-size: clamp(1rem, 3vw, 1.8rem);
      background: linear-gradient(90deg, {self.config.accent_color}, #fff, {self.config.accent_color});
      background-size: 200% 200%;
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 40px;
      animation: fadeInUp 1s ease-out 0.5s both, gradientSubtitle 3s ease infinite;
      max-width: 95vw;
      text-align: center;
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
      margin: clamp(20px, 4vw, 60px) 0;
    }}

    .big-heart {{
      font-size: clamp(4rem, 12vw, 10rem);
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
      padding: clamp(20px, 4vw, 45px);
      width: clamp(300px, 90vw, 700px);
      max-width: 95vw;
      text-align: center;
      animation: fadeInUp 1s ease-out 1s both, boxGlow 3s ease-in-out infinite;
      box-shadow: 0 0 40px {self.config.primary_color}40;
      overflow: hidden;
    }}

    @keyframes boxGlow {{
      0%, 100% {{ box-shadow: 0 0 40px {self.config.primary_color}40; }}
      50% {{ box-shadow: 0 0 60px {self.config.primary_color}60; }}
    }}

    .love-message {{
      font-size: clamp(1rem, 2.5vw, 1.8rem);
      line-height: clamp(1.5, 2.5vw, 2.5);
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
      font-size: clamp(1.2rem, 3vw, 2.2rem);
      animation: gradientHighlight 2s ease infinite;
    }}

    @keyframes gradientHighlight {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}

    .buttons {{
      display: flex;
      gap: clamp(15px, 4vw, 40px);
      margin-top: clamp(20px, 4vw, 50px);
      animation: fadeInUp 1s ease-out 1.5s both;
      flex-wrap: wrap;
      justify-content: center;
    }}

    .btn {{
      padding: clamp(12px, 2vw, 22px) clamp(30px, 5vw, 60px);
      font-size: clamp(1rem, 2.5vw, 1.5rem);
      border: none;
      border-radius: 50px;
      cursor: pointer;
      transition: all 0.3s ease;
      font-weight: bold;
      position: relative;
      overflow: hidden;
      white-space: nowrap;
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
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: white;
      box-shadow: 0 5px 20px rgba(118, 75, 162, 0.5);
      white-space: nowrap;
      position: relative;
      transition: all 0.05s ease;
    }}

    .btn-no.flying {{
      pointer-events: none;
      animation: flyAway 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    }}

    @keyframes flyAway {{
      0% {{ opacity: 1; transform: scale(1) rotate(0deg); filter: blur(0px); }}
      30% {{ opacity: 1; transform: scale(1.2) rotate(-10deg); filter: blur(0px); }}
      60% {{ opacity: 0.8; transform: scale(0.8) rotate(15deg) translateX(300px) translateY(-200px); filter: blur(2px); }}
      100% {{ opacity: 0; transform: scale(0.1) rotate(360deg) translateX(800px) translateY(-600px); filter: blur(10px); }}
    }}

    .btn-no.pop {{
      pointer-events: none;
      animation: popBubble 0.8s ease-out forwards;
    }}

    @keyframes popBubble {{
      0% {{ transform: scale(1); opacity: 1; filter: blur(0px); }}
      20% {{ transform: scale(1.5); opacity: 0.9; filter: blur(0px); }}
      100% {{ transform: scale(0); opacity: 0; filter: blur(20px); }}
    }}

    .shooting-star {{
      position: fixed;
      width: 4px;
      height: 4px;
      background: linear-gradient(45deg, #ffd700, #ff6b9d);
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      animation: shootingStar 1s linear forwards;
      box-shadow: 0 0 10px #ffd700, 0 0 20px #ff6b9d, 0 0 30px #ffd700;
    }}

    @keyframes shootingStar {{
      0% {{ opacity: 1; transform: translate(0, 0) scale(1); }}
      100% {{ opacity: 0; transform: translate(800px, -600px) scale(0); }}
    }}

    .bubble-particle {{
      position: fixed;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      animation: bubbleFloat 1.5s ease-out forwards;
    }}

    @keyframes bubbleFloat {{
      0% {{ opacity: 1; transform: scale(1) translate(0, 0); }}
      100% {{ opacity: 0; transform: scale(0) translate(var(--tx), var(--ty)); }}
    }}

    .btn-no-hint {{
      position: fixed;
      font-size: 1rem;
      color: #ffd700;
      pointer-events: none;
      z-index: 9998;
      animation: hintFloat 2s ease-out forwards;
      text-shadow: 0 0 10px #ffd700, 0 0 20px #ff6b9d;
    }}

    @keyframes hintFloat {{
      0% {{ opacity: 0; transform: translateY(0) scale(0.5); }}
      20% {{ opacity: 1; transform: translateY(-10px) scale(1); }}
      80% {{ opacity: 1; }}
      100% {{ opacity: 0; transform: translateY(-100px) scale(0.5); }}
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

    /* ====== 效果页面样式 ====== */
    .effect-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.98);
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
      animation: journeyFadeIn 1s ease-out;
    }}

    @keyframes journeyFadeIn {{
      from {{ opacity: 0; transform: translateY(50px) scale(0.9); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    .journey-title {{
      font-size: clamp(1.8rem, 5vw, 3.5rem);
      margin-bottom: clamp(15px, 3vw, 40px);
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color});
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: titlePulse 2s ease-in-out infinite, gradientText 3s ease infinite;
      max-width: 95vw;
      text-align: center;
      word-wrap: break-word;
    }}

    .journey-content {{
      font-size: clamp(0.8rem, 2vw, 1.5rem);
      font-family: 'Courier New', monospace;
      line-height: clamp(1.4, 2vw, 2);
      white-space: pre;
      color: {self.config.accent_color};
      animation: matrixGlow 2s ease infinite, contentTyping 0.05s steps(40) both;
      overflow: hidden;
      max-height: 0;
      max-width: 95vw;
      overflow-x: auto;
    }}

    .journey-content.show {{
      max-height: none;
      overflow-y: auto;
    }}

    @keyframes contentTyping {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    @keyframes matrixGlow {{
      0%, 100% {{ text-shadow: 0 0 10px {self.config.primary_color}; }}
      50% {{ text-shadow: 0 0 30px {self.config.accent_color}, 0 0 50px {self.config.secondary_color}; }}
    }}

    .journey-progress {{
      margin-top: 40px;
      font-size: 1.2rem;
      color: #888;
    }}

    .progress-bar {{
      width: 300px;
      height: 8px;
      background: rgba(255,255,255,0.1);
      border-radius: 4px;
      margin: 20px auto;
      overflow: hidden;
    }}

    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, {self.config.primary_color}, {self.config.accent_color}, {self.config.secondary_color});
      border-radius: 4px;
      width: 0%;
      transition: width 1s ease-out;
    }}

    .journey-hint {{
      margin-top: 20px;
      font-size: 1rem;
      color: #666;
      animation: pulseHint 2s ease-in-out infinite;
    }}

    @keyframes pulseHint {{
      0%, 100% {{ opacity: 0.5; }}
      50% {{ opacity: 1; }}
    }}

    .final-message {{
      margin-top: 40px;
      font-size: 2rem;
      color: {self.config.primary_color};
      animation: finalPulse 1s ease-in-out infinite;
    }}

    @keyframes finalPulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
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
      .content {{
        padding: 10px;
      }}
      .love-journey {{
        padding: 10px;
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
        &lt;span class="normal"&gt;{love_message_html.replace(self.config.highlight_text, f'&lt;/span&gt;&lt;span class="highlight"&gt;{self.config.highlight_text}&lt;/span&gt;&lt;span class="normal"&gt;')}&lt;/span&gt;
      &lt;/p&gt;
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
      &lt;div class="journey-content show" id="journey-content"&gt;正在加载爱的旅程...&lt;/div&gt;
      &lt;div class="journey-progress" id="journey-progress"&gt;步骤 1/4&lt;/div&gt;
      &lt;div class="progress-bar"&gt;
        &lt;div class="progress-fill" id="progress-fill"&gt;&lt;/div&gt;
      &lt;/div&gt;
      &lt;div class="journey-hint" id="journey-hint"&gt;✨ 接下来会自动播放，请不要走开哦~&lt;/div&gt;
      &lt;div class="final-message" id="final-message" style="display: none;"&gt;💝 我们的故事才刚刚开始...&lt;/div&gt;
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

    // ====== 爱心逃跑按钮 - 流星飞走效果 ======
    const noTexts = [
      '{self.config.no_button_text}',
      '🌠 再想想嘛~',
      '💫 别追我呀',
      '✨ 人家要飞走啦',
      '🌙 飞向月亮去',
      '⭐ 变成星星了',
      '🌈 彩虹来接我了',
      '🎆 烟花带走了我',
      '💭 你追不上我的',
      '🚀 火箭发射！',
      '🛸 UFO带我走',
      '🌸 花瓣雨带我去远方',
      '💖 变成爱心飞走啦',
      '🎈 气球带我飘走',
      '🌺 飞向花丛中',
      '💝 化作流星消失~',
      '🎠 转着圈圈飞走~',
      '🌊 随波逐流飘走',
      '🍃 乘着风飞走',
      '🌤️ 追着云彩去',
      '🎭 变身术！看不见我~'
    ];

    let btnNo = document.getElementById('btn-no');
    let isFlying = false;
    let clickCount = 0;

    function createShootingStars(x, y) {{
      for (let i = 0; i < 15; i++) {{
        setTimeout(() => {{
          const star = document.createElement('div');
          star.className = 'shooting-star';
          star.style.left = (x + Math.random() * 100 - 50) + 'px';
          star.style.top = (y + Math.random() * 100 - 50) + 'px';
          document.body.appendChild(star);
          setTimeout(() => star.remove(), 1000);
        }}, i * 30);
      }}
    }}

    function createBubbleParticles(x, y) {{
      const colors = ['#ff6b9d', '#ffd700', '#ff1493', '#ff69b4', '#764ba2'];
      for (let i = 0; i < 12; i++) {{
        const particle = document.createElement('div');
        particle.className = 'bubble-particle';
        particle.style.left = x + 'px';
        particle.style.top = y + 'px';
        particle.style.background = colors[Math.floor(Math.random() * colors.length)];
        particle.style.setProperty('--tx', (Math.random() * 200 - 100) + 'px');
        particle.style.setProperty('--ty', (Math.random() * 200 - 100) + 'px');
        particle.style.opacity = Math.random() * 0.8 + 0.2;
        document.body.appendChild(particle);
        setTimeout(() => particle.remove(), 1500);
      }}
    }}

    function showHint(x, y, text) {{
      const hint = document.createElement('div');
      hint.className = 'btn-no-hint';
      hint.textContent = text;
      hint.style.left = (x + 20) + 'px';
      hint.style.top = (y - 30) + 'px';
      document.body.appendChild(hint);
      setTimeout(() => hint.remove(), 2000);
    }}

    function escapeButton(e) {{
      if (isFlying) return;
      
      isFlying = true;
      clickCount++;
      const textIndex = Math.min(clickCount, noTexts.length - 1);
      const randomText = noTexts[textIndex];
      
      btnNo.textContent = randomText;
      
      const rect = btnNo.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;
      
      const effectType = Math.floor(Math.random() * 3);
      
      if (effectType === 0) {{
        btnNo.classList.add('flying');
        createShootingStars(x, y);
        
        setTimeout(() => {{
          btnNo.style.display = 'none';
          isFlying = false;
        }}, 1500);
        
      }} else if (effectType === 1) {{
        btnNo.classList.add('pop');
        createBubbleParticles(x, y);
        
        setTimeout(() => {{
          btnNo.style.display = 'none';
          isFlying = false;
        }}, 800);
        
      }} else {{
        btnNo.classList.add('flying');
        createShootingStars(x, y);
        
        setTimeout(() => {{
          btnNo.classList.remove('flying');
          btnNo.classList.add('pop');
          createBubbleParticles(x, y);
        }}, 900);
        
        setTimeout(() => {{
          btnNo.style.display = 'none';
          isFlying = false;
        }}, 1700);
      }}
      
      setTimeout(() => {{
        showHint(x, y, randomText);
      }}, 200);
    }}

    btnNo.addEventListener('mouseenter', () => {{
      if (!isFlying && btnNo.style.display !== 'none') {{
        escapeButton();
      }}
    }});

    document.addEventListener('mousemove', function(e) {{
      if (isFlying || btnNo.style.display === 'none') return;
      
      const rect = btnNo.getBoundingClientRect();
      const dx = e.clientX - (rect.left + rect.width / 2);
      const dy = e.clientY - (rect.top + rect.height / 2);
      const dist = Math.sqrt(dx * dx + dy * dy);
      
      if (dist < 100) {{
        escapeButton();
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
        
        if (escapeCount &gt; 25) {{
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
        
        for (let i = 0; i &lt; 80; i++) {{
          const angle = (Math.PI * 2 * i) / 80;
          const speed = Math.random() * 8 + 4;
          this.particles.push({{
            x: this.x,
            y: this.y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 1,
            size: Math.random() * 4 + 2
          }});
        }}
      }}

      update() {{
        this.particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.08;
          p.life -= 0.015;
        }});
        this.life -= 0.015;
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
    let fireworkInterval = null;

    // ====== 开始爱心效果 ======
    function startLoveEffect() {{
      const overlay = document.getElementById('effect-overlay');
      overlay.style.display = 'flex';
      
      // 创建烟花
      fireworkInterval = setInterval(() => {{
        const x = Math.random() * effectCanvas.width;
        const y = Math.random() * (effectCanvas.height * 0.6);
        const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}', '#ff1493', '#ffd700'];
        fireworks.push(new Firework(x, y, colors[Math.floor(Math.random() * colors.length)]));
      }}, 400);

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

      // 开始自动播放旅程
      currentPhase = 0;
      showPhase(0);
      
      setTimeout(() => autoPlayJourney(), 3000);
    }}

    function showPhase(index) {{
      currentPhase = index;
      const phase = lovePhases[index];
      const journeyContent = document.getElementById('journey-content');
      
      // 隐藏内容准备更新
      journeyContent.classList.remove('show');
      
      setTimeout(() => {{
        document.getElementById('journey-title').textContent = phase.title;
        journeyContent.textContent = phase.content;
        journeyContent.classList.add('show');
        document.getElementById('journey-progress').textContent = `步骤 ${{index + 1}}/${{lovePhases.length}}`;
        
        // 更新进度条
        const progressPercent = ((index + 1) / lovePhases.length) * 100;
        document.getElementById('progress-fill').style.width = progressPercent + '%';
      }}, 100);
    }}

    function autoPlayJourney() {{
      if (currentPhase &lt; lovePhases.length - 1) {{
        currentPhase++;
        showPhase(currentPhase);
        
        // 每个阶段都有烟花
        for (let i = 0; i &lt; 15; i++) {{
          setTimeout(() => {{
            const x = Math.random() * effectCanvas.width;
            const y = Math.random() * (effectCanvas.height * 0.6);
            const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}'];
            fireworks.push(new Firework(x, y, colors[Math.floor(Math.random() * colors.length)]));
          }}, i * 200);
        }}
        
        // 4秒后播放下一阶段
        setTimeout(autoPlayJourney, 5000);
      }} else {{
        // 最后一个阶段 - 显示最终消息
        document.getElementById('journey-hint').style.display = 'none';
        document.getElementById('journey-progress').style.display = 'none';
        document.getElementById('final-message').style.display = 'block';
        
        // 继续放更多烟花
        clearInterval(fireworkInterval);
        fireworkInterval = setInterval(() => {{
          const x = Math.random() * effectCanvas.width;
          const y = Math.random() * (effectCanvas.height * 0.5);
          const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}', '#ff69b4', '#ff1493', '#ffd700'];
          fireworks.push(new Firework(x, y, colors[Math.floor(Math.random() * colors.length)]));
        }}, 300);
        
        setTimeout(createEscapeButton, 2000);
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

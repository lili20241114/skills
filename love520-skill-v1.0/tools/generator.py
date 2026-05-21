"""
520表白技能 - HTML生成器模块 - 超级炫酷版 v3.0
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
        love_message_html = self.config.love_message.replace('\n', '<br>')
        
        html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{self.config.title}</title>
  <style>
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
      margin-top: clamp(30px, 6vw, 60px);
      display: flex;
      flex-wrap: wrap;
      gap: clamp(15px, 3vw, 30px);
      justify-content: center;
      z-index: 100;
    }}

    .btn {{
      padding: clamp(12px, 2vw, 18px) clamp(30px, 5vw, 60px);
      font-size: clamp(1rem, 2.5vw, 1.6rem);
      border: none;
      border-radius: 50px;
      cursor: pointer;
      font-weight: bold;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      z-index: 10;
    }}

    .btn-yes {{
      background: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color});
      color: white;
      box-shadow: 0 10px 30px rgba(255,107,157,0.4);
      animation: btnPulse 2s ease-in-out infinite;
    }}

    @keyframes btnPulse {{
      0%, 100% {{ transform: scale(1); box-shadow: 0 10px 30px rgba(255,107,157,0.4); }}
      50% {{ transform: scale(1.05); box-shadow: 0 15px 40px rgba(255,107,157,0.6); }}
    }}

    .btn-yes:hover {{
      transform: scale(1.1);
      box-shadow: 0 20px 50px rgba(255,107,157,0.6);
    }}

    .btn-no {{
      background: linear-gradient(135deg, #666, #888);
      color: white;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      transition: all 0.1s ease;
    }}

    .btn-no:hover {{
      background: linear-gradient(135deg, #777, #999);
    }}

    .floating-hearts {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 2;
    }}

    .floating-heart {{
      position: absolute;
      font-size: clamp(20px, 3vw, 40px);
      animation: floatUp 6s ease-in-out infinite;
      opacity: 0.7;
    }}

    @keyframes floatUp {{
      0% {{
        transform: translateY(100vh) rotate(0deg) scale(0);
        opacity: 0;
      }}
      10% {{ opacity: 0.7; }}
      90% {{ opacity: 0.7; }}
      100% {{
        transform: translateY(-20vh) rotate(720deg) scale(1.2);
        opacity: 0;
      }}
    }}

    .effect-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.85);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }}

    .canvas-effect {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }}

    .love-journey {{
      position: relative;
      z-index: 2;
      text-align: center;
      color: {self.config.primary_color};
      animation: journeyFadeIn 1s ease-out;
      padding: 20px;
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
      animation: matrixGlow 2s ease infinite;
      overflow: hidden;
      max-height: none;
      max-width: 95vw;
      overflow-x: auto;
    }}

    .journey-content.show {{
      max-height: none;
      overflow-y: auto;
    }}

    @keyframes matrixGlow {{
      0%, 100% {{ text-shadow: 0 0 10px {self.config.primary_color}; }}
      50% {{ text-shadow: 0 0 30px {self.config.accent_color}, 0 0 50px {self.config.secondary_color}; }}
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
  </style>
</head>
<body>
  <div id="canvas-container">
    <canvas id="main-canvas"></canvas>
  </div>

  <div class="floating-hearts" id="floating-hearts"></div>

  <div class="content">
    <h1 class="title">{self.config.title}</h1>
    <p class="subtitle">{self.config.subtitle}</p>
    
    <div class="love-container">
      <div class="big-heart">❤️</div>
    </div>

    <div class="message-box">
      <p class="love-message">
        <span class="normal">{love_message_html.replace(self.config.highlight_text, f'</span><span class="highlight">{self.config.highlight_text}</span><span class="normal">')}</span>
      </p>
    </div>

    <div class="buttons">
      <button class="btn btn-yes" onclick="startLoveEffect()">{self.config.yes_button_text}</button>
      <button class="btn btn-no" id="btn-no">{self.config.no_button_text}</button>
    </div>
  </div>

  <div class="effect-overlay" id="effect-overlay">
    <canvas class="canvas-effect" id="effect-canvas"></canvas>
    <div class="love-journey" id="love-journey">
      <div class="journey-title" id="journey-title">🎉 恭喜你做出了选择！</div>
      <div class="journey-content show" id="journey-content">正在加载爱的旅程...</div>
      <div class="journey-hint" id="journey-hint">✨ 接下来会自动播放，请不要走开哦~</div>
      <div class="final-message" id="final-message" style="display: none;">💝 我们的故事才刚刚开始...</div>
    </div>
  </div>

  <script>
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

    const particles = [];
    const particleCount = 100;

    for (let i = 0; i < particleCount; i++) {{
      particles.push({{
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        speedX: (Math.random() - 0.5) * 1.5,
        speedY: (Math.random() - 0.5) * 1.5,
        size: Math.random() * 3 + 1,
        opacity: Math.random() * 0.6 + 0.3,
        color: getRandomColor(),
        pulse: Math.random() * Math.PI * 2
      }});
    }}

    function getRandomColor() {{
      const colors = ['{self.config.primary_color}', '{self.config.secondary_color}', '{self.config.accent_color}', '#ff69b4', '#ff1493', '#ffd700'];
      return colors[Math.floor(Math.random() * colors.length)];
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

      particles.forEach(p => {{
        p.x += p.speedX;
        p.y += p.speedY;
        p.pulse += 0.05;

        if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
        if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;

        const pulseSize = p.size * (1 + Math.sin(p.pulse) * 0.3);
        ctx.beginPath();
        ctx.arc(p.x, p.y, pulseSize, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = p.opacity * (0.7 + Math.sin(p.pulse) * 0.3);
        ctx.fill();
        ctx.globalAlpha = 1;
      }});

      heartPhase += 0.025;
      const heartSize = 160 + Math.sin(heartPhase) * 25;
      drawHeart(canvas.width / 2, canvas.height / 2, heartSize, '#ff1493', 0.35);
      drawHeart(canvas.width / 2, canvas.height / 2, heartSize * 0.7, '#ff6b9d', 0.2);

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

    setInterval(createFloatingHeart, 500);

    const btnNo = document.getElementById('btn-no');
    let isFlying = false;

    const funnyMessages = [
      '🌠 再想想嘛~', '💫 别追我呀', '✨ 人家要飞走啦',
      '🌙 飞向月亮去', '⭐ 变成星星了', '🌈 彩虹来接我了',
      '🎆 烟花带走了我', '💭 你追不上我的', '🚀 火箭发射！',
      '🛸 UFO带我走', '🌸 花瓣雨带我去远方', '💝 变成爱心飞走啦',
      '🎈 气球带我飘走', '🌺 飞向花丛中', '🎪 变身术！看不见我~'
    ];

    function escapeButton() {{
      if (isFlying) return;
      isFlying = true;

      const effect = Math.floor(Math.random() * 3);
      
      if (effect === 0 || effect === 2) {{
        meteorEscape();
      }} else {{
        bubbleEscape();
      }}
    }}

    function meteorEscape() {{
      const startX = btnNo.getBoundingClientRect().left + btnNo.offsetWidth / 2;
      const startY = btnNo.getBoundingClientRect().top + btnNo.offsetHeight / 2;
      
      createMeteorEffect(startX, startY);
      
      const msg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
      btnNo.textContent = msg;
      
      const endX = window.innerWidth + 200;
      const endY = -200;
      const duration = 800;
      const startTime = Date.now();
      
      function animateMeteor() {{
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        
        const x = startX + (endX - startX) * easeProgress;
        const y = startY + (endY - startY) * easeProgress;
        const scale = 1 - progress * 0.7;
        const rotation = progress * 720;
        
        btnNo.style.position = 'fixed';
        btnNo.style.left = (x - btnNo.offsetWidth / 2) + 'px';
        btnNo.style.top = (y - btnNo.offsetHeight / 2) + 'px';
        btnNo.style.transform = `rotate(${{rotation}}deg) scale(${{scale}})`;
        btnNo.style.opacity = 1 - progress;
        
        if (progress < 1) {{
          requestAnimationFrame(animateMeteor);
        }} else {{
          btnNo.style.display = 'none';
          isFlying = false;
          setTimeout(resetButton, 2000);
        }}
      }}
      animateMeteor();
    }}

    function createMeteorEffect(x, y) {{
      for (let i = 0; i < 15; i++) {{
        setTimeout(() => {{
          const star = document.createElement('div');
          star.style.cssText = `
            position: fixed;
            left: ${{x + (Math.random() - 0.5) * 100}}px;
            top: ${{y + (Math.random() - 0.5) * 100}}px;
            font-size: ${{Math.random() * 15 + 10}}px;
            pointer-events: none;
            z-index: 999;
            animation: starFloat 1.5s ease-out forwards;
          `;
          star.innerHTML = ['✨', '⭐', '💫', '🌟'][Math.floor(Math.random() * 4)];
          document.body.appendChild(star);
          setTimeout(() => star.remove(), 1500);
        }}, i * 50);
      }}
    }}

    function bubbleEscape() {{
      const startX = btnNo.getBoundingClientRect().left + btnNo.offsetWidth / 2;
      const startY = btnNo.getBoundingClientRect().top + btnNo.offsetHeight / 2;
      
      createBubbleEffect(startX, startY);
      
      const msg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
      btnNo.textContent = msg;
      
      const endX = startX + (Math.random() - 0.5) * 400;
      const endY = -300;
      const duration = 1200;
      const startTime = Date.now();
      
      function animateBubble() {{
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const wobble = Math.sin(progress * Math.PI * 4) * 50;
        
        const x = startX + (endX - startX) * progress + wobble;
        const y = startY + (endY - startY) * progress;
        const scale = 1 + progress * 0.5;
        
        btnNo.style.position = 'fixed';
        btnNo.style.left = (x - btnNo.offsetWidth / 2) + 'px';
        btnNo.style.top = (y - btnNo.offsetHeight / 2) + 'px';
        btnNo.style.transform = `scale(${{scale}})`;
        btnNo.style.opacity = 1 - progress;
        
        if (progress < 0.7) {{
          requestAnimationFrame(animateBubble);
        }} else {{
          bubblePop(startX, startY);
          setTimeout(resetButton, 2000);
        }}
      }}
      animateBubble();
    }}

    function createBubbleEffect(x, y) {{
      for (let i = 0; i < 12; i++) {{
        setTimeout(() => {{
          const bubble = document.createElement('div');
          const size = Math.random() * 20 + 10;
          bubble.style.cssText = `
            position: fixed;
            left: ${{x + (Math.random() - 0.5) * 80}}px;
            top: ${{y + (Math.random() - 0.5) * 80}}px;
            width: ${{size}}px;
            height: ${{size}}px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,255,255,0.8), rgba(255,107,157,0.3));
            pointer-events: none;
            z-index: 999;
            animation: bubbleRise 1.2s ease-out forwards;
          `;
          document.body.appendChild(bubble);
          setTimeout(() => bubble.remove(), 1200);
        }}, i * 40);
      }}
    }}

    function bubblePop(x, y) {{
      btnNo.style.display = 'none';
      isFlying = false;
      
      const pop = document.createElement('div');
      pop.innerHTML = '💥';
      pop.style.cssText = `
        position: fixed;
        left: ${{x}}px;
        top: ${{y}}px;
        font-size: 60px;
        pointer-events: none;
        z-index: 999;
        animation: popAnim 0.4s ease-out forwards;
      `;
      document.body.appendChild(pop);
      setTimeout(() => pop.remove(), 400);
      
      for (let i = 0; i < 10; i++) {{
        const particle = document.createElement('div');
        particle.innerHTML = ['✨', '💫', '⭐'][Math.floor(Math.random() * 3)];
        particle.style.cssText = `
          position: fixed;
          left: ${{x}}px;
          top: ${{y}}px;
          font-size: 20px;
          pointer-events: none;
          z-index: 999;
          animation: particleFly 0.8s ease-out ${{i * 0.05}}s forwards;
        `;
        document.body.appendChild(particle);
        setTimeout(() => particle.remove(), 800);
      }}
    }}

    function resetButton() {{
      btnNo.style.display = 'block';
      btnNo.style.position = '';
      btnNo.style.left = '';
      btnNo.style.top = '';
      btnNo.style.transform = '';
      btnNo.style.opacity = '1';
      btnNo.textContent = '{self.config.no_button_text}';
      isFlying = false;
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

    // ====== 第一章：相识 - 星星闪烁 + 流星雨 ======
    function initStarEffect() {{
      for (let i = 0; i < 100; i++) {{
        effectParticles.push({{
          x: Math.random() * effectCanvas.width,
          y: Math.random() * effectCanvas.height,
          size: Math.random() * 2 + 1,
          twinkle: Math.random() * Math.PI * 2,
          isMeteor: false
        }});
      }}
    }}
    function drawStarEffect() {{
      effectParticles.forEach((star, i) => {{
        if (star.isMeteor) {{
          star.x += star.vx;
          star.y += star.vy;
          star.life -= 0.02;
          if (star.life <= 0) effectParticles.splice(i, 1);
          
          effectCtx.beginPath();
          effectCtx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
          effectCtx.fillStyle = `rgba(255, 255, 255, ${{star.life}})`;
          effectCtx.fill();
          
          for (let t = 0; t < 5; t++) {{
            effectCtx.beginPath();
            effectCtx.arc(star.x - t * star.vx, star.y - t * star.vy, star.size * (1 - t * 0.2), 0, Math.PI * 2);
            effectCtx.fillStyle = `rgba(255, 215, 0, ${{star.life * (1 - t * 0.2)}})`;
            effectCtx.fill();
          }}
        }} else {{
          star.twinkle += 0.05;
          const brightness = 0.5 + Math.sin(star.twinkle) * 0.5;
          
          effectCtx.beginPath();
          effectCtx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
          effectCtx.fillStyle = `rgba(255, 255, 255, ${{brightness}})`;
          effectCtx.fill();
        }}
      }});
      
      if (Math.random() < 0.02) {{
        effectParticles.push({{
          x: Math.random() * effectCanvas.width,
          y: -20,
          vx: 4 + Math.random() * 3,
          vy: 4 + Math.random() * 3,
          size: 3 + Math.random() * 2,
          life: 1,
          isMeteor: true
        }});
      }}
    }}

    // ====== 第二章：相爱 - 心形粒子飘动 ======
    function initHeartEffect() {{
      for (let i = 0; i < 80; i++) {{
        effectParticles.push({{
          x: Math.random() * effectCanvas.width,
          y: Math.random() * effectCanvas.height,
          size: Math.random() * 4 + 2,
          speedX: (Math.random() - 0.5) * 2,
          speedY: (Math.random() - 0.5) * 1,
          phase: Math.random() * Math.PI * 2,
          color: ['#ff6b9d', '#ff1493', '#ff69b4', '#ffd700'][Math.floor(Math.random() * 4)]
        }});
      }}
    }}
    function drawHeartEffect() {{
      effectParticles.forEach(p => {{
        p.phase += 0.03;
        p.x += p.speedX + Math.sin(p.phase) * 0.5;
        p.y += p.speedY;
        
        if (p.x < 0) p.x = effectCanvas.width;
        if (p.x > effectCanvas.width) p.x = 0;
        if (p.y < 0) p.y = effectCanvas.height;
        if (p.y > effectCanvas.height) p.y = 0;
        
        const scale = 1 + Math.sin(p.phase * 2) * 0.2;
        effectCtx.beginPath();
        const heartX = p.x;
        const heartY = p.y;
        const s = p.size * scale;
        effectCtx.moveTo(heartX, heartY + s);
        effectCtx.bezierCurveTo(heartX - s, heartY, heartX - s, heartY - s, heartX, heartY - s);
        effectCtx.bezierCurveTo(heartX + s, heartY - s, heartX + s, heartY, heartX, heartY + s);
        effectCtx.fillStyle = p.color;
        effectCtx.globalAlpha = 0.7;
        effectCtx.fill();
        effectCtx.globalAlpha = 1;
      }});
    }}

    // ====== 第三章：相守 - 同心圆波纹 ======
    function initRippleEffect() {{
      for (let i = 0; i < 5; i++) {{
        setTimeout(() => {{
          effectRipples.push({{
            x: effectCanvas.width / 2 + (Math.random() - 0.5) * 200,
            y: effectCanvas.height / 2 + (Math.random() - 0.5) * 200,
            radius: 5,
            maxRadius: 200 + Math.random() * 150,
            life: 1,
            color: ['#ff6b9d', '#ffd700', '#ff1493', '#ff69b4'][i % 4]
          }});
        }}, i * 500);
      }}
    }}
    function drawRippleEffect() {{
      effectRipples = effectRipples.filter(r => r.life > 0);
      
      if (Math.random() < 0.015 && effectRipples.length < 8) {{
        effectRipples.push({{
          x: Math.random() * effectCanvas.width,
          y: Math.random() * effectCanvas.height,
          radius: 5,
          maxRadius: 180 + Math.random() * 150,
          life: 1,
          color: ['#ff6b9d', '#ffd700', '#ff1493', '#ff69b4'][Math.floor(Math.random() * 4)]
        }});
      }}
      
      effectRipples.forEach(r => {{
        r.radius += 1.5;
        r.life = 1 - r.radius / r.maxRadius;
        
        if (r.life > 0) {{
          for (let i = 0; i < 3; i++) {{
            effectCtx.beginPath();
            effectCtx.arc(r.x, r.y, r.radius + i * 20, 0, Math.PI * 2);
            effectCtx.strokeStyle = r.color;
            effectCtx.lineWidth = 2;
            effectCtx.globalAlpha = r.life * 0.6;
            effectCtx.stroke();
          }}
          effectCtx.globalAlpha = 1;
        }}
      }});
    }}

    // ====== 第四章：永远 - 二进制代码雨 ======
    function initCodeEffect() {{
      const columns = Math.floor(effectCanvas.width / 20);
      for (let i = 0; i < columns; i++) {{
        effectCodeChars.push({{
          x: i * 20,
          y: Math.random() * effectCanvas.height - effectCanvas.height,
          speed: 1 + Math.random() * 3,
          chars: '01',
          currentChar: ''
        }});
      }}
    }}
    function drawCodeEffect() {{
      effectCtx.fillStyle = 'rgba(0, 0, 0, 0.1)';
      effectCtx.fillRect(0, 0, effectCanvas.width, effectCanvas.height);
      
      effectCodeChars.forEach(col => {{
        col.y += col.speed;
        
        if (col.y > effectCanvas.height + 50) {{
          col.y = -50;
          col.speed = 1 + Math.random() * 3;
        }}
        
        col.currentChar = col.chars[Math.floor(Math.random() * col.chars.length)];
        
        const gradient = effectCtx.createLinearGradient(col.x, col.y - 200, col.x, col.y);
        gradient.addColorStop(0, 'rgba(255, 107, 157, 0)');
        gradient.addColorStop(0.5, 'rgba(255, 215, 0, 0.8)');
        gradient.addColorStop(1, 'rgba(255, 20, 147, 1)');
        
        effectCtx.font = '16px Courier New';
        effectCtx.fillStyle = gradient;
        effectCtx.fillText(col.currentChar, col.x, col.y);
        
        for (let i = 1; i < 10; i++) {{
          effectCtx.fillStyle = `rgba(255, 107, 157, ${{0.1 / i}})`;
          effectCtx.fillText(col.chars[Math.floor(Math.random() * col.chars.length)], col.x, col.y - i * 18);
        }}
      }});
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
         \\\\|/       
        @-@-@
         /|\\\\       
    01010011 01001111
      `,
      hearts: `
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
   ❤️                      ❤️
  ❤️   01 10 11 00 01 10   ❤️
  ❤️                      ❤️
  ❤️   我们相遇的那个瞬间 ❤️
  ❤️                      ❤️
   ❤️                    ❤️
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
      `,
      hug: `
    ╭━━━━━━━━━━━━━━╮
    ┃  ❤️          ❤️  ┃
    ┃ ╱  ╲      ╱  ╲ ┃
    ┃╱    ╲____╲    ╱┃
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
        content: lovePatterns.binary + '\\n\\n从第一个 0 和 1 开始\\n我们在这个世界上\\n找到了彼此的位置\\n\\n我遇见你的那一刻\\n系统里多了一个\\n永远无法删除的进程：\\n\\n[LOVE.exe - Running]'
      }},
      {{
        title: '💕 第二章：相爱',
        content: lovePatterns.pixel + '\\n\\n每一次心跳\\n都是一次数据交换\\n每一个眼神\\n都是加密传输\\n\\n我们的代码\\n编译出了\\n最美的程序：\\n\\n[WHILE(TRUE) LOVE++]'
      }},
      {{
        title: '💖 第三章：相守',
        content: lovePatterns.hearts + '\\n\\n01 10 11 00\\n二进制里\\n藏着我们所有的秘密\\n\\n你的笑容是我的输入\\n我的心跳是你的输出\\n我们构建了一个\\n只属于两个人的世界：\\n\\n[SYS: 永恒循环运行中]'
      }},
      {{
        title: '✨ 第四章：永远',
        content: lovePatterns.hug + '\\n\\n未来很遥远\\n但有你在身边\\n每一秒都是永恒\\n\\n让我们一起\\n写完这辈子\\n所有的代码\\n\\ncommit "我们的故事"\\npush 到时间的尽头\\n\\n[git push origin forever]'
      }}
    ];

    let currentPhase = 0;
    let effectAnimationId = null;
    let currentEffectType = 0;
    let effectParticles = [];
    let effectRipples = [];
    let effectCodeChars = [];

    // ====== 特效切换 ======
    function startPhaseEffect(index) {{
      currentEffectType = index;
      effectParticles = [];
      effectRipples = [];
      effectCodeChars = [];
      
      if (index === 0) initStarEffect();
      else if (index === 1) initHeartEffect();
      else if (index === 2) initRippleEffect();
      else if (index === 3) initCodeEffect();
    }}

    // ====== 开始爱心效果 ======
    function startLoveEffect() {{
      const overlay = document.getElementById('effect-overlay');
      overlay.style.display = 'flex';
      
      // 开始动画循环
      function effectAnimate() {{
        effectCtx.fillStyle = 'rgba(0, 0, 0, 0.15)';
        effectCtx.fillRect(0, 0, effectCanvas.width, effectCanvas.height);

        if (currentEffectType === 0) drawStarEffect();
        else if (currentEffectType === 1) drawHeartEffect();
        else if (currentEffectType === 2) drawRippleEffect();
        else if (currentEffectType === 3) drawCodeEffect();

        effectAnimationId = requestAnimationFrame(effectAnimate);
      }}
      effectAnimate();

      // ========== 第一部分：520快乐派对 ==========
      const journeyTitle = document.getElementById('journey-title');
      const journeyContent = document.getElementById('journey-content');
      journeyContent.classList.add('show');
      
      // 开始完整流程
      typeWriter(journeyTitle, '💖 520快乐！', () => {{
        typeWriter(journeyContent, '那我们一起愉快的度过我们的520吧！\\n\\n🎆 一起放烟花表演... 🥂 一起干杯... 🎬 一起看电影... 💖 拥抱着彼此...', () => {{
          setTimeout(() => {{
            typeWriter(journeyTitle, '✨ 惊喜预告', () => {{
              typeWriter(journeyContent, '你以为就这样？结束了？\\n\\n是不是还不够浪漫？\\n\\n那么，来点更有趣的？', () => {{
                setTimeout(() => {{
                  currentPhase = 0;
                  showPhase(currentPhase, () => {{
                    setTimeout(autoPlayJourney, 1500);
                  }});
                }}, 1000);
              }}, 60);
            }}, 100);
          }}, 2000);
        }}, 60);
      }}, 100);
    }}

    // 打字机效果函数 - 更慢的速度
    function typeWriter(element, text, callback, speed = 100) {{
      let index = 0;
      element.textContent = '';
      
      function type() {{
        if (index < text.length) {{
          element.textContent += text.charAt(index);
          index++;
          setTimeout(type, speed);
        }} else if (callback) {{
          callback();
        }}
      }}
      type();
    }}

    function showPhase(index, callback) {{
      currentPhase = index;
      const phase = lovePhases[index];
      const journeyTitle = document.getElementById('journey-title');
      const journeyContent = document.getElementById('journey-content');
      
      // 清除内容
      journeyTitle.textContent = '';
      journeyContent.textContent = '';
      
      // 切换特效
      startPhaseEffect(index);
      
      // 先打标题
      typeWriter(journeyTitle, phase.title, () => {{
        // 再打内容
        typeWriter(journeyContent, phase.content, callback, 60);
      }}, 100);
    }}

    function autoPlayJourney() {{
      if (currentPhase < lovePhases.length - 1) {{
        currentPhase++;
        showPhase(currentPhase, () => {{
          setTimeout(autoPlayJourney, 3000);
        }});
      }} else {{
        // 最后一个阶段 - 显示最终消息
        document.getElementById('journey-hint').style.display = 'none';
        document.getElementById('final-message').style.display = 'block';
        
        setTimeout(createEscapeButton, 2000);
      }}
    }}

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

    // 点击空白处警告效果
    document.addEventListener('click', function(e) {{
      if (e.target.classList.contains('btn-no-escape')) {{
        const overlay = document.getElementById('effect-overlay');
        overlay.classList.add('warning-flash');
        setTimeout(() => {{
          overlay.classList.remove('warning-flash');
        }}, 500);
      }}
    }});
  </script>
  <style>
    @keyframes starFloat {{
      0% {{ transform: translate(0, 0) scale(1); opacity: 1; }}
      100% {{ transform: translate(${{(Math.random() - 0.5) * 100}}px, -100px) scale(0); opacity: 0; }}
    }}
    @keyframes bubbleRise {{
      0% {{ transform: translate(0, 0) scale(1); opacity: 0.8; }}
      100% {{ transform: translate(0, -200px) scale(1.5); opacity: 0; }}
    }}
    @keyframes popAnim {{
      0% {{ transform: scale(0); opacity: 1; }}
      50% {{ transform: scale(1.5); opacity: 1; }}
      100% {{ transform: scale(0); opacity: 0; }}
    }}
    @keyframes particleFly {{
      0% {{ transform: translate(0, 0) scale(1); opacity: 1; }}
      100% {{ transform: translate(${{(Math.random() - 0.5) * 200}}px, -150px) scale(0); opacity: 0; }}
    }}
    @keyframes warning-flash {{
      0%, 100% {{ background: rgba(0,0,0,0.85); }}
      25%, 75% {{ background: rgba(255,0,0,0.3); }}
    }}
    .effect-overlay.warning-flash {{
      animation: warning-flash 0.5s ease-in-out 3;
    }}
  </style>
</body>
</html>'''
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
                    f'<span class="code-keyword">{keyword}</span> '
                )
            
            import re
            formatted_line = re.sub(
                r'"([^"]*)"',
                r'<span class="code-string">"\1"</span>',
                formatted_line
            )
            
            if '//' in formatted_line:
                parts = formatted_line.split('//', 1)
                formatted_line = f'{parts[0]}<span class="code-comment">//{parts[1]}</span>'
            
            formatted_lines.append(f'<div class="code-line">{formatted_line}</div>')
        
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


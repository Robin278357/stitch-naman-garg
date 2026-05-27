import os

posts_dir = 'daily_blogs_naman_garg/posts'
os.makedirs(posts_dir, exist_ok=True)

posts = [
  ('weekly-notes-12th-may-21st-may', 'Weekly Notes (12th May to 21st May)', 'May 21, 2026', 'https://namangarg.in/wp-content/uploads/2026/05/image-18-1024x576.png', '<h2>Health</h2><p>So, this is technically my third attempt to write this weekly note. My gut has been hurting. My head has been hurting.</p><blockquote>Even when my body stopped cooperating, my discipline did not completely disappear.</blockquote><p>My weight dropped to <strong>80.5 kg</strong>. Even though I stopped going to the gym for a few days, I still stayed disciplined with my diet.</p><h2>Work</h2><p>Work this week felt like friction everywhere. Not failure. Not disaster. Just friction. I am working on multiple projects simultaneously.</p><h2>Learning</h2><blockquote>It is the failure you are tasting, not the regret.</blockquote><p>Failure only exists because you tried. Regret is when you never even tried.</p><h2>Closing Thoughts</h2><p>Discipline is not tested when life is easy. Discipline is tested when your body, emotions, and mind stop cooperating.</p>'),
  ('weekly-notes-5th-may-11th-may', 'Weekly Notes (5th May to 11th May)', 'May 13, 2026', 'https://namangarg.in/wp-content/uploads/2026/05/image-10-1024x576.png', '<h2>Health</h2><p>This week felt like proof that discipline actually works when you stop negotiating with yourself.</p><blockquote>Discipline is not starving yourself. Discipline is understanding limits without losing enjoyment.</blockquote><p>I went to the gym every single day. 10k+ steps almost daily.</p><h2>Work</h2><p>Work this week felt exciting again. Creative exciting. We worked on a two-minute episode around Agent One. My own film crossed 3.5 minutes completed.</p><h2>Learning</h2><blockquote>Discipline changes your identity before it changes your results.</blockquote><h2>Closing Thoughts</h2><p>This week was about alignment. My body feels aligned. My work feels aligned. My thoughts feel aligned.</p>'),
  ('weekly-notes-28th-april-5th-may', 'Weekly Notes (28th April to 5th May)', 'May 6, 2026', 'https://namangarg.in/wp-content/uploads/2026/05/image-5-1024x576.png', '<p><em>Its been months since i saw a butterfly</em></p><h2>Health</h2><p>This week did not start with motivation. It started with uncertainty. I had a CT scan and nasal endoscopy. Instead of reacting, I paused.</p><p>I am currently at <strong>82 kg</strong>. The goal is clear: under 80.</p><h2>Work</h2><blockquote>If you do not express what you are learning, you slowly stop valuing it.</blockquote><h2>Learning</h2><p>Self-talk is not about speaking more. It is about becoming aware of the conversation already happening inside you.</p><h2>Closing Thoughts</h2><p>I started listening to myself. And maybe that is the beginning of everything.</p>'),
  ('weekly-notes-22nd-april-27th-april', 'Weekly Notes (22nd April to 27th April)', 'April 28, 2026', 'https://namangarg.in/wp-content/uploads/2026/04/image-13-1024x576.png', '<h2>Health</h2><p>This week was about whether I could hold the structure once normal life returned. And I did.</p><h2>Work</h2><p>I completed scripting for my new film idea. Writing always reminds me I am not limited to one lane.</p><h2>Learning</h2><blockquote>The question is not whether your goal sounds crazy. The question is: Did you earn the right to believe it today through action?</blockquote><h2>Closing Thoughts</h2><p>I need both versions of life: the explorer who gathers perspective, and the builder who applies it.</p>'),
  ('weekly-notes-14th-april-21st-april', 'Weekly Notes (14th April to 21st April)', 'April 22, 2026', 'https://namangarg.in/wp-content/uploads/2026/04/image-6-1024x576.png', '<h2>Health</h2><p>This week felt balanced and stable. The good habits I built are now slowly becoming part of my default life.</p><h2>Work</h2><blockquote>Skill is important, execution is important, but communication multiplies everything.</blockquote><h2>Learning</h2><p>I started asking my clients: How can we kill your company? Sometimes the best questions are uncomfortable ones.</p><h2>Closing Thoughts</h2><p>Bangkok ended but something new returned with me. Proof that I can move alone. Proof that I am changing.</p>'),
  ('weekly-notes-7th-april-13th-april', 'Weekly Notes (7th April to 13th April)', 'April 14, 2026', 'https://namangarg.in/wp-content/uploads/2026/04/image-3-1024x576.png', '<h2>Health</h2><p>I am <strong>2.5 kgs down</strong>. For the first time, I genuinely feel like my appetite is in my control.</p><h2>Work</h2><blockquote>The hardest part is not the technology. It is finding people who genuinely love working together.</blockquote><h2>Learning</h2><p>Speaking less but thinking more is not weakness. It is maturity.</p><h2>Closing Thoughts</h2><p>I feel more aware now. More in control of how I think, speak, and act.</p>'),
  ('weekly-notes-23rd-march-6th-april', 'Weekly Notes (23rd March to 6th April)', 'April 7, 2026', 'https://namangarg.in/wp-content/uploads/2026/04/image-1024x576.png', '<p><em>Sunsets</em></p><p>These two weeks felt different. Not loud, not chaotic, but internally heavy and meaningful.</p><h2>Brain Refreshment</h2><blockquote>Storytellers with communication skills will be the next generation achievers.</blockquote><h2>Work</h2><p>We hit 3 million views on the second video. Key takeaway: Explain everything like the other person knows nothing.</p><h2>Closing Thoughts</h2><p>These two weeks were not about doing more. They were about becoming more aware.</p>'),
  ('a-motorcycle-mind-takeaways-naman', 'A Motorcycle Mind Takeaways', 'March 31, 2026', 'https://namangarg.in/wp-content/uploads/2026/03/image-15.png', '<p>I recently went deep into a conversation by Naval Ravikant on AI. It felt more like a mirror.</p><blockquote>The internet no longer rewards generalization. It rewards specificity.</blockquote><p>AI is not truly creative. It can combine and remix, but it does not have intent or desire. That gap is still human.</p><blockquote>The means of learning are abundant now, but the desire to learn is scarce.</blockquote><p>AI is just leverage. It will not tell you who to become. That part is still yours.</p>'),
  ('weekly-notes-16th-march-22nd-march', 'Weekly Notes (16th March to 22nd March)', 'March 24, 2026', 'https://namangarg.in/wp-content/uploads/2026/03/image-13-1024x576.png', '<h2>Health</h2><p>Health-wise, this week felt strong and stable. Squats with 20 kg on each side. I am around 84-85 kg now.</p><h2>Work</h2><p>I am no longer waiting for motivation. I am just executing.</p><h2>Brain Refreshment</h2><blockquote>Balance is a luxury. You do not start with balance. You earn it.</blockquote><h2>Closing Thoughts</h2><p>When you control your habits, your life starts moving in the right direction automatically.</p>'),
  ('weekly-notes-9th-march-15th-march', 'Weekly Notes (9th March to 15th March)', 'March 15, 2026', 'https://namangarg.in/wp-content/uploads/2026/03/image-12-1024x576.png', '<h2>Health</h2><p>I dropped around <strong>2 kgs</strong>. I also bought my first protein powder through discipline, not impulse.</p><h2>Work</h2><p>This felt like one of my best weeks in terms of flow. When your body is clean and your mind is stable, your work automatically improves.</p><h2>Learning</h2><blockquote>If you attach discipline to reward, you can control your habits better.</blockquote><h2>Closing Thoughts</h2><p>Stretch this consistency as long as possible.</p>'),
]

def make_page(title, date, img, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title} | Naman Garg</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
body{{font-family:'Newsreader',serif;background:#f8f9fa}}
h1,h2,h3,nav,header,a{{font-family:'Manrope',sans-serif}}
h2{{font-size:1.5rem;font-weight:700;margin-top:2.5rem;margin-bottom:1rem;color:#191c1d}}
p{{margin-bottom:1.25rem;line-height:1.8;color:#4c4546;font-size:1.1rem}}
blockquote{{border-left:4px solid #ECB221;padding:1rem 1.5rem;background:#fdf9f0;margin:2rem 0;font-style:italic}}
img{{max-width:100%;border-radius:12px;margin:1.5rem 0}}
</style>
</head>
<body>
<header style="position:fixed;top:0;left:0;width:100%;z-index:50;background:white;border-bottom:1px solid #f3f4f5;height:80px;padding:0 40px;display:flex;align-items:center;justify-content:space-between">
<a style="font-weight:700;font-size:1.25rem;font-family:Manrope" href="../../home_naman_garg/index.html">Naman Garg</a>
<nav style="display:flex;gap:2rem">
<a style="font-size:.875rem;font-weight:500;color:#6b7280;font-family:Manrope" href="../../home_naman_garg/index.html">Home</a>
<a style="font-size:.875rem;font-weight:700;color:#92400e;border-bottom:2px solid #d97706;font-family:Manrope" href="../../daily_blogs_naman_garg/index.html">Daily Blogs</a>
<a style="font-size:.875rem;font-weight:500;color:#6b7280;font-family:Manrope" href="../../contact_naman_garg/index.html">Contact</a>
</nav>
</header>
<main style="padding-top:8rem;padding-bottom:6rem;padding-left:1.5rem;padding-right:1.5rem">
<article style="max-width:42rem;margin:0 auto">
<a href="../../daily_blogs_naman_garg/index.html" style="font-size:.875rem;color:#92400e;font-weight:600;text-transform:uppercase;letter-spacing:.1em;display:block;margin-bottom:2rem;font-family:Manrope">Back to Blogs</a>
<h1 style="font-size:2.5rem;font-weight:800;line-height:1.2;margin-bottom:1rem;font-family:Manrope">{title}</h1>
<p style="font-size:.875rem;color:#9ca3af;text-transform:uppercase;letter-spacing:.1em;margin-bottom:3rem;font-family:Manrope">{date}</p>
<div style="width:4rem;height:4px;background:#d97706;margin-bottom:3rem"></div>
<img src="{img}" style="max-width:100%;border-radius:12px;margin-bottom:2rem"/>
{content}
</article>
</main>
<footer style="padding:2.5rem;background:#f9fafb;border-top:1px solid #f3f4f5;text-align:center">
<p style="font-size:.875rem;color:#9ca3af">2024 Naman Garg. All rights reserved.</p>
</footer>
</body>
</html>"""

index_cards = ''
for slug, title, date, img, content in posts:
    html = make_page(title, date, img, content)
    with open(f'{posts_dir}/{slug}.html', 'w') as f:
        f.write(html)
    print(f'Created: {slug}.html')
    index_cards += f'<a href="posts/{slug}.html" style="display:block;background:white;padding:1.5rem;border-radius:.75rem;box-shadow:0 1px 3px rgba(0,0,0,.1);margin-bottom:1.5rem;border:1px solid #f3f4f5;text-decoration:none"><span style="font-size:.75rem;color:#92400e;text-transform:uppercase;letter-spacing:.1em;display:block;margin-bottom:.5rem;font-family:Manrope">{date}</span><h3 style="font-size:1.25rem;font-weight:700;margin-bottom:.5rem;color:#191c1d;font-family:Manrope">{title}</h3><span style="font-size:.875rem;color:#92400e;font-weight:600;font-family:Manrope">Read more</span></a>\n'

index = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Blogs | Naman Garg</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
</head>
<body style="font-family:'Newsreader',serif;background:#f8f9fa">
<header style="position:fixed;top:0;left:0;width:100%;z-index:50;background:white;border-bottom:1px solid #f3f4f5;height:80px;padding:0 40px;display:flex;align-items:center;justify-content:space-between">
<a style="font-weight:700;font-size:1.25rem;font-family:Manrope" href="../home_naman_garg/index.html">Naman Garg</a>
<nav style="display:flex;gap:2rem">
<a style="font-size:.875rem;font-weight:500;color:#6b7280;font-family:Manrope" href="../home_naman_garg/index.html">Home</a>
<a style="font-size:.875rem;font-weight:700;color:#92400e;border-bottom:2px solid #d97706;font-family:Manrope" href="../daily_blogs_naman_garg/index.html">Daily Blogs</a>
<a style="font-size:.875rem;font-weight:500;color:#6b7280;font-family:Manrope" href="../contact_naman_garg/index.html">Contact</a>
</nav>
</header>
<main style="padding-top:8rem;padding-bottom:6rem;padding-left:1.5rem;padding-right:1.5rem">
<div style="max-width:42rem;margin:0 auto">
<span style="font-size:.75rem;color:#92400e;text-transform:uppercase;letter-spacing:.1em;display:block;margin-bottom:1rem;font-family:Manrope">All Posts</span>
<h1 style="font-size:3rem;font-weight:800;line-height:1.2;margin-bottom:1rem;font-family:Manrope">Naman Garg Blog</h1>
<p style="font-size:1.25rem;color:#9ca3af;font-style:italic;margin-bottom:4rem">Weekly notes, reflections, and personal growth.</p>
<div style="width:4rem;height:4px;background:#d97706;margin-bottom:4rem"></div>
{index_cards}
<!-- BLOG_LIST_END -->
</div>
</main>
<footer style="padding:2.5rem;background:#f9fafb;border-top:1px solid #f3f4f5;text-align:center">
<p style="font-size:.875rem;color:#9ca3af">2024 Naman Garg. All rights reserved.</p>
</footer>
</body>
</html>"""

with open('daily_blogs_naman_garg/index.html', 'w') as f:
    f.write(index)

print('Created: daily_blogs_naman_garg/index.html')
print('ALL DONE! Now run: git add . && git commit -m "migrated blogs" && git push')
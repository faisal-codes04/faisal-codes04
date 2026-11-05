"""Upgrade only the moving snake in a Platane/snk SVG: gradient body, soft glow and eyes.
Everything else (GitHub green cells, layout, animation) stays as generated.
Usage: python style_snake.py <file.svg> <dark|light>"""
import sys

path, theme = sys.argv[1], sys.argv[2]
s = open(path, encoding='utf-8').read()
dark = theme == 'dark'

if dark:
    body = ['#a5f3fc', '#56d4dd', '#39c5cf', '#1f6feb']
    glow, eye = 'rgba(57,197,207,.7)', '#0d1117'
else:
    body = ['#0969da', '#1f6feb', '#218bff', '#54aeff']
    glow, eye = 'rgba(57,197,207,.45)', '#ffffff'

css = (f'.s{{filter:drop-shadow(0 0 3px {glow})}}'
       + ''.join(f'.s.s{i}{{fill:{c}}}' for i, c in enumerate(body))
       + f'.s.eye{{fill:{eye};filter:none}}')
s = s.replace('</style>', css + '</style>', 1)

# eyes use the head's classes, so they follow the head's animation
eyes = ('<rect class="s s0 eye" x="4" y="4.5" width="2.6" height="2.6" rx="1.3"/>'
        '<rect class="s s0 eye" x="9.4" y="4.5" width="2.6" height="2.6" rx="1.3"/>')
s = s.replace('</svg>', eyes + '</svg>')
open(path, 'w', encoding='utf-8').write(s)
print('styled', path)

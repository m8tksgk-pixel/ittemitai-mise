"""行きたい店リストのアイコンを作る（どんぶりの絵＋右下に Claude の印）。
印の描き方は ツール\\アイコン印\\badge_icons.py の badge_logo と同じ。
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Users\kashi\OneDrive\デスクトップ\保管\アプリアイコン\src"


def badge_claude(d):
    b = Image.new("RGBA", (d, d), (0, 0, 0, 0))
    dr = ImageDraw.Draw(b)
    ring = max(2, d // 14)
    dr.ellipse((0, 0, d - 1, d - 1), fill="white")
    dr.ellipse((ring, ring, d - 1 - ring, d - 1 - ring), fill="#D97757")
    logo = Image.open(os.path.join(SRC, "claude.png")).convert("RGBA")
    logo = logo.crop(logo.getchannel("A").getbbox())
    px = logo.load()
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, bb, a = px[x, y]
            px[x, y] = (255, 255, 255, a if (r + g + bb) > 600 else 0)
    inner = int(d * 0.62)
    logo.thumbnail((inner, inner), Image.LANCZOS)
    b.alpha_composite(logo, ((d - logo.width) // 2, (d - logo.height) // 2))
    return b


def base_icon(S=1024):
    im = Image.new("RGBA", (S, S), "#b5432a")
    dr = ImageDraw.Draw(im)
    # 湯気
    for i, x in enumerate((0.38, 0.5, 0.62)):
        cx = int(S * x)
        dr.arc((cx - S * 0.06, S * 0.16, cx + S * 0.06, S * 0.32), 200, 340, fill="#f7f1e8", width=int(S * 0.025))
        dr.arc((cx - S * 0.06, S * 0.26, cx + S * 0.06, S * 0.42), 20, 160, fill="#f7f1e8", width=int(S * 0.025))
    # 箸
    dr.line((S * 0.58, S * 0.30, S * 0.86, S * 0.12), fill="#e9b44c", width=int(S * 0.035))
    dr.line((S * 0.62, S * 0.34, S * 0.90, S * 0.18), fill="#e9b44c", width=int(S * 0.035))
    # どんぶり
    dr.pieslice((S * 0.16, S * 0.22, S * 0.84, S * 0.90), 0, 180, fill="#f7f1e8")
    dr.rectangle((S * 0.14, S * 0.53, S * 0.86, S * 0.58), fill="#f7f1e8")
    dr.rounded_rectangle((S * 0.38, S * 0.86, S * 0.62, S * 0.92), radius=S * 0.02, fill="#f7f1e8")
    dr.arc((S * 0.24, S * 0.40, S * 0.76, S * 0.80), 30, 150, fill="#b5432a", width=int(S * 0.02))
    return im


def main():
    S = 1024
    img = base_icon(S)
    d = int(S * 0.34)
    # 上は湯気と箸があるので、空いている右下に印を置く
    img.alpha_composite(badge_claude(d), (S - d - int(S * 0.02), S - d - int(S * 0.02)))
    for size in (512, 192):
        img.resize((size, size), Image.LANCZOS).save(os.path.join(HERE, f"icon-{size}.png"))
    print("ok")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""news-image-20261119: front page for Thursday 19 November 2026, stdlib only."""
import os, random, struct, zlib

W, H = 1024, 768
INK = (18, 18, 22)
PAPER = (246, 242, 230)
GREY = (118, 112, 100)
RED = (178, 44, 38)
BLUE = (30, 62, 112)

FONT = {
    "A": (0x0E, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "B": (0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E),
    "C": (0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E),
    "D": (0x1C, 0x12, 0x11, 0x11, 0x11, 0x12, 0x1C),
    "E": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F),
    "F": (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10),
    "G": (0x0E, 0x11, 0x10, 0x17, 0x11, 0x11, 0x0F),
    "H": (0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11),
    "I": (0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "J": (0x07, 0x02, 0x02, 0x02, 0x02, 0x12, 0x0C),
    "K": (0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11),
    "L": (0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F),
    "M": (0x11, 0x1B, 0x15, 0x15, 0x11, 0x11, 0x11),
    "N": (0x11, 0x19, 0x15, 0x13, 0x11, 0x11, 0x11),
    "O": (0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "P": (0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10),
    "Q": (0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D),
    "R": (0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11),
    "S": (0x0F, 0x10, 0x10, 0x0E, 0x01, 0x01, 0x1E),
    "T": (0x1F, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04),
    "U": (0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E),
    "V": (0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04),
    "W": (0x11, 0x11, 0x11, 0x15, 0x15, 0x1B, 0x11),
    "X": (0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11),
    "Y": (0x11, 0x11, 0x0A, 0x04, 0x04, 0x04, 0x04),
    "Z": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F),
    "0": (0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E),
    "1": (0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E),
    "2": (0x0E, 0x11, 0x01, 0x02, 0x04, 0x08, 0x1F),
    "3": (0x1F, 0x02, 0x04, 0x02, 0x01, 0x11, 0x0E),
    "4": (0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02),
    "5": (0x1F, 0x10, 0x1E, 0x01, 0x01, 0x11, 0x0E),
    "6": (0x06, 0x08, 0x10, 0x1E, 0x11, 0x11, 0x0E),
    "7": (0x1F, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08),
    "8": (0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E),
    "9": (0x0E, 0x11, 0x11, 0x0F, 0x01, 0x02, 0x0C),
    ".": (0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C),
    ",": (0x00, 0x00, 0x00, 0x00, 0x0C, 0x04, 0x08),
    "!": (0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04),
    "?": (0x0E, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04),
    "-": (0x00, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00),
    ":": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x0C, 0x00),
    ";": (0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x04, 0x08),
    "'": (0x04, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00),
    "(": (0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02),
    ")": (0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08),
    "/": (0x01, 0x01, 0x02, 0x04, 0x08, 0x10, 0x10),
    "&": (0x0C, 0x12, 0x14, 0x08, 0x15, 0x12, 0x0D),
    "%": (0x19, 0x1A, 0x02, 0x04, 0x08, 0x0B, 0x13),
    "$": (0x0F, 0x10, 0x1E, 0x01, 0x1E, 0x10, 0x0F),
    "+": (0x00, 0x04, 0x04, 0x1F, 0x04, 0x04, 0x00),
    "#": (0x0A, 0x1F, 0x0A, 0x0A, 0x1F, 0x0A, 0x00),
    " ": (0, 0, 0, 0, 0, 0, 0),
}

WORDS = (
    "THE DAILY PIXEL PRESS ROOM MORNING EDITION CITY DESK WIRE STORY PAGE PRINT INK PAPER "
    "NEWS HEADLINE COLUMN EDITOR REPORTER SOURCE COPY LATE BREAKING UPDATE ARCHIVE SPECIAL "
    "FEATURES SECTION MARKET WEATHER FORECAST SUNNY CLOUDY MILD BREEZE HIGH LOW TEMP READERS "
    "DIGEST LETTERS OPINION REVIEW ARTS CULTURE SCIENCE TECHNOLOGY COMPUTING SOFTWARE HARDWARE "
    "NETWORK PROTOCOL PACKET BYTES PIXELS LINES RENDER DETERMINISTIC STDLIB ONLY PERFECT "
    "REPRODUCIBLE EVERY TIME AGAIN"
).split()


def tw(text, scale=2):
    return len(text) * 6 * scale


def wrap(text, width, scale):
    lines, cur = [], ""
    for word in text.split():
        cand = (cur + " " + word).strip()
        if tw(cand, scale) <= width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def rect(cv, x, y, w, h, color):
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(W, x + w), min(H, y + h)
    if x1 <= x0 or y1 <= y0:
        return
    row = bytes(color) * (x1 - x0)
    for yy in range(y0, y1):
        o = 3 * (yy * W + x0)
        cv[o : o + len(row)] = row


def text(cv, x, y, s, scale=2, color=INK):
    cx = x
    for ch in s.upper():
        g = FONT.get(ch, FONT["?"])
        for ry, row in enumerate(g):
            for rx in range(5):
                if row & (1 << (4 - rx)):
                    rect(cv, cx + rx * scale, y + ry * scale, scale, scale, color)
        cx += 6 * scale
    return cx


def png(cv):
    def ck(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    raw = b"".join(b"\x00" + cv[y * W * 3 : (y + 1) * W * 3] for y in range(H))
    return (b"\x89PNG\r\n\x1a\n"
            + ck(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
            + ck(b"IDAT", zlib.compress(raw, 9))
            + ck(b"IEND", b""))


def main():
    rng = random.Random(20261119)
    cv = bytearray(W * H * 3)
    for i in range(W * H):
        cv[3 * i : 3 * i + 3] = bytes(PAPER)

    # Masthead
    rect(cv, 0, 0, W, 8, INK)
    text(cv, (W - tw("WORLD NEWS", 8)) // 2, 30, "WORLD NEWS", 8, INK)
    text(cv, (W - tw("THURSDAY 19 NOVEMBER 2026", 3)) // 2, 100,
         "THURSDAY 19 NOVEMBER 2026", 3, RED)
    rect(cv, 30, 134, W - 60, 3, INK)
    text(cv, 30, 144, "VOL. MMXXVI  .  NO. 324  .  GLOBAL EDITION", 2, GREY)
    text(cv, W - 30 - tw("PRICE: 0 BTC", 2), 144, "PRICE: 0 BTC", 2, GREY)
    rect(cv, 30, 170, W - 60, 2, INK)

    # Lead story: GTA VI launch day console release
    text(cv, 30, 184, "EXCLUSIVE", 2, RED)
    rect(cv, 30 + tw("EXCLUSIVE", 2) + 8, 190, 120, 2, RED)
    y = 206
    for line in wrap("GTA VI LAUNCH DAY: CONSOLE STOCKS VANISH WORLDWIDE", W - 60, 5):
        text(cv, (W - tw(line, 5)) // 2, y, line, 5, INK)
        y += 40
    y += 2
    for line in wrap("RETAILERS REPORT MIDNIGHT QUEUES AS GAMERS SNATCH EVERY BOX; "
                     "SECOND-HAND PRICES SOAR ONLINE", W - 240, 2):
        text(cv, (W - tw(line, 2)) // 2, y, line, 2, GREY)
        y += 18
    rect(cv, 30, y + 6, W - 60, 2, INK)
    y += 18

    # Etched 'photo': city at night with a queue of gamers
    px, py, pw, ph = 30, y, 400, 240
    rect(cv, px, py, pw, ph, (26, 30, 48))
    rng2 = random.Random(7)
    for _ in range(240):
        sx, sy = px + rng2.randrange(pw), py + rng2.randrange(ph - 60)
        rect(cv, sx, sy, 1, 1, (240, 230, 160))
    hs = (60, 90, 72, 112, 84, 130, 96, 66, 118, 88, 76, 104)
    bw = (pw - 24) // len(hs)
    for k, hg in enumerate(hs):
        rect(cv, px + 12 + k * bw, py + ph - 40 - hg, bw - 2, hg, (14, 16, 26))
        for _ in range(hg // 12):
            rect(cv, px + 14 + k * bw + rng2.randrange(bw - 6),
                 py + ph - 44 - hg + rng2.randrange(hg - 8), 2, 2, (188, 170, 90))
    for k in range(30):
        qx = px + 10 + (k * 13) % (pw - 20)
        rect(cv, qx, py + ph - 34 - (k % 3) * 4, 3, 7, (200, 60, 50))
    rect(cv, px, py + ph - 26, pw, 26, INK)
    text(cv, px + 8, py + ph - 18, "MIDNIGHT LAUNCH QUEUE. STAFF PHOTO.", 1, PAPER)
    text(cv, px, y + ph + 8, "ABOVE: THE QUEUE OUTSIDE A GAMES STORE AT DAWN.", 2, GREY)

    # Markesidebar next to photo
    sx0 = px + pw + 24
    sw = W - 30 - sx0
    text(cv, sx0, y, "MARKETS TODAY", 3, INK)
    rect(cv, sx0, y + 24, sw, 2, RED)
    rows = (("FTSE 100", "9,842", "+0.8%"), ("DOW JONES", "51,260", "+0.4%"),
            ("NIKKEI 225", "44,118", "-0.6%"), ("EURO STOXX", "6,204", "+0.2%"),
            ("GOLD/OZ", "$4,310", "+1.1%"), ("BRENT CRUDE", "$79.4", "-0.9%"))
    ry = y + 38
    for name, val, chg in rows:
        text(cv, sx0, ry, name, 2, GREY)
        text(cv, sx0 + sw - tw(val, 2) - tw(chg, 2) - 14, ry, val, 2, INK)
        text(cv, sx0 + sw - tw(chg, 2), ry, chg, 2, RED if chg[0] == "+" else BLUE)
        ry += 22
    rect(cv, sx0, ry + 4, sw, 2, GREY)
    ty = ry + 16
    for line in wrap("MARKETS FIRM AS TRADERS EYE RATE CUT HOPES; TECH SHARES LEAD "
                     "GAINERS WHILE ENERGY SLIPS ON SOFT DEMAND DATA", sw, 2):
        text(cv, sx0, ty, line, 2, INK)
        ty += 18

    # Three story columns below the fold
    y2 = y + ph + 40
    rect(cv, 30, y2 - 14, W - 60, 2, INK)
    gap = 22
    cw3 = (W - 60 - 2 * gap) // 3
    cols = (
        ("CLIMATE SUMMIT", RED,
         "DELEGATES AT THE GENEVA CLIMATE SUMMIT AGREE A PHASE-OUT TIMELINE FOR COAL; "
         "SMALL ISLAND STATES CALL THE PACT A FIRST STEP BUT DEMAND FASTER CUTS BY 2030."),
        ("TECH & AI", BLUE,
         "BRUSSELS UNVEILS NEW RULES FOR FRONTIER AI MODELS; MAJOR LABS SIGN A SAFETY "
         "CODE WHILE STARTUPS WARN OF COMPLIANCE COSTS AND DELAYED ROLLOUTS."),
        ("SPORT", INK,
         "DRAMATIC NIGHT IN THE CHAMPIONS LEAGUE AS A LAST-MINUTE FREE KICK SENDS THE "
         "HOME SIDE THROUGH; TEST MATCH ENDS LEVEL AFTER A CAUGHT BEHIND REVIEW."),
    )
    for c, (head, hcol, body) in enumerate(cols):
        cx = 30 + c * (cw3 + gap)
        text(cv, cx, y2, head, 3, hcol)
        rect(cv, cx, y2 + 22, cw3, 2, hcol)
        ty = y2 + 38
        for line in wrap(body, cw3, 2):
            text(cv, cx, ty, line, 2, GREY)
            ty += 18
        fy = ty + 6
        fill = " ".join(rng.choice(WORDS) for _ in range(50))
        for line in wrap(fill, cw3, 2):
            text(cv, cx, fy, line, 2, (150, 144, 132))
            fy += 18
            if fy > y2 + 250:
                break

    # Footer
    rect(cv, 30, H - 44, W - 60, 2, INK)
    text(cv, 30, H - 32, "WORLD NEWS . PAGE ONE . DETERMINISTIC EDITION", 2, GREY)
    text(cv, W - 30 - tw("MAKE.FUN 2026", 2), H - 32, "MAKE.FUN 2026", 2, RED)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    data = png(cv)
    path = os.path.join(out_dir, "entry.png")
    with open(path, "wb") as f:
        f.write(data)
    print("wrote", path, len(data), "bytes")


main()
#!/usr/bin/env python3
"""진본 화면 목업 SVG 생성기.

실제 구현 코드(jinbon-ios / jinbon-web / jinbon-extension)에서 확인한
색상·문구·레이아웃을 그대로 옮긴 와이어프레임을 만든다.

사용법:
    python3 generate.py        # 이 디렉터리에 *.svg 생성
"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ── 실제 코드에서 가져온 색상 ────────────────────────────────
# iOS: source/DIDCA/Custom/ColorPalette.swift
IOS = {
    "primary": "#2457E6", "ink": "#111827", "sub": "#475467",
    "canvas": "#F7F8FC", "success": "#12B76A", "card": "#FFFFFF",
    "warning": "#F79009", "danger": "#F04438", "divider": "#EAECF0",
    "softBlue": "#EEF4FF", "disabled": "#D0D5DD",
}
# web: app/globals.css
WEB = {
    "ink": "#10231d", "paper": "#f4f1e9", "line": "#cfc9bc",
    "accent": "#ff6a3d", "green": "#0f7956", "muted": "#657069",
    "shell": "#fbfaf6",
}

FONT = "-apple-system,'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,monospace"

W, H = 320, 660          # 아이폰 프레임
PAD = 20                 # 좌우 여백
CW = W - PAD * 2         # 콘텐츠 폭


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=13, weight=400, fill=IOS["ink"], anchor="start", font=FONT, op=1):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{op}">{esc(s)}</text>')


def rect(x, y, w, h, fill, r=0, stroke=None, sw=1, op=1, dash=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" opacity="{op}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{sw}"'
    if dash:
        s += f' stroke-dasharray="{dash}"'
    return s + "/>"


def circle(cx, cy, r, fill, stroke=None, sw=1):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{sw}"'
    return s + "/>"


class Screen:
    """세로로 요소를 쌓아 아이폰 화면을 만든다."""

    def __init__(self, name, title=None, tab=None, canvas=None):
        self.name = name
        self.title = title
        self.tab = tab                      # 탭바 활성 인덱스 (None이면 탭바 없음)
        self.bg = canvas or IOS["canvas"]
        self.body = []
        self.y = 52                         # 상태바 아래
        if title is not None:
            self.navbar(title)

    # ── 기본 요소 ────────────────────────────────────────
    def navbar(self, title, back=False, right=None):
        self.body.append(rect(0, 44, W, 44, self.bg))
        self.body.append(txt(W / 2, 72, title, 15, 700, IOS["ink"], "middle"))
        if back:
            self.body.append(txt(PAD, 72, "‹", 20, 700, IOS["primary"]))
        if right:
            self.body.append(txt(W - PAD, 72, right, 13, 600, IOS["primary"], "end"))
        self.y = 100
        return self

    def gap(self, n=12):
        self.y += n
        return self

    def eyebrow(self, s):
        self.body.append(txt(PAD, self.y + 10, s, 10, 700, IOS["primary"]))
        self.y += 20
        return self

    def h1(self, lines, size=20):
        for ln in lines:
            self.body.append(txt(PAD, self.y + size, ln, size, 700, IOS["ink"]))
            self.y += size + 7
        return self

    def body_text(self, lines, size=11, fill=None, x=None, anchor="start"):
        for ln in lines:
            self.body.append(txt(x if x is not None else PAD, self.y + size,
                                 ln, size, 400, fill or IOS["sub"], anchor))
            self.y += size + 5
        return self

    def center_text(self, lines, size=11, weight=400, fill=None):
        for ln in lines:
            self.body.append(txt(W / 2, self.y + size, ln, size, weight,
                                 fill or IOS["sub"], "middle"))
            self.y += size + 6
        return self

    def card(self, h, fill=None, stroke=None, r=16):
        y0 = self.y
        self.body.append(rect(PAD, y0, CW, h, fill or IOS["card"], r,
                              stroke or IOS["divider"]))
        self.y = y0 + h
        return y0

    def button(self, label, filled=True, h=44, icon=None):
        y0 = self.y
        bg = IOS["primary"] if filled else IOS["softBlue"]
        fg = "#FFFFFF" if filled else IOS["primary"]
        self.body.append(rect(PAD, y0, CW, h, bg, 12))
        lab = f"{icon} {label}" if icon else label
        self.body.append(txt(W / 2, y0 + h / 2 + 4, lab, 13, 700, fg, "middle"))
        self.y = y0 + h
        return self

    def badge(self, label, fill, x=PAD, w=None, y=None, fg="#FFFFFF", size=9):
        yy = self.y if y is None else y
        ww = w or (len(label) * 7 + 18)
        self.body.append(rect(x, yy, ww, 19, fill, 9))
        self.body.append(txt(x + ww / 2, yy + 13, label, size, 700, fg, "middle"))
        if y is None:
            self.y += 19
        return self

    def divider(self):
        self.body.append(rect(PAD, self.y, CW, 1, IOS["divider"]))
        self.y += 1
        return self

    def kv(self, k, v, vw=700, vfill=None, font=FONT):
        self.body.append(txt(PAD + 12, self.y + 11, k, 10, 500, IOS["sub"]))
        self.body.append(txt(W - PAD - 12, self.y + 11, v, 10, vw,
                             vfill or IOS["ink"], "end", font))
        self.y += 26
        return self

    def raw(self, s):
        self.body.append(s)
        return self

    # ── 조립 ────────────────────────────────────────────
    def render(self):
        p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" role="img" aria-label="{esc(self.name)}">']
        p.append(f'<rect width="{W}" height="{H}" rx="30" fill="{self.bg}" '
                 f'stroke="{IOS["disabled"]}" stroke-width="1.5"/>')
        # 상태바
        p.append(txt(PAD, 28, "9:41", 11, 700, IOS["ink"]))
        p.append(txt(W - PAD, 28, "▮▮▮", 9, 400, IOS["ink"], "end"))
        p += self.body
        if self.tab is not None:
            p.append(self._tabbar())
        p.append("</svg>")
        return "\n".join(p)

    def _tabbar(self):
        items = ["홈", "내 영상", "보증서", "설정"]
        icons = ["⌂", "▷", "✓", "⚙"]
        ty = H - 62
        s = [rect(1, ty, W - 2, 61, IOS["card"], 0),
             rect(1, ty, W - 2, 1, IOS["divider"])]
        for i, (lab, ic) in enumerate(zip(items, icons)):
            cx = W / 8 * (2 * i + 1)
            col = IOS["primary"] if i == self.tab else IOS["sub"]
            s.append(txt(cx, ty + 26, ic, 16, 400, col, "middle"))
            s.append(txt(cx, ty + 44, lab, 9,
                         700 if i == self.tab else 500, col, "middle"))
        return "\n".join(s)


def write(name, svg):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  {name}")


# ══════════════════════════════════════════════════════════
# iOS 화면
# ══════════════════════════════════════════════════════════

def ios_welcome():
    s = Screen("진본 시작 화면")
    s.y = 60
    s.raw(rect(PAD, s.y, 50, 50, IOS["primary"], 16))
    s.raw(txt(PAD + 25, s.y + 34, "J", 25, 800, "#FFFFFF", "middle"))
    s.y += 68
    s.h1(["진짜를 증명하는", "가장 간단한 방법"], 21)
    s.gap(4)
    s.body_text(["영상의 원본 여부를 안전하게 증명하세요."], 11)
    s.gap(18)
    for icon, ti, de, bt, filled in [
        ("＋", "처음 이용하시나요?", "디지털 신원을 만들고 진본을 시작해요", "회원가입", True),
        ("✓", "이미 가입하셨나요?", "모바일 신분증으로 안전하게 로그인해요", "로그인", False),
    ]:
        y0 = s.card(126, r=20)
        s.raw(txt(PAD + 16, y0 + 32, icon, 15, 700, IOS["primary"]))
        s.raw(txt(PAD + 40, y0 + 32, ti, 12, 700, IOS["ink"]))
        s.raw(txt(PAD + 40, y0 + 50, de, 9.5, 400, IOS["sub"]))
        bg = IOS["primary"] if filled else IOS["softBlue"]
        fg = "#FFFFFF" if filled else IOS["primary"]
        s.raw(rect(PAD + 16, y0 + 66, CW - 32, 42, bg, 11))
        s.raw(txt(W / 2, y0 + 92, bt, 12.5, 700, fg, "middle"))
        s.gap(14)
    s.gap(6)
    s.center_text(["로그인 없이 영상 검증하기  →"], 11.5, 600, IOS["primary"])
    return s.render()


def ios_home():
    s = Screen("진본 홈", "홈", tab=0)
    s.gap(4)
    s.eyebrow("진본 크리에이터 월렛")
    s.h1(["안녕하세요, 홍길동님"], 18)
    s.body_text(["영상의 온체인 등록과 VC 보증서를 관리하세요."], 10.5)
    s.gap(14)

    y0 = s.card(56)
    s.raw(circle(PAD + 26, y0 + 28, 12, IOS["softBlue"]))
    s.raw(txt(PAD + 26, y0 + 32, "✓", 11, 700, IOS["primary"], "middle"))
    s.raw(txt(PAD + 48, y0 + 25, "디지털 신원 연결됨", 12, 700, IOS["ink"]))
    s.raw(txt(PAD + 48, y0 + 41, "공인 등록자 · 영상 등록 가능", 9.5, 400, IOS["sub"]))
    s.gap(12)

    y0 = s.card(118, IOS["primary"], IOS["primary"], r=18)
    s.raw(txt(PAD + 18, y0 + 30, "새 영상 온체인 등록", 13.5, 700, "#FFFFFF"))
    s.raw(txt(PAD + 18, y0 + 50, "영상 디지털 지문을 블록체인에 기록하고", 9.5, 400, "#FFFFFF", op=.85))
    s.raw(txt(PAD + 18, y0 + 64, "등록 보증서를 발급받아요.", 9.5, 400, "#FFFFFF", op=.85))
    s.raw(rect(PAD + 18, y0 + 76, CW - 36, 30, "#FFFFFF", 9))
    s.raw(txt(W / 2, y0 + 96, "영상 등록하기", 12, 700, IOS["primary"], "middle"))
    s.gap(16)

    s.raw(txt(PAD, s.y + 11, "최근 등록", 13, 700, IOS["ink"]))
    s.raw(txt(W - PAD, s.y + 11, "총 2건", 10, 500, IOS["sub"], "end"))
    s.y += 22
    for t, d, ok in [("2026 기자회견 원본", "2026-09-05", True),
                     ("현장 인터뷰 풀영상", "2026-09-03", True)]:
        y0 = s.card(50)
        s.raw(txt(PAD + 14, y0 + 22, t, 11, 600, IOS["ink"]))
        s.raw(txt(PAD + 14, y0 + 38, d, 9, 400, IOS["sub"]))
        s.badge("인증 유효", IOS["success"], x=W - PAD - 62, y=y0 + 16, w=52)
        s.gap(8)
    return s.render()


def ios_list():
    s = Screen("내 영상 목록", "내 영상", tab=1)
    s.body.append(txt(W - PAD, 72, "＋", 18, 700, IOS["primary"], "end"))
    s.gap(4)
    for t, d, ok in [("2026 기자회견 원본", "2026-09-05 · 등록됨", True),
                     ("현장 인터뷰 풀영상", "2026-09-03 · 등록됨", True),
                     ("사전 브리핑 클립", "2026-08-28 · 비활성화됨", False)]:
        y0 = s.card(72)
        s.raw(rect(PAD + 12, y0 + 14, 44, 44, IOS["softBlue"], 8))
        s.raw(txt(PAD + 34, y0 + 42, "▶", 13, 400, IOS["primary"], "middle"))
        s.raw(txt(PAD + 66, y0 + 28, t, 11.5, 600, IOS["ink"]))
        s.raw(txt(PAD + 66, y0 + 46, d, 9, 400, IOS["sub"]))
        lab = "✓ 등록 유효" if ok else "! 비활성"
        col = IOS["success"] if ok else IOS["warning"]
        s.raw(rect(W - PAD - 66, y0 + 14, 54, 18, col, 9, op=.12))
        s.raw(txt(W - PAD - 39, y0 + 27, lab, 8, 700, col, "middle"))
        s.gap(10)
    s.gap(10)
    s.body.append(rect(PAD, s.y, CW, 1, IOS["divider"], dash="3 3"))
    s.y += 14
    s.center_text(["행을 누르면 영상 정보와", "보증서 발급 · 비활성화를 선택할 수 있어요"], 9.5)
    return s.render()


def ios_upload():
    s = Screen("영상 온체인 등록", "영상 온체인 등록")
    s.body.append(txt(PAD, 72, "✕", 15, 600, IOS["sub"]))
    s.gap(2)
    s.eyebrow("온체인 등록")
    s.h1(["영상 디지털 지문을 등록하세요"], 16)
    s.body_text(["영상 해시를 블록체인에 기록해요."], 10.5)
    s.gap(14)

    s.badge("1", IOS["primary"], w=20)
    s.raw(txt(PAD + 28, s.y - 5, "등록할 영상 선택", 12, 700, IOS["ink"]))
    s.raw(txt(PAD + 28, s.y + 9, "MP4, MOV 등 갤러리의 영상 파일", 9, 400, IOS["sub"]))
    s.y += 20

    y0 = s.card(128, IOS["softBlue"], IOS["primary"], r=18)
    s.raw(circle(W / 2, y0 + 52, 24, IOS["primary"]))
    s.raw(txt(W / 2, y0 + 58, "＋", 18, 700, "#FFFFFF", "middle"))
    s.raw(txt(W / 2, y0 + 96, "탭하여 영상 선택", 12, 700, IOS["ink"], "middle"))
    s.gap(18)

    s.badge("2", IOS["primary"], w=20)
    s.raw(txt(PAD + 28, s.y - 5, "영상 정보", 12, 700, IOS["ink"]))
    s.raw(txt(PAD + 28, s.y + 9, "내 영상에서 쉽게 구분할 이름", 9, 400, IOS["sub"]))
    s.y += 20

    y0 = s.card(60, r=14)
    s.raw(txt(PAD + 16, y0 + 22, "제목", 9.5, 700, IOS["sub"]))
    s.raw(txt(PAD + 16, y0 + 44, "영상 제목을 입력하세요", 12, 400, IOS["disabled"]))
    s.gap(14)

    y0 = s.card(44, IOS["softBlue"], IOS["softBlue"], r=12)
    s.raw(txt(W / 2, y0 + 27, "영상 원문은 저장하지 않고", 9.5, 500, IOS["sub"], "middle"))
    s.y = y0 + 32
    s.center_text(["디지털 지문만 블록체인에 등록해요."], 9.5, 500)
    s.gap(14)
    s.button("영상 디지털 지문 등록하기", icon="🛡", h=46)
    return s.render()


def ios_complete():
    s = Screen("등록 완료", "등록 완료", canvas=IOS["canvas"])
    s.body.append(txt(W - PAD, 72, "닫기", 12.5, 600, IOS["primary"], "end"))
    s.gap(14)
    s.raw(circle(W / 2, s.y + 34, 34, IOS["success"], None))
    s.raw(f'<circle cx="{W/2}" cy="{s.y+34}" r="34" fill="{IOS["success"]}" opacity="0.12"/>')
    s.raw(txt(W / 2, s.y + 43, "🛡", 26, 400, IOS["success"], "middle"))
    s.y += 82
    s.center_text(["블록체인 등록 완료"], 19, 700, IOS["ink"])
    s.gap(6)
    s.center_text(["영상 디지털 지문과 등록자 DID가", "블록체인에 기록됐어요."], 10.5)
    s.gap(16)

    y0 = s.card(78, r=18)
    s.y = y0 + 10
    s.kv("영상", "2026 기자회견 원본")
    s.kv("등록일", "2026-09-07")
    s.y = y0 + 78
    s.gap(12)

    y0 = s.card(74, r=18)
    s.raw(txt(PAD + 18, y0 + 26, "영상 블록체인 등록 보증서", 12, 700, IOS["ink"]))
    s.raw(txt(PAD + 18, y0 + 50, "◌", 12, 400, IOS["sub"]))
    s.raw(txt(PAD + 36, y0 + 50, "등록 보증서 발급 대기", 10, 400, IOS["sub"]))
    s.gap(16)
    s.button("등록 보증서 발급하기", h=46)
    s.gap(10)
    s.button("내 영상으로 돌아가기", filled=False, h=44)
    return s.render()


def ios_offer():
    s = Screen("보증서 발급 확인", canvas="#0F172A")
    s.body = [rect(0, 0, W, H, "#0F172A", 30)]
    s.y = 0
    cy = 150
    s.raw(rect(24, cy, W - 48, 330, "#FFFFFF", 24))
    s.raw(f'<circle cx="{W/2}" cy="{cy+56}" r="28" fill="{IOS["softBlue"]}"/>')
    s.raw(txt(W / 2, cy + 65, "✓", 24, 700, IOS["primary"], "middle"))
    s.raw(txt(W / 2, cy + 112, "JINBON WALLET", 10, 700, IOS["primary"], "middle"))
    s.raw(txt(W / 2, cy + 142, "등록 보증서를 발급할까요?", 16, 700, IOS["ink"], "middle"))
    for i, ln in enumerate(["진본 Issuer가 영상 디지털 지문의",
                            "온체인 등록 사실과 등록 주체를 확인한",
                            "VC 보증서를 발급합니다."]):
        s.raw(txt(W / 2, cy + 172 + i * 17, ln, 10, 400, IOS["sub"], "middle"))
    s.raw(rect(48, cy + 232, W - 96, 42, "#FFFFFF", 11, IOS["divider"]))
    s.raw(txt(W / 2, cy + 258, "나중에", 12, 600, IOS["sub"], "middle"))
    s.raw(rect(48, cy + 282, W - 96, 44, IOS["primary"], 11))
    s.raw(txt(W / 2, cy + 309, "등록 보증서 발급하기", 12.5, 700, "#FFFFFF", "middle"))
    return s.render()


def ios_verify():
    s = Screen("영상 검증 결과", "영상 검증")
    s.body.append(txt(PAD, 72, "✕", 15, 600, IOS["sub"]))
    s.gap(8)
    s.center_text(["공식 등록 영상과 비교하세요"], 14, 700, IOS["ink"])
    s.gap(2)
    s.center_text(["갤러리에서 영상 하나를 선택하면 돼요."], 10.5)
    s.gap(12)

    y0 = s.card(96, IOS["softBlue"], IOS["primary"], r=18)
    s.raw(rect(PAD + 90, y0 + 20, 140, 44, IOS["primary"], 8, op=.14))
    s.raw(txt(W / 2, y0 + 48, "▶  interview_final.mp4", 9.5, 600, IOS["primary"], "middle"))
    s.raw(txt(W / 2, y0 + 80, "탭하여 영상 선택", 10.5, 600, IOS["sub"], "middle"))
    s.gap(12)
    s.button("다시 검증", h=44)
    s.gap(14)

    y0 = s.card(232, IOS["card"], IOS["success"], r=18)
    s.raw(txt(PAD + 16, y0 + 34, "✅", 15, 400, IOS["success"]))
    s.raw(txt(PAD + 42, y0 + 32, "등록 영상과 정확히", 13, 700, IOS["ink"]))
    s.raw(txt(PAD + 42, y0 + 50, "일치합니다", 13, 700, IOS["ink"]))
    s.y = y0 + 62
    s.kv("영상 디지털 지문", "정확히 일치")
    s.kv("블록체인 등록", "확인됨")
    s.kv("진본 VC 보증서", "유효")
    yy = s.y + 4
    s.raw(rect(PAD + 12, yy, CW - 24, 34, IOS["success"], 9, op=.09))
    s.raw(txt(PAD + 24, yy + 21, "등록된 원본 파일과 정확히 일치합니다.",
              9.5, 600, IOS["ink"]))
    s.y = yy + 44
    s.kv("등록일", "2026-09-05")
    return s.render()


def ios_certificate():
    s = Screen("등록 보증서 상세", "등록 보증서 상세")
    s.body.append(txt(PAD, 72, "‹", 20, 700, IOS["primary"]))
    s.gap(6)
    y0 = s.card(96, IOS["ink"], IOS["ink"], r=20)
    s.raw(txt(PAD + 18, y0 + 30, "영상 블록체인 등록 보증서", 13, 700, "#FFFFFF"))
    s.raw(txt(PAD + 18, y0 + 48, "JinBon Verifiable Credential", 9.5, 400, "#FFFFFF", op=.6))
    s.raw(rect(PAD + 18, y0 + 60, 86, 22, IOS["success"], 11))
    s.raw(txt(PAD + 61, y0 + 75, "유효한 보증서", 9, 700, "#FFFFFF", "middle"))
    s.gap(14)
    s.raw(txt(PAD, s.y + 12, "진본이 보증하는 내용", 13, 700, IOS["ink"]))
    s.y += 22
    y0 = s.card(184, r=18)
    s.y = y0 + 6
    for k, v in [("보증서 종류", "VideoRegistration…"),
                 ("보증 범위", "BLOCKCHAIN_REG…"),
                 ("영상 디지털 지문", "a1b2c3d4e5…"),
                 ("등록자 DID", "did:omn:abc123…"),
                 ("블록체인 네트워크", "omnione"),
                 ("트랜잭션 해시", "0xabc123…"),
                 ("블록 번호", "12345")]:
        s.kv(k, v, vw=600, font=MONO)
    s.y = y0 + 184
    s.gap(12)
    y0 = s.card(58, IOS["softBlue"], IOS["softBlue"], r=14)
    s.raw(txt(PAD + 14, y0 + 22, "이 보증서는 블록체인 등록 사실과 등록", 9, 400, IOS["sub"]))
    s.raw(txt(PAD + 14, y0 + 36, "주체를 확인했다는 뜻입니다. 영상 내용의", 9, 400, IOS["sub"]))
    s.raw(txt(PAD + 14, y0 + 50, "사실성은 보증하지 않습니다.", 9, 400, IOS["sub"]))
    return s.render()


# ══════════════════════════════════════════════════════════
# 웹 화면 (편집 디자인 스타일)
# ══════════════════════════════════════════════════════════

def web_frame(name, inner, w=880, h=560):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
         f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(name)}">']
    p.append(rect(0, 0, w, h, WEB["paper"]))
    # 브라우저 크롬
    p.append(rect(0, 0, w, 34, "#e7e2d7"))
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        p.append(circle(22 + i * 18, 17, 5.5, c))
    p.append(rect(84, 8, w - 108, 18, WEB["paper"], 5))
    p.append(txt(96, 21, "localhost:8071", 10, 500, WEB["muted"], font=MONO))
    p += inner
    p.append("</svg>")
    return "\n".join(p)


def web_home():
    w, h = 880, 560
    s = []
    # 워터마크
    s.append(f'<text x="{w-40}" y="250" font-family="serif" font-size="300" '
             f'fill="{WEB["ink"]}" opacity="0.035" text-anchor="end">眞</text>')
    # 헤더
    s.append(circle(46, 62, 15, WEB["ink"]))
    s.append(txt(46, 68, "眞", 14, 400, WEB["paper"], "middle", font="serif"))
    s.append(txt(70, 68, "진본", 17, 800, WEB["ink"]))
    s.append(circle(w - 210, 62, 3.5, "#20a976"))
    s.append(txt(w - 200, 66, "블록체인 검증 네트워크 연결됨", 10, 400, WEB["muted"]))
    # 히어로
    s.append(txt(46, 116, "ORIGINALITY, VERIFIED", 9.5, 800, WEB["accent"]))
    s.append(txt(46, 156, "이 영상은", 33, 800, WEB["ink"]))
    s.append(f'<text x="46" y="196" font-family="{FONT}" font-size="33" '
             f'font-weight="800" fill="{WEB["accent"]}" font-style="italic">진짜일까요?</text>')
    s.append(txt(46, 226, "영상을 올리면 원본 해시와 블록체인 기록, 디지털 자격증명을 교차 검증해",
                 11.5, 400, WEB["muted"]))
    s.append(txt(46, 246, "등록된 진본 여부를 확인합니다.", 11.5, 400, WEB["muted"]))
    # 검증 셸 (하드 섀도)
    sx, sy, sw, sh = 46, 274, w - 92, 250
    s.append(rect(sx + 10, sy + 10, sw, sh, WEB["ink"], op=.09))
    s.append(rect(sx, sy, sw, sh, WEB["shell"], stroke=WEB["ink"]))
    # 단계 레일
    s.append(rect(sx, sy, 190, sh, WEB["ink"]))
    steps = [("01", "영상 선택", True), ("02", "무결성 분석", False), ("03", "결과 확인", False)]
    for i, (n, lab, act) in enumerate(steps):
        yy = sy + 44 + i * 72
        bg = WEB["accent"] if act else "none"
        st = WEB["accent"] if act else "rgba(255,255,255,.3)"
        s.append(circle(sx + 30, yy - 4, 9, bg, st))
        s.append(txt(sx + 30, yy, n, 8, 800,
                     WEB["ink"] if act else "rgba(255,255,255,.5)", "middle"))
        s.append(txt(sx + 50, yy + 1, lab, 11.5, 700,
                     "#ffffff" if act else "rgba(255,255,255,.38)"))
        if i < 2:
            s.append(rect(sx + 29, yy + 8, 1, 46, "rgba(255,255,255,.15)"))
    # 드롭존
    dx = sx + 190
    s.append(rect(dx + 26, sy + 26, sw - 190 - 52, 150, "none",
                  stroke="#aaa99f", dash="5 4"))
    cx = dx + (sw - 190) / 2
    s.append(circle(cx, sy + 78, 21, "none", "#aaa99f"))
    s.append(txt(cx, sy + 85, "↑", 18, 400, WEB["ink"], "middle"))
    s.append(txt(cx, sy + 122, "확인할 영상을 올려주세요", 13.5, 800, WEB["ink"], "middle"))
    s.append(txt(cx, sy + 142, "여기로 끌어다 놓거나 눌러서 파일 선택", 10.5, 400, WEB["muted"], "middle"))
    s.append(txt(cx, sy + 163, "MP4 · MOV · AVI · 최대 100MB", 8.5, 400, "#8d918c", "middle", font=MONO))
    # 액션
    s.append(txt(dx + 26, sy + 208, "✓", 10, 700, WEB["green"]))
    s.append(txt(dx + 38, sy + 208, "영상 원본은 서버에 저장되지 않습니다.", 10, 400, WEB["muted"]))
    s.append(rect(sx + sw - 236, sy + 190, 210, 42, WEB["accent"]))
    s.append(txt(sx + sw - 131, sy + 216, "진본 여부 확인하기   →", 12, 800, WEB["ink"], "middle"))
    return web_frame("진본 웹 검증 홈", s)


def web_result():
    w, h = 880, 560
    s = []
    s.append(f'<text x="{w-40}" y="250" font-family="serif" font-size="300" '
             f'fill="{WEB["ink"]}" opacity="0.035" text-anchor="end">眞</text>')
    s.append(circle(46, 62, 15, WEB["ink"]))
    s.append(txt(46, 68, "眞", 14, 400, WEB["paper"], "middle", font="serif"))
    s.append(txt(70, 68, "진본", 17, 800, WEB["ink"]))
    s.append(txt(46, 108, "ORIGINALITY, VERIFIED", 9.5, 800, WEB["accent"]))

    sx, sy, sw, sh = 46, 130, w - 92, 384
    s.append(rect(sx + 10, sy + 10, sw, sh, WEB["ink"], op=.09))
    s.append(rect(sx, sy, sw, sh, WEB["shell"], stroke=WEB["ink"]))
    s.append(rect(sx, sy, 190, sh, WEB["ink"]))
    for i, (n, lab) in enumerate([("01", "영상 선택"), ("02", "무결성 분석"), ("03", "결과 확인")]):
        yy = sy + 52 + i * 76
        done = i < 2
        s.append(circle(sx + 30, yy - 4, 9, WEB["accent"], WEB["accent"]))
        s.append(txt(sx + 30, yy, n, 8, 800, WEB["ink"], "middle"))
        s.append(txt(sx + 50, yy + 1, lab, 11.5, 700,
                     "rgba(255,255,255,.7)" if done else "#ffffff"))
        if i < 2:
            s.append(rect(sx + 29, yy + 8, 1, 50, WEB["accent"]))

    dx = sx + 214
    s.append(circle(dx + 26, sy + 54, 26, WEB["green"]))
    s.append(txt(dx + 26, sy + 63, "✓", 24, 700, WEB["paper"], "middle"))
    s.append(txt(dx + 68, sy + 40, "VERIFICATION COMPLETE", 8.5, 800, WEB["accent"]))
    s.append(txt(dx + 68, sy + 66, "진본으로 확인됐습니다", 22, 800, WEB["ink"]))
    s.append(txt(dx + 68, sy + 88, "등록된 원본 파일과 정확히 일치합니다.", 11, 400, WEB["muted"]))

    grid = [("블록체인 기록", "검증 완료", WEB["green"]),
            ("디지털 자격증명", "VC 유효", WEB["green"]),
            ("등록 상태", "활성", WEB["green"]),
            ("등록 시각", "2026년 9월 5일 오후 2:30", WEB["ink"])]
    for i, (k, v, c) in enumerate(grid):
        gx = dx + (i % 2) * 230
        gy = sy + 126 + (i // 2) * 62
        s.append(rect(gx, gy, 210, 48, WEB["paper"], stroke=WEB["line"]))
        s.append(txt(gx + 14, gy + 19, k, 9, 500, WEB["muted"]))
        s.append(txt(gx + 14, gy + 36, v, 11.5, 800, c))
    s.append(rect(dx, sy + 252, 440, 34, WEB["paper"], stroke=WEB["line"]))
    s.append(txt(dx + 14, sy + 273, "발급자 DID", 9, 500, WEB["muted"]))
    s.append(txt(dx + 90, sy + 273, "did:omn:abc123def…9f2a", 10, 500, WEB["ink"], font=MONO))
    s.append(rect(dx, sy + 302, 200, 40, "none", stroke=WEB["ink"]))
    s.append(txt(dx + 100, sy + 327, "다른 영상 확인하기", 11.5, 700, WEB["ink"], "middle"))
    return web_frame("진본 웹 검증 결과", s)


# ══════════════════════════════════════════════════════════
# Chrome 확장
# ══════════════════════════════════════════════════════════

def ext_panel():
    w, h = 700, 460
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
         f'viewBox="0 0 {w} {h}" role="img" aria-label="진본 확장 결과 패널">']
    p.append(rect(0, 0, w, h, "#0f0f0f"))
    p.append(rect(0, 0, w, 30, "#212121"))
    p.append(txt(16, 20, "▶  YouTube", 11, 700, "#ffffff"))
    p.append(rect(20, 46, w - 300, 250, "#000000", 6))
    p.append(txt((w - 300) / 2 + 20, 178, "▶", 40, 400, "#ffffff", "middle", op=.25))
    p.append(txt(20, 322, "2026 기자회견 전체 영상", 15, 700, "#ffffff"))
    p.append(txt(20, 344, "조회수 12만회 · 2일 전", 10, 400, "#aaaaaa"))

    # 패널
    px, py, pw = w - 262, 60, 242
    p.append(rect(px, py, pw, 232, "#ffffff", 12))
    p.append(rect(px, py, pw, 44, IOS["success"], 12, op=.1))
    p.append(circle(px + 24, py + 22, 9, IOS["success"]))
    p.append(txt(px + 24, py + 26, "✓", 9, 700, "#ffffff", "middle"))
    p.append(txt(px + 40, py + 26, "진본으로 확인됨", 12.5, 700, IOS["ink"]))
    p.append(txt(px + pw - 16, py + 27, "×", 14, 400, IOS["sub"], "end"))
    p.append(txt(px + 16, py + 64, "등록된 원본 파일과 정확히", 10, 400, IOS["sub"]))
    p.append(txt(px + 16, py + 79, "일치합니다.", 10, 400, IOS["sub"]))
    rows = [("판정", "Exact Match"), ("영상 ID", "1"),
            ("등록 시각", "2026-09-05"), ("블록체인", "검증됨"), ("VC", "검증됨")]
    for i, (k, v) in enumerate(rows):
        yy = py + 100 + i * 22
        p.append(txt(px + 16, yy + 12, k, 9.5, 500, IOS["sub"]))
        p.append(txt(px + pw - 16, yy + 12, v, 9.5, 700, IOS["ink"], "end"))
        if i < len(rows) - 1:
            p.append(rect(px + 16, yy + 19, pw - 32, 1, IOS["divider"]))

    # 플로팅 버튼
    bx, by = w - 176, h - 66
    p.append(rect(bx + 3, by + 3, 150, 44, "#000000", 22, op=.3))
    p.append(rect(bx, by, 150, 44, IOS["primary"], 22))
    p.append(circle(bx + 24, by + 22, 11, "#ffffff", None))
    p.append(txt(bx + 24, by + 27, "J", 12, 800, IOS["primary"], "middle"))
    p.append(txt(bx + 44, by + 27, "진본 확인", 12.5, 700, "#ffffff"))
    p.append("</svg>")
    return "\n".join(p)


if __name__ == "__main__":
    print("생성 중…")
    write("ios-01-welcome.svg", ios_welcome())
    write("ios-02-home.svg", ios_home())
    write("ios-03-video-list.svg", ios_list())
    write("ios-04-upload.svg", ios_upload())
    write("ios-05-complete.svg", ios_complete())
    write("ios-06-vc-offer.svg", ios_offer())
    write("ios-07-verify-result.svg", ios_verify())
    write("ios-08-certificate.svg", ios_certificate())
    write("web-01-home.svg", web_home())
    write("web-02-result.svg", web_result())
    write("ext-01-panel.svg", ext_panel())
    print("완료")

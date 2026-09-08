import { defineConfig } from "vitepress";
import markdownItMermaid from "./markdown-mermaid";

export default defineConfig({
  title: "진본 개발자 센터",
  description: "블록체인 기반 영상 진위 검증 서비스 · 기술 문서",
  lang: "ko-KR",
  lastUpdated: true,
  cleanUrls: true,

  head: [
    ["link", { rel: "icon", type: "image/png", href: "/favicon.png" }],
  ],

  markdown: {
    config(md) {
      markdownItMermaid(md);
    },
  },

  themeConfig: {
    logo: "/logo.png",
    siteTitle: "진본 Developers",

    nav: [
      { text: "홈", link: "/" },
      { text: "아키텍처", link: "/architecture/overview" },
      { text: "API", link: "/api/conventions" },
      { text: "플로우", link: "/flows/video-register" },
    ],

    sidebar: [
      {
        text: "시작하기",
        items: [
          { text: "서비스 소개", link: "/guide/introduction" },
          { text: "핵심 개념", link: "/guide/concepts" },
        ],
      },
      {
        text: "아키텍처",
        items: [
          { text: "시스템 구성", link: "/architecture/overview" },
          { text: "저장소 구조", link: "/architecture/repositories" },
        ],
      },
      {
        text: "API 레퍼런스",
        items: [
          { text: "공통 규약", link: "/api/conventions" },
          { text: "인증 API", link: "/api/auth" },
          { text: "회원가입 API", link: "/api/signup" },
          { text: "영상 관리 API", link: "/api/videos" },
          { text: "검증 API", link: "/api/verify" },
          { text: "에러 코드", link: "/api/errors" },
        ],
      },
      {
        text: "플로우",
        items: [
          { text: "영상 등록", link: "/flows/video-register" },
          { text: "영상 검증", link: "/flows/video-verify" },
          { text: "회원가입 / 로그인", link: "/flows/signup-login" },
          { text: "VC 보증서 발급", link: "/flows/vc-issuance" },
        ],
      },
      {
        text: "데이터",
        items: [
          { text: "데이터 모델", link: "/data/model" },
          { text: "스마트 컨트랙트", link: "/data/smart-contract" },
        ],
      },
      {
        text: "보안",
        items: [{ text: "보안 및 개인정보", link: "/security/overview" }],
      },
    ],

    outline: {
      level: [2, 3],
      label: "목차",
    },

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com",
      },
    ],

    search: {
      provider: "local",
      options: {
        translations: {
          button: { buttonText: "검색", buttonAriaLabel: "검색" },
          modal: {
            noResultsText: "결과 없음",
            resetButtonTitle: "초기화",
            footer: {
              selectText: "선택",
              navigateText: "이동",
              closeText: "닫기",
            },
          },
        },
      },
    },

    footer: {
      message: "블록체인 기반 영상 진위 검증 서비스",
      copyright: "진본 (JinBon)",
    },

    docFooter: {
      prev: "이전",
      next: "다음",
    },

    lastUpdated: {
      text: "마지막 수정",
    },
  },
});

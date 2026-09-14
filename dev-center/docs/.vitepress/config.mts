import { defineConfig } from "vitepress";
import markdownItMermaid from "./markdown-mermaid";

export default defineConfig({
  title: "진본",
  description: "블록체인 기반 영상 진위 검증 서비스",
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
    siteTitle: "진본",

    nav: [
      { text: "홈", link: "/" },
      { text: "사용 사례", link: "/use-cases" },
      { text: "개발자 센터", link: "/developers/guide/introduction" },
      { text: "시작하기", link: "/downloads" },
    ],

    sidebar: {
      "/developers/": [
        {
          text: "시작하기",
          items: [
            { text: "서비스 소개", link: "/developers/guide/introduction" },
            { text: "핵심 개념", link: "/developers/guide/concepts" },
          ],
        },
        {
          text: "아키텍처",
          items: [
            { text: "시스템 구성", link: "/developers/architecture/overview" },
            { text: "저장소 구조", link: "/developers/architecture/repositories" },
            { text: "백엔드", link: "/developers/architecture/component-backend" },
            { text: "iOS 앱", link: "/developers/architecture/component-ios" },
            { text: "웹", link: "/developers/architecture/component-web" },
            { text: "Chrome 확장", link: "/developers/architecture/component-extension" },
            { text: "외부 연동", link: "/developers/architecture/integrations" },
          ],
        },
        {
          text: "API 레퍼런스",
          items: [
            { text: "공통 규약", link: "/developers/api/conventions" },
            { text: "인증 API", link: "/developers/api/auth" },
            { text: "회원가입 API", link: "/developers/api/signup" },
            { text: "영상 관리 API", link: "/developers/api/videos" },
            { text: "검증 API", link: "/developers/api/verify" },
            { text: "에러 코드", link: "/developers/api/errors" },
          ],
        },
        {
          text: "플로우",
          items: [
            { text: "영상 등록", link: "/developers/flows/video-register" },
            { text: "영상 검증", link: "/developers/flows/video-verify" },
            { text: "회원가입 / 로그인", link: "/developers/flows/signup-login" },
            { text: "VC 보증서 발급", link: "/developers/flows/vc-issuance" },
          ],
        },
        {
          text: "데이터",
          items: [
            { text: "데이터 모델", link: "/developers/data/model" },
            { text: "스마트 컨트랙트", link: "/developers/data/smart-contract" },
          ],
        },
        {
          text: "보안",
          items: [
            { text: "보안 및 개인정보", link: "/developers/security/overview" },
          ],
        },
      ],
    },

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

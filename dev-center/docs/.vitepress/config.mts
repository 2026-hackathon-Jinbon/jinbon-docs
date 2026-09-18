import { defineConfig } from "vitepress";
import markdownItMermaid from "./markdown-mermaid";

// 카카오톡·슬랙 공유 카드와 canonical/OG 절대 URL의 기준입니다.
const SITE_URL = "https://jinbon-docs.vercel.app";
const OG_IMAGE = `${SITE_URL}/logo-full.png`;

export default defineConfig({
  title: "진본",
  description: "공유하기 전, 영상의 출처를 확인하세요. 진본에서 등록자와 등록 영상의 일치 여부를 확인합니다.",
  lang: "ko-KR",
  lastUpdated: true,
  cleanUrls: true,

  sitemap: { hostname: SITE_URL },

  head: [
    ["link", { rel: "icon", type: "image/png", href: "/favicon.png" }],
    // 페이지별로 안 바뀌는 값만 여기 둡니다.
    // title/description/url은 transformPageData에서 페이지마다 채웁니다.
    ["meta", { property: "og:type", content: "website" }],
    ["meta", { property: "og:site_name", content: "진본" }],
    ["meta", { property: "og:locale", content: "ko_KR" }],
    ["meta", { property: "og:image", content: OG_IMAGE }],
    ["meta", { property: "og:image:width", content: "1024" }],
    ["meta", { property: "og:image:height", content: "1024" }],
    ["meta", { property: "og:image:alt", content: "진본 로고" }],
    ["meta", { name: "twitter:card", content: "summary" }],
    ["meta", { name: "twitter:image", content: OG_IMAGE }],
  ],

  // 검증 채널 중 하나가 카카오톡이라, 공유 시 제목·설명·썸네일이 뜨는 게 중요합니다.
  // frontmatter의 title/description을 페이지별 OG 태그와 canonical로 옮깁니다.
  transformPageData(pageData) {
    const fm = pageData.frontmatter;
    // 개발자 문서는 frontmatter title 없이 H1만 쓰는데, VitePress가 그 H1을
    // pageData.title로 넣어줍니다. 이걸 안 보면 모든 문서가 홈 제목을 공유합니다.
    const pageTitle = fm.title ?? pageData.title;
    const title = pageTitle
      ? fm.titleTemplate === false
        ? pageTitle
        : `${pageTitle} | 진본`
      : "진본 - 공유하기 전, 영상의 출처를 확인하세요.";
    const description =
      fm.description ?? "공유하기 전, 영상의 출처를 확인하세요. 진본에서 등록자와 등록 영상의 일치 여부를 확인합니다.";

    // index.md -> "", developers/guide/introduction.md -> "developers/guide/introduction"
    const slug = pageData.relativePath
      .replace(/(?:index)?\.md$/, "")
      .replace(/\/$/, "");
    const url = slug ? `${SITE_URL}/${slug}` : SITE_URL;

    pageData.frontmatter.head ??= [];
    pageData.frontmatter.head.push(
      ["link", { rel: "canonical", href: url }],
      ["meta", { property: "og:title", content: title }],
      ["meta", { property: "og:description", content: description }],
      ["meta", { property: "og:url", content: url }],
      ["meta", { name: "twitter:title", content: title }],
      ["meta", { name: "twitter:description", content: description }],
    );
  },

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
      { text: "검증 상태", link: "/verification-status" },
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
            { text: "등록자 프로필 API", link: "/developers/api/members" },
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
        {
          text: "운영",
          items: [
            { text: "배포 가이드 (AWS EC2)", link: "/developers/operations/deployment" },
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
        link: "https://github.com/2026-hackathon-Jinbon",
        ariaLabel: "진본 GitHub 조직",
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
      message: "공유하기 전, 영상의 출처를 확인하세요.",
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

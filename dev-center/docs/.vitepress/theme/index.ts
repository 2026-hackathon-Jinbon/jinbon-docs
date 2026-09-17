import DefaultTheme from "vitepress/theme";
import Mermaid from "./Mermaid.vue";
import HomePage from "./HomePage.vue";
import UseCases from "./UseCases.vue";
import Downloads from "./Downloads.vue";
import VerificationStatus from "./VerificationStatus.vue";
import type { Theme } from "vitepress";
import "./custom.css";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("Mermaid", Mermaid);
    app.component("HomePage", HomePage);
    app.component("UseCases", UseCases);
    app.component("Downloads", Downloads);
    app.component("VerificationStatus", VerificationStatus);
  },
} satisfies Theme;

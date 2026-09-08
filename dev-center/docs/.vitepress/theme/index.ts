import DefaultTheme from "vitepress/theme";
import Mermaid from "./Mermaid.vue";
import HomePage from "./HomePage.vue";
import type { Theme } from "vitepress";
import "./custom.css";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("Mermaid", Mermaid);
    app.component("HomePage", HomePage);
  },
} satisfies Theme;

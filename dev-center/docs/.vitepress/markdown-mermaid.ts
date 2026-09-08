import type MarkdownIt from "markdown-it";

/**
 * markdown-it plugin that converts ```mermaid code blocks
 * into <Mermaid :code="..." /> Vue components.
 */
export default function markdownItMermaid(md: MarkdownIt) {
  const fence = md.renderer.rules.fence!.bind(md.renderer.rules);

  md.renderer.rules.fence = (tokens, idx, options, env, self) => {
    const token = tokens[idx];
    if (token.info.trim() === "mermaid") {
      const encoded = encodeURIComponent(token.content);
      return `<Mermaid code="${encoded}" />`;
    }
    return fence(tokens, idx, options, env, self);
  };
}

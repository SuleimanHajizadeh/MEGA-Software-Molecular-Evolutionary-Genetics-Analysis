# LLM Wiki Schema & Operational Guidelines

This document defines the rules, directory structure, page templates, and workflows for the persistent LLM-maintained Wiki.

---

## 1. Architecture & Directories

- `raw/`: **Immutable Source of Truth.** Articles, papers, PDFs, notes, transcripts, and web clippings. The LLM reads from here but never alters original files.
  - `raw/assets/`: Downloaded images and media referenced in raw source documents.
- `wiki/`: **LLM-Maintained Knowledge Graph.** Structured, interlinked markdown pages formatted for Obsidian.
  - `wiki/index.md`: Catalog of all wiki pages grouped by category with one-line descriptions.
  - `wiki/log.md`: Append-only chronological log of all wiki operations (ingest, query, lint).
  - `wiki/sources/`: Distilled summaries, key findings, and citations of ingested raw sources.
  - `wiki/entities/`: Core entities (genes, species, tools, software, institutions, authors).
  - `wiki/concepts/`: Theories, biological mechanisms, phylogenetic models, algorithms, methods.
  - `wiki/synthesis/`: Cross-cutting comparative analyses, evolving theses, and query answers filed back into the wiki.

---

## 2. Page Conventions & Obsidian Linking

1. **Wikilinks**: Use standard Obsidian `[[Page Name]]` or `[[Page Name|Custom Label]]` format for all internal references.
2. **YAML Frontmatter**: Every wiki page must begin with YAML frontmatter:
   ```yaml
   ---
   title: Page Title
   type: entity | concept | source | synthesis
   tags: [relevant, tags]
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   sources: ["[[Source Name]]"]
   ---
   ```
3. **No Dead Links / Dangling References**: When linking to a page that does not exist yet, determine if a stub page should be created or if it should be tracked during the next lint pass.
4. **Citations**: Back claims with links to `[[Source Name]]` or raw files.

---

## 3. Operational Workflows

### 📥 Ingest Flow
When a new source is added to `raw/` or requested by the user:
1. **Read & Extract**: Inspect raw document content thoroughly.
2. **Create Source Note**: In `wiki/sources/<source_slug>.md`, write:
   - Metadata, context, executive summary.
   - Core takeaways and key findings.
   - Quotes or data points with specific citations.
   - Links to affected/related concepts & entities.
3. **Update / Create Graph Nodes**:
   - Touch `wiki/entities/` and `wiki/concepts/` relevant to this source.
   - Integrate new evidence, note any contradictions or corroborations with existing knowledge.
4. **Update `wiki/index.md`**: Add new pages to appropriate category tables/lists with one-line summaries.
5. **Append to `wiki/log.md`**: Log using the format:
   ```markdown
   ## [YYYY-MM-DD] ingest | <Source Title>
   - **Source**: `raw/<filename>`
   - **Created**: [[<Page 1>]], [[<Page 2>]]
   - **Updated**: [[<Page 3>]], [[<Page 4>]]
   - **Summary**: Brief description of what was incorporated.
   ```

---

### 🔍 Query & Synthesis Flow
When the user asks questions or requests deep analysis:
1. **Traverse the Wiki**: Check `wiki/index.md` first, read relevant concept/entity/source pages.
2. **Synthesize**: Deliver a comprehensive answer with citations to internal wiki nodes and raw sources.
3. **Compound Knowledge**: If the query produces a novel synthesis, comparison table, or thesis, file it as a new page in `wiki/synthesis/<topic_slug>.md`, link it in `wiki/index.md`, and log it in `wiki/log.md`.

---

### 🧹 Lint & Health Check Flow
Periodically audit the wiki for:
- **Contradictions & Inconsistencies**: Conflicting data points across different sources.
- **Orphan Pages**: Pages with zero incoming links.
- **Missing Hubs**: Frequently mentioned topics that lack a dedicated page.
- **Outdated Syntheses**: Concept pages needing updates after recent ingests.
- **Research Gaps**: Highlighting suggested questions or missing source documents to find next.

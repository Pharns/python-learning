#!/usr/bin/env bash
set -euo pipefail

# ==== CONFIG: EDIT THESE PATHS ====
LEARNING_ROOT="${LEARNING_ROOT:-$HOME/Dev/python-learning}"
PORTFOLIO_ROOT="${PORTFOLIO_ROOT:-$HOME/Dev/portfolio}"

SRC_NOTES_DIR="$LEARNING_ROOT/Python/100 Days"
SRC_IMG_GLOB="day???-*.*"     # images named like day001-screenshot.png

DST_NOTES_DIR="$PORTFOLIO_ROOT/docs/python/100-days"
DST_IMG_DIR="$PORTFOLIO_ROOT/docs/assets/images/100-days"

# Days to publish (space-separated). Example: "001 002 010"
DAYS="${DAYS:-}"

if [[ -z "${DAYS}" ]]; then
  echo "Usage: DAYS=\"001 002\" ./sync_100days.sh"
  exit 1
fi

mkdir -p "$DST_NOTES_DIR" "$DST_IMG_DIR"

normalize_filename() {
  # "Day 001.md" -> "day001.md"
  local in="$1"
  local daynum
  daynum=$(echo "$in" | grep -Eo '[0-9]{3}')
  echo "day${daynum}.md"
}

for d in $DAYS; do
  src_note="$SRC_NOTES_DIR/Day ${d}.md"
  if [[ ! -f "$src_note" ]]; then
    echo "WARN: Note not found: $src_note (skipping)"
    continue
  fi

  out_note="$(normalize_filename "$(basename "$src_note")")"
  tmp_note="$(mktemp)"

  # --- Convert Obsidian bits to MkDocs-friendly Markdown ---
  # 1) Convert Obsidian embeds ![[file.png]] -> standard images referencing portfolio path
  #    We’ll place images under docs/assets/images/100-days/
  sed -E \
    's/!\[\[\s*([^[\]]+)\s*\]\]/!\[\]\(\/assets\/images\/100-days\/\1\)/g' \
    "$src_note" > "$tmp_note"

  # 2) Strip Obsidian-only Dataview code fences (optional; keep if you want)
  #    Remove ```dataview...``` blocks entirely:
  awk '
    BEGIN{skip=0}
    /```dataview/ {skip=1; next}
    /```/ && skip==1 {skip=0; next}
    skip==0 {print}
  ' "$tmp_note" > "$DST_NOTES_DIR/$out_note"

  rm -f "$tmp_note"

  # --- Copy images for this day if present ---
  # Match files starting with dayXYZ-
  shopt -s nullglob
  day_prefix="day${d}-"
  imgs=( "$SRC_NOTES_DIR"/$day_prefix* )
  if (( ${#imgs[@]} > 0 )); then
    cp -v "${imgs[@]}" "$DST_IMG_DIR/"
  fi
  shopt -u nullglob

  echo "✅ Published Day $d -> $DST_NOTES_DIR/$out_note"
done

# Optional: quick MkDocs link check (local build without deploying)
if command -v mkdocs >/dev/null 2>&1; then
  echo "🔍 Building MkDocs locally (link check)…"
  (cd "$PORTFOLIO_ROOT" && mkdocs build --strict)
  echo "✅ MkDocs build passed."
else
  echo "ℹ️ mkdocs not found — skipping local build check."
fi

echo "Done."

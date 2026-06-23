"""
Extract text and clean embedded figures from a paper PDF.
Usage: python extract_paper.py <pdf_path> <output_dir>
"""
import fitz, os, sys, json

def extract_paper(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)

    # --- Extract text ---
    text_lines = []
    text_lines.append(f"Pages: {doc.page_count}")
    meta = doc.metadata
    text_lines.append(f"Title: {meta.get('title', 'Unknown')}")
    text_lines.append(f"Subject: {meta.get('subject', '')}")
    text_lines.append("=" * 80)

    for i in range(doc.page_count):
        page_text = doc[i].get_text()
        text_lines.append(f"\n--- PAGE {i + 1} ---")
        text_lines.append(page_text)

    text_path = os.path.join(output_dir, "paper_text.txt")
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_lines))
    print(f"Text saved: {text_path}")

    # --- Extract clean embedded figures ---
    fig_dir = os.path.join(output_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)

    extracted = []
    for page_idx in range(doc.page_count):
        page = doc[page_idx]
        images = page.get_images(full=True)

        for img in images:
            xref = img[0]
            base = doc.extract_image(xref)
            w, h = base["width"], base["height"]

            # Skip tiny images and journal logos (~32KB narrow banners)
            if len(base["image"]) < 100_000:
                continue

            ext = base["ext"]
            fname = f"page{page_idx + 1:02d}_fig{len(extracted) + 1:02d}.{ext}"
            fpath = os.path.join(fig_dir, fname)
            with open(fpath, 'wb') as f:
                f.write(base["image"])

            # Find position on page for labeling
            blocks = page.get_text("dict")["blocks"]
            bbox = None
            for blk in blocks:
                if blk["type"] == 1:  # image block
                    bb = blk["bbox"]
                    bw, bh = bb[2] - bb[0], bb[3] - bb[1]
                    if bw > 100 and bh > 100:
                        bbox = bb
                        break

            extracted.append({
                "filename": fname,
                "path": fpath,
                "page": page_idx + 1,
                "width": w,
                "height": h,
                "size_bytes": len(base["image"]),
                "format": ext,
                "bbox": bbox
            })
            print(f"Figure: {fname} ({w}x{h}, {len(base['image']) // 1024}KB)")

    doc.close()

    # Save manifest
    manifest_path = os.path.join(fig_dir, "manifest.json")
    with open(manifest_path, 'w') as f:
        json.dump(extracted, f, indent=2, default=str)

    print(f"\nExtracted {len(extracted)} figures to {fig_dir}")
    print(f"Manifest: {manifest_path}")
    return text_path, extracted


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_paper.py <pdf_path> <output_dir>")
        sys.exit(1)
    extract_paper(sys.argv[1], sys.argv[2])

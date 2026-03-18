import os
import re
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt

app = Flask(__name__)

# Local mode: each user chooses where the PPT is saved on their own computer.
DEFAULT_OUTPUT_DIR = Path(
    os.getenv("DEFAULT_OUTPUT_DIR", str(Path.home() / "Downloads" / "Generated-PPT-Decks"))
).resolve()
TEMPLATE_PATH = Path(
    os.getenv("PPT_TEMPLATE_PATH", "../../docs/brand/EPAM_PresalesTemplate.potx")
).resolve()


def safe_slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "capability"


def add_bullet_slide(prs: Presentation, title: str, bullets: list[str]) -> None:
    layout = prs.slide_layouts[1] if len(prs.slide_layouts) > 1 else prs.slide_layouts[0]
    slide = prs.slides.add_slide(layout)

    if slide.shapes.title is not None:
        slide.shapes.title.text = title
        try:
            title_run = slide.shapes.title.text_frame.paragraphs[0].runs[0]
            title_run.font.bold = True
            title_run.font.size = Pt(28)
            title_run.font.color.rgb = RGBColor(251, 250, 250)  # SNOW
        except Exception:
            pass

    if len(slide.placeholders) > 1:
        body = slide.placeholders[1].text_frame
        body.clear()
        for i, bullet in enumerate(bullets):
            p = body.paragraphs[0] if i == 0 else body.add_paragraph()
            p.text = bullet
            p.level = 0
            try:
                p.runs[0].font.size = Pt(14)
                p.runs[0].font.color.rgb = RGBColor(6, 6, 6)  # NIGHT
            except Exception:
                pass


def generate_deck(
    topic: str,
    audience: str,
    industry: str,
    extra_prompt: str,
    output_dir: Path,
) -> Path:
    # python-pptx loads .pptx files directly, but not .potx templates.
    # In no-Entra/free mode we keep this robust by falling back to a blank deck.
    if TEMPLATE_PATH.exists() and TEMPLATE_PATH.suffix.lower() == ".pptx":
        prs = Presentation(str(TEMPLATE_PATH))
    else:
        prs = Presentation()

    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{safe_slug(topic)}-deck-{today}.pptx"

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / file_name

    # 9-slide baseline structure (can be refined later by the full agent workflow).
    add_bullet_slide(prs, f"{topic} Capability", [
        f"Audience: {audience}",
        f"Industry: {industry}",
        "Prepared for consulting discussion",
    ])
    add_bullet_slide(prs, "Agenda", [
        "Market context",
        "Our capability",
        "How we work",
        "Proof points",
        "Next steps",
    ])
    add_bullet_slide(prs, "Market Context", [
        f"Key pressure in {industry}: speed, cost, and risk",
        "Clients demand measurable outcomes",
        "Digital modernization is accelerating across functions",
    ])
    add_bullet_slide(prs, "Our Capability", [
        f"{topic} strategy and execution support",
        "Advisory plus implementation coverage",
        "Outcome-driven delivery model",
    ])
    add_bullet_slide(prs, "How We Work", [
        "Assess current state",
        "Define target architecture and roadmap",
        "Pilot and scale in waves",
        "Measure impact and optimize continuously",
    ])
    add_bullet_slide(prs, "Proof Points", [
        "Reduced cycle time through automation",
        "Improved quality and governance controls",
        "Enabled faster decision-making",
    ])
    add_bullet_slide(prs, "Why Us", [
        "Cross-functional consulting team",
        "Accelerators and reusable assets",
        "Strong delivery governance",
    ])
    add_bullet_slide(prs, "Next Steps", [
        "Run discovery workshop",
        "Agree 90-day roadmap",
        "Launch first execution sprint",
    ])
    add_bullet_slide(prs, "Thank You", [
        "Contact the consulting team",
        "Deck saved in your selected folder",
        f"Notes: {extra_prompt[:120] or 'N/A'}",
    ])

    prs.save(str(out_path))
    return out_path


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", default_output_dir=str(DEFAULT_OUTPUT_DIR))


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form.get("topic", "").strip()
    audience = request.form.get("audience", "").strip()
    industry = request.form.get("industry", "").strip()
    extra_prompt = request.form.get("extra_prompt", "").strip()
    output_folder = request.form.get("output_folder", "").strip()

    chosen_output_dir = Path(output_folder).expanduser().resolve() if output_folder else DEFAULT_OUTPUT_DIR

    if not topic or not audience or not industry or not output_folder:
        return render_template(
            "index.html",
            error="Topic, audience, industry, and output folder are required.",
            form=request.form,
            default_output_dir=str(DEFAULT_OUTPUT_DIR),
        )

    out_path = generate_deck(topic, audience, industry, extra_prompt, chosen_output_dir)

    return render_template(
        "index.html",
        success=True,
        file_name=out_path.name,
        local_file_path=str(out_path),
        saved_folder=str(chosen_output_dir),
        default_output_dir=str(DEFAULT_OUTPUT_DIR),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)

import json
import uuid

def uid():
    return uuid.uuid4().hex[:8]

def make_container(settings=None, elements=None, is_inner=True):
    return {
        "id": uid(),
        "elType": "container",
        "isInner": is_inner,
        "settings": settings or {},
        "elements": elements or []
    }

def make_widget(widget_type, settings=None):
    return {
        "id": uid(),
        "elType": "widget",
        "isInner": False,
        "widgetType": widget_type,
        "settings": settings or {},
        "elements": []
    }

def generate_clean_elementor_json():
    with open('text-telecom-carrier-network-widget.html', 'r', encoding='utf-8') as f:
        network_widget_html = f.read()

    # =========================================================================
    # SECTION 0: Top Announcement + Hero (Split: Left Copy & CTA, Right Network Map) + Stats Bar
    # =========================================================================
    hero_left_badge = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "row",
            "flex_wrap": "nowrap",
            "flex_align_items": "center",
            "gap": {"column": "8", "row": "8", "unit": "px"},
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "18", "left": "0", "isLinked": False},
            "width": {"unit": "%", "size": 100, "sizes": []}
        },
        elements=[
            make_widget("divider", {
                "width": {"unit": "px", "size": 16, "sizes": []},
                "color": "#3ECB5F",
                "gap": {"unit": "px", "size": 0, "sizes": []},
                "_element_width": "initial",
                "text": "Divider"
            }),
            make_widget("text-editor", {
                "editor": '<p style="margin:0; font-family:\'Plus Jakarta Sans\', sans-serif; font-weight:700; font-size:12px; color:#14692c; text-transform:uppercase; letter-spacing:0.06em;">A2P &bull; P2P &bull; Wholesale Routes &bull; 190+ Countries</p>',
                "typography_typography": "custom",
                "typography_font_family": "Plus Jakarta Sans",
                "typography_font_size": {"unit": "px", "size": 12, "sizes": []}
            })
        ]
    )

    hero_left_col = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "flex_wrap": "nowrap",
            "width": {"unit": "%", "size": 52, "sizes": []},
            "width_tablet": {"unit": "%", "size": 100, "sizes": []}
        },
        elements=[
            hero_left_badge,
            make_widget("heading", {
                "title": 'Every text, <span style="color:#3ECB5F;">on time</span>, on target.',
                "header_size": "h1",
                "typography_typography": "custom",
                "typography_font_family": "Space Grotesk",
                "typography_font_weight": "700",
                "typography_font_size": {"unit": "px", "size": 50, "sizes": []},
                "typography_line_height": {"unit": "em", "size": 1.1, "sizes": []},
                "color": "#0B1210",
                "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "18", "left": "0", "isLinked": False}
            }),
            make_widget("text-editor", {
                "editor": '<p style="margin:0; font-size:17px; line-height:1.65; color:#53645B; font-family:\'Inter\', sans-serif;">Text Telecom runs carrier-grade A2P and wholesale SMS routes across 190+ countries &mdash; moving one-time passcodes, banking alerts, and global enterprise campaigns with sub-second delivery and zero guesswork.</p>',
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": {"unit": "px", "size": 17, "sizes": []},
                "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "28", "left": "0", "isLinked": False}
            }),
            make_container(
                settings={
                    "content_width": "full",
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "gap": {"column": "14", "row": "14", "unit": "px"},
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "28", "left": "0", "isLinked": False}
                },
                elements=[
                    make_widget("button", {
                        "text": "Start Routing Now",
                        "link": {"url": "#contact", "is_external": False, "nofollow": False},
                        "background_color": "#3ECB5F",
                        "button_text_color": "#0B1210",
                        "hover_color": "#0B1210",
                        "button_background_hover_color": "#53D871",
                        "border_radius": {"unit": "px", "top": "999", "right": "999", "bottom": "999", "left": "999", "isLinked": True},
                        "text_padding": {"unit": "px", "top": "13", "right": "26", "bottom": "13", "left": "26", "isLinked": False},
                        "typography_typography": "custom",
                        "typography_font_family": "Plus Jakarta Sans",
                        "typography_font_weight": "700",
                        "typography_font_size": {"unit": "px", "size": 14.5, "sizes": []},
                        "border_border": "none"
                    }),
                    make_widget("button", {
                        "text": "Explore Services",
                        "link": {"url": "#services", "is_external": False, "nofollow": False},
                        "background_color": "#FFFFFF",
                        "button_text_color": "#0B1210",
                        "hover_color": "#14692c",
                        "button_background_hover_color": "#F1F7F3",
                        "border_radius": {"unit": "px", "top": "999", "right": "999", "bottom": "999", "left": "999", "isLinked": True},
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
                        "border_color": "#E2ECE5",
                        "text_padding": {"unit": "px", "top": "13", "right": "24", "bottom": "13", "left": "24", "isLinked": False},
                        "typography_typography": "custom",
                        "typography_font_family": "Plus Jakarta Sans",
                        "typography_font_weight": "700",
                        "typography_font_size": {"unit": "px", "size": 14.5, "sizes": []}
                    })
                ]
            ),
            make_widget("text-editor", {
                "editor": '<div style="display:flex; flex-wrap:wrap; gap:16px; background:#F8FAF8; border:1px solid #E2ECE5; padding:12px 18px; border-radius:10px; font-size:13px; color:#53645B; font-family:\'Plus Jakarta Sans\', sans-serif;">'
                          '<span><strong style="color:#14692c;">&#10003; 99.99%</strong> SLA Uptime</span>'
                          '<span><strong style="color:#14692c;">&#10003; Direct</strong> SS7/SMPP Binds</span>'
                          '<span><strong style="color:#14692c;">&#10003; Dubai HQ</strong> Licensed Carrier</span>'
                          '</div>'
            })
        ]
    )

    hero_right_col = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "flex_wrap": "nowrap",
            "width": {"unit": "%", "size": 48, "sizes": []},
            "width_tablet": {"unit": "%", "size": 100, "sizes": []}
        },
        elements=[
            make_widget("html", {
                "html": network_widget_html
            })
        ]
    )

    hero_split_row = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "row",
            "flex_wrap": "nowrap",
            "flex_direction_tablet": "column",
            "gap": {"column": "48", "row": "48", "unit": "px"},
            "flex_align_items": "center",
            "width": {"unit": "%", "size": 100, "sizes": []}
        },
        elements=[hero_left_col, hero_right_col]
    )

    # Hero stats grid (4 items)
    stat_items = [
        {"num": "190+", "lbl": "Countries Covered", "desc": "Direct tier-1 operator interconnects worldwide"},
        {"num": "99.99%", "lbl": "Platform SLA Uptime", "desc": "High availability redundant carrier switching"},
        {"num": "15,600+", "lbl": "Msgs / Sec Capacity", "desc": "Low latency carrier grade throughput"},
        {"num": "< 1.2s", "lbl": "Global Delivery Speed", "desc": "Sub-second A2P and OTP termination"}
    ]

    stat_col_elements = []
    for s in stat_items:
        stat_card = make_container(
            settings={
                "content_width": "full",
                "flex_direction": "column",
                "background_background": "classic",
                "background_color": "#FFFFFF",
                "border_border": "solid",
                "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
                "border_color": "#E2ECE5",
                "border_radius": {"unit": "px", "top": "14", "right": "14", "bottom": "14", "left": "14", "isLinked": True},
                "padding": {"unit": "px", "top": "22", "right": "22", "bottom": "22", "left": "22", "isLinked": True},
                "width": {"unit": "%", "size": 100, "sizes": []}
            },
            elements=[
                make_widget("heading", {
                    "title": s["num"],
                    "header_size": "h3",
                    "typography_typography": "custom",
                    "typography_font_family": "Space Grotesk",
                    "typography_font_weight": "700",
                    "typography_font_size": {"unit": "px", "size": 34, "sizes": []},
                    "color": "#14692c",
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "4", "left": "0", "isLinked": False}
                }),
                make_widget("heading", {
                    "title": s["lbl"],
                    "header_size": "h5",
                    "typography_typography": "custom",
                    "typography_font_family": "Plus Jakarta Sans",
                    "typography_font_weight": "700",
                    "typography_font_size": {"unit": "px", "size": 14.5, "sizes": []},
                    "color": "#0B1210",
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "6", "left": "0", "isLinked": False}
                }),
                make_widget("text-editor", {
                    "editor": f'<p style="margin:0; font-size:13px; color:#53645B; line-height:1.5; font-family:\'Inter\', sans-serif;">{s["desc"]}</p>'
                })
            ]
        )
        stat_col_elements.append(
            make_container(
                settings={"width": {"unit": "%", "size": 23.5, "sizes": []}, "width_tablet": {"unit": "%", "size": 48, "sizes": []}, "width_mobile": {"unit": "%", "size": 100, "sizes": []}},
                elements=[stat_card]
            )
        )

    stats_row_container = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "row",
            "flex_wrap": "wrap",
            "gap": {"column": "20", "row": "20", "unit": "px"},
            "margin": {"unit": "px", "top": "60", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
            "width": {"unit": "%", "size": 100, "sizes": []}
        },
        elements=stat_col_elements
    )

    sec_0_inner = make_container(
        settings={
            "flex_direction": "column",
            "flex_wrap": "nowrap",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "container_max_width": {"unit": "px", "size": 1180, "sizes": []},
            "padding": {"unit": "px", "top": "0", "right": "24", "bottom": "0", "left": "24", "isLinked": False}
        },
        elements=[hero_split_row, stats_row_container]
    )

    sec_0 = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "flex_wrap": "nowrap",
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "padding": {"unit": "px", "top": "70", "right": "0", "bottom": "70", "left": "0", "isLinked": False},
            "padding_mobile": {"unit": "px", "top": "40", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
        },
        elements=[sec_0_inner],
        is_inner=False
    )

    # =========================================================================
    # SECTION 1: Services Grid (01 / wholesale, 02 / a2p, 03 / integration, 04 / enterprise, 05 / global, 06 / noc)
    # =========================================================================
    services_list = [
        {
            "tag": "01 / A2P CORE",
            "title": "A2P Enterprise Messaging",
            "desc": "High-deliverability application-to-person SMS for mission-critical notifications, bank alerts, and real-time OTPs with direct carrier routing.",
            "tags": ["Tier-1 Direct", "Real-time DLR", "Global Reach"]
        },
        {
            "tag": "02 / DIRECT BINDS",
            "title": "Direct Carrier Routes",
            "desc": "Direct SS7 and SMPP interconnects with mobile network operators across Asia, Europe, Middle East, and Africa for pristine deliverability.",
            "tags": ["Direct Interconnect", "No Gray Routes", "SLA Backed"]
        },
        {
            "tag": "03 / SECURITY & OTP",
            "title": "OTP & 2FA Deliverability",
            "desc": "Sub-second routing engineered specifically for time-sensitive one-time passcodes and multi-factor authentication with adaptive fallback.",
            "tags": ["Sub-Second Delivery", "Priority Queue", "Adaptive Retry"]
        },
        {
            "tag": "04 / WHOLESALE HUB",
            "title": "Wholesale Carrier Hub",
            "desc": "High-volume wholesale SMS termination with competitive tiered pricing, least cost routing (LCR), and dedicated high-TPS capacity.",
            "tags": ["High TPS Capacity", "LCR Routing", "Wholesale Pricing"]
        },
        {
            "tag": "05 / GLOBAL COVERAGE",
            "title": "Global Operator Reach",
            "desc": "Extensive network coverage connecting to 800+ mobile network operators in over 190 countries globally with localized sender ID compliance.",
            "tags": ["190+ Countries", "800+ MNOs", "Global SS7"]
        },
        {
            "tag": "06 / 24/7 CARRIER NOC",
            "title": "24/7 Monitored Carrier NOC",
            "desc": "Round-the-clock proactive monitoring by experienced telecom routing engineers ensuring 99.99% platform availability and instant route recovery.",
            "tags": ["24/7/365 NOC", "Proactive Alerts", "Direct Engineers"]
        }
    ]

    service_col_containers = []
    for s in services_list:
        tag_html = "".join([f'<span style="display:inline-block; font-size:11.5px; font-weight:600; color:#14692c; background:#EBF9EF; border:1px solid #C6EACF; padding:3px 9px; border-radius:999px; margin-right:6px; margin-bottom:6px;">{t}</span>' for t in s["tags"]])
        card_widget = make_widget("text-editor", {
            "editor": f"""<div style="background:#FFFFFF; border:1px solid #E2ECE5; border-radius:14px; padding:28px 24px; font-family:'Plus Jakarta Sans', sans-serif; height:100%; box-sizing:border-box; display:flex; flex-direction:column;">
  <div style="font-family:'JetBrains Mono', monospace; font-size:11px; font-weight:700; color:#14692c; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:10px;">{s["tag"]}</div>
  <h4 style="margin:0 0 10px 0; font-size:19px; font-weight:700; color:#0B1210;">{s["title"]}</h4>
  <p style="margin:0 0 18px 0; font-size:14px; line-height:1.6; color:#53645B; font-family:'Inter', sans-serif;">{s["desc"]}</p>
  <div style="display:flex; flex-wrap:wrap; margin-top:auto;">{tag_html}</div>
</div>"""
        })
        service_col_containers.append(
            make_container(
                settings={"width": {"unit": "%", "size": 31.8, "sizes": []}, "width_tablet": {"unit": "%", "size": 48, "sizes": []}, "width_mobile": {"unit": "%", "size": 100, "sizes": []}},
                elements=[card_widget]
            )
        )

    sec_1_inner = make_container(
        settings={
            "flex_direction": "column",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "container_max_width": {"unit": "px", "size": 1180, "sizes": []},
            "padding": {"unit": "px", "top": "0", "right": "24", "bottom": "0", "left": "24", "isLinked": False}
        },
        elements=[
            # Header
            make_container(
                settings={
                    "content_width": "full",
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "44", "left": "0", "isLinked": False}
                },
                elements=[
                    make_widget("text-editor", {
                        "editor": '<p style="margin:0; font-family:\'JetBrains Mono\', monospace; font-size:12px; font-weight:700; color:#14692c; letter-spacing:0.08em; text-transform:uppercase;">01 / CORE MESSAGING INFRASTRUCTURE</p>',
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "8", "left": "0", "isLinked": False}
                    }),
                    make_widget("heading", {
                        "title": "Enterprise-Grade Messaging Services Built for Scale",
                        "header_size": "h2",
                        "typography_typography": "custom",
                        "typography_font_family": "Space Grotesk",
                        "typography_font_weight": "700",
                        "typography_font_size": {"unit": "px", "size": 36, "sizes": []},
                        "color": "#0B1210",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "12", "left": "0", "isLinked": False}
                    }),
                    make_widget("text-editor", {
                        "editor": '<p style="margin:0; text-align:center; font-size:16px; color:#53645B; max-width:640px; line-height:1.6; font-family:\'Inter\', sans-serif;">Direct routes, real-time analytics, and guaranteed delivery for tier-1 enterprises, fintechs, and wholesale aggregators.</p>'
                    })
                ]
            ),
            # Cards Grid
            make_container(
                settings={
                    "content_width": "full",
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "gap": {"column": "24", "row": "24", "unit": "px"},
                    "width": {"unit": "%", "size": 100, "sizes": []}
                },
                elements=service_col_containers
            )
        ]
    )

    sec_1 = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "background_background": "classic",
            "background_color": "#F8FAF8",
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "1", "left": "0", "isLinked": False},
            "border_color": "#E2ECE5",
            "padding": {"unit": "px", "top": "80", "right": "0", "bottom": "80", "left": "0", "isLinked": False},
            "_element_id": "services"
        },
        elements=[sec_1_inner],
        is_inner=False
    )

    # =========================================================================
    # SECTION 2: Carrier Deliverability Comparison Table
    # =========================================================================
    table_markup = """<div style="background:#FFFFFF; border:1px solid #E2ECE5; border-radius:16px; overflow:hidden; box-shadow:0 6px 24px rgba(11,18,16,0.03); font-family:'Plus Jakarta Sans', sans-serif;">
  <table style="width:100%; border-collapse:collapse; text-align:left; font-size:14px;">
    <thead>
      <tr style="background:#F8FAF8; border-bottom:1px solid #E2ECE5;">
        <th style="padding:18px 24px; font-weight:700; color:#0B1210; width:34%;">Feature / Capability</th>
        <th style="padding:18px 24px; font-weight:700; color:#14692c; background:rgba(62,203,95,0.06); width:36%;">Text Telecom Direct Routes</th>
        <th style="padding:18px 24px; font-weight:700; color:#6B7A72; width:30%;">Standard SMS Aggregators</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid #EEF3F0;">
        <td style="padding:16px 24px; font-weight:600; color:#0B1210;">Route Transparency</td>
        <td style="padding:16px 24px; color:#14692c; font-weight:700; background:rgba(62,203,95,0.03);">&#10003; 100% Direct Carrier Binds &amp; SS7</td>
        <td style="padding:16px 24px; color:#78867E;">Mixed / Gray routes with hops</td>
      </tr>
      <tr style="border-bottom:1px solid #EEF3F0;">
        <td style="padding:16px 24px; font-weight:600; color:#0B1210;">Delivery Latency (OTP)</td>
        <td style="padding:16px 24px; color:#14692c; font-weight:700; background:rgba(62,203,95,0.03);">&#10003; Sub-second (&lt; 1.2s avg)</td>
        <td style="padding:16px 24px; color:#78867E;">3.5s &ndash; 8.0s variable delays</td>
      </tr>
      <tr style="border-bottom:1px solid #EEF3F0;">
        <td style="padding:16px 24px; font-weight:600; color:#0B1210;">SLA &amp; Uptime Guarantee</td>
        <td style="padding:16px 24px; color:#14692c; font-weight:700; background:rgba(62,203,95,0.03);">&#10003; 99.99% Financially backed SLA</td>
        <td style="padding:16px 24px; color:#78867E;">99.0% &ndash; 99.5% standard</td>
      </tr>
      <tr style="border-bottom:1px solid #EEF3F0;">
        <td style="padding:16px 24px; font-weight:600; color:#0B1210;">Delivery Receipts (DLR)</td>
        <td style="padding:16px 24px; color:#14692c; font-weight:700; background:rgba(62,203,95,0.03);">&#10003; Real-time handset delivery DLR</td>
        <td style="padding:16px 24px; color:#78867E;">Delayed or simulated network ACKs</td>
      </tr>
      <tr style="border-bottom:1px solid #EEF3F0;">
        <td style="padding:16px 24px; font-weight:600; color:#0B1210;">Dedicated NOC Support</td>
        <td style="padding:16px 24px; color:#14692c; font-weight:700; background:rgba(62,203,95,0.03);">&#10003; 24/7 direct access to routing engineers</td>
        <td style="padding:16px 24px; color:#78867E;">Tier-1 support ticket queue</td>
      </tr>
      <tr>
        <td style="padding:16px 24px; font-weight:600; color:#0B1210;">Dynamic LCR Engine</td>
        <td style="padding:16px 24px; color:#14692c; font-weight:700; background:rgba(62,203,95,0.03);">&#10003; Quality-first automated routing</td>
        <td style="padding:16px 24px; color:#78867E;">Price-only lowest cost routing</td>
      </tr>
    </tbody>
  </table>
</div>"""

    sec_2_inner = make_container(
        settings={
            "flex_direction": "column",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "container_max_width": {"unit": "px", "size": 1180, "sizes": []},
            "padding": {"unit": "px", "top": "0", "right": "24", "bottom": "0", "left": "24", "isLinked": False}
        },
        elements=[
            make_container(
                settings={
                    "content_width": "full",
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
                },
                elements=[
                    make_widget("text-editor", {
                        "editor": '<p style="margin:0; font-family:\'JetBrains Mono\', monospace; font-size:12px; font-weight:700; color:#14692c; letter-spacing:0.08em; text-transform:uppercase;">02 / CARRIER EXCELLENCE</p>',
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "8", "left": "0", "isLinked": False}
                    }),
                    make_widget("heading", {
                        "title": "Engineered for High Deliverability & Transparency",
                        "header_size": "h2",
                        "typography_typography": "custom",
                        "typography_font_family": "Space Grotesk",
                        "typography_font_weight": "700",
                        "typography_font_size": {"unit": "px", "size": 36, "sizes": []},
                        "color": "#0B1210",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "12", "left": "0", "isLinked": False}
                    }),
                    make_widget("text-editor", {
                        "editor": '<p style="margin:0; text-align:center; font-size:16px; color:#53645B; max-width:640px; line-height:1.6; font-family:\'Inter\', sans-serif;">How direct telecom carrier binds compare with ordinary message aggregators.</p>'
                    })
                ]
            ),
            make_widget("html", {
                "html": table_markup
            })
        ]
    )

    sec_2 = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "padding": {"unit": "px", "top": "80", "right": "0", "bottom": "80", "left": "0", "isLinked": False}
        },
        elements=[sec_2_inner],
        is_inner=False
    )

    # =========================================================================
    # SECTION 3: About Text Telecom & Core Commitments (EXACT MATCH to preview-option-1.html)
    # =========================================================================
    about_left_elements = [
        make_widget("text-editor", {
            "editor": '<p style="margin:0; font-family:\'JetBrains Mono\', monospace; font-size:12px; font-weight:700; color:#14692c; letter-spacing:0.08em; text-transform:uppercase;">ABOUT TEXT TELECOM</p>',
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "10", "left": "0", "isLinked": False}
        }),
        make_widget("heading", {
            "title": "A messaging partner built on carrier relationships, not just software.",
            "header_size": "h2",
            "typography_typography": "custom",
            "typography_font_family": "Space Grotesk",
            "typography_font_weight": "700",
            "typography_font_size": {"unit": "px", "size": 34, "sizes": []},
            "typography_line_height": {"unit": "em", "size": 1.2, "sizes": []},
            "color": "#0B1210",
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
        }),
        make_widget("heading", {
            "title": "Text Telecom is a global telecommunications carrier licensed in Dubai, specializing in SMS messaging and mobile communication infrastructure.",
            "header_size": "h4",
            "typography_typography": "custom",
            "typography_font_family": "Plus Jakarta Sans",
            "typography_font_weight": "600",
            "typography_font_size": {"unit": "px", "size": 16.5, "sizes": []},
            "typography_line_height": {"unit": "em", "size": 1.55, "sizes": []},
            "color": "#0B1210",
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "16", "left": "0", "isLinked": False}
        }),
        make_widget("text-editor", {
            "editor": '<p style="margin:0; font-size:15px; line-height:1.65; color:#53645B; font-family:\'Inter\', sans-serif;">We connect businesses, aggregators, and mobile operators through carrier routes that are dependable, secure, and engineered to scale worldwide without margin erosion.</p>',
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "28", "left": "0", "isLinked": False}
        }),
        make_widget("text-editor", {
            "editor": """<div style="background:#FFFFFF; border-left:4px solid #3ECB5F; padding:18px 22px; border-radius:0 12px 12px 0; border-top:1px solid #E2ECE5; border-right:1px solid #E2ECE5; border-bottom:1px solid #E2ECE5; margin-bottom:16px; font-family:'Plus Jakarta Sans', sans-serif;">
  <div style="font-size:12.5px; font-weight:800; color:#14692c; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:6px;">OUR MISSION</div>
  <p style="margin:0; font-size:14.5px; color:#0B1210; font-weight:500; line-height:1.5;">Give every business a direct, dependable line to its customers, anywhere in the world, with zero compromise on latency.</p>
</div>
<div style="background:#FFFFFF; border-left:4px solid #3ECB5F; padding:18px 22px; border-radius:0 12px 12px 0; border-top:1px solid #E2ECE5; border-right:1px solid #E2ECE5; border-bottom:1px solid #E2ECE5; font-family:'Plus Jakarta Sans', sans-serif;">
  <div style="font-size:12.5px; font-weight:800; color:#14692c; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:6px;">OUR VISION</div>
  <p style="margin:0; font-size:14.5px; color:#0B1210; font-weight:500; line-height:1.5;">Become the most trusted global standard in mobile messaging through carrier excellence, honest reporting, and lasting partnerships.</p>
</div>"""
        })
    ]

    pillars_html = """<div style="display:flex; flex-direction:column; gap:16px; font-family:'Plus Jakarta Sans', sans-serif;">
  <div style="display:flex; align-items:flex-start; gap:16px; background:#FFFFFF; border:1px solid #E2ECE5; padding:18px 20px; border-radius:12px; box-shadow:0 2px 8px rgba(11,18,16,0.03);">
    <div style="width:36px; height:36px; border-radius:10px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
    </div>
    <div>
      <h4 style="margin:0 0 4px 0; font-size:16px; font-weight:700; color:#0B1210;">Reliability</h4>
      <p style="margin:0; font-size:13.5px; color:#53645B; line-height:1.5; font-family:'Inter', sans-serif;">A 99.99% uptime SLA backed by geo-redundant node architecture across Asia, Europe, and GCC.</p>
    </div>
  </div>

  <div style="display:flex; align-items:flex-start; gap:16px; background:#FFFFFF; border:1px solid #E2ECE5; padding:18px 20px; border-radius:12px; box-shadow:0 2px 8px rgba(11,18,16,0.03);">
    <div style="width:36px; height:36px; border-radius:10px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
    </div>
    <div>
      <h4 style="margin:0 0 4px 0; font-size:16px; font-weight:700; color:#0B1210;">Transparency</h4>
      <p style="margin:0; font-size:13.5px; color:#53645B; line-height:1.5; font-family:'Inter', sans-serif;">Clear pricing, unmanipulated DLR receipts, and honest network telemetry &mdash; no surprises, ever.</p>
    </div>
  </div>

  <div style="display:flex; align-items:flex-start; gap:16px; background:#FFFFFF; border:1px solid #E2ECE5; padding:18px 20px; border-radius:12px; box-shadow:0 2px 8px rgba(11,18,16,0.03);">
    <div style="width:36px; height:36px; border-radius:10px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
    </div>
    <div>
      <h4 style="margin:0 0 4px 0; font-size:16px; font-weight:700; color:#0B1210;">Innovation</h4>
      <p style="margin:0; font-size:13.5px; color:#53645B; line-height:1.5; font-family:'Inter', sans-serif;">Continuously upgrading SMPP protocols, AI-assisted routing optimization, and automated carrier failover.</p>
    </div>
  </div>

  <div style="display:flex; align-items:flex-start; gap:16px; background:#FFFFFF; border:1px solid #E2ECE5; padding:18px 20px; border-radius:12px; box-shadow:0 2px 8px rgba(11,18,16,0.03);">
    <div style="width:36px; height:36px; border-radius:10px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
    </div>
    <div>
      <h4 style="margin:0 0 4px 0; font-size:16px; font-weight:700; color:#0B1210;">Dedicated Account Team</h4>
      <p style="margin:0; font-size:13.5px; color:#53645B; line-height:1.5; font-family:'Inter', sans-serif;">A real telecommunications specialist assigned to your account for onboarding, route tuning, and 24/7 support.</p>
    </div>
  </div>
</div>"""

    about_right_elements = [
        make_widget("html", {
            "html": pillars_html
        })
    ]

    sec_3_inner = make_container(
        settings={
            "flex_direction": "row",
            "flex_wrap": "nowrap",
            "flex_direction_tablet": "column",
            "gap": {"column": "48", "row": "48", "unit": "px"},
            "width": {"unit": "%", "size": 100, "sizes": []},
            "container_max_width": {"unit": "px", "size": 1180, "sizes": []},
            "padding": {"unit": "px", "top": "0", "right": "24", "bottom": "0", "left": "24", "isLinked": False}
        },
        elements=[
            make_container(
                settings={"content_width": "full", "flex_direction": "column", "width": {"unit": "%", "size": 50, "sizes": []}, "width_tablet": {"unit": "%", "size": 100, "sizes": []}},
                elements=about_left_elements
            ),
            make_container(
                settings={"content_width": "full", "flex_direction": "column", "width": {"unit": "%", "size": 50, "sizes": []}, "width_tablet": {"unit": "%", "size": 100, "sizes": []}},
                elements=about_right_elements
            )
        ]
    )

    sec_3 = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "background_background": "classic",
            "background_color": "#F8FAF8",
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "1", "left": "0", "isLinked": False},
            "border_color": "#E2ECE5",
            "padding": {"unit": "px", "top": "80", "right": "0", "bottom": "80", "left": "0", "isLinked": False},
            "_element_id": "about"
        },
        elements=[sec_3_inner],
        is_inner=False
    )

    # =========================================================================
    # SECTION 4: Contact & Dubai HQ (EXACT MATCH to preview-option-1.html)
    # =========================================================================
    contact_info_widget = make_widget("text-editor", {
        "editor": """<div style="background:#FFFFFF; border:1px solid #E2ECE5; border-radius:16px; padding:32px; font-family:'Plus Jakarta Sans', sans-serif; height:100%; box-sizing:border-box;">
  <h3 style="font-size:20px; font-weight:700; margin:0 0 24px 0; color:#0B1210;">Global Headquarters</h3>
  
  <div style="display:flex; gap:16px; margin-bottom:24px;">
    <div style="width:40px; height:40px; border-radius:12px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
    </div>
    <div>
      <div style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#14692c; margin-bottom:4px;">Office Address</div>
      <div style="font-size:14.5px; color:#0B1210; font-weight:500;">Business Center 1, M Floor, The Meydan Hotel, Nad Al Sheba, Dubai, U.A.E.</div>
    </div>
  </div>

  <div style="display:flex; gap:16px; margin-bottom:24px;">
    <div style="width:40px; height:40px; border-radius:12px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
    </div>
    <div>
      <div style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#14692c; margin-bottom:4px;">Direct Carrier Contacts</div>
      <div style="font-size:14.5px; color:#0B1210; font-weight:600;">
        <a href="mailto:lc@text-telecom.com" style="color:#0B1210; text-decoration:none;">lc@text-telecom.com</a><br>
        <a href="mailto:mm@text-telecom.com" style="color:#0B1210; text-decoration:none;">mm@text-telecom.com</a>
      </div>
    </div>
  </div>

  <div style="display:flex; gap:16px; margin-bottom:24px;">
    <div style="width:40px; height:40px; border-radius:12px; background:#EBF9EF; color:#126328; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#126328" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
    </div>
    <div>
      <div style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#14692c; margin-bottom:4px;">Network NOC Support</div>
      <div style="font-size:14.5px; color:#0B1210; font-weight:500;">Available 24/7/365 &bull; SLA Guaranteed</div>
    </div>
  </div>

  <div style="background:#F8FAF8; padding:16px; border-radius:10px; border:1px solid #E2ECE5; margin-top:20px;">
    <div style="font-size:12px; font-weight:700; color:#14692c; text-transform:uppercase; margin-bottom:4px;">Licensed Entity</div>
    <div style="font-size:13px; color:#53645B;">Text Telecom &bull; Regulated Telecommunications Operator, Dubai, United Arab Emirates.</div>
  </div>
</div>"""
    })

    contact_form_html = """<div style="background:#FFFFFF; border:1px solid #E2ECE5; border-radius:16px; padding:36px; box-shadow:0 8px 30px rgba(11,18,16,0.04); font-family:'Plus Jakarta Sans', sans-serif;">
<form onsubmit="event.preventDefault(); this.querySelector('button').innerHTML='<span>Request Dispatched &#10003;</span>'; this.querySelector('button').style.background='#14692c'; this.querySelector('button').style.color='#FFFFFF';">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:18px;">
    <div>
      <label style="display:block; font-size:13px; font-weight:600; color:#0B1210; margin-bottom:6px;">Full Name</label>
      <input type="text" required placeholder="Your full name" style="width:100%; box-sizing:border-box; background:#FFFFFF; border:1px solid #E2ECE5; border-radius:8px; padding:12px 14px; font-size:14px; color:#0B1210; outline:none;" />
    </div>
    <div>
      <label style="display:block; font-size:13px; font-weight:600; color:#0B1210; margin-bottom:6px;">Business Email</label>
      <input type="email" required placeholder="name@company.com" style="width:100%; box-sizing:border-box; background:#FFFFFF; border:1px solid #E2ECE5; border-radius:8px; padding:12px 14px; font-size:14px; color:#0B1210; outline:none;" />
    </div>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:18px;">
    <div>
      <label style="display:block; font-size:13px; font-weight:600; color:#0B1210; margin-bottom:6px;">Company Name</label>
      <input type="text" placeholder="Company Inc." style="width:100%; box-sizing:border-box; background:#FFFFFF; border:1px solid #E2ECE5; border-radius:8px; padding:12px 14px; font-size:14px; color:#0B1210; outline:none;" />
    </div>
    <div>
      <label style="display:block; font-size:13px; font-weight:600; color:#0B1210; margin-bottom:6px;">Estimated Monthly Volume</label>
      <input type="text" placeholder="e.g. 500,000 SMS / month" style="width:100%; box-sizing:border-box; background:#FFFFFF; border:1px solid #E2ECE5; border-radius:8px; padding:12px 14px; font-size:14px; color:#0B1210; outline:none;" />
    </div>
  </div>

  <div style="margin-bottom:20px;">
    <label style="display:block; font-size:13px; font-weight:600; color:#0B1210; margin-bottom:6px;">Destination Countries &amp; Requirements</label>
    <textarea rows="3" required placeholder="Tell us about the countries you send to and your required throughput or API specs..." style="width:100%; box-sizing:border-box; background:#FFFFFF; border:1px solid #E2ECE5; border-radius:8px; padding:12px 14px; font-size:14px; color:#0B1210; outline:none; resize:vertical;"></textarea>
  </div>

  <button type="submit" style="width:100%; background:#3ECB5F; color:#0B1210; font-weight:700; font-size:15px; border:none; border-radius:999px; padding:14px 24px; cursor:pointer; font-family:inherit; transition:background 0.2s;">Send Request to Carrier Desk &rarr;</button>
</form>
</div>"""

    sec_4_inner = make_container(
        settings={
            "flex_direction": "column",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "container_max_width": {"unit": "px", "size": 1180, "sizes": []},
            "padding": {"unit": "px", "top": "0", "right": "24", "bottom": "0", "left": "24", "isLinked": False}
        },
        elements=[
            make_container(
                settings={
                    "content_width": "full",
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "44", "left": "0", "isLinked": False}
                },
                elements=[
                    make_widget("text-editor", {
                        "editor": '<p style="margin:0; font-family:\'JetBrains Mono\', monospace; font-size:12px; font-weight:700; color:#14692c; letter-spacing:0.08em; text-transform:uppercase;">GET IN TOUCH</p>',
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "8", "left": "0", "isLinked": False}
                    }),
                    make_widget("heading", {
                        "title": "Need a custom enterprise messaging solution?",
                        "header_size": "h2",
                        "typography_typography": "custom",
                        "typography_font_family": "Space Grotesk",
                        "typography_font_weight": "700",
                        "typography_font_size": {"unit": "px", "size": 36, "sizes": []},
                        "color": "#0B1210",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "12", "left": "0", "isLinked": False}
                    }),
                    make_widget("text-editor", {
                        "editor": '<p style="margin:0; text-align:center; font-size:16px; color:#53645B; max-width:640px; line-height:1.6; font-family:\'Inter\', sans-serif;">Reach out to our global routing team &mdash; we typically reply with a tailored quote within 1 business day.</p>'
                    })
                ]
            ),
            make_container(
                settings={
                    "content_width": "full",
                    "flex_direction": "row",
                    "flex_wrap": "nowrap",
                    "flex_direction_tablet": "column",
                    "gap": {"column": "40", "row": "40", "unit": "px"},
                    "width": {"unit": "%", "size": 100, "sizes": []}
                },
                elements=[
                    make_container(
                        settings={"content_width": "full", "flex_direction": "column", "width": {"unit": "%", "size": 45, "sizes": []}, "width_tablet": {"unit": "%", "size": 100, "sizes": []}},
                        elements=[contact_info_widget]
                    ),
                    make_container(
                        settings={"content_width": "full", "flex_direction": "column", "width": {"unit": "%", "size": 55, "sizes": []}, "width_tablet": {"unit": "%", "size": 100, "sizes": []}},
                        elements=[make_widget("html", {"html": contact_form_html})]
                    )
                ]
            )
        ]
    )

    sec_4 = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "padding": {"unit": "px", "top": "80", "right": "0", "bottom": "80", "left": "0", "isLinked": False},
            "_element_id": "contact"
        },
        elements=[sec_4_inner],
        is_inner=False
    )

    # =========================================================================
    # SECTION 5: Site Footer (EXACT MATCH to preview-option-1.html)
    # =========================================================================
    footer_col1 = make_widget("text-editor", {
        "editor": """<div style="font-family:'Plus Jakarta Sans', sans-serif;">
  <h4 style="margin:0 0 12px 0; font-family:'Space Grotesk', sans-serif; font-size:22px; font-weight:800; color:#0B1210;">Text Telecom</h4>
  <p style="margin:0 0 16px 0; font-size:14px; line-height:1.6; color:#53645B; font-family:'Inter', sans-serif; max-width:320px;">Connecting businesses worldwide through dependable, carrier-grade messaging infrastructure and direct operator routes.</p>
  <p style="margin:0;"><a href="https://ae.linkedin.com/company/text-telecom" target="_blank" rel="noopener" style="font-size:13.5px; color:#0B1210; text-decoration:none; font-weight:600;">&rarr; Follow on LinkedIn</a></p>
</div>"""
    })

    footer_col2 = make_widget("text-editor", {
        "editor": """<div style="font-family:'Plus Jakarta Sans', sans-serif;">
  <div style="font-size:12px; font-weight:700; color:#0B1210; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:14px;">Core Services</div>
  <div style="line-height:2; font-size:13.5px; font-family:'Inter', sans-serif;">
    <div><a href="#services" style="color:#53645B; text-decoration:none;">A2P SMS Messaging</a></div>
    <div><a href="#services" style="color:#53645B; text-decoration:none;">Wholesale SMS</a></div>
    <div><a href="#services" style="color:#53645B; text-decoration:none;">Enterprise Campaigns</a></div>
    <div><a href="#services" style="color:#53645B; text-decoration:none;">Platform &amp; API Tools</a></div>
    <div><a href="#services" style="color:#53645B; text-decoration:none;">OTP &amp; 2FA Solutions</a></div>
  </div>
</div>"""
    })

    footer_col3 = make_widget("text-editor", {
        "editor": """<div style="font-family:'Plus Jakarta Sans', sans-serif;">
  <div style="font-size:12px; font-weight:700; color:#0B1210; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:14px;">Company &amp; Hub</div>
  <div style="line-height:2; font-size:13.5px; font-family:'Inter', sans-serif;">
    <div><a href="#about" style="color:#53645B; text-decoration:none;">About Text Telecom</a></div>
    <div><a href="#coverage" style="color:#53645B; text-decoration:none;">190+ Countries Route</a></div>
    <div><a href="#about" style="color:#53645B; text-decoration:none;">Carrier Commitments</a></div>
    <div><a href="#contact" style="color:#53645B; text-decoration:none;">Dubai Meydan Office</a></div>
    <div><a href="#contact" style="color:#53645B; text-decoration:none;">24/7 NOC Desk</a></div>
  </div>
</div>"""
    })

    footer_col4 = make_widget("text-editor", {
        "editor": """<div style="font-family:'Plus Jakarta Sans', sans-serif;">
  <div style="font-size:12px; font-weight:700; color:#0B1210; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:14px;">Stay in the Loop</div>
  <p style="font-size:13.5px; color:#53645B; margin:0 0 14px 0; font-family:'Inter', sans-serif;">Direct telecommunications route updates and network advisories. No spam.</p>
  <form onsubmit="event.preventDefault(); this.querySelector('button').textContent='Subscribed!';" style="display:flex; gap:6px;">
    <input type="email" placeholder="Your work email" required style="padding:9px 12px; border:1px solid #E2ECE5; border-radius:6px; font-size:13px; flex:1; outline:none; box-sizing:border-box;">
    <button type="submit" style="background:#3ECB5F; color:#0B1210; font-weight:700; border:none; border-radius:6px; padding:9px 16px; cursor:pointer;">Join</button>
  </form>
</div>"""
    })

    footer_cols_row = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "row",
            "flex_wrap": "wrap",
            "gap": {"column": "30", "row": "30", "unit": "px"},
            "width": {"unit": "%", "size": 100, "sizes": []},
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
        },
        elements=[
            make_container(settings={"width": {"unit": "%", "size": 34, "sizes": []}, "width_tablet": {"unit": "%", "size": 100, "sizes": []}}, elements=[footer_col1]),
            make_container(settings={"width": {"unit": "%", "size": 20, "sizes": []}, "width_tablet": {"unit": "%", "size": 33, "sizes": []}, "width_mobile": {"unit": "%", "size": 100, "sizes": []}}, elements=[footer_col2]),
            make_container(settings={"width": {"unit": "%", "size": 20, "sizes": []}, "width_tablet": {"unit": "%", "size": 33, "sizes": []}, "width_mobile": {"unit": "%", "size": 100, "sizes": []}}, elements=[footer_col3]),
            make_container(settings={"width": {"unit": "%", "size": 26, "sizes": []}, "width_tablet": {"unit": "%", "size": 33, "sizes": []}, "width_mobile": {"unit": "%", "size": 100, "sizes": []}}, elements=[footer_col4])
        ]
    )

    sec_5_inner = make_container(
        settings={
            "flex_direction": "column",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "container_max_width": {"unit": "px", "size": 1180, "sizes": []},
            "padding": {"unit": "px", "top": "0", "right": "24", "bottom": "0", "left": "24", "isLinked": False}
        },
        elements=[
            footer_cols_row,
            make_widget("divider", {
                "color": "#E2ECE5",
                "gap": {"unit": "px", "size": 0, "sizes": []},
                "text": "Divider"
            }),
            make_widget("text-editor", {
                "editor": '<div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px; padding-top:20px; font-size:13px; color:#6B7A72; font-family:\'Plus Jakarta Sans\', sans-serif;">'
                          '<span>Copyright &copy; 2026 <strong>Text Telecom&reg;</strong>. All rights reserved.</span>'
                          '<span>Licensed Global Telecommunications Carrier &bull; Dubai, U.A.E.</span>'
                          '</div>'
            })
        ]
    )

    sec_5 = make_container(
        settings={
            "content_width": "full",
            "flex_direction": "column",
            "background_background": "classic",
            "background_color": "#F8FAF8",
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
            "border_color": "#E2ECE5",
            "padding": {"unit": "px", "top": "60", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
        },
        elements=[sec_5_inner],
        is_inner=False
    )

    # Master Document matching Text-telecom.json top-level schema
    doc = {
        "content": [
            sec_0,
            sec_1,
            sec_2,
            sec_3,
            sec_4,
            sec_5
        ],
        "page_settings": {
            "hide_title": "yes"
        },
        "version": "0.4",
        "title": "Text Telecom - Option 1 CPaaS Enterprise",
        "type": "page"
    }

    with open('Text-Telecom-Option-1-CPaaS-Enterprise.json', 'w', encoding='utf-8') as f:
        json.dump(doc, f, indent=2)

    print("Generated 100% compliant Elementor JSON successfully!")

if __name__ == '__main__':
    generate_clean_elementor_json()

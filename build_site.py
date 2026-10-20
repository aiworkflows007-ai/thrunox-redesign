import os
import re

print("Starting build of index.html for Thrunox Systems 2.0...")

with open('/home/ashok/thrunox-redesign/details_extracted/privacy.txt') as f:
    privacy_raw = f.read()

with open('/home/ashok/thrunox-redesign/details_extracted/terms.txt') as f:
    terms_raw = f.read()

# Helper to format text paragraphs for HTML modals
def text_to_html_paragraphs(txt):
    paragraphs = txt.split('\n\n')
    out = []
    for p in paragraphs:
        p_clean = p.strip()
        if not p_clean:
            continue
        # check if it looks like a heading
        lines = p_clean.split('\n')
        if len(lines) == 1 and (lines[0].startswith(tuple(f'{i}.' for i in range(1, 20))) or lines[0].isupper() or len(lines[0]) < 60):
            out.append(f'<h3 class="text-base font-bold text-amber-400 mt-4 mb-2">{lines[0]}</h3>')
        else:
            formatted_lines = '<br>'.join(lines)
            out.append(f'<p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-3">{formatted_lines}</p>')
    return '\n'.join(out)

privacy_html = text_to_html_paragraphs(privacy_raw)
terms_html = text_to_html_paragraphs(terms_raw)

html_content = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thrunox Systems LLP | Notions in Motion. Results in Reality.</title>
  <meta name="description" content="Thrunox Systems is an execution-focused business platform translating strategy into structured, practical, and scalable execution across Project Management, Operations, Supply Chain, Accounting, US Healthcare RCM, Digital Compliance, Cyber Security, and ESG Advisory.">
  <link rel="icon" href="logo.png">

  <!-- Google Fonts: Manrope (Required by Brand Guidelines) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Manrope"', 'sans-serif'],
            display: ['"Manrope"', 'sans-serif']
          }},
          colors: {{
            brand: {{
              gold: '#c89641',
              darkgold: '#a67319',
              crownred: '#7f1c21',
              void: '#070a10',
              surface: '#0e131d',
              card: '#121824',
              border: '#1f293d'
            }}
          }},
          animation: {{
            'slow-spin': 'slowSpin 32s linear infinite',
            'slow-spin-reverse': 'slowSpinReverse 28s linear infinite',
            'slow-float': 'slowFloat 8s ease-in-out infinite',
            'slow-float-delayed': 'slowFloat 10s ease-in-out 3s infinite',
            'slow-pulse': 'slowPulse 7s ease-in-out infinite',
            'radar-sweep': 'radarSweep 6s linear infinite',
            'pulse-glow': 'pulseGlow 5s ease-in-out infinite'
          }},
          keyframes: {{
            slowSpin: {{
              '0%': {{ transform: 'rotate(0deg)' }},
              '100%': {{ transform: 'rotate(360deg)' }}
            }},
            slowSpinReverse: {{
              '0%': {{ transform: 'rotate(360deg)' }},
              '100%': {{ transform: 'rotate(0deg)' }}
            }},
            slowFloat: {{
              '0%, 100%': {{ transform: 'translateY(0px)' }},
              '50%': {{ transform: 'translateY(-8px)' }}
            }},
            slowPulse: {{
              '0%, 100%': {{ opacity: '0.4', transform: 'scale(1)' }},
              '50%': {{ opacity: '0.8', transform: 'scale(1.02)' }}
            }},
            radarSweep: {{
              '0%': {{ transform: 'rotate(0deg)' }},
              '100%': {{ transform: 'rotate(360deg)' }}
            }},
            pulseGlow: {{
              '0%, 100%': {{ opacity: '0.25' }},
              '50%': {{ opacity: '0.5' }}
            }}
          }}
        }}
      }}
    }};
  </script>

  <style>
    /* Custom Styling for Thrunox Brochure Theme */
    body {{
      background-color: #070a10;
      color: #e2e8f0;
      font-family: 'Manrope', sans-serif;
      overflow-x: hidden;
    }}

    /* Restrained Engineering Glass Card */
    .thrunox-card {{
      background: linear-gradient(145deg, rgba(18, 24, 36, 0.88), rgba(11, 15, 23, 0.95));
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .thrunox-card:hover {{
      border-color: rgba(200, 150, 65, 0.35);
      transform: translateY(-2px);
      box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.7), 0 0 20px -5px rgba(200, 150, 65, 0.15);
    }}

    /* Subtle Technical Grid Lines */
    .cad-grid {{
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      background-size: 24px 24px;
    }}

    /* Darkened Crown Golden Buttons */
    .btn-gold {{
      background: linear-gradient(135deg, #b8860b 0%, #a67319 50%, #8c5d14 100%);
      color: #ffffff;
      box-shadow: 0 4px 15px -3px rgba(166, 115, 25, 0.35);
      transition: all 0.25s ease;
    }}
    .btn-gold:hover {{
      background: linear-gradient(135deg, #c89641 0%, #b8860b 50%, #9a6713 100%);
      box-shadow: 0 6px 22px -2px rgba(200, 150, 65, 0.5);
      transform: translateY(-1px);
    }}

    /* Titanium Dark Secondary Buttons */
    .btn-secondary {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #f1f5f9;
      transition: all 0.25s ease;
    }}
    .btn-secondary:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(200, 150, 65, 0.4);
      color: #ffffff;
    }}

    /* Animated Logo Badge with Darkened Crown Sheen */
    .logo-badge {{
      position: relative;
      overflow: hidden;
      box-shadow: 0 0 15px -3px rgba(166, 115, 25, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.1);
      transition: all 0.3s ease;
    }}
    .logo-badge:hover {{
      box-shadow: 0 0 25px rgba(200, 150, 65, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.2);
      transform: scale(1.02);
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #070a10;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1f293d;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #c89641;
    }}

    /* Modal Styling */
    .modal-backdrop {{
      background: rgba(4, 7, 12, 0.85);
      backdrop-filter: blur(8px);
    }}
  </style>
</head>
<body class="selection:bg-amber-600/30 selection:text-amber-200">

  <!-- Interactive Background Canvas: Restrained Engineering Particle Network -->
  <canvas id="particleCanvas" class="fixed inset-0 pointer-events-none z-0 opacity-40"></canvas>

  <!-- Sticky Header: Navigation as per Content Handoff -->
  <header class="sticky top-0 z-50 bg-[#0c1018]/95 backdrop-blur-xl border-b border-white/10 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- Logo linking to About Us page -->
        <a href="#about" class="flex items-center gap-3 group" aria-label="Thrunox Systems Home">
          <div class="logo-badge px-3 py-1.5 rounded-xl bg-slate-900/80 border border-white/15 flex items-center justify-center">
            <img src="logo.png" alt="Thrunox Systems" class="h-8 sm:h-9 md:h-10 w-auto object-contain">
          </div>
        </a>

        <!-- Main Desktop Navigation: 4 Core Tabs as per Handoff Doc -->
        <nav class="hidden lg:flex items-center gap-8 text-xs font-semibold uppercase tracking-wider text-slate-300">
          <a href="#about" class="nav-tab hover:text-amber-400 transition-colors py-2 border-b-2 border-transparent hover:border-amber-400">About Us</a>
          <a href="#services" class="nav-tab hover:text-amber-400 transition-colors py-2 border-b-2 border-transparent hover:border-amber-400">Services</a>
          <a href="#industries" class="nav-tab hover:text-amber-400 transition-colors py-2 border-b-2 border-transparent hover:border-amber-400">Industries</a>
          <a href="#innovation" class="nav-tab hover:text-amber-400 transition-colors py-2 border-b-2 border-transparent hover:border-amber-400">Innovation & Solutions</a>
        </nav>

        <!-- Fast Actions & Header Contact Us Button -->
        <div class="flex items-center gap-2 sm:gap-3">
          <a href="#contact" class="hidden sm:inline-flex items-center gap-2 text-xs font-bold px-4 py-2.5 rounded-xl btn-gold shadow-md">
            <i data-lucide="mail" class="w-3.5 h-3.5"></i> Contact Us
          </a>
          <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20visited%20your%20website%20and%20would%20like%20to%20discuss%20a%20business%20requirement.%20Please%20let%20me%20know%20the%20appropriate%20next%20steps." target="_blank" class="inline-flex items-center gap-1.5 text-xs font-bold px-3 py-2 sm:px-3.5 sm:py-2.5 rounded-xl bg-emerald-600/90 hover:bg-emerald-500 text-white border border-emerald-400/30 transition-all shadow-md">
            <i data-lucide="message-circle" class="w-3.5 h-3.5"></i> <span class="hidden xs:inline">WhatsApp</span>
          </a>
          <!-- Mobile Menu Button -->
          <button id="mobileMenuBtn" aria-label="Toggle Navigation" class="lg:hidden p-2 rounded-xl text-slate-300 hover:text-white hover:bg-white/10 transition-colors border border-white/10">
            <i data-lucide="menu" class="w-5 h-5"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Responsive Slide-Down Mobile Drawer -->
    <div id="mobileDrawer" class="hidden lg:hidden bg-[#0a0f17]/98 border-b border-white/10 px-4 pt-4 pb-6 space-y-3 backdrop-blur-2xl transition-all">
      <div class="grid grid-cols-2 gap-2 text-xs font-semibold">
        <a href="#about" class="mobile-nav-link p-3 rounded-lg bg-white/5 text-slate-200 hover:bg-amber-500/20 hover:text-amber-300 transition-all flex items-center gap-2">
          <i data-lucide="info" class="w-4 h-4 text-amber-400"></i> About Us
        </a>
        <a href="#services" class="mobile-nav-link p-3 rounded-lg bg-white/5 text-slate-200 hover:bg-amber-500/20 hover:text-amber-300 transition-all flex items-center gap-2">
          <i data-lucide="layers" class="w-4 h-4 text-amber-400"></i> Services
        </a>
        <a href="#industries" class="mobile-nav-link p-3 rounded-lg bg-white/5 text-slate-200 hover:bg-amber-500/20 hover:text-amber-300 transition-all flex items-center gap-2">
          <i data-lucide="factory" class="w-4 h-4 text-amber-400"></i> Industries
        </a>
        <a href="#innovation" class="mobile-nav-link p-3 rounded-lg bg-white/5 text-slate-200 hover:bg-amber-500/20 hover:text-amber-300 transition-all flex items-center gap-2">
          <i data-lucide="cpu" class="w-4 h-4 text-amber-400"></i> Innovation &amp; Solutions
        </a>
      </div>
      <div class="pt-2 flex flex-col gap-2">
        <a href="#contact" class="w-full text-center py-2.5 rounded-xl btn-gold text-white font-bold text-xs flex items-center justify-center gap-2">
          <i data-lucide="mail" class="w-4 h-4"></i> Contact Us
        </a>
        <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems" target="_blank" class="w-full text-center py-2.5 rounded-xl bg-emerald-600/90 text-white font-bold text-xs flex items-center justify-center gap-2">
          <i data-lucide="message-circle" class="w-4 h-4"></i> WhatsApp Support Desk
        </a>
      </div>
    </div>
  </header>

  <!-- ========================================== -->
  <!-- TAB 1: ABOUT US & HERO SECTION             -->
  <!-- ========================================== -->
  <section id="about" class="relative pt-12 pb-24 md:pt-16 md:pb-32 overflow-hidden z-10 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Top Introduction & Tagline -->
      <div class="text-center max-w-3xl mx-auto mb-14">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-950/40 border border-amber-600/30 text-amber-300 text-xs font-semibold uppercase tracking-wider mb-5">
          <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
          Notions in Motion. Results in Reality.
        </div>
        <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight text-white mb-6">
          Thrunox Systems LLP
        </h1>
        <p class="text-base sm:text-lg text-slate-300 leading-relaxed font-normal mb-8">
          Thrunox Systems is an execution-focused business platform that helps organisations translate strategy into structured, practical and scalable execution.
        </p>
        <p class="text-sm sm:text-base text-slate-400 leading-relaxed mb-8">
          We bring together business operations, project management, supply chain, financial and revenue cycle support, regulatory coordination, digital compliance and sustainability advisory to help businesses address operational challenges and strengthen their systems.
        </p>
        <p class="text-xs sm:text-sm text-slate-400 mb-8 italic">
          Our approach is centred on understanding business requirements into a clear scope, practical workstreams, responsibilities and an execution plan. Our model is designed to be adaptable to different business sizes, operational environments and stages of growth.
        </p>
        
        <!-- Hero Action Buttons as defined in handoff doc -->
        <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4">
          <a href="#services" class="btn-gold px-5 py-3 rounded-xl font-bold text-xs sm:text-sm inline-flex items-center gap-2">
            Explore Our Services <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </a>
          <a href="#innovation" class="btn-secondary px-5 py-3 rounded-xl font-bold text-xs sm:text-sm inline-flex items-center gap-2">
            Explore Innovation &amp; Solutions <i data-lucide="compass" class="w-4 h-4 text-amber-400"></i>
          </a>
          <a href="Thrunox-Systems-Company-Brochure.pdf" download="Thrunox-Systems-Company-Brochure.pdf" class="btn-secondary px-5 py-3 rounded-xl font-bold text-xs sm:text-sm inline-flex items-center gap-2 border-amber-600/30 text-amber-300 hover:text-white">
            <i data-lucide="download" class="w-4 h-4 text-amber-400"></i> Download Company Brochure
          </a>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- HERO SECTION INDICATIVE IMAGES SHOWCASE:                        -->
      <!-- MECHANICAL ENGINEERING ON LEFT & SOFTWARE ENGINEERING ON RIGHT -->
      <!-- With Slow Elegant Animation as explicitly instructed           -->
      <!-- ============================================================== -->
      <div class="mt-8 mb-20">
        <div class="text-center mb-6">
          <span class="text-xs uppercase font-extrabold tracking-widest text-slate-400">
            Core Engineering Execution Disciplines
          </span>
          <p class="text-sm text-slate-400 mt-1">Bridging physical industrial machinery with advanced software simulation</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
          
          <!-- LEFT SIDE: MECHANICAL ENGINEERING -->
          <div class="thrunox-card rounded-2xl p-6 sm:p-8 relative overflow-hidden group flex flex-col justify-between cad-grid">
            <!-- Subtle slow rotating CAD blueprint ring in background -->
            <div class="absolute -top-16 -right-16 w-64 h-64 border border-amber-500/15 rounded-full pointer-events-none animate-slow-spin">
              <div class="absolute inset-4 border border-dashed border-amber-400/20 rounded-full"></div>
              <div class="absolute top-1/2 left-0 w-full h-[1px] bg-amber-500/20"></div>
              <div class="absolute top-0 left-1/2 h-full w-[1px] bg-amber-500/20"></div>
            </div>

            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-amber-950/60 border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider">
                  <i data-lucide="cog" class="w-3.5 h-3.5 animate-slow-spin"></i> Mechanical Engineering
                </span>
                <span class="text-[11px] font-mono text-slate-400 flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span> CAD / CAM &amp; Tooling
                </span>
              </div>

              <h3 class="text-xl sm:text-2xl font-bold text-white mb-2 group-hover:text-amber-300 transition-colors">
                Mechanical Design &amp; Custom Fabrication
              </h3>
              <p class="text-xs sm:text-sm text-slate-300 mb-6 leading-relaxed">
                Precision engineering execution spanning 3D CAD modeling, custom mechanical fabrication, structural stress analysis (FEA), and industrial machinery coordination.
              </p>

              <!-- Image Container with Slow Floating / Zoom Animation -->
              <div class="relative rounded-xl overflow-hidden mb-6 aspect-video border border-white/10 group-hover:border-amber-500/30 transition-all shadow-xl">
                <img src="images/mechanical-hero.jpg" alt="Mechanical Engineering CAD and Industrial Robotics" class="w-full h-full object-cover transform scale-100 group-hover:scale-105 transition-transform duration-1000 ease-out">
                <div class="absolute inset-0 bg-gradient-to-t from-[#070a10] via-transparent to-transparent"></div>
                
                <!-- Telemetry HUD Overlay -->
                <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-[11px] font-mono text-amber-200 bg-slate-900/80 backdrop-blur-md px-3 py-1.5 rounded-lg border border-white/10">
                  <span class="flex items-center gap-1.5"><i data-lucide="crosshair" class="w-3.5 h-3.5 text-amber-400"></i> Tol: ±0.02 mm</span>
                  <span>CAD Model: SolidWorks / NX</span>
                  <span class="text-emerald-400">Execution Ready</span>
                </div>
              </div>

              <!-- Core Highlights -->
              <div class="grid grid-cols-2 gap-2 text-xs text-slate-300">
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-amber-400 shrink-0"></i>
                  <span>AI &amp; Software Planning</span>
                </div>
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-amber-400 shrink-0"></i>
                  <span>Mechanical Design Execution</span>
                </div>
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-amber-400 shrink-0"></i>
                  <span>Custom Fabrication</span>
                </div>
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-amber-400 shrink-0"></i>
                  <span>Deliverable Management</span>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-white/10 flex items-center justify-between">
              <span class="text-xs text-slate-400 font-medium">From Bid to Execution &amp; Delivery</span>
              <a href="#services" class="text-xs font-bold text-amber-400 hover:text-amber-300 inline-flex items-center gap-1">
                Explore Mechanical Scope <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

          <!-- RIGHT SIDE: SOFTWARE ENGINEERING -->
          <div class="thrunox-card rounded-2xl p-6 sm:p-8 relative overflow-hidden group flex flex-col justify-between cad-grid">
            <!-- Subtle slow reverse spinning cyber circuit in background -->
            <div class="absolute -top-16 -right-16 w-64 h-64 border border-cyan-500/10 rounded-full pointer-events-none animate-slow-spin-reverse">
              <div class="absolute inset-6 border border-dotted border-amber-400/15 rounded-full"></div>
            </div>

            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-slate-900/80 border border-cyan-500/30 text-cyan-300 text-xs font-bold uppercase tracking-wider">
                  <i data-lucide="code-2" class="w-3.5 h-3.5 animate-pulse"></i> Software Engineering
                </span>
                <span class="text-[11px] font-mono text-slate-400 flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span> Cloud &amp; Digital Twin
                </span>
              </div>

              <h3 class="text-xl sm:text-2xl font-bold text-white mb-2 group-hover:text-cyan-300 transition-colors">
                Software Systems &amp; Connected Architecture
              </h3>
              <p class="text-xs sm:text-sm text-slate-300 mb-6 leading-relaxed">
                Full-stack software engineering, distributed cloud architecture, data pipelines, and research towards an accessible Digital Twin &amp; Virtual Sandbox for MSMEs.
              </p>

              <!-- Image Container with Slow Floating / Pulse Animation -->
              <div class="relative rounded-xl overflow-hidden mb-6 aspect-video border border-white/10 group-hover:border-cyan-500/30 transition-all shadow-xl">
                <img src="images/software-hero.jpg" alt="Software Engineering Code and Systems Architecture" class="w-full h-full object-cover transform scale-100 group-hover:scale-105 transition-transform duration-1000 ease-out">
                <div class="absolute inset-0 bg-gradient-to-t from-[#070a10] via-transparent to-transparent"></div>
                
                <!-- Terminal Code HUD Overlay -->
                <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-[11px] font-mono text-cyan-200 bg-slate-900/85 backdrop-blur-md px-3 py-1.5 rounded-lg border border-white/10">
                  <span class="flex items-center gap-1.5 text-amber-300"><i data-lucide="terminal" class="w-3.5 h-3.5"></i> twin.evaluate()</span>
                  <span>Pipeline: Active</span>
                  <span class="text-emerald-400">&lt; 12ms Latency</span>
                </div>
              </div>

              <!-- Core Highlights -->
              <div class="grid grid-cols-2 gap-2 text-xs text-slate-300">
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cyan-400 shrink-0"></i>
                  <span>Cloud &amp; Edge Architecture</span>
                </div>
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cyan-400 shrink-0"></i>
                  <span>Digital Twin Virtual Sandbox</span>
                </div>
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cyan-400 shrink-0"></i>
                  <span>Workflow Modelling</span>
                </div>
                <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 flex items-center gap-2">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cyan-400 shrink-0"></i>
                  <span>Digital Compliance APIs</span>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-white/10 flex items-center justify-between">
              <span class="text-xs text-slate-400 font-medium">From Strategy to Digital Execution</span>
              <a href="#innovation" class="text-xs font-bold text-cyan-400 hover:text-cyan-300 inline-flex items-center gap-1">
                Explore Software &amp; Sandbox <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

        </div>
      </div>

      <!-- Section 2: What We Focus On (Tab 1, Section 2) -->
      <div class="mt-16 pt-12 border-t border-white/10">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold text-white mb-3">Our Focus Areas</h2>
          <p class="text-sm text-slate-400">Structured competencies designed to bring clarity, discipline, and measurable outcomes to operational challenges.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          <div class="thrunox-card p-6 rounded-xl">
            <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <i data-lucide="briefcase" class="w-5 h-5"></i>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Business Operations &amp; Project Execution</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Bringing structure, coordination and accountability to operational initiatives.
            </p>
          </div>

          <div class="thrunox-card p-6 rounded-xl">
            <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <i data-lucide="truck" class="w-5 h-5"></i>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Supply Chain &amp; Process Improvement</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Supporting better visibility, coordination and workflow efficiency.
            </p>
          </div>

          <div class="thrunox-card p-6 rounded-xl">
            <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <i data-lucide="calculator" class="w-5 h-5"></i>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Financial &amp; Revenue Cycle Support</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Helping organisations organise accounting, bookkeeping and revenue cycle processes.
            </p>
          </div>

          <div class="thrunox-card p-6 rounded-xl">
            <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <i data-lucide="shield-check" class="w-5 h-5"></i>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Regulatory &amp; Digital Compliance Coordination</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Supporting defined licensing, liaisoning and digital compliance requirements.
            </p>
          </div>

          <div class="thrunox-card p-6 rounded-xl">
            <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <i data-lucide="cpu" class="w-5 h-5"></i>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Technology &amp; Innovation</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Exploring practical digital solutions for operational challenges.
            </p>
          </div>

          <div class="thrunox-card p-6 rounded-xl">
            <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <i data-lucide="leaf" class="w-5 h-5"></i>
            </div>
            <h3 class="text-base font-bold text-white mb-2">Sustainability &amp; ESG Advisory</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Supporting organisations in understanding and structuring their environmental, social and governance requirements.
            </p>
          </div>

        </div>
      </div>

      <!-- Section 3: Innovation Direction (Tab 1, Section 3) -->
      <div class="mt-16 p-8 rounded-2xl thrunox-card border-amber-600/30 relative overflow-hidden">
        <div class="max-w-3xl">
          <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-2">Innovation Direction</span>
          <h3 class="text-2xl font-bold text-white mb-4">Building Towards More Accessible Industrial Simulation</h3>
          <p class="text-sm text-slate-300 leading-relaxed mb-4">
            Our current work across Business Operations, Engineering, Compliance and Technology Services helps us understand the practical challenges organisations face in planning, coordinating and improving complex workflows. These real-world insights will inform our long-term vision of developing an affordable Digital Twin &amp; Virtual Sandbox Platform that enables MSMEs to model processes, evaluate operational scenarios and validate decisions before committing to physical implementation.
          </p>
          <p class="text-xs text-slate-400 leading-relaxed mb-6">
            The long-term vision is to make practical simulation and evidence-based operational decision-making more accessible to businesses that may not have the resources or specialist teams required for complex industrial simulation platforms. This initiative is at the concept and development-planning stage. Its scope will be refined through technical exploration, prototype development and appropriate validation.
          </p>
          <a href="#innovation" class="btn-gold px-4 py-2.5 rounded-xl font-bold text-xs inline-flex items-center gap-2">
            Explore Innovation &amp; Solutions <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>
      </div>

      <!-- Why Thrunox & Approach (From Brochure) -->
      <div class="mt-16 grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div class="thrunox-card p-8 rounded-2xl">
          <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-2">Why Thrunox ?</span>
          <h3 class="text-2xl font-bold text-white mb-6">Proven Leadership &amp; Execution Discipline</h3>
          <ul class="space-y-4 text-sm text-slate-300">
            <li class="flex items-start gap-3">
              <i data-lucide="award" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
              <span><strong>75+ years of combined leadership experience</strong> delivering across complex engineering, operations, and regulatory landscapes.</span>
            </li>
            <li class="flex items-start gap-3">
              <i data-lucide="check-circle-2" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
              <span><strong>Cross-industry expertise</strong> covering Deep-Tech, Manufacturing, Engineering Fabrication, Pharma &amp; Healthcare.</span>
            </li>
            <li class="flex items-start gap-3">
              <i data-lucide="trending-up" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
              <span><strong>Execution-led consulting</strong> — beyond advisory to hands-on coordination and measurable results.</span>
            </li>
            <li class="flex items-start gap-3">
              <i data-lucide="zap" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
              <span><strong>Measurable impact</strong> on cost rationalization, operational efficiency, and scalable business governance.</span>
            </li>
          </ul>
        </div>

        <div class="thrunox-card p-8 rounded-2xl">
          <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-2">Our Structured Approach</span>
          <h3 class="text-2xl font-bold text-white mb-6">Execution-Driven Lifecycle</h3>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center mb-6">
            <div class="p-3 rounded-xl bg-white/5 border border-white/10">
              <div class="text-xs font-mono text-amber-400 mb-1">01</div>
              <div class="text-sm font-bold text-white">Diagnose</div>
              <div class="text-[11px] text-slate-400 mt-1">Data-driven insight</div>
            </div>
            <div class="p-3 rounded-xl bg-white/5 border border-white/10">
              <div class="text-xs font-mono text-amber-400 mb-1">02</div>
              <div class="text-sm font-bold text-white">Design</div>
              <div class="text-[11px] text-slate-400 mt-1">Structured blueprint</div>
            </div>
            <div class="p-3 rounded-xl bg-white/5 border border-white/10">
              <div class="text-xs font-mono text-amber-400 mb-1">03</div>
              <div class="text-sm font-bold text-white">Deliver</div>
              <div class="text-[11px] text-slate-400 mt-1">Hands-on execution</div>
            </div>
            <div class="p-3 rounded-xl bg-white/5 border border-white/10">
              <div class="text-xs font-mono text-amber-400 mb-1">04</div>
              <div class="text-sm font-bold text-white">Sustain</div>
              <div class="text-[11px] text-slate-400 mt-1">Scalable governance</div>
            </div>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed italic">
            "We combine data-driven insights with hands-on implementation, ensuring outcomes are realized — not just recommended."
          </p>
        </div>
      </div>

      <!-- Section 4: Company Brochure Section (Tab 1, Section 4) -->
      <div class="mt-16 text-center p-8 rounded-2xl bg-gradient-to-r from-amber-950/30 via-slate-900 to-amber-950/30 border border-amber-600/30">
        <h3 class="text-xl sm:text-2xl font-bold text-white mb-3">Explore Thrunox Systems</h3>
        <p class="text-sm text-slate-300 max-w-2xl mx-auto mb-6">
          Download our company brochure to learn more about Thrunox Systems, our service areas, industry focus and approach to business execution.
        </p>
        <a href="Thrunox-Systems-Company-Brochure.pdf" download="Thrunox-Systems-Company-Brochure.pdf" class="btn-gold px-6 py-3 rounded-xl font-bold text-sm inline-flex items-center gap-2">
          <i data-lucide="file-text" class="w-4 h-4"></i> Download Company Brochure
        </a>
      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- TAB 2: SERVICES                            -->
  <!-- ========================================== -->
  <section id="services" class="py-24 relative z-10 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section 1: Services Introduction -->
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-3">Our Services</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mb-4">Practical Support for Business Execution</h2>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
          Every business faces operational, financial, regulatory and organisational challenges that require the right combination of planning, coordination and specialist support.
        </p>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">
          Thrunox Systems helps businesses structure these requirements and explore practical ways to address them. Depending on the engagement, we coordinate with relevant professionals and specialist service partners to support defined business objectives.
        </p>
      </div>

      <!-- Section 2: Service Verticals (Stacked Cards with Specific CTAs) -->
      <div class="space-y-12">
        
        <!-- ========================================== -->
        <!-- Service 1: Project Management & Operations -->
        <!-- ========================================== -->
        <div class="thrunox-card p-6 sm:p-10 rounded-2xl border-white/10 relative">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-white/10 mb-8">
            <div>
              <span class="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest block mb-1">Service 1</span>
              <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Project Management, Operations &amp; Supply Chain</h3>
              <p class="text-xs sm:text-sm text-slate-400 mt-1">From Bid to Execution — Delivered with Control from Tendering to Delivery to Operations.</p>
            </div>
            <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20would%20like%20to%20discuss%20a%20requirement%20related%20to%20Project%20Management,%20Operations%20%26%20Supply%20Chain." target="_blank" class="btn-gold px-4 py-2.5 rounded-xl font-bold text-xs inline-flex items-center gap-2 self-start md:self-auto shrink-0">
              <i data-lucide="message-circle" class="w-4 h-4"></i> Discuss Your Requirements
            </a>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            
            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-3 flex items-center gap-2">
                <i data-lucide="file-check" class="w-4 h-4"></i> Pre-Project / Tendering
              </div>
              <ul class="text-xs text-slate-300 space-y-2">
                <li>• Tender Tracking (GeM, CPPP &amp; State)</li>
                <li>• Tender Document Analysis</li>
                <li>• Bid / No-Bid Decision Support</li>
                <li>• Tender Filing &amp; Submission</li>
                <li>• BOQ Preparation &amp; Pricing Strategy</li>
                <li>• Technical &amp; Commercial Compliance</li>
              </ul>
            </div>

            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-3 flex items-center gap-2">
                <i data-lucide="cpu" class="w-4 h-4"></i> Project Management
              </div>
              <ul class="text-xs text-slate-300 space-y-2">
                <li>• AI &amp; Software Project Execution</li>
                <li>• Mechanical Design &amp; CAD Execution</li>
                <li>• Custom Fabrication Execution</li>
                <li>• Technical Resource Coordination</li>
                <li>• Risk Mitigation &amp; Monitoring</li>
              </ul>
            </div>

            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-3 flex items-center gap-2">
                <i data-lucide="sliders" class="w-4 h-4"></i> Operations Management
              </div>
              <ul class="text-xs text-slate-300 space-y-2">
                <li>• Process Optimization</li>
                <li>• Efficiency Improvement</li>
                <li>• Cost Rationalization</li>
                <li>• Resource Alignment</li>
                <li>• Scalable Operational Frameworks</li>
              </ul>
            </div>

            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-3 flex items-center gap-2">
                <i data-lucide="truck" class="w-4 h-4"></i> Supply Chain
              </div>
              <ul class="text-xs text-slate-300 space-y-2">
                <li>• Procurement &amp; Vendor Optimization</li>
                <li>• Supply Chain Visibility</li>
                <li>• Coordination across stakeholders</li>
                <li>• Delay &amp; Inefficiency Reduction</li>
                <li>• Leakage Prevention Systems</li>
              </ul>
            </div>

          </div>

          <div class="mt-6 pt-4 border-t border-white/5 flex flex-wrap items-center justify-between text-xs text-slate-400 gap-2">
            <div><strong class="text-slate-300">Brochure Impact:</strong> Reduced delays &amp; cost overruns | Higher project success rates | Scalable frameworks</div>
            <a href="#contact" class="text-amber-400 hover:text-amber-300 font-bold inline-flex items-center gap-1">Initiate Project Scope &rarr;</a>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- Service 2: Accounting & US Healthcare RCM   -->
        <!-- ========================================== -->
        <div class="thrunox-card p-6 sm:p-10 rounded-2xl border-white/10 relative">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-white/10 mb-8">
            <div>
              <span class="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest block mb-1">Service 2</span>
              <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Accounting, Bookkeeping &amp; Revenue Cycle Management (RCM)</h3>
              <p class="text-xs sm:text-sm text-slate-400 mt-1">Maximizing Revenue. Minimizing Leakage. We build systems ensuring predictable cash flow and compliance.</p>
            </div>
            <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20would%20like%20to%20discuss%20an%20Accounting,%20Bookkeeping%20or%20Revenue%20Cycle%20Management%20requirement." target="_blank" class="btn-gold px-4 py-2.5 rounded-xl font-bold text-xs inline-flex items-center gap-2 self-start md:self-auto shrink-0">
              <i data-lucide="message-circle" class="w-4 h-4"></i> Discuss Your Requirements
            </a>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">Accounting &amp; Bookkeeping (US Focus)</div>
              <p class="text-xs text-slate-400 mb-3">Enabling businesses to stay audit-ready, compliant, and financially informed:</p>
              <ul class="text-xs text-slate-300 space-y-1.5">
                <li>✔ Financial reporting &amp; forecasting</li>
                <li>✔ Payroll processing &amp; MIS reporting</li>
                <li>✔ Budgeting &amp; forecasting</li>
                <li>✔ Bank reconciliation</li>
                <li>✔ Centralized accounting &amp; SOP creation</li>
                <li>✔ Intercompany entries &amp; reconciliations</li>
              </ul>
              <div class="mt-4 p-2 rounded bg-amber-950/40 border border-amber-600/20 text-[11px] text-amber-300 font-semibold">
                Result: Clarity in numbers. Confidence in decisions.
              </div>
            </div>

            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">General Ledger &amp; US Tax Services</div>
              <p class="text-xs text-slate-400 mb-3">Precision-driven support for entities in the US ecosystem:</p>
              <ul class="text-xs text-slate-300 space-y-1.5">
                <li>✔ End-to-end General Ledger accounting</li>
                <li>✔ Audit-ready bookkeeping &amp; reconciliations</li>
                <li>✔ Virtual CPA support for NRIs, H1B/L1, F1 &amp; Green Card</li>
                <li>✔ US individual &amp; business tax returns</li>
                <li>✔ NRI filings &amp; cross-border compliance</li>
                <li>✔ CPT / OPT tax support</li>
              </ul>
            </div>

            <div class="bg-white/5 p-5 rounded-xl border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">Revenue Cycle Management (RCM)</div>
              <p class="text-xs text-slate-400 mb-3">Built for Accuracy &amp; Speed across US Healthcare:</p>
              <ul class="text-xs text-slate-300 space-y-1.5">
                <li>✔ HIPAA-compliant, SOP-driven processes</li>
                <li>✔ Dedicated client-specific teams</li>
                <li>✔ Seamless EMR integration</li>
                <li>✔ Multi-level quality checks</li>
                <li>✔ Transparent MIS reporting</li>
                <li>✔ Time-zone advantage for faster turnaround</li>
              </ul>
              <div class="mt-4 p-2 rounded bg-amber-950/40 border border-amber-600/20 text-[11px] text-amber-300 font-semibold">
                Result: Higher collections, reduced denials, faster revenue realization.
              </div>
            </div>

          </div>
        </div>

        <!-- ========================================== -->
        <!-- Service 3: Compliance & Cyber Security      -->
        <!-- ========================================== -->
        <div class="thrunox-card p-6 sm:p-10 rounded-2xl border-white/10 relative">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-white/10 mb-8">
            <div>
              <span class="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest block mb-1">Service 3</span>
              <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Compliance &amp; Cyber Security</h3>
              <p class="text-xs sm:text-sm text-slate-400 mt-1">From Paperwork to Seamless Digital Execution &amp; Enterprise Cyber Resilience.</p>
            </div>
            <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20would%20like%20to%20enquire%20about%20Compliance%20%26%20Cyber%20Security%20Solutions." target="_blank" class="btn-gold px-4 py-2.5 rounded-xl font-bold text-xs inline-flex items-center gap-2 self-start md:self-auto shrink-0">
              <i data-lucide="shield" class="w-4 h-4"></i> Explore Solutions
            </a>
          </div>

          <!-- 3 Pillars: Licensing, Digital Signatures, Cyber Security -->
          <div class="space-y-8">
            
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <!-- Sub-part I: Licensing & Liaisoning -->
              <div class="p-5 rounded-xl bg-white/5 border border-white/5">
                <span class="text-xs font-mono text-amber-400 font-bold uppercase block mb-1">Part I</span>
                <h4 class="text-base font-bold text-white mb-2">Licensing, Liaisoning &amp; Strategic Consulting</h4>
                <p class="text-xs text-slate-300 mb-3">From documentation to final approvals — we take complete ownership:</p>
                <ul class="text-xs text-slate-300 space-y-2">
                  <li><strong>▪ Single Point of Contact:</strong> One dedicated partner managing departments, follow-ups, and coordination.</li>
                  <li><strong>▪ Faster Approvals:</strong> Structured follow-ups and strong ground-level understanding to help reduce delays.</li>
                  <li><strong>▪ Strategy + Execution Integration:</strong> We don't just advise — we help turn plans into action.</li>
                </ul>
              </div>

              <!-- Sub-part II: Digital Signature & E-Signature -->
              <div class="p-5 rounded-xl bg-white/5 border border-white/5">
                <span class="text-xs font-mono text-amber-400 font-bold uppercase block mb-1">Part II</span>
                <h4 class="text-base font-bold text-white mb-2">Digital Signature &amp; E-Signature Solutions</h4>
                <p class="text-xs text-slate-300 mb-3">Partnered with leading licensed Certifying Authorities and Digital Compliance Providers:</p>
                <div class="grid grid-cols-2 gap-2 text-xs text-slate-300">
                  <div>• Class 3 DSC (Individuals &amp; Org)</div>
                  <div>• Foreign National DSCs</div>
                  <div>• Aadhaar-based e-Sign</div>
                  <div>• OTP-based authentication</div>
                  <div>• Bulk Document Signing</div>
                  <div>• Enterprise API Integration</div>
                </div>
                <div class="mt-3 text-[11px] text-amber-300 font-semibold">
                  ✔ Government-compliant solutions | Faster onboarding | Secure digital workflows
                </div>
              </div>
            </div>

            <!-- Sub-part III: Cyber Security Solutions (7 Focus Areas from Content Doc) -->
            <div>
              <span class="text-xs font-mono text-amber-400 font-bold uppercase block mb-2">Part III</span>
              <h4 class="text-lg font-bold text-white mb-4">Cyber Security Solutions (7 Core Capabilities)</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                
                <div class="p-4 rounded-lg bg-black/40 border border-white/5">
                  <div class="text-amber-400 font-bold text-xs mb-1">1. VAPT Assessments</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Identify security weaknesses across websites, APIs, mobile apps, networks, and cloud environments.
                  </p>
                </div>

                <div class="p-4 rounded-lg bg-black/40 border border-white/5">
                  <div class="text-amber-400 font-bold text-xs mb-1">2. Cyber Risk Review</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Security gap assessments, attack-surface reviews, access-control assessments, and risk prioritisation.
                  </p>
                </div>

                <div class="p-4 rounded-lg bg-black/40 border border-white/5">
                  <div class="text-amber-400 font-bold text-xs mb-1">3. DPDP Compliance</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Assess personal data handling, consent processes, data flows, and breach preparedness under DPDP.
                  </p>
                </div>

                <div class="p-4 rounded-lg bg-black/40 border border-white/5">
                  <div class="text-amber-400 font-bold text-xs mb-1">4. ISO 27001 Readiness</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Structured ISMS approach through gap analysis, security policies, control mapping, and audit coordination.
                  </p>
                </div>

                <div class="p-4 rounded-lg bg-black/40 border border-white/5">
                  <div class="text-amber-400 font-bold text-xs mb-1">5. Exposure Monitoring</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Visibility into exposed digital assets, cloud configurations, credential leaks, and coordinated remediation.
                  </p>
                </div>

                <div class="p-4 rounded-lg bg-black/40 border border-white/5">
                  <div class="text-amber-400 font-bold text-xs mb-1">6. Incident Response</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Evidence preservation, response planning, and translating incident findings into tightened controls.
                  </p>
                </div>

                <div class="p-4 rounded-lg bg-black/40 border border-white/5 col-span-1 sm:col-span-2">
                  <div class="text-amber-400 font-bold text-xs mb-1">7. Security Awareness &amp; Governance</div>
                  <p class="text-[11px] text-slate-300 leading-relaxed">
                    Employee education, phishing simulations, access-management governance, and incident-reporting procedures.
                  </p>
                </div>

              </div>
            </div>

          </div>
        </div>

        <!-- ========================================== -->
        <!-- Service 4: ESG Advisory                     -->
        <!-- ========================================== -->
        <div class="thrunox-card p-6 sm:p-10 rounded-2xl border-white/10 relative">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-white/10 mb-8">
            <div>
              <span class="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest block mb-1">Service 4</span>
              <h3 class="text-2xl sm:text-3xl font-extrabold text-white">ESG Advisory &amp; Sustainable Operations</h3>
              <p class="text-xs sm:text-sm text-slate-400 mt-1">Building Responsible and Future-Ready Businesses.</p>
            </div>
            <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20would%20like%20to%20discuss%20an%20ESG%20Advisory%20requirement." target="_blank" class="btn-gold px-4 py-2.5 rounded-xl font-bold text-xs inline-flex items-center gap-2 self-start md:self-auto shrink-0">
              <i data-lucide="leaf" class="w-4 h-4"></i> Discuss Your ESG Requirements
            </a>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <div class="p-5 rounded-xl bg-white/5 border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">Framework Development</div>
              <p class="text-xs text-slate-300">Designing practical, business-aligned ESG strategies and execution frameworks.</p>
            </div>
            <div class="p-5 rounded-xl bg-white/5 border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">Regulatory Alignment</div>
              <p class="text-xs text-slate-300">Supporting requirements such as BRSR, ESG disclosures, and relevant global benchmarks.</p>
            </div>
            <div class="p-5 rounded-xl bg-white/5 border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">Data, Reporting &amp; MIS</div>
              <p class="text-xs text-slate-300">Building measurable ESG tracking, reporting, and monitoring systems.</p>
            </div>
            <div class="p-5 rounded-xl bg-white/5 border border-white/5">
              <div class="text-amber-400 font-bold text-sm mb-2">Process Integration</div>
              <p class="text-xs text-slate-300">Embedding ESG principles into operations, supply chains, and governance structures.</p>
            </div>
          </div>

          <div class="p-4 rounded-xl bg-black/40 border border-white/5 flex flex-wrap items-center justify-between text-xs text-slate-300 gap-4">
            <div>
              <strong class="text-amber-400">Our Approach:</strong> Define &rarr; Implement &rarr; Monitor &rarr; Improve
            </div>
            <div>
              <strong class="text-amber-400">Why It Matters:</strong> Investor confidence • Regulatory compliance • Brand credibility • Long-term sustainability
            </div>
          </div>
        </div>

      </div>

      <!-- Section 3: Service Enquiry Banner (Tab 2, Section 3) -->
      <div class="mt-16 text-center p-8 sm:p-12 rounded-2xl thrunox-card border-amber-600/30">
        <h3 class="text-2xl sm:text-3xl font-bold text-white mb-3">Have a Specific Business Requirement?</h3>
        <p class="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto mb-6">
          Not every business challenge fits neatly into one category. Tell us what you are trying to achieve, and we can explore the appropriate scope, capabilities and next steps with you.
        </p>
        <a href="#contact" class="btn-gold px-6 py-3 rounded-xl font-bold text-sm inline-flex items-center gap-2">
          Contact Thrunox Systems <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- TAB 3: INDUSTRIES                          -->
  <!-- ========================================== -->
  <section id="industries" class="py-24 relative z-10 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section 1: Industries Introduction -->
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-3">Industries We Support</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mb-4">Solutions Shaped Around Industry Requirements</h2>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
          Different industries operate under different technical, operational, regulatory and commercial constraints.
        </p>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">
          Thrunox Systems focuses on understanding these differences before structuring an engagement. Our service capabilities and specialist collaborations can be aligned with the requirements of the organisation, the operating environment and the agreed scope of work.
        </p>
      </div>

      <!-- Section 2: Industry Domains (4 Focus Areas) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
        
        <!-- Domain 1: Deep-Tech -->
        <div class="thrunox-card p-8 rounded-2xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400">
                <i data-lucide="cpu" class="w-5 h-5"></i>
              </div>
              <h3 class="text-xl font-bold text-white">1. Deep-Tech &amp; Technology-Led Businesses</h3>
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-6">
              Technology-led businesses often need to coordinate product development, business operations, documentation, specialist resources and commercial execution.
            </p>
            <p class="text-xs text-slate-400 mb-6">
              Thrunox Systems aims to support defined operational and execution requirements while exploring practical technology solutions that address real business needs.
            </p>
          </div>
          <div class="pt-4 border-t border-white/10 text-xs text-amber-300 font-mono">
            <strong>Relevant areas:</strong> Project coordination, process structuring, digital compliance, specialist coordination and technology-led solution exploration.
          </div>
        </div>

        <!-- Domain 2: Manufacturing & Industrial Operations -->
        <div class="thrunox-card p-8 rounded-2xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400">
                <i data-lucide="factory" class="w-5 h-5"></i>
              </div>
              <h3 class="text-xl font-bold text-white">2. Manufacturing &amp; Industrial Operations</h3>
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-6">
              Manufacturing environments depend on coordinated workflows, capacity planning, resource utilisation, supply chain visibility and reliable operational processes.
            </p>
            <p class="text-xs text-slate-400 mb-6">
              Thrunox Systems focuses on relevant execution and process requirements, while its longer-term innovation direction includes exploring accessible tools for simplified production-flow modelling and operational scenario evaluation.
            </p>
          </div>
          <div class="pt-4 border-t border-white/10 text-xs text-amber-300 font-mono">
            <strong>Relevant areas:</strong> Project and operations coordination, supply chain support, process improvement, documentation and manufacturing simulation concepts.
          </div>
        </div>

        <!-- Domain 3: Engineering Services & Fabrication -->
        <div class="thrunox-card p-8 rounded-2xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400">
                <i data-lucide="wrench" class="w-5 h-5"></i>
              </div>
              <h3 class="text-xl font-bold text-white">3. Engineering Services &amp; Fabrication</h3>
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-6">
              Engineering and fabrication businesses operate across technical requirements, project schedules, material coordination, vendor dependencies and delivery commitments.
            </p>
            <p class="text-xs text-slate-400 mb-6">
              Thrunox Systems aims to help structure and coordinate defined business and operational requirements, with specialist engineering activities undertaken through appropriately qualified resources where required.
            </p>
          </div>
          <div class="pt-4 border-t border-white/10 text-xs text-amber-300 font-mono">
            <strong>Relevant areas:</strong> Project coordination, procurement &amp; vendor coordination, workflow structuring, operational documentation and engineering solution exploration.
          </div>
        </div>

        <!-- Domain 4: Pharmaceutical & Healthcare -->
        <div class="thrunox-card p-8 rounded-2xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-lg bg-amber-950/50 border border-amber-500/30 flex items-center justify-center text-amber-400">
                <i data-lucide="activity" class="w-5 h-5"></i>
              </div>
              <h3 class="text-xl font-bold text-white">4. Pharmaceutical, Healthcare &amp; Medical Equipment</h3>
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-6">
              Healthcare and medical equipment environments involve specialised workflows, documentation requirements, quality considerations and regulatory processes.
            </p>
            <p class="text-xs text-slate-400 mb-6">
              Thrunox Systems aims to support relevant operational coordination, defined documentation and licensing-related workstreams, and the exploration of practical healthcare and medical equipment solutions.
            </p>
          </div>
          <div class="pt-4 border-t border-white/10 text-xs text-amber-300 font-mono">
            <strong>Relevant areas:</strong> Healthcare operations concepts, disaster management concepts, mobile laboratory solutions, licensing coordination and medical equipment innovation.
          </div>
        </div>

      </div>

      <!-- Section 3: Industry Call to Action -->
      <div class="text-center p-8 sm:p-10 rounded-2xl bg-gradient-to-r from-amber-950/20 via-slate-900 to-amber-950/20 border border-amber-600/30">
        <h3 class="text-xl sm:text-2xl font-bold text-white mb-3">Let Us Understand Your Industry Requirement</h3>
        <p class="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto mb-6 leading-relaxed">
          Share your business context, the challenge you are addressing and the outcome you are seeking. We will review the requirement and explore whether our service capabilities or specialist collaborations are suitable.
        </p>
        <a href="#contact" class="btn-gold px-6 py-3 rounded-xl font-bold text-sm inline-flex items-center gap-2">
          Discuss Your Requirement <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- TAB 4: INNOVATION & SOLUTIONS              -->
  <!-- ========================================== -->
  <section id="innovation" class="py-24 relative z-10 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section 1: Innovation Introduction -->
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-3">Innovation &amp; Solutions</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mb-4">Practical Ideas. Purposeful Solutions.</h2>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
          At Thrunox Systems, we explore solutions that address practical operational and business challenges. Our innovation direction focuses on making technology more accessible, improving how organisations evaluate decisions and developing structured solutions around real-world requirements.
        </p>
        <p class="text-xs sm:text-sm text-slate-400 mt-2">
          Our portfolio brings together selected healthcare-related solution concepts and a longer-term vision for affordable industrial simulation for MSMEs. Each initiative will progress according to its technical feasibility, development status, validation requirements and intended use.
        </p>
      </div>

      <!-- Section 2: Affordable Digital Twin & Virtual Sandbox -->
      <div class="thrunox-card p-8 sm:p-12 rounded-2xl border-amber-600/40 relative mb-16">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-6">
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-amber-950/60 border border-amber-500/40 text-amber-300 text-xs font-bold uppercase tracking-wider">
            Concept &amp; Development Planning
          </span>
          <span class="text-xs font-mono text-slate-400">Targeting MSMEs Across Industrial &amp; Medical Manufacturing</span>
        </div>

        <h3 class="text-2xl sm:text-3xl font-extrabold text-white mb-4">
          1) Affordable Digital Twin &amp; Virtual Sandbox for MSMEs
        </h3>
        <p class="text-base font-semibold text-amber-400 mb-4">Evaluate Before You Implement</p>
        
        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">
          Small and medium-sized manufacturers may need to assess production layouts, capacity constraints, workflow changes and operational scenarios before committing to physical changes. However, complex simulation solutions can require specialist expertise, implementation effort and investment.
        </p>
        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-6">
          Thrunox Systems is exploring an affordable Digital Twin &amp; Virtual Sandbox platform intended to make selected forms of operational modelling and scenario evaluation more accessible to MSMEs. The initial product-development direction is intended to address selected operational modelling needs in:
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-8">
          <div class="p-3.5 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-200 font-semibold flex items-center gap-2">
            <i data-lucide="check" class="w-4 h-4 text-amber-400"></i> Industrial Equipment &amp; Manufacturing
          </div>
          <div class="p-3.5 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-200 font-semibold flex items-center gap-2">
            <i data-lucide="check" class="w-4 h-4 text-amber-400"></i> Healthcare &amp; Medical Equipment
          </div>
          <div class="p-3.5 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-200 font-semibold flex items-center gap-2">
            <i data-lucide="check" class="w-4 h-4 text-amber-400"></i> Medical Devices
          </div>
        </div>

        <!-- Section 3: Proposed Platform Modules -->
        <div class="mb-10">
          <h4 class="text-lg font-bold text-white mb-4">Proposed Platform Modules (Concept Stage)</h4>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            <div class="p-5 rounded-xl bg-black/40 border border-white/5">
              <span class="text-[11px] font-mono text-amber-400 uppercase font-bold block mb-1">Module A • Concept</span>
              <h5 class="text-base font-bold text-white mb-2">Production Flow Modelling</h5>
              <p class="text-xs text-slate-300 leading-relaxed mb-3">
                Explore how selected production steps, resources and workflow arrangements may interact within a simplified manufacturing model.
              </p>
              <div class="text-[11px] text-slate-400 font-mono">
                Internal concept: <em>Factory Flow Sandbox</em>
              </div>
            </div>

            <div class="p-5 rounded-xl bg-black/40 border border-white/5">
              <span class="text-[11px] font-mono text-amber-400 uppercase font-bold block mb-1">Module B • Concept</span>
              <h5 class="text-base font-bold text-white mb-2">Capacity &amp; Process Constraints</h5>
              <p class="text-xs text-slate-300 leading-relaxed mb-3">
                Explore selected process constraints, resource limitations and potential bottlenecks within a simplified operational model.
              </p>
              <div class="text-[11px] text-slate-400 font-mono">
                Internal concept: <em>Capacity &amp; Bottleneck Analyzer</em>
              </div>
            </div>

            <div class="p-5 rounded-xl bg-black/40 border border-white/5">
              <span class="text-[11px] font-mono text-amber-400 uppercase font-bold block mb-1">Module C • Concept</span>
              <h5 class="text-base font-bold text-white mb-2">Scenario Comparison &amp; Reports</h5>
              <p class="text-xs text-slate-300 leading-relaxed mb-3">
                Compare selected operational scenarios and organise their model outputs into a structured format for review.
              </p>
              <div class="text-[11px] text-slate-400 font-mono">
                Internal concept: <em>What-if Scenario &amp; Evidence Studio</em>
              </div>
            </div>

          </div>
        </div>

        <!-- Section 4: How the Concept is Intended to Help (4-step model) -->
        <div>
          <h4 class="text-lg font-bold text-white mb-4">From Operational Questions to Structured Evaluation</h4>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div class="p-4 rounded-xl bg-white/5 border border-white/5">
              <div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-300 font-bold mx-auto flex items-center justify-center mb-2">1</div>
              <div class="text-xs font-bold text-white">Represent</div>
              <p class="text-[11px] text-slate-400 mt-1">Define a simplified model of a selected process or workflow.</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/5">
              <div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-300 font-bold mx-auto flex items-center justify-center mb-2">2</div>
              <div class="text-xs font-bold text-white">Explore</div>
              <p class="text-[11px] text-slate-400 mt-1">Evaluate selected operating scenarios within the model.</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/5">
              <div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-300 font-bold mx-auto flex items-center justify-center mb-2">3</div>
              <div class="text-xs font-bold text-white">Compare</div>
              <p class="text-[11px] text-slate-400 mt-1">Review differences between scenarios and stated assumptions.</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/5">
              <div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-300 font-bold mx-auto flex items-center justify-center mb-2">4</div>
              <div class="text-xs font-bold text-white">Assess</div>
              <p class="text-[11px] text-slate-400 mt-1">Input structured results into operational decision-making.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Section 6: Existing Healthcare-Related Solution Concepts -->
      <div class="mb-16">
        <div class="text-center max-w-2xl mx-auto mb-10">
          <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-2">Proposed Directions</span>
          <h3 class="text-2xl font-bold text-white">Healthcare-Related Solution Concepts</h3>
          <p class="text-xs text-slate-400 mt-1">Conceptual initiatives exploring structured workflows, modular disaster coordination, and mobile laboratory setups.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <div class="thrunox-card p-6 rounded-2xl flex flex-col justify-between">
            <div>
              <span class="inline-block px-2.5 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-950/60 border border-amber-500/30 text-amber-300 mb-3">
                Concept
              </span>
              <h4 class="text-base font-bold text-white mb-2">Healthcare Operations &amp; Management Platform</h4>
              <p class="text-xs text-slate-300 leading-relaxed mb-4">
                A proposed solution direction focused on supporting the organisation and coordination of selected healthcare operational workflows. The concept may explore how structured information, workflow visibility and coordinated processes can help healthcare organisations manage defined operational activities.
              </p>
            </div>
            <div class="text-[11px] text-slate-400 pt-3 border-t border-white/5 italic">
              Scope and implementation model will be determined through further assessment.
            </div>
          </div>

          <div class="thrunox-card p-6 rounded-2xl flex flex-col justify-between">
            <div>
              <span class="inline-block px-2.5 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-950/60 border border-amber-500/30 text-amber-300 mb-3">
                Concept
              </span>
              <h4 class="text-base font-bold text-white mb-2">Modular Healthcare Disaster Management Platform</h4>
              <p class="text-xs text-slate-300 leading-relaxed mb-4">
                A proposed modular solution direction for supporting selected healthcare coordination requirements during disaster or emergency situations. The concept may explore modular workflows, resource coordination and information organisation to help stakeholders plan for defined operational needs.
              </p>
            </div>
            <div class="text-[11px] text-slate-400 pt-3 border-t border-white/5 italic">
              Actual deployment would require technical validation and compliance with applicable requirements.
            </div>
          </div>

          <div class="thrunox-card p-6 rounded-2xl flex flex-col justify-between">
            <div>
              <span class="inline-block px-2.5 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-950/60 border border-amber-500/30 text-amber-300 mb-3">
                Concept
              </span>
              <h4 class="text-base font-bold text-white mb-2">Modular &amp; Smart Mobile Laboratory Solutions</h4>
              <p class="text-xs text-slate-300 leading-relaxed mb-4">
                A proposed solution direction focused on modular and mobile laboratory environments designed around defined testing, equipment, workflow and deployment requirements. The concept may explore modular layouts, operational coordination and appropriate technology integration.
              </p>
            </div>
            <div class="text-[11px] text-slate-400 pt-3 border-t border-white/5 italic">
              Actual capabilities, equipment suitability, and approvals would be established for each use case.
            </div>
          </div>

        </div>
      </div>

      <!-- Section 7: Innovation Enquiry (Tab 4, Section 7) -->
      <div class="text-center p-8 sm:p-12 rounded-2xl thrunox-card border-amber-600/30">
        <h3 class="text-2xl sm:text-3xl font-bold text-white mb-3">Interested in Exploring a Solution With Us?</h3>
        <p class="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto mb-6 leading-relaxed">
          We welcome conversations with MSMEs, industry professionals, engineering specialists, technology developers and potential collaborators interested in exploring practical solutions to operational challenges. Share your use case, technical requirement or collaboration interest to begin a discussion.
        </p>
        <div class="flex flex-wrap items-center justify-center gap-4">
          <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20would%20like%20to%20discuss%20an%20Innovation%20%26%20Solutions%20requirement%20or%20potential%20collaboration." target="_blank" class="btn-gold px-5 py-3 rounded-xl font-bold text-xs sm:text-sm inline-flex items-center gap-2">
            <i data-lucide="message-circle" class="w-4 h-4"></i> Discuss an Innovation Requirement
          </a>
          <a href="#careers" class="btn-secondary px-5 py-3 rounded-xl font-bold text-xs sm:text-sm inline-flex items-center gap-2">
            <i data-lucide="users" class="w-4 h-4 text-amber-400"></i> Explore Collaboration Opportunities
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- TAB 5: CAREERS & COLLABORATIONS            -->
  <!-- ========================================== -->
  <section id="careers" class="py-24 relative z-10 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-3">Partnerships &amp; Talent</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mb-4">Careers &amp; Collaborations</h2>
        <p class="text-base font-semibold text-amber-400 mb-4">Build Capabilities. Create Practical Impact.</p>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed mb-4">
          Thrunox Systems welcomes conversations with professionals, independent specialists, consultants, technology developers and organisations interested in contributing to practical business and technology solutions.
        </p>
        <p class="text-xs sm:text-sm text-slate-400 leading-relaxed">
          We believe effective collaboration brings together complementary expertise, clear responsibilities and a shared focus on delivering defined outcomes.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
        
        <div class="thrunox-card p-8 rounded-2xl">
          <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
            <i data-lucide="network" class="w-5 h-5 text-amber-400"></i> Areas for Collaboration
          </h3>
          <ul class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm text-slate-300">
            <li class="flex items-center gap-2">• Project Management &amp; Supply Chain</li>
            <li class="flex items-center gap-2">• Accounting, Bookkeeping &amp; RCM</li>
            <li class="flex items-center gap-2">• Licensing &amp; Liaisoning</li>
            <li class="flex items-center gap-2">• Cyber Security &amp; Cyber Resilience</li>
            <li class="flex items-center gap-2">• ESG Advisory</li>
            <li class="flex items-center gap-2">• Software, Data &amp; AI Solutions</li>
            <li class="flex items-center gap-2">• Mechanical Design &amp; Fabrication</li>
            <li class="flex items-center gap-2">• Digital Twin &amp; Industrial Simulation</li>
          </ul>
        </div>

        <div class="thrunox-card p-8 rounded-2xl flex flex-col justify-between">
          <div>
            <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
              <i data-lucide="handshake" class="w-5 h-5 text-amber-400"></i> How We Collaborate
            </h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">
              Depending on the requirement, an association may take the form of a project-based engagement, specialist service partnership, independent professional collaboration or another mutually agreed arrangement.
            </p>
            <p class="text-xs text-slate-400 leading-relaxed">
              The scope, responsibilities, commercial terms and expected contribution will be discussed and agreed before a specific engagement begins.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-white/10 flex items-center justify-between">
            <span class="text-xs text-slate-300 font-semibold">Interested in working with us?</span>
            <button onclick="prefillContactForm('Careers & Collaborations')" class="btn-gold px-4 py-2 rounded-xl text-xs font-bold inline-flex items-center gap-1.5">
              Express Your Interest <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- TAB 6: CONTACT US                          -->
  <!-- ========================================== -->
  <section id="contact" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 block mb-3">Get in Touch</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mb-4">Contact Thrunox Systems</h2>
        <p class="text-base font-semibold text-amber-400 mb-4">Tell Us What You Need to Achieve</p>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
          Whether you are looking for business execution support, operational coordination, regulatory documentation assistance, digital compliance solutions or a potential technology collaboration, we welcome the opportunity to understand your requirement.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Contact Information Cards (5 Cols) -->
        <div class="lg:col-span-5 space-y-6">
          
          <div class="thrunox-card p-6 sm:p-8 rounded-2xl">
            <h3 class="text-lg font-bold text-white mb-4">Direct Contact Details</h3>
            <ul class="space-y-4 text-xs sm:text-sm text-slate-300">
              <li class="flex items-start gap-3">
                <i data-lucide="mail" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
                <div>
                  <strong class="text-white block">Email</strong>
                  <a href="mailto:contact@thrunoxsystems.in?bcc=thrunoxsystems@gmail.com" class="hover:text-amber-400 transition-colors">contact@thrunoxsystems.in</a>
                  <span class="block text-[11px] text-slate-400">BCC: thrunoxsystems@gmail.com</span>
                </div>
              </li>
              <li class="flex items-start gap-3">
                <i data-lucide="phone" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
                <div>
                  <strong class="text-white block">Direct Line &amp; WhatsApp</strong>
                  <a href="tel:+919980182009" class="hover:text-amber-400 transition-colors">+91-9980182009</a>
                </div>
              </li>
              <li class="flex items-start gap-3">
                <i data-lucide="globe" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
                <div>
                  <strong class="text-white block">Official Website</strong>
                  <a href="https://thrunoxsystems.in" target="_blank" class="hover:text-amber-400 transition-colors">https://thrunoxsystems.in</a>
                </div>
              </li>
              <li class="flex items-start gap-3">
                <i data-lucide="map-pin" class="w-5 h-5 text-amber-400 shrink-0 mt-0.5"></i>
                <div>
                  <strong class="text-white block">Registered Office</strong>
                  <address class="not-italic text-slate-400 leading-relaxed text-xs">
                    Flat No. 201, Building No. 28, Bohra Layout, Bangalore South, Bengaluru, Karnataka – 560083.
                  </address>
                </div>
              </li>
            </ul>
          </div>

          <div class="thrunox-card p-6 rounded-2xl border-emerald-600/30">
            <h4 class="text-base font-bold text-white mb-2 flex items-center gap-2">
              <i data-lucide="message-circle" class="w-5 h-5 text-emerald-400"></i> Fast-Track WhatsApp
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-4">
              Connect directly with our partner desk for swift operational coordination or service inquiries.
            </p>
            <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20visited%20your%20website%20and%20would%20like%20to%20discuss%20a%20business%20requirement.%20Please%20let%20me%20know%20the%20appropriate%20next%20steps." target="_blank" class="w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-md transition-all">
              <i data-lucide="message-circle" class="w-4 h-4"></i> Start WhatsApp Conversation
            </a>
          </div>

        </div>

        <!-- Interactive Form (7 Cols) -->
        <div class="lg:col-span-7">
          <div class="thrunox-card p-6 sm:p-8 rounded-2xl">
            <h3 class="text-xl font-bold text-white mb-2">Send an Enquiry</h3>
            <p class="text-xs text-slate-400 mb-6">
              Please share a brief description of your requirement. Our team will review the information and determine the appropriate next step.
            </p>

            <form id="contactForm" onsubmit="handleContactSubmit(event)" class="space-y-4">
              
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label for="formName" class="block text-xs font-semibold text-slate-300 mb-1">Your Name *</label>
                  <input type="text" id="formName" required placeholder="Full Name" class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-amber-400">
                </div>
                <div>
                  <label for="formOrg" class="block text-xs font-semibold text-slate-300 mb-1">Organisation (Optional)</label>
                  <input type="text" id="formOrg" placeholder="Company / Entity Name" class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-amber-400">
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label for="formEmail" class="block text-xs font-semibold text-slate-300 mb-1">Business Email *</label>
                  <input type="email" id="formEmail" required placeholder="you@company.com" class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-amber-400">
                </div>
                <div>
                  <label for="formPhone" class="block text-xs font-semibold text-slate-300 mb-1">Phone Number (Optional)</label>
                  <input type="tel" id="formPhone" placeholder="+91 / International" class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-amber-400">
                </div>
              </div>

              <!-- Area of Interest (As specified in Developer Notes) -->
              <div>
                <label for="formInterest" class="block text-xs font-semibold text-slate-300 mb-1">Area of Interest *</label>
                <select id="formInterest" required class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-white text-xs focus:outline-none focus:border-amber-400">
                  <option value="" disabled selected>Select an area of interest...</option>
                  <option value="Project Management, Operations & Supply Chain">Project Management, Operations &amp; Supply Chain</option>
                  <option value="Accounting, Bookkeeping & Revenue Cycle Management">Accounting, Bookkeeping &amp; Revenue Cycle Management</option>
                  <option value="Licensing, Liaisoning & Strategic Consulting">Licensing, Liaisoning &amp; Strategic Consulting</option>
                  <option value="Digital Compliance & E-Signature Solutions">Digital Compliance &amp; E-Signature Solutions</option>
                  <option value="ESG Advisory">ESG Advisory</option>
                  <option value="Innovation & Solutions">Innovation &amp; Solutions</option>
                  <option value="Careers & Collaborations">Careers &amp; Collaborations</option>
                  <option value="Other Enquiry">Other Enquiry</option>
                </select>
              </div>

              <div>
                <label for="formDesc" class="block text-xs font-semibold text-slate-300 mb-1">Brief Description of Your Requirement *</label>
                <textarea id="formDesc" rows="4" required placeholder="Share context, intended outcome, deliverables or operational questions..." class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-amber-400"></textarea>
              </div>

              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Preferred Contact Method</label>
                <div class="flex items-center gap-6 text-xs text-slate-300">
                  <label class="flex items-center gap-2 cursor-pointer">
                    <input type="radio" name="contactMethod" value="Email" checked class="accent-amber-500">
                    <span>Email</span>
                  </label>
                  <label class="flex items-center gap-2 cursor-pointer">
                    <input type="radio" name="contactMethod" value="WhatsApp" class="accent-amber-500">
                    <span>WhatsApp</span>
                  </label>
                  <label class="flex items-center gap-2 cursor-pointer">
                    <input type="radio" name="contactMethod" value="Phone" class="accent-amber-500">
                    <span>Phone</span>
                  </label>
                </div>
              </div>

              <!-- Privacy Notice (Rule 3) -->
              <div class="text-[11px] text-slate-400 leading-relaxed pt-2">
                By submitting this form, you acknowledge that submitted details are handled in accordance with our 
                <button type="button" onclick="openModal('privacyModal')" class="text-amber-400 underline hover:text-amber-300">Privacy Policy</button>.
                For security, please do not include confidential technical files, passwords, or patient records.
              </div>

              <div class="pt-2">
                <button type="submit" class="w-full btn-gold py-3 rounded-xl font-bold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-lg">
                  <i data-lucide="send" class="w-4 h-4"></i> Submit Enquiry
                </button>
              </div>

            </form>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================== -->
  <!-- FOOTER (All Pages Requirement)             -->
  <!-- ========================================== -->
  <footer class="bg-[#05080e] border-t border-white/10 pt-16 pb-12 relative z-10 text-slate-400">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 pb-12 border-b border-white/5">
        
        <!-- Company Identity -->
        <div class="lg:col-span-2 space-y-4">
          <div class="flex items-center gap-3">
            <div class="logo-badge px-2.5 py-1 rounded-lg bg-slate-900/90 border border-white/10">
              <img src="logo.png" alt="Thrunox Systems" class="h-8 w-auto object-contain">
            </div>
            <div>
              <span class="text-white font-extrabold text-sm block">Thrunox Systems LLP</span>
              <span class="text-[11px] text-amber-400 font-medium">Notions in Motion. Results in Reality.</span>
            </div>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed max-w-sm">
            Thrunox Systems is an execution-focused business platform supporting organisations through business operations, project coordination, specialist service coordination, digital compliance and technology-led solution exploration.
          </p>
          <div class="text-[11px] text-slate-400 pt-2">
            <strong>Registered Office:</strong><br>
            Flat No. 201, Building No. 28, Bohra Layout, Bangalore South, Bengaluru, Karnataka – 560083.
          </div>
        </div>

        <!-- Explore Links -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-white mb-4">Explore</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#about" class="hover:text-amber-400 transition-colors">About Us</a></li>
            <li><a href="#services" class="hover:text-amber-400 transition-colors">Services</a></li>
            <li><a href="#industries" class="hover:text-amber-400 transition-colors">Industries</a></li>
            <li><a href="#innovation" class="hover:text-amber-400 transition-colors">Innovation &amp; Solutions</a></li>
          </ul>
        </div>

        <!-- Connect Links -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-white mb-4">Connect</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#careers" class="hover:text-amber-400 transition-colors">Careers &amp; Collaborations</a></li>
            <li><a href="#contact" class="hover:text-amber-400 transition-colors">Contact Us</a></li>
            <li>
              <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems" target="_blank" class="hover:text-emerald-400 transition-colors flex items-center gap-1.5">
                <i data-lucide="message-circle" class="w-3.5 h-3.5 text-emerald-400"></i> WhatsApp
              </a>
            </li>
            <li><a href="mailto:connect@thrunoxsystems.in" class="hover:text-amber-400 transition-colors">connect@thrunoxsystems.in</a></li>
          </ul>
        </div>

        <!-- Resources & Downloads -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-white mb-4">Resources</h4>
          <ul class="space-y-2 text-xs">
            <li>
              <a href="Thrunox-Systems-Company-Brochure.pdf" download="Thrunox-Systems-Company-Brochure.pdf" class="hover:text-amber-400 transition-colors inline-flex items-center gap-1.5 text-amber-300 font-semibold">
                <i data-lucide="download" class="w-3.5 h-3.5"></i> Download Brochure
              </a>
            </li>
            <li><button type="button" onclick="openModal('privacyModal')" class="hover:text-amber-400 transition-colors text-left">Privacy Policy</button></li>
            <li><button type="button" onclick="openModal('termsModal')" class="hover:text-amber-400 transition-colors text-left">Terms &amp; Conditions</button></li>
          </ul>
        </div>

      </div>

      <!-- Copyright & Legal -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-400 gap-4">
        <div>
          &copy; 2026 Thrunox Systems LLP. All rights reserved.
        </div>
        <div class="flex items-center gap-4">
          <button type="button" onclick="openModal('privacyModal')" class="hover:text-slate-300 transition-colors">Privacy Policy</button>
          <span>•</span>
          <button type="button" onclick="openModal('termsModal')" class="hover:text-slate-300 transition-colors">Terms &amp; Conditions</button>
        </div>
      </div>

    </div>
  </footer>

  <!-- ========================================== -->
  <!-- FLOATING WHATSAPP BUTTON (Unobtrusive)     -->
  <!-- ========================================== -->
  <div class="fixed bottom-6 right-6 z-40 flex items-center gap-3">
    <a href="https://wa.me/919980182009?text=Hello%20Thrunox%20Systems,%20I%20visited%20your%20website%20and%20would%20like%20to%20discuss%20a%20business%20requirement.%20Please%20let%20me%20know%20the%20appropriate%20next%20steps." target="_blank" aria-label="Chat on WhatsApp" class="p-3.5 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white shadow-xl shadow-emerald-950/60 transition-all transform hover:scale-110 flex items-center justify-center border border-emerald-400/30 group">
      <i data-lucide="message-circle" class="w-6 h-6"></i>
      <span class="max-w-0 overflow-hidden whitespace-nowrap group-hover:max-w-xs transition-all duration-300 text-xs font-bold pl-0 group-hover:pl-2">
        Chat with Thrunox
      </span>
    </a>
  </div>

  <!-- ========================================== -->
  <!-- WEBSITE CHATBOT: THRUNOX ASSISTANT         -->
  <!-- ========================================== -->
  <div class="fixed bottom-6 left-6 z-40">
    <!-- Chatbot Toggle Launcher Button -->
    <button id="chatbotToggleBtn" onclick="toggleChatbot()" aria-label="Open Thrunox Assistant" class="p-3.5 rounded-full btn-gold text-white shadow-xl shadow-amber-950/60 transition-all transform hover:scale-105 flex items-center justify-center gap-2 border border-amber-400/40">
      <i data-lucide="bot" class="w-6 h-6"></i>
      <span class="hidden sm:inline text-xs font-bold pr-1">Thrunox Assistant</span>
    </button>

    <!-- Chatbot Window -->
    <div id="chatbotWindow" class="hidden absolute bottom-16 left-0 w-[92vw] sm:w-[420px] max-h-[80vh] h-[580px] bg-[#0c121d] border border-amber-600/40 rounded-2xl shadow-2xl flex flex-col overflow-hidden backdrop-blur-2xl">
      
      <!-- Chat Header -->
      <div class="p-4 bg-slate-900 border-b border-white/10 flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-amber-950/60 border border-amber-500/40 flex items-center justify-center text-amber-400">
            <i data-lucide="bot" class="w-4 h-4"></i>
          </div>
          <div>
            <h4 class="text-xs font-bold text-white">Thrunox Assistant</h4>
            <span class="text-[10px] text-emerald-400 flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Automated Assistant
            </span>
          </div>
        </div>
        <div class="flex items-center gap-1">
          <button onclick="resetChatbot()" title="Restart Conversation" class="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/5 text-xs">
            <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
          </button>
          <button onclick="toggleChatbot()" title="Close" class="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/5 text-xs">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

      <!-- Messages Log Container -->
      <div id="chatMessages" class="flex-1 p-4 overflow-y-auto space-y-3 text-xs">
        
        <!-- Welcome Message -->
        <div class="flex items-start gap-2">
          <div class="w-6 h-6 rounded-full bg-amber-950 text-amber-400 flex items-center justify-center shrink-0 mt-0.5">
            <i data-lucide="bot" class="w-3.5 h-3.5"></i>
          </div>
          <div class="p-3 rounded-2xl rounded-tl-none bg-slate-900 border border-white/10 text-slate-200 leading-relaxed">
            Hello and welcome to Thrunox Systems.<br><br>
            I can help you explore our services, industries, Innovation &amp; Solutions, company brochure and collaboration options.<br><br>
            What would you like to know?
          </div>
        </div>

        <!-- Main Menu Buttons Container (Populated via JS) -->
        <div id="chatMenuButtons" class="pl-8 space-y-1.5 pt-1">
          <button onclick="handleMenuClick('Explore Services')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>1. Explore Services</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Explore Innovation & Solutions')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>2. Explore Innovation &amp; Solutions</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Industries We Support')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>3. Industries We Support</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Download Company Brochure')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>4. Download Company Brochure</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Careers & Collaborations')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>5. Careers &amp; Collaborations</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Contact Thrunox')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>6. Contact Thrunox</span> &rarr;
          </button>
        </div>

      </div>

      <!-- Quick FAQs Carousel & Input -->
      <div class="p-3 bg-slate-900 border-t border-white/10">
        <form onsubmit="handleChatSubmit(event)" class="flex gap-2">
          <input type="text" id="chatInput" placeholder="Ask a question about our services or FAQ..." class="flex-1 px-3 py-2 rounded-xl bg-slate-800 border border-white/10 text-white placeholder-slate-500 text-xs focus:outline-none focus:border-amber-400">
          <button type="submit" class="btn-gold p-2 rounded-xl text-white">
            <i data-lucide="send" class="w-4 h-4"></i>
          </button>
        </form>
      </div>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: PRIVACY POLICY                      -->
  <!-- ========================================== -->
  <div id="privacyModal" class="hidden fixed inset-0 z-50 modal-backdrop flex items-center justify-center p-4">
    <div class="bg-[#0e1420] border border-white/15 rounded-2xl max-w-3xl w-full max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-5 border-b border-white/10 flex items-center justify-between bg-slate-900/80">
        <div>
          <h3 class="text-lg font-bold text-white">Privacy Policy</h3>
          <span class="text-xs text-amber-400">Thrunox Systems LLP • Last Updated: 19 October 2026</span>
        </div>
        <button onclick="closeModal('privacyModal')" class="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-white/10">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs leading-relaxed text-slate-300">
        {privacy_html}
      </div>
      <div class="p-4 border-t border-white/10 flex items-center justify-between bg-slate-900/60">
        <a href="privacy-policy.pdf" download="Thrunox-Privacy-Policy.pdf" class="btn-secondary px-3 py-1.5 rounded-lg text-xs font-semibold inline-flex items-center gap-1.5">
          <i data-lucide="download" class="w-3.5 h-3.5"></i> Download PDF
        </a>
        <button onclick="closeModal('privacyModal')" class="btn-gold px-4 py-1.5 rounded-lg text-xs font-bold">
          Close Window
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL: TERMS & CONDITIONS                  -->
  <!-- ========================================== -->
  <div id="termsModal" class="hidden fixed inset-0 z-50 modal-backdrop flex items-center justify-center p-4">
    <div class="bg-[#0e1420] border border-white/15 rounded-2xl max-w-3xl w-full max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-5 border-b border-white/10 flex items-center justify-between bg-slate-900/80">
        <div>
          <h3 class="text-lg font-bold text-white">Terms &amp; Conditions</h3>
          <span class="text-xs text-amber-400">Thrunox Systems LLP • Last Updated: 19 October 2026</span>
        </div>
        <button onclick="closeModal('termsModal')" class="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-white/10">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs leading-relaxed text-slate-300">
        {terms_html}
      </div>
      <div class="p-4 border-t border-white/10 flex items-center justify-between bg-slate-900/60">
        <a href="terms-and-conditions.pdf" download="Thrunox-Terms-and-Conditions.pdf" class="btn-secondary px-3 py-1.5 rounded-lg text-xs font-semibold inline-flex items-center gap-1.5">
          <i data-lucide="download" class="w-3.5 h-3.5"></i> Download PDF
        </a>
        <button onclick="closeModal('termsModal')" class="btn-gold px-4 py-1.5 rounded-lg text-xs font-bold">
          Close Window
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- JAVASCRIPT LOGIC                           -->
  <!-- ========================================== -->
  <script>
    // Initialize Lucide Icons
    lucide.createIcons();

    // Mobile Drawer Toggle
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    if (mobileBtn && mobileDrawer) {{
      mobileBtn.addEventListener('click', () => {{
        mobileDrawer.classList.toggle('hidden');
      }});
      // Close on navigation link click
      document.querySelectorAll('.mobile-nav-link').forEach(link => {{
        link.addEventListener('click', () => {{
          mobileDrawer.classList.add('hidden');
        }});
      }});
    }}

    // Modals
    function openModal(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
      }}
    }}
    function closeModal(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.classList.add('hidden');
        document.body.style.overflow = '';
      }}
    }}

    // Contact Form Handler & Pre-fill
    function prefillContactForm(subject) {{
      const select = document.getElementById('formInterest');
      if (select) {{
        select.value = subject;
      }}
      const contactSection = document.getElementById('contact');
      if (contactSection) {{
        contactSection.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    function handleContactSubmit(e) {{
      e.preventDefault();
      const name = document.getElementById('formName').value;
      const org = document.getElementById('formOrg').value || 'Not Specified';
      const email = document.getElementById('formEmail').value;
      const phone = document.getElementById('formPhone').value || 'Not Specified';
      const interest = document.getElementById('formInterest').value;
      const desc = document.getElementById('formDesc').value;
      const method = document.querySelector('input[name="contactMethod"]:checked')?.value || 'Email';

      // Construct mailto link with BCC as explicitly instructed
      const subject = encodeURIComponent(`[Website Enquiry] ${interest} - ${name} (${org})`);
      const body = encodeURIComponent(
        `Thrunox Systems Enquiry\n` +
        `----------------------------------------\n` +
        `Name: ${name}\n` +
        `Organisation: ${org}\n` +
        `Business Email: ${email}\n` +
        `Phone Number: ${phone}\n` +
        `Area of Interest: ${interest}\n` +
        `Preferred Contact Method: ${method}\n\n` +
        `Description of Requirement:\n${desc}\n\n` +
        `----------------------------------------\n` +
        `Routing: Primary to contact@thrunoxsystems.in, BCC to thrunoxsystems@gmail.com`
      );

      // Trigger mailto fallback window
      window.location.href = `mailto:contact@thrunoxsystems.in?bcc=thrunoxsystems@gmail.com&subject=${subject}&body=${body}`;

      alert("Thank you, " + name + "! Your enquiry has been prepared. If your email client does not open automatically, please reach us directly at contact@thrunoxsystems.in with BCC to thrunoxsystems@gmail.com or via WhatsApp.");
      document.getElementById('contactForm').reset();
    }}

    // ==========================================
    // CHATBOT: THRUNOX ASSISTANT DATA & STATE
    // ==========================================
    const faqs = [
      {{
        q: "What does Thrunox Systems do?",
        keywords: ["what", "do", "overview", "about", "thrunox", "company"],
        ans: "Thrunox Systems is an execution-focused business platform supporting organisations through project management, operations, supply chain, accounting and revenue cycle support, licensing and liaisoning coordination, digital compliance, and ESG advisory.\\n\\nWe also explore technology-led solutions for practical business and industrial challenges. You can explore our current service areas on the Services section."
      }},
      {{
        q: "What is the Digital Twin & Virtual Sandbox initiative?",
        keywords: ["digital", "twin", "virtual", "sandbox", "simulation", "msme"],
        ans: "Thrunox Systems is exploring an affordable Digital Twin & Virtual Sandbox platform intended to help MSMEs evaluate selected operational scenarios before making physical changes or investments.\\n\\nThe initial development direction focuses on simplified manufacturing workflows, production flow, capacity constraints and scenario comparison.\\n\\nThe initiative is currently at the concept and development-planning stage. It should not be treated as a fully implemented or commercially available product."
      }},
      {{
        q: "Can I purchase or use the platform now?",
        keywords: ["purchase", "buy", "pricing", "cost", "use", "available", "now"],
        ans: "The Digital Twin & Virtual Sandbox initiative is currently presented as a concept and development-planning effort. We are not representing it as a commercially available platform.\\n\\nIf you are interested in the concept, have a manufacturing use case or would like to explore a potential collaboration, please contact Thrunox Systems for a discussion."
      }},
      {{
        q: "Which industries does Thrunox focus on?",
        keywords: ["industry", "industries", "sectors", "domain", "focus"],
        ans: "Our industry focus includes:\\n• Deep-Tech & Technology-Led Businesses\\n• Manufacturing & Industrial Operations\\n• Engineering Services & Fabrication\\n• Pharmaceutical, Healthcare & Medical Equipment\\n\\nOur proposed Digital Twin & Virtual Sandbox development direction initially focuses on Industrial Equipment & Manufacturing, Healthcare & Medical Equipment, and Medical Devices."
      }},
      {{
        q: "Can Thrunox obtain a regulatory licence or approval for my business?",
        keywords: ["licence", "license", "approval", "regulatory", "guarantee"],
        ans: "Thrunox Systems can discuss your licensing or regulatory coordination requirement and help identify the documentation, specialist expertise and process considerations involved.\\n\\nThe requirements depend on the product, activity, jurisdiction and relevant authority. Some matters may require appropriately qualified consultants or other specialists.\\n\\nWe cannot guarantee the grant of a licence, approval or regulatory outcome. Please contact us with a brief description of your requirement so that the appropriate next steps can be explored."
      }},
      {{
        q: "How can I enquire about a service?",
        keywords: ["enquire", "inquiry", "hire", "service", "contact", "talk"],
        ans: "You can submit an enquiry through the Contact Us page, email contact@thrunoxsystems.in with BCC to thrunoxsystems@gmail.com or use the WhatsApp option on our website.\\n\\nPlease share your area of interest and a brief description of the requirement. Our team can then review the enquiry and determine the appropriate next step."
      }},
      {{
        q: "How can I collaborate with Thrunox Systems?",
        keywords: ["collaborate", "partnership", "career", "jobs", "consultant", "join"],
        ans: "We welcome discussions with independent professionals, specialist consultants, service providers, technology developers and organisations interested in complementary capabilities.\\n\\nPlease visit Careers & Collaborations or contact us with your expertise, proposed contribution and preferred collaboration model. Specific engagements will be subject to mutually agreed scope and commercial terms."
      }},
      {{
        q: "Where can I download the company brochure?",
        keywords: ["brochure", "download", "pdf", "deck"],
        ans: "You can download the company brochure using the Download Company Brochure button on our About Us page or in the website footer. You can also click below to download directly:\\n\\n[Download Thrunox Brochure](Thrunox-Systems-Company-Brochure.pdf)"
      }},
      {{
        q: "What are your fees and delivery timelines?",
        keywords: ["fee", "price", "timeline", "rates", "cost", "duration"],
        ans: "Fees and timelines depend on the nature, complexity, scope and specialist requirements of each engagement.\\n\\nPlease share a brief description of your requirement through our Contact Us page. Any proposed scope, commercial terms and timelines will need to be assessed and agreed before the engagement begins."
      }},
      {{
        q: "How does Thrunox Systems handle my information?",
        keywords: ["privacy", "data", "security", "confidential", "information"],
        ans: "Please refer to the Privacy Policy on our website for information about how submitted information is handled.\\n\\nFor your security, do not share passwords, payment-card details, patient information or confidential technical documents through this chatbot. If additional information is required for a specific engagement, the appropriate method of sharing it should be agreed separately."
      }}
    ];

    function toggleChatbot() {{
      const win = document.getElementById('chatbotWindow');
      if (win) {{
        win.classList.toggle('hidden');
      }}
    }}

    function appendUserMessage(text) {{
      const container = document.getElementById('chatMessages');
      const msgDiv = document.createElement('div');
      msgDiv.className = 'flex items-start justify-end gap-2';
      msgDiv.innerHTML = `
        <div class="p-3 rounded-2xl rounded-tr-none bg-amber-600 text-white leading-relaxed max-w-[85%]">
          ${{text}}
        </div>
      `;
      container.appendChild(msgDiv);
      container.scrollTop = container.scrollHeight;
    }}

    function appendBotMessage(text) {{
      const container = document.getElementById('chatMessages');
      const msgDiv = document.createElement('div');
      msgDiv.className = 'flex items-start gap-2';
      const formatted = text.replace(/\\n/g, '<br>');
      msgDiv.innerHTML = `
        <div class="w-6 h-6 rounded-full bg-amber-950 text-amber-400 flex items-center justify-center shrink-0 mt-0.5">
          <i data-lucide="bot" class="w-3.5 h-3.5"></i>
        </div>
        <div class="p-3 rounded-2xl rounded-tl-none bg-slate-900 border border-white/10 text-slate-200 leading-relaxed max-w-[85%]">
          ${{formatted}}
        </div>
      `;
      container.appendChild(msgDiv);
      lucide.createIcons();
      container.scrollTop = container.scrollHeight;
    }}

    function handleMenuClick(action) {{
      appendUserMessage(action);
      setTimeout(() => {{
        if (action === 'Explore Services') {{
          appendBotMessage(
            "We offer 5 core service verticals:\\n" +
            "1. Project Management, Operations & Supply Chain\\n" +
            "2. Accounting, Bookkeeping & Revenue Cycle Management (US Market & RCM)\\n" +
            "3. Compliance & Cyber Security (Licensing, Digital Signatures, Cyber VAPT)\\n" +
            "4. ESG Advisory & Sustainable Operations\\n\\n" +
            "You can scroll to the Services section to view detailed breakdowns and initiate specific inquiries."
          );
        }} else if (action === 'Explore Innovation & Solutions') {{
          appendBotMessage(
            "Our innovation direction focuses on:\\n" +
            "• Affordable Digital Twin & Virtual Sandbox for MSMEs (Concept stage)\\n" +
            "• Healthcare Operations & Management Platform\\n" +
            "• Modular Healthcare Disaster Management\\n" +
            "• Modular & Smart Mobile Laboratories\\n\\n" +
            "These initiatives are in development planning to help MSMEs evaluate before physical implementation."
          );
        }} else if (action === 'Industries We Support') {{
          appendBotMessage(
            "We shape solutions around 4 key industry domains:\\n" +
            "1. Deep-Tech & Technology-Led Businesses\\n" +
            "2. Manufacturing & Industrial Operations\\n" +
            "3. Engineering Services & Fabrication\\n" +
            "4. Pharmaceutical, Healthcare & Medical Equipment"
          );
        }} else if (action === 'Download Company Brochure') {{
          appendBotMessage(
            "Here is the verified company brochure link:\\n" +
            "<a href='Thrunox-Systems-Company-Brochure.pdf' download class='text-amber-400 underline font-bold'>Click here to Download Thrunox Systems Brochure (PDF)</a>"
          );
        }} else if (action === 'Careers & Collaborations') {{
          appendBotMessage(
            "We welcome discussions with independent professionals, specialist consultants, service providers and technology developers in:\\n" +
            "• Operations & Supply Chain\\n• Accounting & US RCM\\n• Cyber Security & ESG\\n• Mechanical & Software Engineering\\n\\nReach out via our Contact form to express your interest!"
          );
        }} else if (action === 'Contact Thrunox') {{
          appendBotMessage(
            "You can reach us directly via:\\n" +
            "• Email: contact@thrunoxsystems.in (BCC: thrunoxsystems@gmail.com)\\n" +
            "• WhatsApp / Phone: +91-9980182009\\n" +
            "• Registered Office: Flat 201, Bldg 28, Bohra Layout, Bengaluru 560083."
          );
        }}
      }}, 300);
    }}

    function handleChatSubmit(e) {{
      e.preventDefault();
      const input = document.getElementById('chatInput');
      const val = input.value.trim();
      if (!val) return;
      appendUserMessage(val);
      input.value = '';

      setTimeout(() => {{
        const lower = val.toLowerCase();
        let matched = null;
        let maxScore = 0;

        for (const item of faqs) {{
          let score = 0;
          for (const kw of item.keywords) {{
            if (lower.includes(kw)) score++;
          }}
          if (score > maxScore) {{
            maxScore = score;
            matched = item;
          }}
        }}

        if (matched && maxScore > 0) {{
          appendBotMessage(matched.ans);
        }} else {{
          // Chatbot Fallback Message as specified in Section D
          appendBotMessage(
            "I may not have enough information to answer that accurately.\\n\\n" +
            "You can explore our website or contact Thrunox Systems directly at contact@thrunoxsystems.in with BCC to thrunoxsystems@gmail.com. You may also use the WhatsApp option (+91-9980182009) to request further assistance."
          );
        }}
      }}, 400);
    }}

    function resetChatbot() {{
      const container = document.getElementById('chatMessages');
      container.innerHTML = `
        <div class="flex items-start gap-2">
          <div class="w-6 h-6 rounded-full bg-amber-950 text-amber-400 flex items-center justify-center shrink-0 mt-0.5">
            <i data-lucide="bot" class="w-3.5 h-3.5"></i>
          </div>
          <div class="p-3 rounded-2xl rounded-tl-none bg-slate-900 border border-white/10 text-slate-200 leading-relaxed">
            Hello and welcome to Thrunox Systems.<br><br>
            I can help you explore our services, industries, Innovation &amp; Solutions, company brochure and collaboration options.<br><br>
            What would you like to know?
          </div>
        </div>
        <div id="chatMenuButtons" class="pl-8 space-y-1.5 pt-1">
          <button onclick="handleMenuClick('Explore Services')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>1. Explore Services</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Explore Innovation & Solutions')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>2. Explore Innovation &amp; Solutions</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Industries We Support')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>3. Industries We Support</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Download Company Brochure')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>4. Download Company Brochure</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Careers & Collaborations')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>5. Careers &amp; Collaborations</span> &rarr;
          </button>
          <button onclick="handleMenuClick('Contact Thrunox')" class="w-full text-left px-3 py-2 rounded-xl bg-white/5 hover:bg-amber-500/20 text-slate-200 hover:text-amber-300 border border-white/10 transition-all text-xs font-medium flex items-center justify-between">
            <span>6. Contact Thrunox</span> &rarr;
          </button>
        </div>
      `;
      lucide.createIcons();
    }}

    // ==========================================
    // RESTRAINED ENGINEERING PARTICLE NETWORK
    // Subtle connected nodes representing
    // engineering intelligence & digital systems
    // ==========================================
    const canvas = document.getElementById('particleCanvas');
    if (canvas) {{
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {{
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      }});

      const particleCount = Math.min(Math.floor(w / 35), 45);
      const particles = [];
      for (let i = 0; i < particleCount; i++) {{
        particles.push({{
          x: Math.random() * w,
          y: Math.random() * h,
          vx: (Math.random() - 0.5) * 0.25,
          vy: (Math.random() - 0.5) * 0.25,
          radius: Math.random() * 1.5 + 1.0,
          color: Math.random() > 0.5 ? 'rgba(200, 150, 65, ' : 'rgba(203, 213, 225, '
        }});
      }}

      function animateParticles() {{
        ctx.clearRect(0, 0, w, h);

        for (let i = 0; i < particles.length; i++) {{
          const p = particles[i];
          p.x += p.vx;
          p.y += p.vy;

          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
          if (p.y < 0) p.y = h;
          if (p.y > h) p.y = 0;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fillStyle = p.color + '0.4)';
          ctx.fill();

          for (let j = i + 1; j < particles.length; j++) {{
            const p2 = particles[j];
            const dx = p.x - p2.x;
            const dy = p.y - p2.y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < 130) {{
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(p2.x, p2.y);
              ctx.strokeStyle = `rgba(180, 130, 40, ${{0.15 * (1 - dist / 130)}})`;
              ctx.lineWidth = 0.7;
              ctx.stroke();
            }}
          }}
        }}

        requestAnimationFrame(animateParticles);
      }}

      animateParticles();
    }}
  </script>

</body>
</html>
'''

with open('/home/ashok/thrunox-redesign/index.html', 'w') as f:
    f.write(html_content)

print(f"Successfully generated /home/ashok/thrunox-redesign/index.html ({len(html_content)} bytes)")

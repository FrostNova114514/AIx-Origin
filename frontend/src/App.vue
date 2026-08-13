<template>
<canvas id="novaLightBackground" class="fixed inset-0 w-full h-full pointer-events-none" aria-hidden="true" style="z-index:0"></canvas>
    <div class="gradient-blur" aria-hidden="true" style="z-index: 20;">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    

    <!-- ============ HEADER ============ -->
    <header id="siteHeader" class="fixed top-0 inset-x-0 z-50 transition-all duration-300 border-b border-transparent">
      <div class="max-w-7xl mx-auto px-5 sm:px-8 flex items-center justify-between h-16">
        <a href="/" class="flex items-center" aria-label="AIx Origin Summit">
          <img :src="staticPath('images/aix-origin-logo-smooth.png')" alt="AIx Origin Summit" class="h-[18px] w-auto">
        </a>
        <nav class="horizon-nav-shell hidden md:flex items-center text-sm text-neutral-300" aria-label="Primary">
          <a href="/story/" class="horizon-nav-link">
            Story
          </a>
          <a href="/information/" class="horizon-nav-link">
            Information
          </a>
          <a href="/application/" class="horizon-nav-link">
            Application
          </a>
          <a href="/community/" class="horizon-nav-link">
            Community
          </a>
          <a href="/announcement/" class="horizon-nav-link">
            Announcement
          </a>
          <a href="/faq/" class="horizon-nav-link">
            F&amp;Q
          </a>
          <div class="horizon-lang-switch" aria-label="Language switch">
            <button type="button" data-lang-btn="zh-CN" class="lang-btn horizon-lang-btn text-[13px] uppercase tracking-normal text-neutral-400">中</button>
            <button type="button" data-lang-btn="en" class="lang-btn horizon-lang-btn text-[13px] uppercase tracking-normal text-neutral-400">EN</button>
          </div>
        </nav>
        <div class="flex items-center gap-3">
          <a href="/application/" class="horizon-pill horizon-pill-ghost hidden sm:inline-flex items-center gap-2 text-sm font-medium px-4 py-2">
            Application
            <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
          </a>
          <button id="menuBtn" class="horizon-icon-btn md:hidden p-2" aria-label="Open menu" aria-expanded="false">
            <i data-lucide="menu" class="w-5 h-5"></i>
          </button>
        </div>
      </div>
      <!-- Mobile menu -->
      <div id="mobileMenu" class="horizon-mobile-menu hidden md:hidden">
        <nav class="px-5 py-6 flex flex-col gap-2 text-lg" aria-label="Mobile">
          <a href="/story/" class="horizon-mobile-link">
            Story
          </a>
          <a href="/information/" class="horizon-mobile-link">
            Information
          </a>
          <a href="/application/" class="horizon-mobile-link">
            Application
          </a>
          <a href="/community/" class="horizon-mobile-link">
            Community
          </a>
          <a href="/announcement/" class="horizon-mobile-link">
            Announcement
          </a>
          <a href="/faq/" class="horizon-mobile-link">
            F&amp;Q
          </a>
          <div class="horizon-lang-switch mt-3 self-start" aria-label="Language switch">
            <button type="button" data-lang-btn="zh-CN" class="lang-btn horizon-lang-btn text-sm uppercase tracking-normal text-neutral-400">中</button>
            <button type="button" data-lang-btn="en" class="lang-btn horizon-lang-btn text-sm uppercase tracking-normal text-neutral-400">EN</button>
          </div>
        </nav>
      </div>
    </header>

    <main id="top" class="relative z-10">
      <!-- ============ HERO ============ -->
      <section v-show="currentPage === 'home'" class="relative pt-28 sm:pt-32 pb-8 sm:pb-10 lg:pb-12 min-h-[100svh] border-b border-neutral-800" style="background-color: rgb(2, 4, 8);">
        <div id="abyssWrap" class="absolute inset-0 overflow-hidden" aria-hidden="true" style="background:#020408">
          <canvas id="abyssCanvas" class="block w-full h-full"></canvas>
          <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-neutral-950/70 pointer-events-none"></div>
        </div>
        <div class="max-w-7xl mx-auto px-5 sm:px-8 relative z-10 flex min-h-[calc(100svh-7rem)] flex-col pb-24 lg:pb-0">
          <div class="flex items-center justify-between mb-8 reveal in">
            <span class="text-2xl sm:text-3xl lg:text-4xl font-medium tracking-normal text-neutral-500">
              溯源初心·共筑实境
            </span>
          </div>

          <h1 id="heroHeading" class="max-w-5xl reveal in">
            <img :src="staticPath('images/aix-origin-logo-smooth.png')" alt="AIx Origin - Trace Origin, Build Together." class="w-full max-w-[720px] h-auto">
          </h1>

          <div class="mt-auto flex flex-col gap-8 sm:flex-row sm:items-end sm:justify-between reveal lg:absolute lg:inset-x-0 lg:bottom-10 lg:mt-0 lg:px-8" style="transition-delay:.3s">
            <div>
              <div class="flex flex-wrap items-center gap-3">
                <a href="/application/" class="horizon-pill horizon-pill-ghost inline-flex items-center gap-2 font-medium px-6 py-3">
                  Start to Apply
                  <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
                <a href="/story/" class="horizon-pill horizon-pill-ghost inline-flex items-center gap-2 px-6 py-3 font-medium">
                  About
                </a>
              </div>
            </div>
            <img :src="staticPath('images/innoai-logo-transparent.png')" alt="INNOAI" class="w-[120px] sm:w-[150px] h-auto">
          </div>
        </div>
      </section>

      <!-- ============ PROOF STRIP ============ -->
      <section v-show="currentPage === 'home'" class="border-b border-neutral-800" aria-label="Studio proof">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
          <p class="mono text-xs text-neutral-500 uppercase tracking-wider pt-16 sm:pt-20 mb-8 reveal">
            (01) Snapshot
          </p>
        </div>
        <div class="max-w-7xl mx-auto px-5 sm:px-8 grid grid-cols-2 md:grid-cols-4 divide-x divide-neutral-800">
          <div class="pb-8 pr-6 reveal">
            <p class="text-3xl sm:text-4xl font-semibold tracking-tight">
              300+
            </p>
            <p class="text-lg sm:text-xl text-neutral-500 leading-relaxed mt-2">
              线下到场开发者 / 创业者 / 科研硬件 / 创意人群
            </p>
          </div>
          <div class="pb-8 px-6 reveal" style="transition-delay:.08s">
            <p class="text-3xl sm:text-4xl font-semibold tracking-tight">
              4
            </p>
            <p class="text-lg sm:text-xl text-neutral-500 leading-relaxed mt-2">
              硬核赛道 Flux · Vital · Anchor · Weave
            </p>
          </div>
          <div class="pb-8 px-6 border-t md:border-t-0 border-neutral-800 reveal" style="transition-delay:.16s">
            <p class="text-3xl sm:text-4xl font-semibold tracking-tight">
              5
            </p>
            <p class="text-lg sm:text-xl text-neutral-500 leading-relaxed mt-2">
              总时长天数线上 + 48h线下冲刺高端圆桌会议 + StudyLab3
            </p>
          </div>
          <div class="pb-8 pl-6 border-t md:border-t-0 border-neutral-800 reveal" style="transition-delay:.24s">
            <p class="text-3xl sm:text-4xl font-semibold tracking-tight">
              15+
            </p>
            <p class="text-lg sm:text-xl text-neutral-500 leading-relaxed mt-2">
              高校联合港八大 + 内地高校 + 海外高校
            </p>
          </div>
        </div>
      </section>

      <!-- ============ STORY ============ -->
      <section v-show="currentPage === 'story'" id="work" class="page-panel py-28 sm:py-36 border-b border-neutral-800 scroll-mt-16 overflow-hidden">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
          <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-8 reveal">
            (02) Story
          </p>
          <div class="max-w-5xl reveal">
            <h2 class="text-3xl sm:text-5xl lg:text-6xl font-semibold tracking-tight leading-tight">
              大多数黑客松，止于颁奖
            </h2>
            <div class="mt-8 space-y-6 text-lg sm:text-xl leading-relaxed text-neutral-300">
              <p>
                聚光灯亮起，奖杯颁出，人群散去。很多绝佳的灵感不是输给了技术，不是输给了对手，只是再也没有人给它时间，去长成一个真正有用的东西。
              </p>
              <p>
                如果终点是奖杯，那只是一场 weekend party。我们要的终点，在六个月后。
              </p>
              <p class="text-neutral-100 font-medium">
                到那时，你的项目还活着，还在跑，还有人用。
              </p>
            </div>
          </div>

          <div class="mt-24 grid grid-cols-1 lg:grid-cols-3 gap-8 reveal">
            <div class="border-t border-neutral-800 pt-6">
              <p class="text-3xl sm:text-4xl font-semibold tracking-tight text-cyan-300">1903</p>
              <h3 class="mt-8 text-xl sm:text-2xl font-semibold tracking-tight">莱特兄弟</h3>
              <p class="mt-4 text-base sm:text-lg leading-relaxed text-neutral-400">
                离地十二秒，一头栽进沙里。后来人类飞出了太阳系，而起点，是沙地里那行扶正架子的脚印。
              </p>
            </div>
            <div class="border-t border-neutral-800 pt-6">
              <p class="text-3xl sm:text-4xl font-semibold tracking-tight text-neutral-200">1991</p>
              <h3 class="mt-8 text-xl sm:text-2xl font-semibold tracking-tight">林纳斯·托瓦兹</h3>
              <p class="mt-4 text-base sm:text-lg leading-relaxed text-neutral-400">
                宿舍里一句「就是个爱好，别指望成气候」。今天你每张排队等的显卡底下，还跑着它。
              </p>
            </div>
            <div class="border-t border-neutral-800 pt-6">
              <p class="text-3xl sm:text-4xl font-semibold tracking-tight text-orange-400">2025</p>
              <h3 class="mt-8 text-xl sm:text-2xl font-semibold tracking-tight">DeepSeek</h3>
              <p class="mt-4 text-base sm:text-lg leading-relaxed text-neutral-400">
                被反复告知「算力不够，别想了」，却用最少的牌，让中国第一次坐上同一张牌桌。
              </p>
            </div>
          </div>

          <div class="mt-28 grid grid-cols-1 lg:grid-cols-12 gap-12 reveal">
            <div class="lg:col-span-5">
              <h2 class="text-4xl sm:text-6xl font-semibold tracking-tight leading-none">
                这儿有个缺口。<br>
                我来补。
              </h2>
              <p class="mt-8 text-xl sm:text-2xl text-neutral-300">
                这句话没有体面的名字。我们叫它 Origin。
              </p>
            </div>
            <div class="lg:col-span-7 space-y-8 text-lg sm:text-xl leading-relaxed text-neutral-300">
              <div>
                <h3 class="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                  为什么是香港和深圳
                </h3>
                <p class="mt-5">
                  Origin 光被看见，还不够。它要真补上那个缺口，得从念头变成手里的东西，再走到需要它的人手里。
                </p>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="border-l border-orange-400/70 pl-5">
                  <p class="mono text-sm uppercase tracking-wider text-orange-400">Shenzhen</p>
                  <h4 class="mt-4 text-2xl sm:text-3xl font-semibold tracking-tight text-white">深圳，替你把它造出来。</h4>
                  <p class="mt-4 text-base sm:text-lg text-neutral-400">
                    从机器人到可穿戴，从 IoT 到边缘 AI，「造出来」这件事的密度，全球第一，没有之一。
                  </p>
                </div>
                <div class="border-l border-cyan-300/70 pl-5">
                  <p class="mono text-sm uppercase tracking-wider text-cyan-300">Hong Kong</p>
                  <h4 class="mt-4 text-2xl sm:text-3xl font-semibold tracking-tight text-white">香港，替它铺好该走的路。</h4>
                  <p class="mt-4 text-base sm:text-lg text-neutral-400">
                    无论是前沿的金融与 Web3，还是生命科学与医疗，在各个领域「走出去」，香港是连接全球的最佳跳板。
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-28 reveal">
            <p class="text-xl sm:text-2xl lg:text-3xl font-semibold tracking-tight leading-tight max-w-5xl">
              一边造得出，一边送得出——<br>
              你那个缺口，从被看见、到被补上、到被需要它的人握住，第一次，不必在中间断掉。
            </p>
            <div class="mt-16 grid grid-cols-1 lg:grid-cols-12 gap-10">
              <div class="lg:col-span-7 space-y-6 text-lg sm:text-xl leading-relaxed text-neutral-300">
                <p>
                  你还记得吗——你第一次，全靠自己，把一个东西「做出来」的那个瞬间。
                </p>
                <p>
                  没人教你，你只是盯着它，琢磨，试，错了，再试。然后某一个时刻，它动了，亮了，成了。
                </p>
                <p>
                  那种感觉，不是骄傲。是你忽然发现，原来这个世界，是可以被你亲手撬动一点的。
                </p>
              </div>
              <div class="lg:col-span-5 text-xl sm:text-3xl leading-relaxed text-neutral-400">
                <p>2026 年 9 月，香港 &amp; 深圳。</p>
                <p class="mt-6 text-white font-semibold">
                  我们把灯打开，把桌子摆好，把同样较劲的人放到你旁边。然后退后一步，看你们创造。
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ EVENT OVERVIEW ============ -->
      <section v-show="currentPage === 'information'" id="overview" class="page-panel py-28 sm:py-32 border-b border-neutral-800 scroll-mt-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
          <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-8 reveal">
            (03) Information
          </p>
          <h2 class="text-xl sm:text-2xl font-semibold tracking-tight reveal">
            活动全景
          </h2>
          <div class="overview-glass-grid mt-12 grid grid-cols-1 md:grid-cols-4 gap-px overflow-hidden">
            <div class="overview-glass-cell p-5 sm:p-6 reveal">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">地点</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">香港会场 + 深圳会场</p>
              <p class="mt-2 text-sm sm:text-base text-neutral-400">首次双城联动</p>
            </div>
            <div class="overview-glass-cell p-5 sm:p-6 reveal" style="transition-delay:.06s">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">时间</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">2026.08.31 — 2026.09.06</p>
              <p class="mt-2 text-sm sm:text-base text-neutral-400">共 7 天 · 线上 + 线下混合模式</p>
            </div>
            <div class="overview-glass-cell p-5 sm:p-6 reveal" style="transition-delay:.12s">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">规模</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">300+ 线下到场创造者</p>
              <p class="mt-2 text-sm sm:text-base text-neutral-400">开发者 / 创业者 / 科研硬件 / 创意人群</p>
            </div>
            <div class="overview-glass-cell p-5 sm:p-6 reveal" style="transition-delay:.18s">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">高校</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">30+ 所</p>
              <p class="mt-2 text-sm sm:text-base text-neutral-400">港八大 + 内地 + 海外</p>
              <p class="mt-1 text-sm sm:text-base text-neutral-500">高校联合</p>
            </div>
            <div class="overview-glass-cell p-5 sm:p-6 reveal" style="transition-delay:.24s">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">赛后</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">投资 / 资源持续对接</p>
            </div>
            <div class="overview-glass-cell p-5 sm:p-6 reveal" style="transition-delay:.30s">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">语言</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">中英双语</p>
            </div>
            <div class="overview-glass-cell p-5 sm:p-6 reveal" style="transition-delay:.36s">
              <p class="text-lg sm:text-xl font-medium tracking-tight text-neutral-500">组队</p>
              <p class="mt-4 text-xl sm:text-2xl font-semibold tracking-tight text-white">2 — 5 人 / 队</p>
              <p class="mt-2 text-sm sm:text-base text-neutral-400">允许个人报名，主办方帮组队</p>
            </div>
          </div>
          <div class="mt-16 grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div class="lg:col-span-5 reveal">
              <h2 class="text-xl sm:text-2xl font-semibold tracking-tight">
                多元背景
              </h2>
              <p class="mt-5 text-base sm:text-lg leading-relaxed text-neutral-400">
                来自港校 + 内地 + 海外高校的参赛选手首次进行全域联合，形成香港本土体量天花板级别的跨校创造者网络。
              </p>
            </div>
            <div class="lg:col-span-7 reveal" style="transition-delay:.08s">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
                <div>
                  <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">Hong Kong</p>
                  <p class="text-base sm:text-lg leading-relaxed text-neutral-300">
                    香港大学 / 香港中文大学 / 香港科技大学 / PolyU / CityU / HKBU / LingU / EdUHK
                  </p>
                </div>
                <div>
                  <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">Mainland + Global</p>
                  <p class="text-base sm:text-lg leading-relaxed text-neutral-300">
                    清华深研院 / 北大深研院 / 哈工深 / Yale / UPenn / NYU / JHU / NUS / NTU
                  </p>
                </div>
              </div>
            </div>
            <div class="lg:col-span-12 reveal" style="transition-delay:.14s">
              <div class="logo-board school-logo-board" aria-label="高校 logo">
                <div class="logo-region">
                  <p class="logo-region-title">香港高校</p>
                  <div class="school-logo-grid school-logo-grid-featured">
                    <div class="school-logo-item"><p>香港大学</p><img :src="staticPath('images/ppt-logos/slide-11/image18.png')" alt="香港大学 logo"></div>
                    <div class="school-logo-item"><p>香港中文大学</p><img :src="staticPath('images/ppt-logos/slide-11/image20.png')" alt="香港中文大学 logo"></div>
                    <div class="school-logo-item"><p>香港科技大学</p><img :src="staticPath('images/ppt-logos/slide-11/image19.png')" alt="香港科技大学 logo"></div>
                  </div>
                </div>
                <div class="logo-region">
                  <p class="logo-region-title">内地高校</p>
                  <div class="school-logo-grid school-logo-grid-compact">
                    <div class="school-logo-item"><p>清华深研院</p><img :src="staticPath('images/ppt-logos/slide-11/image16.png')" alt="清华深研院 logo"></div>
                    <div class="school-logo-item"><p>北大深研院</p><img :src="staticPath('images/ppt-logos/slide-11/image17.png')" alt="北大深研院 logo"></div>
                    <div class="school-logo-item"><p>哈工深</p><img :src="staticPath('images/ppt-logos/slide-11/image21.png')" alt="哈工深 logo"></div>
                  </div>
                </div>
                <div class="logo-region">
                  <p class="logo-region-title">海外高校</p>
                  <div class="school-logo-grid school-logo-grid-overseas">
                    <div class="school-logo-item"><p>Yale</p><img :src="staticPath('images/ppt-logos/slide-11/image25.png')" alt="Yale logo"></div>
                    <div class="school-logo-item"><p>UPenn</p><img :src="staticPath('images/ppt-logos/slide-11/image23.png')" alt="UPenn logo"></div>
                    <div class="school-logo-item"><p>NYU</p><img :src="staticPath('images/ppt-logos/slide-11/image22.png')" alt="NYU logo"></div>
                    <div class="school-logo-item"><p>JHU</p><img :src="staticPath('images/ppt-logos/slide-11/image24.png')" alt="JHU logo"></div>
                    <div class="school-logo-item"><p>NUS</p><img :src="staticPath('images/ppt-logos/slide-11/image31.png')" alt="NUS logo"></div>
                    <div class="school-logo-item"><p>NTU</p><img :src="staticPath('images/ppt-logos/slide-11/image32.png')" alt="NTU logo"></div>
                  </div>
                </div>
                <div class="logo-region">
                  <p class="logo-region-title">香港更多高校</p>
                  <div class="school-logo-grid school-logo-grid-local">
                    <div class="school-logo-item"><p>PolyU</p><img :src="staticPath('images/ppt-logos/slide-11/image26.png')" alt="PolyU logo"></div>
                    <div class="school-logo-item"><p>CityU</p><img :src="staticPath('images/ppt-logos/slide-11/image30.png')" alt="CityU logo"></div>
                    <div class="school-logo-item"><p>HKBU</p><img :src="staticPath('images/ppt-logos/slide-11/image27.png')" alt="HKBU logo"></div>
                    <div class="school-logo-item"><p>LingU</p><img :src="staticPath('images/ppt-logos/slide-11/image28.png')" alt="LingU logo"></div>
                    <div class="school-logo-item"><p>EdUHK</p><img :src="staticPath('images/ppt-logos/slide-11/image29.png')" alt="EdUHK logo"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-16 pt-16 border-t border-neutral-800 grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div class="lg:col-span-5 reveal">
              <h2 class="text-xl sm:text-2xl font-semibold tracking-tight">
                当前合作方生态
              </h2>
              <p class="mt-5 text-base sm:text-lg leading-relaxed text-neutral-400">
                多元化合作版图正在持续扩展，覆盖社群组织、合办企业与支持单位，为参赛项目提供更完整的资源入口。
              </p>
            </div>
            <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-3 gap-px bg-neutral-800 border border-neutral-800 overflow-hidden reveal" style="transition-delay:.08s">
              <div class="bg-neutral-950/55 backdrop-blur-sm p-5 sm:p-6">
                <p class="text-lg sm:text-xl font-medium tracking-tight text-white">社群组织</p>
                <p class="mt-3 text-sm sm:text-base text-neutral-500">+ 更多</p>
              </div>
              <div class="bg-neutral-950/55 backdrop-blur-sm p-5 sm:p-6">
                <p class="text-lg sm:text-xl font-medium tracking-tight text-white">联合主办单位</p>
                <p class="mt-3 text-sm sm:text-base text-neutral-500">+ 更多</p>
              </div>
              <div class="bg-neutral-950/55 backdrop-blur-sm p-5 sm:p-6">
                <p class="text-lg sm:text-xl font-medium tracking-tight text-white">支持单位</p>
                <p class="mt-3 text-sm sm:text-base text-neutral-500">+ 更多</p>
              </div>
            </div>
            <div v-if="false" class="lg:col-span-12 reveal" style="transition-delay:.14s">
              <div class="logo-board partner-logo-board" aria-label="合作方 logo">
                <div class="partner-feature">
                  <p class="logo-region-title">联合主办单位</p>
                  <div class="partner-logo-stack">
                    <img :src="staticPath('images/ppt-logos/slide-17/image58.jpg')" alt="鲲腾能科 logo">
                    <img :src="staticPath('images/ppt-logos/slide-17/tenwings-accelerator.png')" alt="Tenwings Accelerator logo">
                  </div>
                </div>
                <div class="partner-main">
                  <div class="logo-region">
                    <p class="logo-region-title">支持单位</p>
                    <div class="partner-logo-grid partner-logo-grid-support">
                      <div class="partner-logo-card partner-logo-card-composite"><img :src="staticPath('images/ppt-logos/slide-17/viewpoint-yueqian.png')" alt="观点跃迁 logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/image62.png')" alt="SoftSunc logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/image63.png')" alt="TokenDance logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/insta360.png')" alt="Insta360 影石 logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/studyspace.png')" alt="StudySpace logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/medo.png')" alt="MeDo logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/gobi-partners.png')" alt="Gobi Partners logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image61.png')" alt="支持单位 logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image37.png')" alt="奇绩创坛 logo"></div>
                    </div>
                  </div>
                  <div class="logo-region">
                    <p class="logo-region-title">社群组织</p>
                    <div class="partner-logo-grid partner-logo-grid-community">
                      <div class="partner-logo-card partner-logo-card-innoai"><img :src="staticPath('images/ppt-logos/slide-17/innoai-white.webp')" alt="INNOAI logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image36.png')" alt="agency 青年力社区 logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image45.jpeg')" alt="colorblock logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image46.png')" alt="观塔 logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/neic.png')" alt="NEIC logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/image53.png')" alt="Wharton Alumni Club Beijing logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image57.jpeg')" alt="W创 logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/image60.png')" alt="BitGates Web3 logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/emerge.png')" alt="emerge logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image55.jpeg')" alt="HKUNAA logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image49.png')" alt="ISEA logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/image50.jpeg')" alt="UChicago Venture Club logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/wave.png')" alt="WAVE logo"></div>
                      <div class="partner-logo-card"><img :src="staticPath('images/ppt-logos/slide-17/uci.png')" alt="UCI logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/see-ai.png')" alt="SEE AI logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/atox.png')" alt="ATOX logo"></div>
                      <div class="partner-logo-card partner-logo-card-wide"><img :src="staticPath('images/ppt-logos/slide-17/waytoagi.png')" alt="WaytoAGI logo"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ PROCESS ============ -->
      <section v-show="currentPage === 'information'" id="process" class="py-24 sm:py-32 border-b border-neutral-800 scroll-mt-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 grid grid-cols-1 lg:grid-cols-12 gap-12">
          <div class="lg:col-span-5">
            <div class="lg:sticky lg:top-28 reveal">
              <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">
                (04) Tracks
              </p>
              <h2 class="text-4xl sm:text-5xl font-semibold tracking-tight leading-tight">
                四条赛道，两种城市基因
              </h2>
              <p class="text-lg text-neutral-400 mt-6 max-w-sm leading-relaxed">
                我们不是拍脑袋定的赛道。每一条赛道，都长在它所在城市的产业土壤里。
              </p>
            </div>
          </div>
          <div class="lg:col-span-7 flex flex-col divide-y divide-neutral-800 border-t border-neutral-800 relative pl-8" data-timeline="true">
            <div class="py-10 grid grid-cols-12 gap-4 reveal">
              <span class="col-span-3 sm:col-span-2 text-5xl sm:text-6xl font-semibold tracking-tight text-neutral-700">
                01
              </span>
              <div class="col-span-9 sm:col-span-10">
                <h3 class="text-xl font-semibold tracking-tight mb-2">
                  香港 · Flux
                </h3>
                <p class="text-lg text-neutral-400 leading-relaxed">
                  流境 — 数字金融 &amp; Web3.0
                  <br>
                  钱该怎么流动？——跨境支付、数字资产、金融合规、新的交易与信任方式。用代码重新定义价值的流动。
                </p>
              </div>
            <span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span></div>
            <div class="py-10 grid grid-cols-12 gap-4 reveal" style="transition-delay:.08s">
              <span class="col-span-3 sm:col-span-2 text-5xl sm:text-6xl font-semibold tracking-tight text-neutral-700">
                02
              </span>
              <div class="col-span-9 sm:col-span-10">
                <h3 class="text-xl font-semibold tracking-tight mb-2">
                  香港 · Vital
                </h3>
                <p class="text-lg text-neutral-400 leading-relaxed">
                  活域 — 生命科学 &amp; Healthcare
                  <br>
                  人该怎么更健康？——AI 辅助问诊、健康数据管理、医疗流程优化、生命科学应用。用 AI 让人活得更久、更好。
                </p>
              </div>
            <span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span></div>
            <div class="py-10 grid grid-cols-12 gap-4 reveal" style="transition-delay:.16s">
              <span class="col-span-3 sm:col-span-2 text-5xl sm:text-6xl font-semibold tracking-tight text-neutral-700">
                03
              </span>
              <div class="col-span-9 sm:col-span-10">
                <h3 class="text-xl font-semibold tracking-tight mb-2">
                  深圳 · Anchor
                </h3>
                <p class="text-lg text-neutral-400 leading-relaxed">
                  具构 — 具身智能 &amp; 智能硬件
                  <br>
                  AI 怎么走出屏幕？——AI + 智能硬件、机器人、IoT 联动、软硬件结合的创意产品。让 AI 进入真实世界。
                </p>
              </div>
            <span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span></div>
            <div class="py-10 grid grid-cols-12 gap-4 reveal" style="transition-delay:.24s">
              <span class="col-span-3 sm:col-span-2 text-5xl sm:text-6xl font-semibold tracking-tight text-neutral-700">
                04
              </span>
              <div class="col-span-9 sm:col-span-10">
                <h3 class="text-xl font-semibold tracking-tight mb-2">
                  深圳 · Weave
                </h3>
                <p class="text-lg text-neutral-400 leading-relaxed">
                  织域 — 全域融合 &amp; Agent + 创意
                  <br>
                  万物怎么连起来？——AI Agent、创意工具、跨界融合、用 AI 做以前做不到的事。不设限的赛道，给不按常理出牌的人。
                </p>
              </div>
            <span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span><span class="tl-dot" aria-hidden="true"></span></div>
            <div class="absolute left-0 top-0 bottom-0 w-px pointer-events-none" aria-hidden="true">
              <div class="absolute inset-0 bg-neutral-800"></div>
              <div id="processProgressLine" class="absolute inset-0 bg-white origin-top" style="transform:scaleY(0)"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ FINAL CTA ============ -->
      <section v-show="currentPage === 'application'" id="contact" class="page-panel py-28 sm:py-32 border-b border-neutral-800 scroll-mt-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
          <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-8 reveal">
            (04) Application
          </p>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight leading-[0.95] reveal">
            填写申请
          </h2>
          <form id="applicationForm" class="application-card reveal in" style="transition-delay:.2s" enctype="multipart/form-data" novalidate>
            <p class="application-intro">
              请按问卷内容填写个人信息、作品经历、组队偏好等信息，以上信息仅用于比赛审核。如申请者未满 18 周岁，请取得父母或法定监护人知情同意。申请结果将通过邮箱发送。
              <br>
              <span class="text-white underline underline-offset-4">已填写飞书问卷无需再次填写。</span>
            </p>
            <div class="application-form">
              <div class="app-field">
                <label for="app-name" class="app-field-label">
                  姓名（必选）
                </label>
                <p class="app-field-help">您希望我们怎样称呼您？</p>
                <input id="app-name" name="name" type="text" required="" placeholder="待填写者输入" class="app-control">
              </div>
              <div class="app-field">
                <label for="app-phone" class="app-field-label">
                  手机号（必选）
                </label>
                <p class="app-field-help">确保可以加到微信</p>
                <input id="app-phone" name="phone" type="tel" required="" placeholder="待填写者输入" class="app-control">
              </div>
              <div class="app-field">
                <label for="app-email" class="app-field-label">
                  电子邮箱（必选）
                </label>
                <p class="app-field-help">email</p>
                <input id="app-email" name="email" type="email" required="" placeholder="待填写者输入" class="app-control">
              </div>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  你的身份（可选）
                </legend>
                <div class="app-choice-grid">
                  <label class="app-choice">
                    <input type="checkbox" name="role" value="学生">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('学生') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="checkbox" name="role" value="职场人士">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('职场人士') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="checkbox" name="role" value="独立开发者/创作者">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('独立开发者/创作者') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="checkbox" name="role" value="创业者">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('创业者') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="checkbox" name="role" value="其他">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('其他') }}</span>
                  </label>
                </div>
              </fieldset>
              <div class="app-field app-field-full">
                <label for="app-background" class="app-field-label">
                  学校背景/工作背景（必选）
                </label>
                <p class="app-field-help">学校标注：院校 + 专业 + 年级；工作表明：公司 + 岗位 + 工作年限</p>
                <input id="app-background" name="background" type="text" required="" placeholder="待填写者输入" class="app-control">
              </div>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）（必选）
                </legend>
                <p class="app-field-help">参赛者可以在选手交流群里找到自己期待的队友。如果暂时没有找到合适的队友又不希望单枪匹马开发，主办方这边也可以帮你匹配。</p>
                <div class="app-choice-grid">
                  <label class="app-choice">
                    <input type="radio" name="team_method" value="自行组队（请补充队友姓名/联系方式）">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('自行组队（请补充队友姓名/联系方式）') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="team_method" value="个人参赛">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('个人参赛') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="team_method" value="希望由主办方随机匹配队友">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('希望由主办方随机匹配队友') }}</span>
                  </label>
                </div>
              </fieldset>
              <div class="app-field app-field-full">
                <label for="app-team-name" class="app-field-label">
                  若自行组队，请输入队名（可选）
                </label>
                <input id="app-team-name" name="team_name" type="text" placeholder="待填写者输入" class="app-control">
              </div>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  参加方式（必选）
                </legend>
                <div class="app-choice-grid app-choice-grid-2">
                  <label class="app-choice">
                    <input type="radio" name="participation_city" value="深圳（Anchor+Weave）" required="">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('深圳（Anchor+Weave）') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="participation_city" value="香港（Flux+Vital）（必须有港澳通行证及相关证件）">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('香港（Flux+Vital）（必须有港澳通行证及相关证件）') }}</span>
                  </label>
                </div>
              </fieldset>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  参与赛道（深圳）（必选）
                </legend>
                <p class="app-field-help">选好后不可再改</p>
                <div class="app-choice-grid app-choice-grid-2">
                  <label class="app-choice">
                    <input type="radio" name="track_shenzhen" value="Anchor · 具构（深圳）— 具身智能 & 智能硬件" required="">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('Anchor · 具构（深圳）— 具身智能 & 智能硬件') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="track_shenzhen" value="Weave · 织域（深圳）— 全域融合 & Agent + 创意">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('Weave · 织域（深圳）— 全域融合 & Agent + 创意') }}</span>
                  </label>
                </div>
              </fieldset>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  参与赛道（香港）（必选）
                </legend>
                <p class="app-field-help">选好后不可再改</p>
                <div class="app-choice-grid app-choice-grid-2">
                  <label class="app-choice">
                    <input type="radio" name="track_hong_kong" value="Flux · 流境（香港）— 数字金融 & Web3.0" required="">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('Flux · 流境（香港）— 数字金融 & Web3.0') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="track_hong_kong" value="Vital · 活域（香港）— 生命科学 & Healthcare">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('Vital · 活域（香港）— 生命科学 & Healthcare') }}</span>
                  </label>
                </div>
              </fieldset>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  是否参与过完整的创业项目或开发项目（可选）
                </legend>
                <div class="app-choice-grid app-choice-grid-2">
                  <label class="app-choice">
                    <input type="radio" name="complete_project" value="是">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('是') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="complete_project" value="否">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('否') }}</span>
                  </label>
                </div>
              </fieldset>
              <div class="app-field app-field-full">
                <label for="app-github" class="app-field-label">
                  Your GitHub / personal homepage (optional)
                </label>
                <input id="app-github" name="github_homepage" type="text" placeholder="待填写者输入" class="app-control">
              </div>
              <div class="app-field app-field-full">
                <label for="app-portfolio" class="app-field-label">
                  你的作品集，简历（可选）
                </label>
                <input id="app-portfolio" name="portfolio_resume" type="file" class="app-control">
              </div>
              <div class="app-field app-field-full">
                <label for="app-project" class="app-field-label">
                  项目简述（可选）
                </label>
                <p class="app-field-help">请简单介绍你的创意 / 项目，以及你希望落地这个方向的原因。</p>
                <textarea id="app-project" name="project_description" rows="4" placeholder="待填写者输入" class="app-control app-textarea"></textarea>
              </div>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  你是否愿意在赛后将你的优秀项目进一步推进落地？（必选）
                </legend>
                <div class="app-choice-grid">
                  <label class="app-choice">
                    <input type="radio" name="post_event_followup" value="是" required="">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">是</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="post_event_followup" value="否">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">否</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="post_event_followup" value="其他">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('其他') }}</span>
                  </label>
                </div>
              </fieldset>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  技能评价（必选）
                </legend>
                <p class="app-field-help">{{ t('1=从未接触; 2=初学; 3=能独立完成; 4=有丰富项目经验') }}</p>
                <div class="app-rating-table">
                  <div class="app-rating-row">
                    <span>{{ t('编程能力（如 C/C++/Python/Java 等）') }}</span>
                    <label><input type="radio" name="skill_programming" value="1" required="">1</label>
                    <label><input type="radio" name="skill_programming" value="2">2</label>
                    <label><input type="radio" name="skill_programming" value="3">3</label>
                    <label><input type="radio" name="skill_programming" value="4">4</label>
                  </div>
                  <div class="app-rating-row">
                    <span>{{ t('硬件开发（如 PCB设计、电路调试、嵌入式系统）') }}</span>
                    <label><input type="radio" name="skill_hardware" value="1" required="">1</label>
                    <label><input type="radio" name="skill_hardware" value="2">2</label>
                    <label><input type="radio" name="skill_hardware" value="3">3</label>
                    <label><input type="radio" name="skill_hardware" value="4">4</label>
                  </div>
                  <div class="app-rating-row">
                    <span>{{ t('产品/用户研究（需求挖掘、洞察）') }}</span>
                    <label><input type="radio" name="skill_research" value="1" required="">1</label>
                    <label><input type="radio" name="skill_research" value="2">2</label>
                    <label><input type="radio" name="skill_research" value="3">3</label>
                    <label><input type="radio" name="skill_research" value="4">4</label>
                  </div>
                  <div class="app-rating-row">
                    <span>{{ t('设计表达（UI/UX、3D建模、视觉传达）') }}</span>
                    <label><input type="radio" name="skill_design" value="1" required="">1</label>
                    <label><input type="radio" name="skill_design" value="2">2</label>
                    <label><input type="radio" name="skill_design" value="3">3</label>
                    <label><input type="radio" name="skill_design" value="4">4</label>
                  </div>
                  <div class="app-rating-row">
                    <span>{{ t('项目协作（进度把控、跨学科沟通、文档整理）') }}</span>
                    <label><input type="radio" name="skill_collaboration" value="1" required="">1</label>
                    <label><input type="radio" name="skill_collaboration" value="2">2</label>
                    <label><input type="radio" name="skill_collaboration" value="3">3</label>
                    <label><input type="radio" name="skill_collaboration" value="4">4</label>
                  </div>
                </div>
                <input name="skill_other" type="text" :placeholder="t('其他')" class="app-control app-rating-other">
              </fieldset>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  你的“硬”实力 (Hardware Skills)（必选）
                </legend>
                <div class="app-choice-grid">
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="PCB设计"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('PCB设计 (KiCad/Altium)') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="嵌入式开发"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('嵌入式开发 (Arduino/ESP32/STM32)') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="结构设计/3D建模"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('结构设计/3D建模 (Fusion360/SolidWorks/Blender)') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="手工/焊接"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('手工/焊接') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="快速模型制作"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('快速模型制作3d打印/激光切割') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="传感器与电路"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('传感器与电路') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="导电织物/可穿戴电子"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('导电织物 / 可穿戴电子') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="hardware_skills" value="其他"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('其他') }}</span></label>
                </div>
              </fieldset>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  你的“软”实力 (Software &amp; AI)（必选）
                </legend>
                <div class="app-choice-grid">
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="大模型API调用"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('大模型API调用') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="AI Agent"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('AI Agent') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="机器视觉"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('机器视觉') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="运动算法"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('运动算法') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="后端开发"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('后端开发') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="前端工程"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('前端工程（React / Vue.js 等）') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="边缘计算/端侧部署"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('边缘计算/端侧部署') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="Vibe coding"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('Vibe coding') }}</span></label>
                  <label class="app-choice"><input type="checkbox" name="software_skills" value="其他"><span class="app-choice-mark"></span><span class="app-choice-text">{{ t('其他') }}</span></label>
                </div>
              </fieldset>
              <div class="app-field app-field-full">
                <label for="app-social" class="app-field-label">
                  请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）（可选）
                </label>
                <p class="app-field-help">{{ t('可以是你的个人网站、LinkedIn、Github、小红书、X、Bilibili、Reddit、Instagram...') }}</p>
                <textarea id="app-social" name="social_links" rows="3" placeholder="待填写者输入" class="app-control app-textarea"></textarea>
              </div>
              <div class="app-field app-field-full">
                <label for="app-past-18" class="app-field-label">
                  {{ t('在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。（可选）') }}
                </label>
                <p class="app-field-help">{{ t('包括产品/项目、你具体做了什么部分、花了多久、有没有真实用户/收入/下载/开源 star/粉丝等结果。一个APP？电路板？网站？Agent？还是一个小红书视频账号？一个赚钱的生意？一个github开源项目？') }}</p>
                <textarea id="app-past-18" name="past_18_months" rows="5" placeholder="待填写者输入" class="app-control app-textarea"></textarea>
              </div>
              <fieldset class="app-field app-field-full">
                <legend class="app-field-label">
                  {{ t('是否愿意信息公开联系方式给合作方公司用于招聘/投资对接（可选）') }}
                </legend>
                <p class="app-field-help">{{ t('我们充分尊重你的意愿') }}</p>
                <div class="app-choice-grid app-choice-grid-2">
                  <label class="app-choice">
                    <input type="radio" name="public_contact" value="愿意">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('愿意') }}</span>
                  </label>
                  <label class="app-choice">
                    <input type="radio" name="public_contact" value="不愿意">
                    <span class="app-choice-mark"></span>
                    <span class="app-choice-text">{{ t('不愿意') }}</span>
                  </label>
                </div>
              </fieldset>
              <div class="app-field app-field-full">
                <button type="submit" class="horizon-pill horizon-pill-primary w-full sm:w-auto inline-flex items-center justify-center gap-2 font-medium px-8 py-4">
                  送出申请
                  <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </button>
              </div>
            </div>
          </form>
        </div>
      </section>

      <!-- ============ TESTIMONIALS ============ -->
      <section v-show="currentPage === 'community'" id="community" class="page-panel py-28 sm:py-32 border-b border-neutral-800 scroll-mt-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
          <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-12 reveal">
            (05) Community
          </p>
          <div class="grid grid-cols-1 gap-px bg-neutral-800 border border-neutral-800">
            <div class="bg-neutral-950/90 p-6 sm:p-8 reveal">
              <div class="grid grid-cols-1 md:grid-cols-[1fr_180px] gap-8 items-center">
                <div>
                  <p class="text-xl sm:text-2xl font-semibold tracking-tight text-white">
                    加入交流群
                  </p>
                  <p class="mt-3 text-sm sm:text-base leading-relaxed text-neutral-400">
                    赛事咨询，赛制答疑，组队
                  </p>
                </div>
                <img :src="staticPath('images/community-group.jpg')" alt="加入交流群二维码" class="w-full max-w-[180px] justify-self-start md:justify-self-end bg-white p-1">
              </div>
            </div>
            <div class="bg-neutral-950/90 p-6 sm:p-8 reveal">
              <div class="grid grid-cols-1 md:grid-cols-[1fr_180px] gap-8 items-center">
                <div>
                  <p class="text-xl sm:text-2xl font-semibold tracking-tight text-white">
                    Amanda微信
                  </p>
                  <p class="mt-3 text-sm sm:text-base leading-relaxed text-neutral-400">
                    商务合作 / 媒体合作 / 赛道赞助
                  </p>
                </div>
                <img :src="staticPath('images/amanda-wechat.jpg')" alt="Amanda微信二维码" class="w-full max-w-[180px] justify-self-start md:justify-self-end bg-white p-2">
              </div>
            </div>
            <div class="bg-neutral-950/90 p-6 sm:p-8 reveal">
              <div class="grid grid-cols-1 md:grid-cols-[1fr_180px] gap-8 items-center">
                <div>
                  <p class="text-xl sm:text-2xl font-semibold tracking-tight text-white">
                    加入 InnoAI x HKU
                  </p>
                  <p class="mt-3 text-sm sm:text-base leading-relaxed text-neutral-400">
                    一个以实践为导向的社群
                  </p>
                </div>
                <img :src="staticPath('images/innoai-application-form-d6f1424d.png')" alt="加入 InnoAI x HKU 二维码" class="w-full max-w-[220px] justify-self-start md:justify-self-end bg-white p-3">
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ ANNOUNCEMENT ============ -->
      <section v-show="currentPage === 'announcement'" id="announcement" class="page-panel py-28 sm:py-32 border-b border-neutral-800 scroll-mt-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
          <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4 reveal">
            (06) Announcement
          </p>
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
            <div class="lg:col-span-4 reveal">
              <h2 class="text-4xl sm:text-5xl font-semibold tracking-tight">
                Announcement
              </h2>
              <p class="mt-6 text-lg text-neutral-400 leading-relaxed max-w-sm">
                这里放最新通知、报名节点、赛道更新和现场安排。
              </p>
            </div>
            <div class="lg:col-span-8 grid grid-cols-1 gap-px bg-neutral-800 border border-neutral-800">
              <div class="bg-neutral-950/90 p-6 sm:p-8 reveal">
                <p class="mono text-xs text-neutral-500 uppercase tracking-wider">2026.08</p>
                <p class="mt-3 text-xl sm:text-2xl font-semibold tracking-tight text-white">报名信息持续更新中</p>
                <p class="mt-3 text-sm sm:text-base leading-relaxed text-neutral-400">如有新的开放时间、场地说明或合作信息，会优先同步在这里。</p>
              </div>
              <div class="bg-neutral-950/90 p-6 sm:p-8 reveal" style="transition-delay:.08s">
                <p class="mono text-xs text-neutral-500 uppercase tracking-wider">Updates</p>
                <p class="mt-3 text-xl sm:text-2xl font-semibold tracking-tight text-white">请关注社群与顶部入口</p>
                <p class="mt-3 text-sm sm:text-base leading-relaxed text-neutral-400">重要变化会同步到 Application 和 Community 两个入口，方便快速查看。</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ FAQ ============ -->
      <section v-show="currentPage === 'faq'" id="faq" class="page-panel py-28 sm:py-32 border-b border-neutral-800 scroll-mt-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 grid grid-cols-1 lg:grid-cols-12 gap-12">
          <div class="lg:col-span-4 reveal">
            <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">
              (07) F&amp;Q
            </p>
            <h2 class="text-4xl sm:text-5xl font-semibold tracking-tight">
              常见问题
            </h2>
          </div>
          <div class="lg:col-span-8 border-t border-neutral-800">
            <details class="group border-b border-neutral-800 reveal">
              <summary class="flex items-center justify-between gap-4 py-6 cursor-pointer list-none text-lg font-medium hover:text-neutral-300 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-white">
                我没有技术背景，可以参加吗？
                <i data-lucide="plus" class="w-5 h-5 shrink-0 transition-transform duration-200 group-open:rotate-45"></i>
              </summary>
              <div class="faq-answer">
                <p class="text-lg text-neutral-400 leading-relaxed pb-6 max-w-2xl">
                  可以。我们不设技术门槛。你需要的是「我看到了一个问题，我想解决它」这个念头。技术是手段，不是入场券。如果你是设计师、产品经理、商业方向的人，你在这里的价值可能比一个纯写代码的人更大。
                </p>
              </div>
            </details>
            <details class="group border-b border-neutral-800 reveal" style="transition-delay:.06s">
              <summary class="flex items-center justify-between gap-4 py-6 cursor-pointer list-none text-lg font-medium hover:text-neutral-300 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-white">
                我没有团队，可以参加吗？
                <i data-lucide="plus" class="w-5 h-5 shrink-0 transition-transform duration-200 group-open:rotate-45"></i>
              </summary>
              <div class="faq-answer">
                <p class="text-lg text-neutral-400 leading-relaxed pb-6 max-w-2xl">
                  可以。个人报名完全没问题，主办方会帮你匹配队友。事实上，很多人在黑客松上认识的队友，后来成了创业合伙人。
                </p>
              </div>
            </details>
            <details class="group border-b border-neutral-800 reveal" style="transition-delay:.12s">
              <summary class="flex items-center justify-between gap-4 py-6 cursor-pointer list-none text-lg font-medium hover:text-neutral-300 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-white">
                硬件赛道需要自己带设备吗？
                <i data-lucide="plus" class="w-5 h-5 shrink-0 transition-transform duration-200 group-open:rotate-45"></i>
              </summary>
              <div class="faq-answer">
                <p class="text-lg text-neutral-400 leading-relaxed pb-6 max-w-2xl">
                  不需要。深圳会场有合作方提供硬件资源。你带着想法来就行。当然，如果你有自己的设备，也欢迎带来。
                </p>
              </div>
            </details>
            <details class="group border-b border-neutral-800 reveal" style="transition-delay:.18s">
              <summary class="flex items-center justify-between gap-4 py-6 cursor-pointer list-none text-lg font-medium hover:text-neutral-300 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-white">
                不是港深的学生，可以参加吗？
                <i data-lucide="plus" class="w-5 h-5 shrink-0 transition-transform duration-200 group-open:rotate-45"></i>
              </summary>
              <div class="faq-answer">
                <p class="text-lg text-neutral-400 leading-relaxed pb-6 max-w-2xl">
                  可以。我们欢迎全球任何地区的参赛者。
                </p>
              </div>
            </details>
            <details class="group border-b border-neutral-800 reveal" style="transition-delay:.24s">
              <summary class="flex items-center justify-between gap-4 py-6 cursor-pointer list-none text-lg font-medium hover:text-neutral-300 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-white">
                我可以围观吗？
                <i data-lucide="plus" class="w-5 h-5 shrink-0 transition-transform duration-200 group-open:rotate-45"></i>
              </summary>
              <div class="faq-answer">
                <p class="text-lg text-neutral-400 leading-relaxed pb-6 max-w-2xl">
                  可以。Demo Day 开放公众参观，你可以亲手体验选手的作品并参与投票。观众报名通道稍后开放，敬请关注。
                </p>
              </div>
            </details>
          </div>
        </div>
      </section>

    </main>

    <!-- ============ FOOTER ============ -->
    <footer class="pt-16 relative overflow-hidden z-10">
      <canvas id="footerParticles" class="absolute inset-0 w-full h-full pointer-events-none" aria-hidden="true" style="z-index:0"></canvas>
      <div class="max-w-7xl mx-auto px-5 sm:px-8 relative z-10">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-10 pb-16 border-b border-neutral-800">
          <div class="col-span-2 md:col-span-1">
            <p class="font-semibold tracking-tight text-lg flex items-center gap-2">
              <span class="w-2 h-2 bg-white inline-block"></span>
              AIx Origin Summit
            </p>
            <p class="text-sm text-neutral-500 mt-3 max-w-xs leading-relaxed">
              Trace Origin, Build Together.
            </p>
          </div>
          <nav aria-label="Footer navigation">
            <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">
              Studio
            </p>
            <ul class="flex flex-col gap-2 text-sm text-neutral-400">
              <li>
                <a href="/story/" class="hover:text-white transition-colors">
                  Story
                </a>
              </li>
              <li>
                <a href="/information/" class="hover:text-white transition-colors">
                  Information
                </a>
              </li>
              <li>
                <a href="/community/" class="hover:text-white transition-colors">
                  Community
                </a>
              </li>
              <li>
                <a href="/faq/" class="hover:text-white transition-colors">
                  FAQ
                </a>
              </li>
            </ul>
          </nav>
          <nav aria-label="Social links">
            <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">
              Social
            </p>
            <ul class="flex flex-col gap-2 text-sm text-neutral-400">
              <li>
                <a href="https://mp.weixin.qq.com/s/CvT4-rnpuHviJlwYYzpB1A" class="hover:text-white transition-colors" target="_blank" rel="noopener noreferrer">
                  WeChat
                </a>
              </li>
              <li>
                <a href="https://www.linkedin.com/company/innoaixhku/" class="hover:text-white transition-colors" target="_blank" rel="noopener noreferrer">LinkedIn</a>
              </li>
              <li>
                <a href="https://www.instagram.com/innoaixhku/" class="hover:text-white transition-colors" target="_blank" rel="noopener noreferrer">
                  Instagram
                </a>
              </li>
              <li>
                <a href="https://xhslink.cn/m/VpRhklfjHp" class="hover:text-white transition-colors" target="_blank" rel="noopener noreferrer">
                  小红书
                </a>
              </li>
            </ul>
          </nav>
          <div>
            <p class="mono text-xs text-neutral-500 uppercase tracking-wider mb-4">
              Contact
            </p>
            <ul class="flex flex-col gap-2 text-sm text-neutral-400">
              <li>
                <a href="mailto:innoaihku@gmail.com" class="hover:text-white transition-colors">
                  innoaihku@gmail.com
                </a>
              </li>
              <li>
                <a href="mailto:innoaixhku@outlook.com" class="hover:text-white transition-colors">
                  innoaixhku@outlook.com
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
</template>

<script setup>
import { onMounted } from 'vue';
import { initAixOriginPage } from './aixorigin-page.js';
import './assets/aixorigin.css';

const pageByPath = {
  '/': 'home',
  '/story/': 'story',
  '/information/': 'information',
  '/application/': 'application',
  '/community/': 'community',
  '/announcement/': 'announcement',
  '/faq/': 'faq',
};

const staticPath = (path) => {
  const cleanPath = path.replace(/^\/+/, '');
  return window.location.protocol === 'file:' ? `./static/${cleanPath}` : `/static/${cleanPath}`;
};

const normalizePagePath = (pathname) => {
  const cleanPath = pathname.replace(/\/index\.html$/, '/');
  return cleanPath.endsWith('/') ? cleanPath : `${cleanPath}/`;
};
const currentPage = pageByPath[normalizePagePath(window.location.pathname)] || 'home';
const uiLang = (() => {
  try {
    return window.localStorage.getItem('aixorigin-lang') || 'zh-CN';
  } catch {
    return 'zh-CN';
  }
})();

const uiText = {
  '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）（必选）': {
    en: 'Team preference (1-5 people per team; cross-school and cross-organization teams allowed) (required)',
  },
  '若自行组队，请输入队名（可选）': {
    en: 'If you have a team, enter the team name (optional)',
  },
  '编程能力（如 C/C++/Python/Java 等）': {
    en: 'Programming (e.g. C/C++/Python/Java)',
  },
  '硬件开发（如 PCB设计、电路调试、嵌入式系统）': {
    en: 'Hardware development (e.g. PCB design, circuit debugging, embedded systems)',
  },
  '产品/用户研究（需求挖掘、洞察）': {
    en: 'Product / user research (needs discovery, insights)',
  },
  '设计表达（UI/UX、3D建模、视觉传达）': {
    en: 'Design expression (UI/UX, 3D modeling, visual communication)',
  },
  '项目协作（进度把控、跨学科沟通、文档整理）': {
    en: 'Project collaboration (timeline control, cross-disciplinary communication, documentation)',
  },
  '可以是你的个人网站、LinkedIn、Github、小红书、X、Bilibili、Reddit、Instagram...': {
    en: 'This can be your personal site, LinkedIn, GitHub, Xiaohongshu, X, Bilibili, Reddit, Instagram, etc.',
  },
  '在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。（可选）': {
    en: 'What interesting things have you done in the past 18 months? Please describe in detail. (optional)',
  },
  '包括产品/项目、你具体做了什么部分、花了多久、有没有真实用户/收入/下载/开源 star/粉丝等结果。一个APP？电路板？网站？Agent？还是一个小红书视频账号？一个赚钱的生意？一个github开源项目？': {
    en: 'Include the product or project, what parts you specifically worked on, how long it took, and whether there were real users, revenue, downloads, open-source stars, followers, or other results. Was it an app, a circuit board, a website, an agent, a Xiaohongshu video account, a profitable business, or a GitHub open-source project?',
  },
  '是否愿意信息公开联系方式给合作方公司用于招聘/投资对接（可选）': {
    en: 'May we share your contact information with partners for recruiting or investment matching? (optional)',
  },
  '1=从未接触; 2=初学; 3=能独立完成; 4=有丰富项目经验': {
    en: '1 = no experience; 2 = beginner; 3 = independent; 4 = strong project experience',
  },
  '手工/焊接': {
    en: 'Handcraft / soldering',
  },
  'AI Agent': {
    en: 'AI agent',
  },
  '前端工程（React / Vue.js 等）': {
    en: 'Frontend engineering (React / Vue.js, etc.)',
  },
  'Vibe coding': {
    en: 'Vibe coding',
  },
  '我们充分尊重你的意愿': {
    en: 'We fully respect your preference.',
  },
  '愿意': {
    en: 'Yes',
  },
  '不愿意': {
    en: 'No',
  },
  '其他': {
    en: 'Other',
  },
};

const t = (text) => {
  const entry = uiText[text];
  if (uiLang === 'en') return entry?.en || text;
  return text;
};

onMounted(() => {
  initAixOriginPage();
});
</script>

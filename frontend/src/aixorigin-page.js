const externalScripts = [
  {
    "src": "https://www.googletagmanager.com/gtag/js?id=G-2M6V79H761",
    "asyncAttr": true
  },
  {
    "src": "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js",
    "asyncAttr": false
  },
  {
    "src": "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js",
    "asyncAttr": false
  },
  {
    "src": "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js",
    "asyncAttr": false
  }
];

function loadScript(src, asyncAttr = false) {
  return new Promise((resolve, reject) => {
    const existing = document.querySelector('script[data-aixorigin-src="' + src + '"]');
    if (existing) {
      if (existing.dataset.loaded === 'true') resolve();
      else existing.addEventListener('load', resolve, { once: true });
      return;
    }
    const script = document.createElement('script');
    script.src = src;
    script.async = asyncAttr;
    script.dataset.aixoriginSrc = src;
    script.addEventListener('load', () => { script.dataset.loaded = 'true'; resolve(); }, { once: true });
    script.addEventListener('error', () => reject(new Error('Failed to load ' + src)), { once: true });
    document.head.appendChild(script);
  });
}

async function loadExternalScripts() {
  for (const script of externalScripts) {
    try {
      await loadScript(script.src, script.asyncAttr);
    } catch (error) {
      // Keep the page usable even when external CDNs are unavailable.
      console.warn(error);
    }
  }
}

export async function initAixOriginPage() {
  await loadExternalScripts();

  // Original page script 1
  {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    if (typeof window.gtag === 'function') {
      gtag('js', new Date());
      gtag('config', 'G-2M6V79H761');
    }
  }

  // Original page script 2
  {
    if (window.lucide?.createIcons) {
      window.lucide.createIcons({ attrs: { 'stroke-width': 1.5 } });
    }
    
          // Header contrast on scroll
          const header = document.getElementById('siteHeader');
          const onScroll = () => {
            if (window.scrollY > 24) {
              header.classList.add('bg-neutral-950/85', 'backdrop-blur-md', 'border-neutral-800');
            } else {
              header.classList.remove('bg-neutral-950/85', 'backdrop-blur-md', 'border-neutral-800');
            }
          };
          window.addEventListener('scroll', onScroll, { passive: true });
          onScroll();
    
          // Mobile menu
          const menuBtn = document.getElementById('menuBtn');
          const mobileMenu = document.getElementById('mobileMenu');
          menuBtn.addEventListener('click', () => {
            const open = mobileMenu.classList.toggle('hidden') === false;
            menuBtn.setAttribute('aria-expanded', open);
          });
          mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
            menuBtn.setAttribute('aria-expanded', 'false');
          }));
          document.addEventListener('keydown', e => {
            if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
              mobileMenu.classList.add('hidden');
              menuBtn.setAttribute('aria-expanded', 'false');
              menuBtn.focus();
            }
          });
    
          // Reveal on scroll
          const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
          const targets = document.querySelectorAll('.reveal, .mask-reveal');
          if (reduced || !('IntersectionObserver' in window)) {
            targets.forEach(el => el.classList.add('in'));
          } else {
            const io = new IntersectionObserver(entries => {
              entries.forEach(entry => {
                if (entry.isIntersecting) {
                  entry.target.classList.add('in');
                  io.unobserve(entry.target);
                }
              });
            }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
            targets.forEach(el => io.observe(el));
          }
  }

  // Original page script 3
  {
    (function(){
            // Scroll-scrubbed word reveal — flexible params
            var cfg = {
              hiddenOpacity: 0.12, // starting opacity per word
              blur: 6,             // starting blur in px
              yOffset: 14,         // starting y offset in px
              stagger: 0.05,       // stagger between words
              start: 'top 80%',    // scroll start
              end: 'bottom 55%'    // scroll end
            };
            var el = document.getElementById('scrubText');
            if (!el || !window.gsap || !window.ScrollTrigger) return;
            gsap.registerPlugin(ScrollTrigger);
            var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            // Split text nodes into word spans, preserving inline emphasis elements
            function splitWords(node){
              Array.prototype.slice.call(node.childNodes).forEach(function(child){
                if (child.nodeType === 3) {
                  var frag = document.createDocumentFragment();
                  child.textContent.split(/(\s+)/).forEach(function(part){
                    if (!part) return;
                    if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); }
                    else {
                      var s = document.createElement('span');
                      s.className = 'scrub-word';
                      s.style.display = 'inline-block';
                      s.style.willChange = 'opacity, filter, transform';
                      s.textContent = part;
                      frag.appendChild(s);
                    }
                  });
                  node.replaceChild(frag, child);
                } else if (child.nodeType === 1) {
                  splitWords(child);
                }
              });
            }
            splitWords(el);
            var words = el.querySelectorAll('.scrub-word');
            if (!words.length || reduced) return;
            gsap.fromTo(words,
              { opacity: cfg.hiddenOpacity, filter: 'blur(' + cfg.blur + 'px)', y: cfg.yOffset },
              {
                opacity: 1, filter: 'blur(0px)', y: 0, ease: 'none', stagger: cfg.stagger,
                scrollTrigger: { trigger: el, start: cfg.start, end: cfg.end, scrub: true }
              }
            );
          })();
  }

  // Original page script 4
  {
    (function(){var wrap=document.querySelector('[data-timeline]');if(!wrap)return;var line=document.getElementById('processProgressLine');var steps=Array.prototype.filter.call(wrap.children,function(c){return c.classList.contains('py-10');});steps.forEach(function(s){var d=document.createElement('span');d.className='tl-dot';d.setAttribute('aria-hidden','true');s.appendChild(d);});var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;function update(){var r=wrap.getBoundingClientRect();var vh=window.innerHeight;var p=(vh*0.7-r.top)/r.height;p=Math.max(0,Math.min(1,p));if(line)line.style.transform='scaleY('+p+')';steps.forEach(function(s){var sr=s.getBoundingClientRect();if(sr.top<vh*0.75){s.classList.add('tl-active');}else{s.classList.remove('tl-active');}});}if(reduced){if(line)line.style.transform='scaleY(1)';steps.forEach(function(s){s.classList.add('tl-active');});return;}var ticking=false;function onScroll(){if(!ticking){ticking=true;requestAnimationFrame(function(){update();ticking=false;});}}window.addEventListener('scroll',onScroll,{passive:true});window.addEventListener('resize',onScroll);update();})();
  }

  // Original page script 5
  {
    (function(){function init(){var canvas=document.getElementById('footerParticles');if(!canvas||!window.THREE)return;var renderer=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:true});var scene=new THREE.Scene();var camera=new THREE.OrthographicCamera(-1,1,1,-1,0,1);var material=new THREE.ShaderMaterial({transparent:true,depthWrite:false,uniforms:{uTime:{value:0},uResolution:{value:new THREE.Vector2()}},vertexShader:'void main(){gl_Position=vec4(position,1.0);}',fragmentShader:'uniform float uTime;uniform vec2 uResolution;void main(){vec2 st=gl_FragCoord.xy/uResolution.xy;float aspect=uResolution.x/uResolution.y;st.x*=aspect;float angle=-0.7;mat2 rot=mat2(cos(angle),-sin(angle),sin(angle),cos(angle));vec2 pos=rot*st;float wave1=sin(pos.y*8.0-uTime*0.5);float wave2=sin(pos.y*18.0-uTime*0.8);float wave3=sin(pos.y*4.0-uTime*0.2);float ray1=pow(wave1*0.5+0.5,6.0);float ray2=pow(wave2*0.5+0.5,12.0)*0.5;float ray3=pow(wave3*0.5+0.5,3.0)*0.3;float rays=max(max(ray1,ray2),ray3);vec3 whiteBlue=vec3(0.49,0.83,0.98);vec3 deepBlue=vec3(0.1,0.5,1.0);float mixAmount=(gl_FragCoord.x/uResolution.x)*0.7+(1.0-gl_FragCoord.y/uResolution.y)*0.3;vec3 color=mix(whiteBlue,deepBlue,mixAmount);vec3 finalColor=color*rays*1.5+color*0.05;float fadeY=smoothstep(0.0,0.5,st.y)*smoothstep(1.2,0.3,st.y);float directionalFade=smoothstep(1.5,0.0,st.x/aspect+st.y*0.5);gl_FragColor=vec4(finalColor*fadeY*directionalFade,1.0);}'});scene.add(new THREE.Mesh(new THREE.PlaneGeometry(2,2),material));function resize(){var rect=canvas.parentElement.getBoundingClientRect();renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));renderer.setSize(rect.width,rect.height,false);material.uniforms.uResolution.value.set(rect.width,rect.height);}window.addEventListener('resize',resize,{passive:true});resize();var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;function render(time){material.uniforms.uTime.value=time*0.001;renderer.render(scene,camera);if(!reduced)requestAnimationFrame(render);}requestAnimationFrame(render);}window.addEventListener('load',init);})();
  }

  // Original page script 6
  {
    (function(){if(!window.THREE)return;var wrap=document.getElementById('abyssWrap'),cv=document.getElementById('abyssCanvas');if(!wrap||!cv)return;var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;var COUNT=reduced?8750:(window.innerWidth<768?40000:120000);var renderer=new THREE.WebGLRenderer({canvas:cv,antialias:false,alpha:true});renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));var scene=new THREE.Scene();var cam=new THREE.PerspectiveCamera(60,1,0.1,100);cam.position.z=14;var BX=22,BY=12,BZ=14;var pos=new Float32Array(COUNT*3),vel=new Float32Array(COUNT*3),size=new Float32Array(COUNT),phase=new Float32Array(COUNT),hue=new Float32Array(COUNT),boost=new Float32Array(COUNT);for(var i=0;i<COUNT;i++){pos[i*3]=(Math.random()-0.5)*BX*2;pos[i*3+1]=(Math.random()-0.5)*BY*2;pos[i*3+2]=(Math.random()-0.5)*BZ;size[i]=1.5+Math.random()*3.5;phase[i]=Math.random()*6.283;hue[i]=Math.random()*0.35;}var geo=new THREE.BufferGeometry();geo.setAttribute('position',new THREE.BufferAttribute(pos,3));geo.setAttribute('aSize',new THREE.BufferAttribute(size,1));geo.setAttribute('aPhase',new THREE.BufferAttribute(phase,1));geo.setAttribute('aHue',new THREE.BufferAttribute(hue,1));var mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,uniforms:{uTime:{value:0}},vertexShader:'attribute float aSize;attribute float aPhase;attribute float aHue;uniform float uTime;varying float vHue;varying float vF;varying float vDepth;void main(){vHue=aHue;vF=0.75+0.25*sin(uTime*1.7+aPhase);vec4 mv=modelViewMatrix*vec4(position,1.0);vDepth=clamp((-mv.z-4.0)/22.0,0.0,1.0);gl_PointSize=aSize*(30.0/-mv.z);gl_Position=projectionMatrix*mv;}',fragmentShader:'varying float vHue;varying float vF;varying float vDepth;void main(){float d=length(gl_PointCoord-vec2(0.5));if(d>0.5)discard;float a=pow(1.0-d*2.0,1.6);vec3 c1=vec3(0.32,0.70,1.0);vec3 c2=vec3(0.82,0.94,1.0);vec3 c3=vec3(1.0,1.0,1.0);float h=clamp(vHue,0.0,1.0);vec3 c=h<0.5?mix(c1,c2,h*2.0):mix(c2,c3,(h-0.5)*2.0);float dim=mix(1.0,0.45,vDepth);gl_FragColor=vec4(c*a*vF*1.8*dim,a*vF*dim);}'});var pts=new THREE.Points(geo,mat);scene.add(pts);function resize(){var w=Math.max(wrap.clientWidth,1),h=Math.max(wrap.clientHeight,1);renderer.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix();}window.addEventListener('resize',resize);resize();var ptr={x:0,y:0,on:false,hold:false};function setPtr(cx,cy){var r=wrap.getBoundingClientRect();if(cy<r.top||cy>r.bottom||cx<r.left||cx>r.right){ptr.on=false;return;}var nx=(cx-r.left)/r.width*2-1,ny=-(((cy-r.top)/r.height)*2-1);var s=Math.tan(cam.fov*Math.PI/360)*cam.position.z;ptr.x=nx*s*cam.aspect;ptr.y=ny*s;ptr.on=true;}window.addEventListener('pointermove',function(e){setPtr(e.clientX,e.clientY);},{passive:true});window.addEventListener('pointerdown',function(e){ptr.hold=true;setPtr(e.clientX,e.clientY);});window.addEventListener('pointerup',function(){ptr.hold=false;});function curl(x,y,z,t){return[Math.sin(y*0.35+t*0.4)+0.6*Math.cos(z*0.5+t*0.3),Math.sin(z*0.4-t*0.35)+0.6*Math.cos(x*0.3+t*0.25)-0.15,Math.sin(x*0.3+t*0.3)*0.5];}var t=0,visible=false,raf=null,last=performance.now();function tick(now){raf=null;var dt=Math.min((now-last)/1000,0.05);last=now;t+=dt;mat.uniforms.uTime.value=t;for(var i=0;i<COUNT;i++){var ix=i*3,x=pos[ix],y=pos[ix+1],z=pos[ix+2];var depth=1.0-((z+BZ*0.5)/BZ)*0.6;var f=curl(x,y,z,t);vel[ix]+=(f[0]*0.6*depth-vel[ix])*0.03;vel[ix+1]+=(f[1]*0.6*depth-vel[ix+1])*0.03;vel[ix+2]+=(f[2]*0.4-vel[ix+2])*0.03;if(ptr.on){var dx=x-ptr.x,dy=y-ptr.y,dd=dx*dx+dy*dy;if(dd<9){var d2=Math.sqrt(dd)+0.001,st=1-d2/3;if(ptr.hold){vel[ix]-=dx/d2*st*0.25;vel[ix+1]-=dy/d2*st*0.25;}else{vel[ix]+=dx/d2*st*0.5;vel[ix+1]+=dy/d2*st*0.5;}boost[i]=Math.min(boost[i]+st*0.3,1);}}boost[i]*=0.97;x+=vel[ix]*dt*2.2;y+=vel[ix+1]*dt*2.2;z+=vel[ix+2]*dt*2.2;if(x>BX)x-=BX*2;if(x<-BX)x+=BX*2;if(y>BY)y-=BY*2;if(y<-BY)y+=BY*2;if(z>BZ*0.5)z-=BZ;if(z<-BZ*0.5)z+=BZ;pos[ix]=x;pos[ix+1]=y;pos[ix+2]=z;var sp=Math.min(Math.sqrt(vel[ix]*vel[ix]+vel[ix+1]*vel[ix+1])*0.9,1);hue[i]=Math.min(sp*0.7+boost[i],1);}geo.attributes.position.needsUpdate=true;geo.attributes.aHue.needsUpdate=true;renderer.render(scene,cam);if(visible&&!reduced)raf=requestAnimationFrame(tick);}if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){visible=e.isIntersecting;if(visible&&!raf){last=performance.now();raf=requestAnimationFrame(tick);}});},{threshold:0.05}).observe(wrap);}else{visible=true;raf=requestAnimationFrame(tick);}if(reduced){renderer.render(scene,cam);}})();
  }

  // Original page script 7
  {
    (function(){var heading=document.getElementById('heroHeading');if(!heading)return;var words=heading.querySelectorAll('.hero-word');words.forEach(function(w){w.style.fontVariationSettings='"wght" 300';w.style.fontWeight='300';});})();
  }

  // Original page script 8
  {
    (function(){var canvas=document.getElementById('novaLightBackground');if(!canvas||!window.THREE)return;var renderer=new THREE.WebGLRenderer({canvas:canvas,alpha:true,antialias:true});var scene=new THREE.Scene();var camera=new THREE.OrthographicCamera(-1,1,1,-1,0,1);var material=new THREE.ShaderMaterial({transparent:true,depthWrite:false,uniforms:{uTime:{value:0},uResolution:{value:new THREE.Vector2()}},vertexShader:'void main(){gl_Position=vec4(position,1.0);}',fragmentShader:'uniform float uTime;uniform vec2 uResolution;void main(){vec2 st=gl_FragCoord.xy/uResolution.xy;float aspect=uResolution.x/uResolution.y;st.x*=aspect;float angle=-0.7;mat2 rot=mat2(cos(angle),-sin(angle),sin(angle),cos(angle));vec2 pos=rot*st;float wave1=sin(pos.y*8.0-uTime*0.5);float wave2=sin(pos.y*18.0-uTime*0.8);float wave3=sin(pos.y*4.0-uTime*0.2);float ray1=pow(wave1*0.5+0.5,6.0);float ray2=pow(wave2*0.5+0.5,12.0)*0.5;float ray3=pow(wave3*0.5+0.5,3.0)*0.3;float rays=max(max(ray1,ray2),ray3);vec3 whiteBlue=vec3(0.49,0.83,0.98);vec3 deepBlue=vec3(0.1,0.5,1.0);float mixAmount=(gl_FragCoord.x/uResolution.x)*0.7+(1.0-gl_FragCoord.y/uResolution.y)*0.3;vec3 color=mix(whiteBlue,deepBlue,mixAmount);vec3 finalColor=color*rays*1.5+color*0.05;float fadeY=smoothstep(0.0,0.5,st.y)*smoothstep(1.2,0.3,st.y);float directionalFade=smoothstep(1.5,0.0,st.x/aspect+st.y*0.5);gl_FragColor=vec4(finalColor*fadeY*directionalFade,1.0);}'});scene.add(new THREE.Mesh(new THREE.PlaneGeometry(2,2),material));function resize(){renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));renderer.setSize(window.innerWidth,window.innerHeight,false);material.uniforms.uResolution.value.set(window.innerWidth,window.innerHeight);}window.addEventListener('resize',resize,{passive:true});resize();var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;function render(time){material.uniforms.uTime.value=time*0.001;renderer.render(scene,camera);if(!reduced)requestAnimationFrame(render);}requestAnimationFrame(render);})();
  }

  // FAQ accordion animation
  {
    (function () {
            var details = document.querySelectorAll('#faq details');
            details.forEach(function (item) {
              var summary = item.querySelector('summary');
              if (!summary) return;
              summary.addEventListener('click', function (event) {
                if (!item.open || item.classList.contains('faq-closing')) return;
                event.preventDefault();
                item.classList.add('faq-closing');
                window.setTimeout(function () {
                  item.open = false;
                  item.classList.remove('faq-closing');
                }, 460);
              });
            });
          })();
  }

  // Original page script 9
  {
    (function () {
            var cityInputs = document.querySelectorAll('input[name="participation_city"]');
            var shenzhenInputs = document.querySelectorAll('input[name="track_shenzhen"]');
            var hongKongInputs = document.querySelectorAll('input[name="track_hong_kong"]');
            if (!cityInputs.length || !shenzhenInputs.length || !hongKongInputs.length) return;

            function setTrackGroup(inputs, enabled) {
              inputs.forEach(function (input, index) {
                input.disabled = !enabled;
                input.required = enabled && index === 0;
                if (!enabled) input.checked = false;
                var choice = input.closest('.app-choice');
                if (choice) choice.classList.toggle('app-choice-disabled', !enabled);
              });
            }

            function syncTrackAvailability() {
              var selected = document.querySelector('input[name="participation_city"]:checked');
              var value = selected ? selected.value : '';
              var isShenzhen = value.indexOf('深圳') !== -1;
              var isHongKong = value.indexOf('香港') !== -1;
              setTrackGroup(shenzhenInputs, isShenzhen);
              setTrackGroup(hongKongInputs, isHongKong);
            }

            cityInputs.forEach(function (input) {
              input.addEventListener('change', syncTrackAvailability);
            });
            syncTrackAvailability();
          })();

    (function () {
            var form = document.getElementById('applicationForm');
            if (!form) return;

            form.addEventListener('submit', function (event) {
              event.preventDefault();
              var button = form.querySelector('button[type="submit"]');
              var originalText = button ? button.textContent.trim() : '';
              if (button) {
                button.disabled = true;
                button.textContent = '提交中...';
              }

              fetch('/api/contracts/', {
                method: 'POST',
                body: new FormData(form)
              })
                .then(function (response) {
                  return response.text().then(function (text) {
                    var payload = null;
                    try {
                      payload = text ? JSON.parse(text) : null;
                    } catch (error) {
                      payload = null;
                    }
                    if (!response.ok || !payload.ok) {
                      var message = payload && payload.error ? payload.error : (text && text.trim() ? '提交失败，请稍后重试' : '提交失败，请检查必填项');
                      throw new Error(message);
                    }
                    return payload;
                  });
                })
                .then(function () {
                  if (button) button.textContent = '已收到申请';
                  form.reset();
                  form.querySelectorAll('.app-choice-disabled').forEach(function (choice) {
                    choice.classList.remove('app-choice-disabled');
                  });
                  document.querySelectorAll('input[name="participation_city"]').forEach(function (input) {
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                  });
                })
                .catch(function (error) {
                  alert(error.message || '提交失败，请检查必填项');
                  if (button) {
                    button.disabled = false;
                    button.textContent = originalText || '送出申请';
                  }
                });
            });
          })();

    (function () {
            var defaults = {};
            var lang = 'zh-CN';
    
            function store(key, el, mode) {
              if (!el) return;
              defaults[key] = defaults[key] || {};
              defaults[key][mode || 'text'] = mode === 'html' ? el.innerHTML : el.textContent;
            }
            function setText(el, value) { if (el) el.textContent = value; }
            function setHTML(el, value) { if (el) el.innerHTML = value; }
            function restore(key, el, mode) {
              if (!el || !defaults[key]) return;
              var value = defaults[key][mode || 'text'];
              if (typeof value !== 'string') return;
              if (mode === 'html') el.innerHTML = value; else el.textContent = value;
            }
            function applyButtons(active) {
              document.querySelectorAll('[data-lang-btn]').forEach(function (btn) {
                var on = btn.getAttribute('data-lang-btn') === active;
                btn.classList.toggle('bg-white', on);
                btn.classList.toggle('text-neutral-950', on);
                btn.classList.toggle('border-white', on);
                btn.classList.toggle('text-neutral-400', !on);
              });
            }
            function applyTextMap(langCode) {
              var maps = {
                'zh-CN': {
                  'F&Q': 'F&Q',
                  'FAQ': 'F&Q',
                  '多元背景': '多元背景',
                  '当前合作方生态': '当前合作方生态',
                  '来自港校 + 内地 + 海外高校的参赛选手首次进行全域联合，形成香港本土体量天花板级别的跨校创造者网络。': '来自港校 + 内地 + 海外高校的参赛选手首次进行全域联合，形成香港本土体量天花板级别的跨校创造者网络。',
                  '多元化合作版图正在持续扩展，覆盖社群组织、合办企业与支持单位，为参赛项目提供更完整的资源入口。': '多元化合作版图正在持续扩展，覆盖社群组织、合办企业与支持单位，为参赛项目提供更完整的资源入口。',
                  'Hong Kong': 'Hong Kong',
                  'Mainland + Global': 'Mainland + Global',
                  '香港大学 / 香港中文大学 / 香港科技大学 / PolyU / CityU / HKBU / LingU / EdUHK': '香港大学 / 香港中文大学 / 香港科技大学 / PolyU / CityU / HKBU / LingU / EdUHK',
                  '清华深研院 / 北大深研院 / 哈工深 / Yale / UPenn / NYU / JHU / NUS / NTU': '清华深研院 / 北大深研院 / 哈工深 / Yale / UPenn / NYU / JHU / NUS / NTU',
                  '香港高校': '香港高校',
                  '内地高校': '内地高校',
                  '海外高校': '海外高校',
                  '香港更多高校': '香港更多高校',
                  '香港大学': '香港大学',
                  '香港中文大学': '香港中文大学',
                  '香港科技大学': '香港科技大学',
                  '清华深研院': '清华深研院',
                  '北大深研院': '北大深研院',
                  '哈工深': '哈工深',
                  'PolyU': 'PolyU',
                  'CityU': 'CityU',
                  'HKBU': 'HKBU',
                  'LingU': 'LingU',
                  'EdUHK': 'EdUHK',
                  'Yale': 'Yale',
                  'UPenn': 'UPenn',
                  'NYU': 'NYU',
                  'JHU': 'JHU',
                  'NUS': 'NUS',
                  'NTU': 'NTU',
                  '社群组织': '社群组织',
                  '合办企业': '联合主办单位',
                  '支持单位': '支持单位',
                  '+ 更多': '+ 更多',
                  '姓名（必选）': '姓名（必选）',
                  '您希望我们怎样称呼您？': '您希望我们怎样称呼您？',
                  '手机号（必选）': '手机号（必选）',
                  '确保可以加到微信': '确保可以加到微信',
                  '电子邮箱（必选）': '电子邮箱（必选）',
                  '你的身份（可选）': '你的身份（可选）',
                  '学生': '学生',
                  '职场人士': '职场人士',
                  '独立开发者/创作者': '独立开发者/创作者',
                  '创业者': '创业者',
                  '其他': '其他',
                  '是': '是',
                  '否': '否',
                  '学校背景/工作背景（必选）': '学校背景/工作背景（必选）',
                  '学校标注：院校 + 专业 + 年级；工作表明：公司 + 岗位 + 工作年限': '学校标注：院校 + 专业 + 年级；工作表明：公司 + 岗位 + 工作年限',
                  '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）（必选）': '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）（必选）',
                  '参赛者可以在选手交流群里找到自己期待的队友。如果暂时没有找到合适的队友又不希望单枪匹马开发，主办方这边也可以帮你匹配。': '参赛者可以在选手交流群里找到自己期待的队友。如果暂时没有找到合适的队友又不希望单枪匹马开发，主办方这边也可以帮你匹配。',
                  '自行组队（请补充队友姓名/联系方式）': '自行组队（请补充队友姓名/联系方式）',
                  '个人参赛': '个人参赛',
                  '希望由主办方随机匹配队友': '希望由主办方随机匹配队友',
                  '若自行组队，请输入队名（可选）': '若自行组队，请输入队名（可选）',
                  '参加方式（必选）': '参加方式（必选）',
                  '深圳（Anchor+Weave）': '深圳（Anchor+Weave）',
                  '香港（Flux+Vital）（必须有港澳通行证及相关证件）': '香港（Flux+Vital）（必须有港澳通行证及相关证件）',
                  '参与赛道（深圳）（必选）': '参与赛道（深圳）（必选）',
                  '选好后不可再改': '选好后不可再改',
                  'Anchor · 具构（深圳）— 具身智能 & 智能硬件': 'Anchor · 具构（深圳）— 具身智能 & 智能硬件',
                  'Weave · 织域（深圳）— 全域融合 & Agent + 创意': 'Weave · 织域（深圳）— 全域融合 & Agent + 创意',
                  '参与赛道（香港）（必选）': '参与赛道（香港）（必选）',
                  'Flux · 流境（香港）— 数字金融 & Web3.0': 'Flux · 流境（香港）— 数字金融 & Web3.0',
                  'Vital · 活域（香港）— 生命科学 & Healthcare': 'Vital · 活域（香港）— 生命科学 & Healthcare',
                  '是否参与过完整的创业项目或开发项目（可选）': '是否参与过完整的创业项目或开发项目（可选）',
                  '是': '是',
                  '否': '否',
                  'Your GitHub / personal homepage (optional)': '你的GitHub/个人主页（可选）',
                  '你的作品集，简历（可选）': '你的作品集，简历（可选）',
                  '项目简述（可选）': '项目简述（可选）',
                  '请简单介绍你的创意 / 项目，以及你希望落地这个方向的原因。': '请简单介绍你的创意 / 项目，以及你希望落地这个方向的原因。',
                  '你是否愿意在赛后将你的优秀项目进一步推进落地？（必选）': '你是否愿意在赛后将你的优秀项目进一步推进落地？（必选）',
                  '技能评价（必选）': '技能评价（必选）',
                  '1=从未接触; 2=初学; 3=能独立完成; 4=有丰富项目经验': '1=从未接触; 2=初学; 3=能独立完成; 4=有丰富项目经验',
                  '编程能力（如 C/C++/Python/Java 等）': '编程能力（如 C/C++/Python/Java 等）',
                  '硬件开发（如 PCB设计、电路调试、嵌入式系统）': '硬件开发（如 PCB设计、电路调试、嵌入式系统）',
                  '产品/用户研究（需求挖掘、洞察）': '产品/用户研究（需求挖掘、洞察）',
                  '设计表达（UI/UX、3D建模、视觉传达）': '设计表达（UI/UX、3D建模、视觉传达）',
                  '项目协作（进度把控、跨学科沟通、文档整理）': '项目协作（进度把控、跨学科沟通、文档整理）',
                  '你的“硬”实力 (Hardware Skills)（必选）': '你的“硬”实力 (Hardware Skills)（必选）',
                  'PCB设计 (KiCad/Altium)': 'PCB设计 (KiCad/Altium)',
                  '嵌入式开发 (Arduino/ESP32/STM32)': '嵌入式开发 (Arduino/ESP32/STM32)',
                  '结构设计/3D建模 (Fusion360/SolidWorks/Blender)': '结构设计/3D建模 (Fusion360/SolidWorks/Blender)',
                  '手工/焊接': '手工/焊接',
                  '快速模型制作3d打印/激光切割': '快速模型制作3d打印/激光切割',
                  '传感器与电路': '传感器与电路',
                  '导电织物 / 可穿戴电子': '导电织物 / 可穿戴电子',
                  '你的“软”实力 (Software & AI)（必选）': '你的“软”实力 (Software & AI)（必选）',
                  '大模型API调用': '大模型API调用',
                  'AI Agent': 'AI Agent',
                  '机器视觉': '机器视觉',
                  '运动算法': '运动算法',
                  '后端开发': '后端开发',
                  '前端工程（React / Vue.js 等）': '前端工程（React / Vue.js 等）',
                  '边缘计算/端侧部署': '边缘计算/端侧部署',
                  'Vibe coding': 'Vibe coding',
                  '请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）（可选）': '请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）（可选）',
                  '可以是你的个人网站、LinkedIn、Github、小红书、X、Bilibili、Reddit、Instagram...': '可以是你的个人网站、LinkedIn、Github、小红书、X、Bilibili、Reddit、Instagram...',
                  '在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。（可选）': '在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。（可选）',
                  '包括产品/项目、你具体做了什么部分、花了多久、有没有真实用户/收入/下载/开源 star/粉丝等结果。一个APP？电路板？网站？Agent？还是一个小红书视频账号？一个赚钱的生意？一个github开源项目？': '包括产品/项目、你具体做了什么部分、花了多久、有没有真实用户/收入/下载/开源 star/粉丝等结果。一个APP？电路板？网站？Agent？还是一个小红书视频账号？一个赚钱的生意？一个github开源项目？',
                  '我们充分尊重你的意愿': '我们充分尊重你的意愿',
                  '选好后不可再改': '选好后不可再改',
                  '是否愿意信息公开联系方式给合作方公司用于招聘/投资对接（可选）': '是否愿意信息公开联系方式给合作方公司用于招聘/投资对接（可选）',
                  '愿意': '愿意',
                  '不愿意': '不愿意',
                  '待填写者输入': '待填写者输入'
                },
                'en': {
                  'F&Q': 'FAQ',
                  'FAQ': 'FAQ',
                  '多元背景': 'Diverse Backgrounds',
                  '当前合作方生态': 'Current Partnership Ecosystem',
                  '来自港校 + 内地 + 海外高校的参赛选手首次进行全域联合，形成香港本土体量天花板级别的跨校创造者网络。': 'Participants from Hong Kong, mainland China, and overseas universities are joining together for the first full-region collaboration, forming a cross-campus builder network at unprecedented local scale.',
                  '多元化合作版图正在持续扩展，覆盖社群组织、合办企业与支持单位，为参赛项目提供更完整的资源入口。': 'The partnership map continues to expand across communities, co-hosting companies, and supporting organizations, giving projects a stronger resource network.',
                  'Hong Kong': 'Hong Kong',
                  'Mainland + Global': 'Mainland + Global',
                  '香港大学 / 香港中文大学 / 香港科技大学 / PolyU / CityU / HKBU / LingU / EdUHK': 'HKU / CUHK / HKUST / PolyU / CityU / HKBU / LingU / EdUHK',
                  '清华深研院 / 北大深研院 / 哈工深 / Yale / UPenn / NYU / JHU / NUS / NTU': 'Tsinghua SIGS / PKU Shenzhen / HITSZ / Yale / UPenn / NYU / JHU / NUS / NTU',
                  '香港高校': 'Hong Kong Universities',
                  '内地高校': 'Mainland Universities',
                  '海外高校': 'Overseas Universities',
                  '香港更多高校': 'More Hong Kong Universities',
                  '香港大学': 'HKU',
                  '香港中文大学': 'CUHK',
                  '香港科技大学': 'HKUST',
                  '清华深研院': 'Tsinghua SIGS',
                  '北大深研院': 'PKU Shenzhen',
                  '哈工深': 'HITSZ',
                  'PolyU': 'PolyU',
                  'CityU': 'CityU',
                  'HKBU': 'HKBU',
                  'LingU': 'LingU',
                  'EdUHK': 'EdUHK',
                  'Yale': 'Yale',
                  'UPenn': 'UPenn',
                  'NYU': 'NYU',
                  'JHU': 'JHU',
                  'NUS': 'NUS',
                  'NTU': 'NTU',
                  '社群组织': 'Communities',
                  '合办企业': 'Co-hosted by',
                  '支持单位': 'Supporting Organizations',
                  '+ 更多': '+ More',
                  '姓名（必选）': 'Name (required)',
                  '您希望我们怎样称呼您？': 'How should we address you?',
                  '手机号（必选）': 'Phone number (required)',
                  '确保可以加到微信': 'Make sure we can add you on WeChat',
                  '电子邮箱（必选）': 'Email (required)',
                  '你的身份（可选）': 'Your identity (optional)',
                  '学生': 'Student',
                  '职场人士': 'Professional',
                  '独立开发者/创作者': 'Independent developer / creator',
                  '创业者': 'Founder',
                  '其他': 'Other',
                  '是': 'Yes',
                  '否': 'No',
                  '学校背景/工作背景（必选）': 'School / work background (required)',
                  '学校标注：院校 + 专业 + 年级；工作表明：公司 + 岗位 + 工作年限': 'For school: university + major + year. For work: company + role + years of experience.',
                  '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）（必选）': 'Team preference (1-5 people per team; cross-school and cross-organization teams allowed) (required)',
                  '参赛者可以在选手交流群里找到自己期待的队友。如果暂时没有找到合适的队友又不希望单枪匹马开发，主办方这边也可以帮你匹配。': 'Participants can find teammates in the group chat. If you cannot find a suitable team but do not want to build alone, the organizers can help match you.',
                  '自行组队（请补充队友姓名/联系方式）': 'Form my own team (please add teammate names/contact)',
                  '个人参赛': 'Join solo',
                  '希望由主办方随机匹配队友': 'Match me with teammates',
                  '若自行组队，请输入队名（可选）': 'If you have a team, enter the team name (optional)',
                  '参加方式（必选）': 'Participation city (required)',
                  '深圳（Anchor+Weave）': 'Shenzhen (Anchor + Weave)',
                  '香港（Flux+Vital）（必须有港澳通行证及相关证件）': 'Hong Kong (Flux + Vital; travel documents required)',
                  '参与赛道（深圳）（必选）': 'Track in Shenzhen (required)',
                  '选好后不可再改': 'Cannot be changed after selection',
                  'Anchor · 具构（深圳）— 具身智能 & 智能硬件': 'Anchor (Shenzhen) - Embodied AI & Smart Hardware',
                  'Weave · 织域（深圳）— 全域融合 & Agent + 创意': 'Weave (Shenzhen) - Full-Spectrum Fusion & Agent + Creativity',
                  '参与赛道（香港）（必选）': 'Track in Hong Kong (required)',
                  'Flux · 流境（香港）— 数字金融 & Web3.0': 'Flux (Hong Kong) - Digital Finance & Web3.0',
                  'Vital · 活域（香港）— 生命科学 & Healthcare': 'Vital (Hong Kong) - Life Sciences & Healthcare',
                  '是否参与过完整的创业项目或开发项目（可选）': 'Have you participated in a complete startup or development project? (optional)',
                  'Your GitHub / personal homepage (optional)': 'Your GitHub / personal homepage (optional)',
                  '你的作品集，简历（可选）': 'Portfolio / resume (optional)',
                  '项目简述（可选）': 'Project summary (optional)',
                  '请简单介绍你的创意 / 项目，以及你希望落地这个方向的原因。': 'Briefly introduce your idea or project, and why you want to build in this direction.',
                  '你是否愿意在赛后将你的优秀项目进一步推进落地？（必选）': 'Are you willing to continue developing a strong project after the event? (required)',
                  '技能评价（必选）': 'Skill self-assessment (required)',
                  '1=从未接触; 2=初学; 3=能独立完成; 4=有丰富项目经验': '1 = no experience; 2 = beginner; 3 = independent; 4 = strong project experience',
                  '编程能力（如 C/C++/Python/Java 等）': 'Programming (e.g. C/C++/Python/Java)',
                  '硬件开发（如 PCB设计、电路调试、嵌入式系统）': 'Hardware development (e.g. PCB design, circuit debugging, embedded systems)',
                  '产品/用户研究（需求挖掘、洞察）': 'Product / user research (needs discovery, insights)',
                  '设计表达（UI/UX、3D建模、视觉传达）': 'Design expression (UI/UX, 3D modeling, visual communication)',
                  '项目协作（进度把控、跨学科沟通、文档整理）': 'Project collaboration (timeline control, cross-disciplinary communication, documentation)',
                  '你的“硬”实力 (Hardware Skills)（必选）': 'Hardware skills (required)',
                  'PCB设计 (KiCad/Altium)': 'PCB design (KiCad / Altium)',
                  '嵌入式开发 (Arduino/ESP32/STM32)': 'Embedded development (Arduino / ESP32 / STM32)',
                  '结构设计/3D建模 (Fusion360/SolidWorks/Blender)': 'Structural design / 3D modeling (Fusion360 / SolidWorks / Blender)',
                  '手工/焊接': 'Handcraft / soldering',
                  '快速模型制作3d打印/激光切割': 'Rapid prototyping (3D printing / laser cutting)',
                  '传感器与电路': 'Sensors and circuits',
                  '导电织物 / 可穿戴电子': 'Conductive textiles / wearable electronics',
                  '你的“软”实力 (Software & AI)（必选）': 'Software & AI skills (required)',
                  '大模型API调用': 'LLM API integration',
                  'AI Agent': 'AI agent',
                  '机器视觉': 'Computer vision',
                  '运动算法': 'Motion / control algorithms',
                  '后端开发': 'Backend development',
                  '前端工程（React / Vue.js 等）': 'Frontend engineering (React / Vue.js, etc.)',
                  '边缘计算/端侧部署': 'Edge computing / on-device deployment',
                  'Vibe coding': 'Vibe coding',
                  '请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）（可选）': 'Paste your most active social links here (1-3 if available) (optional)',
                  '可以是你的个人网站、LinkedIn、Github、小红书、X、Bilibili、Reddit、Instagram...': 'This can be your personal site, LinkedIn, GitHub, Xiaohongshu, X, Bilibili, Reddit, Instagram, etc.',
                  '在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。（可选）': 'What interesting things have you done in the past 18 months? Please describe in detail. (optional)',
                  '我们充分尊重你的意愿': 'We fully respect your preference.',
                  '选好后不可再改': 'Cannot be changed after selection',
                  '是否愿意信息公开联系方式给合作方公司用于招聘/投资对接（可选）': 'May we share your contact information with partners for recruiting or investment matching? (optional)',
                  '愿意': 'Yes',
                  '不愿意': 'No',
                  '待填写者输入': 'Enter your answer'
                }
              };
              var source = maps['zh-CN'];
              var target = maps[langCode] || maps['zh-CN'];
              document.querySelectorAll('p, h2, h3, h4, legend, label, span.app-choice-text, button, a').forEach(function (el) {
                if (el.children.length && !el.classList.contains('app-choice-text')) return;
                var text = el.textContent.trim();
                if (target[text]) {
                  el.textContent = target[text];
                  return;
                }
                Object.keys(source).some(function (key) {
                  if (source[key] === text || maps.en[key] === text) {
                    el.textContent = target[key];
                    return true;
                  }
                  return false;
                });
              });
              document.querySelectorAll('input[placeholder], textarea[placeholder]').forEach(function (el) {
                var text = el.getAttribute('placeholder');
                Object.keys(source).some(function (key) {
                  if (source[key] === text || maps.en[key] === text) {
                    el.setAttribute('placeholder', target[key]);
                    return true;
                  }
                  return false;
                });
              });
            }
    
            var primaryNav = Array.prototype.slice.call(document.querySelectorAll('nav[aria-label="Primary"] > a'));
            var mobileNav = Array.prototype.slice.call(document.querySelectorAll('#mobileMenu > nav > a'));
            var footerNav = Array.prototype.slice.call(document.querySelectorAll('nav[aria-label="Footer navigation"] a'));
            var heroTopline = document.querySelector('main > section:first-of-type .flex.items-center.justify-between span');
            var heroWords = document.querySelectorAll('#heroHeading .hero-word');
            var heroButtons = document.querySelectorAll('main > section:first-of-type .horizon-pill');
            var snapshotLabel = document.querySelector('section[aria-label="Studio proof"] .mono');
            var snapshotCards = document.querySelectorAll('section[aria-label="Studio proof"] .grid > div > p:last-child');
            var storyLabel = document.querySelector('#work .mono');
            var storyTitle = document.querySelector('#work .max-w-5xl h2');
            var storyParas = document.querySelectorAll('#work .space-y-6 p');
            var storyMilestoneTitles = document.querySelectorAll('#work .mt-24.grid h3');
            var storyMilestoneParas = document.querySelectorAll('#work .mt-24.grid > div > p.mt-4');
            var storyBridgeTitle = document.querySelector('#work .lg\\:col-span-5 h2');
            var storyBridgeSub = document.querySelector('#work .lg\\:col-span-5 p');
            var storyWhyTitle = document.querySelector('#work .lg\\:col-span-7 > div:first-child h3');
            var storyWhyPara = document.querySelector('#work .lg\\:col-span-7 > div:first-child p');
            var storyCityLabels = document.querySelectorAll('#work .grid.grid-cols-1.md\\:grid-cols-2 .mono');
            var storyCityTitles = document.querySelectorAll('#work .grid.grid-cols-1.md\\:grid-cols-2 h4');
            var storyCityParas = document.querySelectorAll('#work .grid.grid-cols-1.md\\:grid-cols-2 p:not(.mono)');
            var storyBuildSend = document.querySelector('#work .mt-28.reveal > p');
            var storyClosingLeft = document.querySelector('#work .lg\\:col-span-7.space-y-6');
            var storyClosingRight = document.querySelector('#work .lg\\:col-span-5.text-xl');
            var infoLabel = document.querySelector('#overview .mono');
            var infoTitle = document.querySelector('#overview h2');
            var infoCards = document.querySelectorAll('#overview .grid > div');
            var tracksLabel = document.querySelector('#process .lg\\:sticky .mono');
            var tracksTitle = document.querySelector('#process .lg\\:sticky h2');
            var tracksIntro = document.querySelector('#process .lg\\:sticky p.text-lg');
            var trackNames = document.querySelectorAll('#process [data-timeline] h3');
            var trackTexts = document.querySelectorAll('#process [data-timeline] p.text-lg');
            var appLabel = document.querySelector('#contact .mono');
            var appTitle = document.querySelector('#contact h2');
            var appButton = document.querySelector('#contact button');
            var appIntro = document.querySelector('#contact .application-intro');
            var communityLabel = document.querySelector('#community .mono');
            var communityTitles = document.querySelectorAll('#community h3, #community p.text-xl.sm\\:text-2xl');
            var announcementLabel = document.querySelector('#announcement .mono');
            var announcementTitle = document.querySelector('#announcement h2');
            var announcementDescs = document.querySelectorAll('#announcement p:not(.mono):not(h2)');
            var faqLabel = document.querySelector('#faq .mono');
            var faqTitle = document.querySelector('#faq h2');
            var faqSummaries = document.querySelectorAll('#faq summary');
            var faqAnswers = document.querySelectorAll('#faq .text-lg.text-neutral-400.leading-relaxed.pb-6.max-w-2xl');
            var footerStudio = document.querySelector('nav[aria-label="Footer navigation"] .mono');
            var footerSocial = document.querySelector('nav[aria-label="Social links"] .mono');
            var footerContact = document.querySelector('footer > div > div:last-of-type .mono');
    
            store('heroTopline', heroTopline);
            store('heroApply', heroButtons[0]);
            store('heroAbout', heroButtons[1]);
            store('snapshotLabel', snapshotLabel);
            store('storyLabel', storyLabel);
            store('storyTitle', storyTitle);
            Array.prototype.forEach.call(storyMilestoneTitles, function (el, i) { store('storyMilestoneTitle' + i, el); });
            Array.prototype.forEach.call(storyMilestoneParas, function (el, i) { store('storyMilestonePara' + i, el); });
            store('storyBridgeTitle', storyBridgeTitle, 'html');
            store('storyBridgeSub', storyBridgeSub);
            store('storyWhyTitle', storyWhyTitle);
            store('storyWhyPara', storyWhyPara);
            store('storyBuildSend', storyBuildSend, 'html');
            store('infoLabel', infoLabel);
            store('infoTitle', infoTitle);
            store('tracksLabel', tracksLabel);
            store('tracksTitle', tracksTitle);
            store('tracksIntro', tracksIntro);
            store('appLabel', appLabel);
            store('appTitle', appTitle);
            store('appButton', appButton);
            store('appIntro', appIntro);
            store('communityLabel', communityLabel);
            store('announcementLabel', announcementLabel);
            store('announcementTitle', announcementTitle);
            store('faqLabel', faqLabel);
            store('faqTitle', faqTitle);
            store('footerStudio', footerStudio);
            store('footerSocial', footerSocial);
            store('footerContact', footerContact);
    
            function render(langCode) {
              lang = langCode;
              try {
                window.localStorage.setItem('aixorigin-lang', langCode);
              } catch (e) {}
              document.documentElement.lang = langCode === 'en' ? 'en' : 'zh-Hans';
    
              if (langCode === 'zh-CN') {
                restore('heroTopline', heroTopline);
                restore('heroApply', heroButtons[0]);
                restore('heroAbout', heroButtons[1]);
                restore('snapshotLabel', snapshotLabel);
                snapshotCards.forEach(function (el, i) { restore('snapshotCard' + i, el); });
                restore('storyLabel', storyLabel);
                restore('storyTitle', storyTitle);
                storyMilestoneTitles.forEach(function (el, i) { restore('storyMilestoneTitle' + i, el); });
                storyMilestoneParas.forEach(function (el, i) { restore('storyMilestonePara' + i, el); });
                restore('storyBridgeTitle', storyBridgeTitle, 'html');
                restore('storyBridgeSub', storyBridgeSub);
                restore('storyWhyTitle', storyWhyTitle);
                restore('storyWhyPara', storyWhyPara);
                restore('storyBuildSend', storyBuildSend, 'html');
                restore('infoLabel', infoLabel);
                restore('infoTitle', infoTitle);
                restore('tracksLabel', tracksLabel);
                restore('tracksTitle', tracksTitle);
                restore('tracksIntro', tracksIntro);
                restore('appLabel', appLabel);
                restore('appTitle', appTitle);
                restore('appButton', appButton);
                restore('appIntro', appIntro);
                restore('communityLabel', communityLabel);
                restore('announcementLabel', announcementLabel);
                restore('announcementTitle', announcementTitle);
                restore('faqLabel', faqLabel);
                restore('faqTitle', faqTitle);
                restore('footerStudio', footerStudio);
                restore('footerSocial', footerSocial);
                restore('footerContact', footerContact);
              } else {
                setText(primaryNav[0], 'Story');
                setText(primaryNav[1], 'Information');
                setText(primaryNav[2], 'Application');
                setText(primaryNav[3], 'Community');
                setText(primaryNav[4], 'Announcement');
                setText(primaryNav[5], 'FAQ');
                setText(mobileNav[0], 'Story');
                setText(mobileNav[1], 'Information');
                setText(mobileNav[2], 'Application');
                setText(mobileNav[3], 'Community');
                setText(mobileNav[4], 'Announcement');
                setText(mobileNav[5], 'FAQ');
    
                setText(heroTopline, 'Trace Origin. Build Together.');
                setText(heroButtons[0], 'Start to Apply');
                setText(heroButtons[1], 'About');
                setText(snapshotLabel, '(01) Snapshot');
                setText(snapshotCards[0], 'On-site builders / founders / researchers / hardware creators');
                setText(snapshotCards[1], 'Four hard tracks: Flux, Vital, Anchor, Weave');
                setText(snapshotCards[2], '7-day program: online + 48h in-person sprint + roundtable + StudyLab3');
                setText(snapshotCards[3], 'University alliance: HK top 8 + mainland + overseas');
    
                setText(storyLabel, '(02) Story');
                setText(storyTitle, 'Most hackathons end at the awards');
                setText(storyParas[0], 'Spotlights come on, trophies are handed out, and the crowd leaves. Too many strong ideas do not lose to technology or competition. They simply never get the time to become something useful.');
                setText(storyParas[1], 'If the finish line is a trophy, that is just a weekend party. We want a finish line six months later.');
                setText(storyParas[2], 'By then, your project is still alive, still running, and still being used.');
                setText(storyMilestoneTitles[0], 'The Wright Brothers');
                setText(storyMilestoneTitles[1], 'Linus Torvalds');
                setText(storyMilestoneTitles[2], 'DeepSeek');
                setText(storyMilestoneParas[0], 'Twelve seconds off the ground, then a crash into the sand. Later, humanity flew beyond the solar system. It began with footprints around a frame being set upright in the sand.');
                setText(storyMilestoneParas[1], "From a dorm-room line: \"just a hobby, won't be big.\" Today, it still runs underneath the GPUs everyone queues for.");
                setText(storyMilestoneParas[2], 'Told again and again that there was not enough compute, it played the fewest cards and put China at the same table for the first time.');
                setHTML(storyBridgeTitle, 'There is a gap.<br>I will fill it.');
                setText(storyBridgeSub, 'That sentence has no polite name. We call it Origin.');
                setText(storyWhyTitle, 'Why Hong Kong and Shenzhen');
                setText(storyWhyPara, 'Being seen is not enough. To really fill the gap, an idea has to become something in your hands, then reach the people who need it.');
                setText(storyCityLabels[0], 'Shenzhen');
                setText(storyCityLabels[1], 'Hong Kong');
                setText(storyCityTitles[0], 'Shenzhen will help you build it.');
                setText(storyCityTitles[1], 'Hong Kong will open the road for it.');
                setText(storyCityParas[0], 'From robotics to wearables, from IoT to edge AI, nowhere matches Shenzhen when it comes to turning ideas into hardware.');
                setText(storyCityParas[1], 'Whether it is finance and Web3, or life sciences and healthcare, Hong Kong is the best launchpad to take things global.');
                setHTML(storyBuildSend, 'Built on one side, delivered on the other—<br>For the first time, your gap can be seen, filled, and placed into the hands of the people who need it without breaking in the middle.');
                storyClosingLeft.querySelectorAll('p').forEach(function (p, i) {
                  if (i === 0) p.textContent = 'Do you remember the first time you built something completely on your own?';
                  if (i === 1) p.textContent = 'No one taught you. You just stared, adjusted, failed, tried again. Then one moment later, it moved, lit up, and became real.';
                  if (i === 2) p.textContent = 'That feeling is not pride. It is the realization that the world can be nudged by your own hands.';
                });
                storyClosingRight.querySelectorAll('p').forEach(function (p, i) {
                  if (i === 0) p.textContent = 'September 2026, Hong Kong & Shenzhen.';
                  if (i === 1) p.textContent = 'We turn the lights on, set the table, and put other stubborn builders beside you. Then we step back and watch you create.';
                });
    
                setText(infoLabel, '(03) Information');
                setText(infoTitle, 'Event Overview');
                infoCards[0].querySelector('p:nth-of-type(1)').textContent = 'Location';
                infoCards[0].querySelector('p:nth-of-type(2)').textContent = 'Hong Kong + Shenzhen';
                infoCards[0].querySelector('p:nth-of-type(3)').textContent = 'First dual-city edition';
                infoCards[1].querySelector('p:nth-of-type(1)').textContent = 'Dates';
                infoCards[1].querySelector('p:nth-of-type(2)').textContent = '2026.08.31 — 2026.09.06';
                infoCards[1].querySelector('p:nth-of-type(3)').textContent = '7 days · hybrid online + offline';
                infoCards[2].querySelector('p:nth-of-type(1)').textContent = 'Scale';
                infoCards[2].querySelector('p:nth-of-type(2)').textContent = '300+ on-site builders';
                infoCards[2].querySelector('p:nth-of-type(3)').textContent = 'Developers / founders / hardware / creatives';
                infoCards[3].querySelector('p:nth-of-type(1)').textContent = 'Universities';
                infoCards[3].querySelector('p:nth-of-type(2)').textContent = '30+ schools';
                infoCards[3].querySelector('p:nth-of-type(3)').textContent = 'HK top 8 + mainland + overseas';
                infoCards[3].querySelector('p:nth-of-type(4)').textContent = 'University alliance';
                infoCards[4].querySelector('p:nth-of-type(1)').textContent = 'After';
                infoCards[4].querySelector('p:nth-of-type(2)').textContent = 'Investment and resource follow-up';
                infoCards[5].querySelector('p:nth-of-type(1)').textContent = 'Language';
                infoCards[5].querySelector('p:nth-of-type(2)').textContent = 'Bilingual Chinese and English';
                infoCards[6].querySelector('p:nth-of-type(1)').textContent = 'Teams';
                infoCards[6].querySelector('p:nth-of-type(2)').textContent = '2 - 5 people per team';
                infoCards[6].querySelector('p:nth-of-type(3)').textContent = 'Solo signups allowed; organizers will match teammates';
    
                setText(tracksLabel, '(04) Tracks');
                setText(tracksTitle, 'Four tracks, two city DNA');
                setText(tracksIntro, 'We did not pick these tracks randomly. Each one grows out of the industrial soil of its city.');
                trackNames[0].textContent = 'Hong Kong · Flux';
                trackNames[1].textContent = 'Hong Kong · Vital';
                trackNames[2].textContent = 'Shenzhen · Anchor';
                trackNames[3].textContent = 'Shenzhen · Weave';
                trackTexts[0].innerHTML = 'Flow — Digital Finance & Web3.0<br>How should money move? Cross-border payments, digital assets, financial compliance, and new ways of exchanging trust. Reimagine the flow of value with code.';
                trackTexts[1].innerHTML = 'Vital — Life Sciences & Healthcare<br>How can people get healthier? AI-assisted diagnosis, health data management, medical workflow optimization, and life science applications. Use AI to help people live longer and better.';
                trackTexts[2].innerHTML = 'Anchor — Embodied AI & Smart Hardware<br>How does AI get out of the screen? AI with robotics, IoT, and tightly integrated hardware products that bring AI into the real world.';
                trackTexts[3].innerHTML = 'Weave — Full-Spectrum Fusion & Agent + Creativity<br>How do things connect? AI agents, creative tools, cross-domain fusion, and ideas that were impossible before. A track with no ceiling for people who think differently.';
    
                setText(appLabel, '(04) Application');
                setText(appTitle, 'Application');
                setText(appIntro, 'Fill in the same application items from the Feishu questionnaire: personal info, portfolio, team preference, and post-event consent.');
                setText(appButton, 'Send application');
    
                setText(communityLabel, '(05) Community');
                communityTitles[0].textContent = 'Join the group chat';
                communityTitles[1].textContent = 'Amanda WeChat';
                communityTitles[2].textContent = 'Join InnoAI x HKU';
                document.querySelectorAll('#community p.mt-3.text-sm.sm\\:text-base.leading-relaxed.text-neutral-400').forEach(function (p, i) {
                  if (i === 0) p.textContent = 'Event inquiries, rule questions, and team building';
                  if (i === 1) p.textContent = 'Business partnerships / media / sponsorship';
                  if (i === 2) p.textContent = 'A practice-driven community';
                });
    
                setText(announcementLabel, '(06) Announcement');
                setText(announcementTitle, 'Announcement');
                announcementDescs[0].textContent = 'Latest notices, registration milestones, track updates, and venue logistics live here.';
                announcementDescs[1].textContent = 'If opening times, venue notes, or partnership info change, they will be posted here first.';
                announcementDescs[2].textContent = 'Please follow the community and top navigation';
                announcementDescs[3].textContent = 'Important changes will also be synced to the Application and Community entries for quick access.';
    
                setText(faqLabel, '(07) FAQ');
                setText(faqTitle, 'Frequently Asked Questions');
                faqSummaries[0].childNodes[0].textContent = 'Can I join without a technical background?';
                faqSummaries[1].childNodes[0].textContent = 'Can I join without a team?';
                faqSummaries[2].childNodes[0].textContent = 'Do I need to bring my own hardware?';
                faqSummaries[3].childNodes[0].textContent = 'Can non-Hong Kong and Shenzhen students join?';
                faqSummaries[4].childNodes[0].textContent = 'Can I just come and watch?';
                faqAnswers[0].textContent = 'Yes. There is no technical barrier. What matters is the thought, "I saw a problem and I want to solve it." Technology is a tool, not a ticket in. Designers, product people, and business-minded participants can be just as valuable.';
                faqAnswers[1].textContent = 'Yes. Solo applications are completely fine, and the organizers will help you find teammates. In fact, many hackathon teammates later become startup cofounders.';
                faqAnswers[2].textContent = 'No. Hardware resources will be provided at the Shenzhen venue. Bring your ideas. If you have your own devices, you are welcome to bring them too.';
                faqAnswers[3].textContent = 'Yes. We welcome participants from anywhere in the world.';
                faqAnswers[4].textContent = 'Yes. Demo Day is open to the public. You can try the projects yourself and vote. Public registration will open later, so please stay tuned.';
    
                setText(footerStudio, 'Studio');
                setText(footerSocial, 'Social');
                setText(footerContact, 'Contact');
                footerNav[0].textContent = 'Story';
                footerNav[1].textContent = 'Information';
                footerNav[2].textContent = 'Community';
                footerNav[3].textContent = 'FAQ';
              }
    
              applyTextMap(langCode);
              applyButtons(langCode);
            }
    
            defaults.navStory = { text: primaryNav[0] ? primaryNav[0].textContent : 'Story' };
            defaults.navInformation = { text: primaryNav[1] ? primaryNav[1].textContent : 'Information' };
            defaults.navApplication = { text: primaryNav[2] ? primaryNav[2].textContent : 'Application' };
            defaults.navCommunity = { text: primaryNav[3] ? primaryNav[3].textContent : 'Community' };
            defaults.navFaq = { text: primaryNav[4] ? primaryNav[4].textContent : 'F&Q' };
            Array.prototype.forEach.call(document.querySelectorAll('#work .space-y-6 p'), function (el, i) { defaults['storyPara' + i] = { text: el.textContent }; });
            Array.prototype.forEach.call(snapshotCards, function (el, i) { defaults['snapshotCard' + i] = { text: el.textContent }; });
    
            document.querySelectorAll('[data-lang-btn]').forEach(function (btn) {
              btn.addEventListener('click', function () { render(btn.getAttribute('data-lang-btn')); });
            });
    
            var savedLang = 'zh-CN';
            try {
              savedLang = window.localStorage.getItem('aixorigin-lang') || 'zh-CN';
            } catch (e) {}
            if (['zh-CN', 'en'].indexOf(savedLang) === -1) savedLang = 'zh-CN';
            render(savedLang);
          })();
  }
}

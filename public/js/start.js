// Startseite: wanderndes Logo, Kapitel-Effekte, Vorher/Nachher, Galerie-Streifen.
(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var logo=document.getElementById('s-logo'),head=document.querySelector('.site-header'),brand=document.querySelector('.brand img');
  var chs=[].slice.call(document.querySelectorAll('[data-ch]')),ba=document.getElementById('s-ba');
  var after=ba&&ba.querySelector('.after'),line=ba&&ba.querySelector('.line');
  var gal=document.querySelector('#arbeiten .gallery'),galSec=document.getElementById('arbeiten');
  var heroBg=document.querySelector('.s-hero .bg');
  function clamp(v,a,b){return Math.min(b===undefined?1:b,Math.max(a||0,v))}
  function ease(t){return 1-Math.pow(1-t,3)}
  function frame(){
    var vh=innerHeight,vw=innerWidth,y=scrollY;
    if(logo&&brand){
      var p=reduce?1:ease(clamp(y/(vh*.45)));
      var r=brand.getBoundingClientRect(),hh=head.offsetHeight;
      var smallH=Math.max(40,hh-16),smallW=smallH*300/128,h1=document.getElementById('hero-titel'),y0=Math.max(hh+6,vh*.1),room=h1?(h1.getBoundingClientRect().top+y-y0-14):999,bigW=Math.max(smallW,Math.min(vw*.62,420,room*300/128));
      
      var tx=r.left,ty=(hh-3-smallH)/2;
      if(room<smallH*1.3){p=1;}
      var w=bigW+(smallW-bigW)*p;
      var x0=(vw-bigW)/2,x=x0+(tx-x0)*p,yy=y0+(ty-y0)*p;
      logo.style.transform='translate('+x+'px,'+yy+'px) scale('+(w/300)+')';
      head.classList.toggle('solid',p>.9);
    }
    if(reduce)return;
    if(heroBg)heroBg.style.transform='translateY('+(y*.25)+'px)';
    chs.forEach(function(ch){
      var r=ch.getBoundingClientRect(),tot=ch.offsetHeight-vh,q=clamp(-r.top/tot),en=ease(clamp(1-r.top/vh));
      var img=ch.querySelector('.img'),big=ch.querySelector('.s-big'),t=ch.querySelector('.s-txt');
      img.style.clipPath='inset('+((1-en)*18)+'% '+((1-en)*8)+'% 0 '+((1-en)*8)+'% round '+((1-en)*28)+'px)';
      img.style.transform='scale('+(1.18-.18*q)+')';
      if(big)big.style.transform='translateX('+(40-120*q)+'%)';
      var c=clamp((q-.05)/.35);t.style.opacity=c;t.style.transform='translateY('+((1-ease(c))*60)+'px)';
    });
    if(ba){var r=ba.getBoundingClientRect(),q=clamp(-r.top/(ba.offsetHeight-vh)*1.25),x=(1-q)*100;after.style.clipPath='inset(0 0 0 '+x+'%)';line.style.left=x+'%';}
    if(gal&&galSec){var g=galSec.getBoundingClientRect(),gq=clamp((vh-g.top)/(vh+g.height));var maxX=Math.max(0,gal.scrollWidth-gal.clientWidth);gal.style.transform='translateX('+(-gq*maxX)+'px)';}
  }
  var tk=false;
  function onS(){if(!tk){tk=true;requestAnimationFrame(function(){tk=false;frame()})}}
  addEventListener('scroll',onS,{passive:true});addEventListener('resize',frame);addEventListener('load',frame);frame();
})();

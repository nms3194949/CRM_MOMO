/* LINE 圖文選單分級＋動態圖卡互動示範。用法：放 <div data-line-demo></div>，再載入本檔。 */
(function(){
var LINE='https://liff.line.me/2000189532-mPbqGd5y/subscribe-3q5l5619';
var css='.ld{display:flex;flex-wrap:wrap;gap:22px;align-items:center;justify-content:center}'+
'.ld-ph{width:272px;max-width:100%;background:#e9efe9;border-radius:30px;padding:11px;flex:none}'+
'.ld-scr{background:#8fadd6;border-radius:20px;overflow:hidden;display:flex;flex-direction:column;height:500px}'+
'.ld-top{background:#2f3a4d;color:#fff;font-size:13px;padding:11px 14px}'+
'.ld-chat{flex:1;padding:10px;display:flex;flex-direction:column;gap:8px;overflow:hidden}'+
'.ld-bub{background:#fff;color:#222;border-radius:14px;padding:8px 11px;font-size:13px;max-width:86%;line-height:1.5}'+
'.ld-cards{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:4px}'+
'.ld-fc{flex:none;width:148px;background:#fff;border-radius:12px;overflow:hidden;scroll-snap-align:start;color:#222}'+
'.ld-img{height:66px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900}'+
'.ld-bd{padding:7px 9px;font-size:12px;line-height:1.45}.ld-bd b{display:block;font-size:13px}'+
'.ld-go{margin:0 9px 9px;background:#06c755;color:#fff;border-radius:8px;text-align:center;font-size:12px;padding:5px}'+
'.ld-menu{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#d9d9d9}'+
'.ld-menu div{background:#fff;color:#222;height:60px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:12px;transition:background .3s,color .3s}'+
'.ld-menu span{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:#e6f6ec;color:#058a3c;font-size:12px;font-weight:900}'+
'.ld-vip .ld-menu div{background:#1f2a24;color:#f2d38a}.ld-vip .ld-menu span{background:#3a3220;color:#f2d38a}'+
'.ld-bar{background:#fff;color:#555;font-size:12px;text-align:center;padding:6px;border-top:1px solid #ddd}'+
'.ld-side{max-width:320px;font-size:15px;line-height:1.7}'+
'.ld-seg{display:flex;gap:8px;margin:10px 0 12px}'+
'.ld-seg button{flex:1;min-height:44px;border-radius:999px;border:2px solid #cfe0d6;background:#fff;color:#10201a;font:inherit;font-weight:700;cursor:pointer}'+
'.ld-seg button[aria-pressed=true]{border-color:#06c755;color:#058a3c;background:#f0fbf4}'+
'.ld-seg button:focus-visible{outline:3px solid #ffd23f;outline-offset:2px}'+
'.ld-tip{background:#fff8dc;border:1px solid #f1df9a;border-radius:12px;padding:10px 12px;font-size:14px;margin-top:12px}'+
'.ld-tip a{color:#058a3c;font-weight:700}'+
'@media (prefers-reduced-motion:reduce){.ld-menu div{transition:none}}';
var D=[{hi:'歡迎回來！本週會員優惠在下方。',bar:'一般會員選單',m:[['訂','線上訂位'],['券','我的優惠券'],['點','集點卡'],['推','推薦好友'],['店','門市資訊'],['升','升級 VIP']],c:[['#ffe3cc','#9a3b0c','9折','平日午餐 9 折','週一至週五午餐時段'],['#dff6e7','#0b6b35','送','推薦好友送菜盤','朋友到店消費即送'],['#e6f1fb','#0b4f8a','壽','壽星禮','生日當月領取']]},
{hi:'VIP 您好！專屬禮遇已為您準備好。',bar:'VIP 專屬選單',m:[['優','VIP 優先訂位'],['鑽','VIP 專屬券'],['倍','點數加倍'],['推','推薦好友'],['隱','隱藏菜單'],['專','專人服務']],c:[['#2b3a31','#f2d38a','升','和牛升級','每月一次免費升級'],['#3b2f1a','#f2d38a','包','包廂優先訂','提前開放預訂'],['#2b3a31','#f2d38a','×2','點數雙倍','本月消費點數加倍']]}];
function esc(t){return String(t).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function build(el){
  el.innerHTML='<div class="ld"><div class="ld-ph" aria-label="LINE 官方帳號畫面示範" role="img"><div class="ld-scr"><div class="ld-top">小森火鍋（示範店家）</div><div class="ld-chat"><div class="ld-bub"></div><div class="ld-cards"></div></div><div class="ld-menu"></div><div class="ld-bar"></div></div></div>'+
  '<div class="ld-side"><b>同一個官方帳號，不同會員看到不同畫面</b><div class="ld-seg"><button type="button" aria-pressed="true">一般會員</button><button type="button" aria-pressed="false">VIP 會員</button></div>'+
  '<div>切換看看：圖文選單（下方六格）和優惠圖卡（可左右滑）會依會員等級改變，熟客一打開 LINE 就看到專屬內容。</div>'+
  '<div class="ld-tip">這裡是簡化示範。實際的圖文選單和動態圖卡更精美，<a href="'+LINE+'" target="_blank" rel="noopener">加入官方 LINE</a> 就能直接看到真實畫面。</div></div></div>';
  var ph=el.querySelector('.ld-ph'),bs=el.querySelectorAll('.ld-seg button');
  function show(k){var d=D[k];ph.classList.toggle('ld-vip',k===1);
    el.querySelector('.ld-bub').textContent=d.hi;el.querySelector('.ld-bar').textContent=d.bar;
    el.querySelector('.ld-menu').innerHTML=d.m.map(function(x){return '<div><span>'+esc(x[0])+'</span>'+esc(x[1])+'</div>'}).join('');
    el.querySelector('.ld-cards').innerHTML=d.c.map(function(x){return '<div class="ld-fc"><div class="ld-img" style="background:'+x[0]+';color:'+x[1]+'">'+esc(x[2])+'</div><div class="ld-bd"><b>'+esc(x[3])+'</b>'+esc(x[4])+'</div><div class="ld-go">立即領取</div></div>'}).join('');
    bs[0].setAttribute('aria-pressed',k===0);bs[1].setAttribute('aria-pressed',k===1)}
  bs[0].addEventListener('click',function(){show(0)});bs[1].addEventListener('click',function(){show(1)});show(0);
}
function init(){var s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  var els=document.querySelectorAll('[data-line-demo]');for(var i=0;i<els.length;i++)build(els[i])}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();

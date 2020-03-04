/* Version: 1.0.7 - Last modified: 2019-05-30 18:55:47 */
String.prototype.simpleMaskStringCount=function(e){return(this.length-this.replace(new RegExp(e,"g"),"").length)/e.length},function(e){var t={mask:"",nextInput:null,onComplete:null},n=[],s={init:function(n){var s=e.extend({},t,n);return this.each(function(){e.fn.simpleMask.process(e(this),s)})},unmask:function(){return this.each(function(){e.fn.simpleMask.unmask(this)})}};e.fn.simpleMask=function(t){return s[t]?s[t].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof t&&t?void e.error("Method "+t+" does not exist on jQuery.SimpleMask"):s.init.apply(this,arguments)},e.fn.simpleMask.makeId=function(){for(var e="",t="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz0123456789",n=t.length,s=0;s<8;s++)e+=t.charAt(Math.floor(Math.random()*n));return e},e.fn.simpleMask._onComplete=function(t){var s="object"==typeof t?e(t).attr("data-mask-ids"):t;null!==n[s].options.onComplete?(n[s].options.onComplete.call(this,n[s]),e.fn.simpleMask._nextInput(s)):e.fn.simpleMask._nextInput(s)},e.fn.simpleMask.nextOnTabIndex=function(t){var n=e(t),s=!1,a=[];return n.closest("form").find("input,select").each(function(t){var l=e(this);if(s)return a=l,!1;l[0]==n[0]&&(s=!0)}),a},e.fn.simpleMask._nextInput=function(t){var s="object"==typeof t?e(t).attr("data-mask-ids"):t;if(null!==n[s].options.nextInput)if(!0===n[s].options.nextInput){var a=e.fn.simpleMask.nextOnTabIndex(n[s].element);a.length>0&&a.select().focus()}else n[s].options.nextInput.length>0&&n[s].options.nextInput.select().focus()},e.fn.simpleMask.unmask=function(t){var s="object"==typeof t?e(t).attr("data-mask-ids"):t;e(n[s].element).removeClass("input-masked").removeAttr("data-mask-ids"),""===e(n[s].element).attr("class")&&e(n[s].element).removeAttr("class"),e(document).off("keyup.simpleMask change.simpleMask",'input[data-mask-ids="'+s+'"]'),e(document).off("keydown.simpleMask",'input[data-mask-ids="'+s+'"]')},e.fn.simpleMask.isNumber=function(e){return""!==e.replace(/\D/g,"")},e.fn.simpleMask.onlyNumbers=function(e){return e.replace(/\D/g,"")},e.fn.simpleMask.onlyNumbersLength=function(e){return e.replace(/\D/g,"").length},e.fn.simpleMask.applyMask=function(t,n){var s=t.element,a=e(s)[0],l=(a.selectionStart,a.selectionEnd),i=t.oldvalue,o=e(s).val(),r=e.fn.simpleMask.onlyNumbers(e(s).val()),m=t.masks[0],p=t.masks[t.masks.length-1].simpleMaskStringCount("#");r.length>p&&(r=r.substr(0,p));var u=r.length;for(var k in t.masks)if(t.masks[k].simpleMaskStringCount("#")==u){m=t.masks[k];break}if(r.length>0){r=r.trim();for(var f=m,c=r.length,d=0;d<c;d++)f=f.replace("#",r.charAt(d));var h=f.indexOf("#");-1!=h&&(f=f.substr(0,h));var g=f.substr(f.length-1,1);""===e.fn.simpleMask.onlyNumbers(g)&&(f=f.substr(0,h-1));for(var M=f.substr(f.length-1,1);f.length>0&&!1===e.fn.simpleMask.isNumber(M);)f=f.substr(0,f.length-1),M=f.substr(f.length-1,1);f!=o&&e(s).val(f),f!=i&&f.length==m.length&&f.length<=l&&f.length==t.maxlengthmask&&Number.isInteger(n)&&e.fn.simpleMask._onComplete(s.attr("data-mask-ids"))}else e(s).val("");t.oldvalue=e(s).val()},e.fn.simpleMask.process=function(t,s){for(var a=e.fn.simpleMask.makeId();void 0!==n[a];)a=e.fn.simpleMask.makeId();var l={};l.element=t,l.options=s,l.nextInput=s.nextInput,l.onComplete=s.onComplete,l.oldvalue=e(t).val();var i=[];i="string"==typeof s.mask?[s.mask]:s.mask;for(var o in i)switch(i[o].toLowerCase()){case"cpf":i[o]="###.###.###-##";break;case"cnpj":i[o]="##.###.###/####-##";break;case"cep":i[o]="#####-###";break;case"date":case"data":i[o]="##/##/####";break;case"telefone":case"tel":i[o]="####-####";break;case"telefone9":case"tel9":i[o]="####-####",i.push("#####-####");break;case"ddd-telefone9":case"ddd-tel9":i[o]="(##) ####-####",i.push("(##) #####-####")}l.masks=i,l.masks.sort(function(e,t){return e.length-t.length}),l.maxlengthmask=l.masks[l.masks.length-1].length,n[a]=l,t.attr("data-mask-ids",a).addClass("input-masked"),e(document).on("keyup.simpleMask change.simpleMask",'input[data-mask-ids="'+a+'"]',function(t){e.fn.simpleMask.applyMask(l,parseInt(t.key))}),e(document).on("paste",'input[data-mask-ids="'+a+'"]',function(t){var n=e(this);setTimeout(function(){n.keyup()},100)}),e(document).on("keydown.simpleMask",'input[data-mask-ids="'+a+'"]',function(e){e.ctrlKey||e.keyCode>=65&&e.keyCode<=90&&(e.metaKey||e.preventDefault())}),e.fn.simpleMask.applyMask(l)}}(jQuery);
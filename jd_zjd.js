/*
作者：小手冰凉
export zjd_num='' 默认8
[task_local]
#赚京豆
0 10 0-4 * * ? jd_zjd.js, tag=赚京豆
*/

var OＯ0$='jsjiami.com.v6',OＯ0$_=['‮OＯ0$'],$0QQ0Q=[OＯ0$,'5bey5byA5ZuiKOacqui+vuS4iumZkCnvvIzkvYblm6LmiJDlkZjkurrmnKrmu6EKCg==','dHVhbkFjdElk','amRqaWFiYW8=','YXBpLm0uamQuY29t','YXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVk','a2VlcC1hbGl2ZQ==','Z3ppcCxjb21wcmVzcyxicixkZWZsYXRl','aHR0cHM6Ly9zZXJ2aWNld2VjaGF0LmNvbS93eGE1YmY1ZWU2NjdkOTE2MjYvMTkwL3BhZ2UtZnJhbWUuaHRtbA==','c3dhdF9taW5pcHJvZ3JhbQ==','My4xLjM=','dGpqX20=','JmZyb21UeXBlPXd4YXBwJnRpbWVzdGFtcD0=','bm93','Ym9keT0=','JnV1aWQ9','TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDk7IE5vdGU5IEJ1aWxkL1BLUTEuMTgxMjAzLjAwMTsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS84Ni4wLjQyNDAuOTkgWFdFQi8zMjExIE1NV0VCU0RLLzIwMjIwMzAzIE1vYmlsZSBTYWZhcmkvNTM3LjM2IE1NV0VCSUQvODgxMyBNaWNyb01lc3Nlbmdlci84LjAuMjEuMjEyMCgweDI4MDAxNTNCKSBQcm9jZXNzL2FwcGJyYW5kMSBXZUNoYXQvYXJtNjQgV2VpeGluIE5ldFR5cGUvNEcgTGFuZ3VhZ2UvemhfQ04gQUJJL2FybTY0IE1pbmlQcm9ncmFtRW52L2FuZHJvaWQ=','cGFyc2U=','d2luZG93','c2lnbldhYXA=','aHR0cHM6Ly9tc2l0ZXBwLWZtLmpkLmNvbS9yZXN0L3ByaWNlcHJvcGhvbmUvcHJpY2VQcm9QaG9uZU1lbnU=','ZGFuZ2Vyb3VzbHk=','VmlydHVhbENvbnNvbGU=','PGJvZHk+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly8vL3N0YXRpYy4zNjBidXlpbWcuY29tL3NpdGVwcFN0YXRpYy9zY3JpcHQvbWVzY3JvbGwvbWFwLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL3N0b3JhZ2UuMzYwYnV5aW1nLmNvbS93ZWJjb250YWluZXIvanNfc2VjdXJpdHlfdjMuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vc3RhdGljLjM2MGJ1eWltZy5jb20vc2l0ZXBwU3RhdGljL3NjcmlwdC91dGlscy5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9qcy1ub2NhcHRjaGEuamQuY29tL3N0YXRpY3MvanMvbWFpbi5taW4uanMiPjwvc2NyaXB0PgogICAgPC9ib2R5Pg==','5bey5byA5ZuiKOacqui+vuS4iumZkCnvvIzlm6LmiJDlkZjkurrlt7Lmu6EKCg==','amFi','SkFC','Zmxvb3I=','c2xpY2U=','6LWa5Lqs6LGG','aXNOb2Rl','anNkb20=','dXVpZA==','a2V5cw==','Zm9yRWFjaA==','cHVzaA==','SkRfREVCVUc=','ZW52','ZmFsc2U=','Z2V0ZGF0YQ==','Q29va2llSkQ=','Q29va2llc0pE','bWFw','ZmlsdGVy','44CQ5o+Q56S644CR6K+35YWI6I635Y+W5Lqs5Lic6LSm5Y+35LiAY29va2llCuebtOaOpeS9v+eUqE5vYnlEYeeahOS6rOS4nOetvuWIsOiOt+WPlg==','aHR0cHM6Ly9iZWFuLm0uamQuY29tL2JlYW4vc2lnbkluZGV4LmFjdGlvbg==','NXwzfDF8NHwwfDI=','bXNn','bmFtZQ==','bG9n','5b2T5YmN5Y+v5byA5Zui5pWw77ya','d2FpdA==','CioqKioq5byA5aeL44CQ5Lqs5Lic6LSm5Y+3','aW5kZXg=','VXNlck5hbWU=','bGVuZ3Ro','Y2FuSGVscA==','Y29va2ll','bWF0Y2g=','dHVhbkxpc3Q=','CuW8gOWbouWksei0pe+8mg==','dXNlcg==','bWF4','aW5jbHVkZXM=','cmFuZG9t','Cui0puWPtyA=','IOW8gOWni+e7mSDjgJA=','LCDlpLHotKUhIOWOn+WboDog','ZmluYWxseQ==','ZG9uZQ==','Q29va2llSkQy','dnZpcGNsdWJfZGlzdHJpYnV0ZUJlYW5fc3RhcnRBc3Npc3Q=','RklTU0lPTl9CRUFO','ZGRlMmI=','c3VjY2Vzcw==','YXNzaXN0ZWRQaW5FbmNyeXB0ZWQ=','dHVhbg==','aGFzT3Blbg==','YXNzaXN0U3RhdHVz','Y2FuU3RhcnROZXdBc3Npc3Q=','5YeG5aSH5YaN5qyh5byA5Zui','44CQ6LWa5Lqs6LGGKOW+ruS/oeWwj+eoi+W6jykt55Oc5YiG5Lqs6LGG44CR5byA5Zui5oiQ5Yqf','c3RyaW5naWZ5','aGFzT3duUHJvcGVydHk=','dnZpcGNsdWJfZGlzdHJpYnV0ZUJlYW5fYXNzaXN0','Yjk3OTA=','5Yqp5Yqb57uT5p6c77ya5Yqp5Yqb5oiQ5Yqf','OTIwMDAwOA==','OTIwMDAxMQ==','5Yqp5Yqb57uT5p6c77ya5bey57uP5Yqp5Yqb6L+H','MjQwMDIwNQ==','5Yqp5Yqb57uT5p6c77ya5Yqp5Yqb5qyh5pWw5bey6ICX5bC9','MTAx','MTAwMDAyMg==','5Yqp5Yqb57uT5p6c77ya5rS75Yqo54Gr54iG77yM6Lez5Ye6','bG9nRXJy','cmVzdWx0Q29kZQ==','cm91bmQ=','IEFQSeivt+axguWksei0pe+8jOivt+ajgOafpee9kei3r+mHjeivlQ==','5Yqp5Yqb57uT5p6c77ya5pyq55+l6ZSZ6K+v77ya','ZGlzdHJpYnV0ZUJlYW5BY3Rpdml0eUluZm8=','dW5kZWZpbmVk','YXNzaXN0TnVt','ZGF0YQ==','CuW9k+WJjeOAkOi1muS6rOixhijlvq7kv6HlsI/nqIvluo8pLeeTnOWIhuS6rOixhuOAkeiDveWQpuWGjeasoeW8gOWbojog','HjRsjtHiCzeamiNBGKuH.cwRoDm.v6=='];if(function(_0x36d776,_0x45aaef,_0x5ce6e1){function _0x138edd(_0x135541,_0x344f01,_0x13ebd3,_0x34a078,_0x368e92,_0x1ac613){_0x344f01=_0x344f01>>0x8,_0x368e92='po';var _0x241af6='shift',_0x3c94a0='push',_0x1ac613='‮';if(_0x344f01<_0x135541){while(--_0x135541){_0x34a078=_0x36d776[_0x241af6]();if(_0x344f01===_0x135541&&_0x1ac613==='‮'&&_0x1ac613['length']===0x1){_0x344f01=_0x34a078,_0x13ebd3=_0x36d776[_0x368e92+'p']();}else if(_0x344f01&&_0x13ebd3['replace'](/[HRtHCzeNBGKuHwRD=]/g,'')===_0x344f01){_0x36d776[_0x3c94a0](_0x34a078);}}_0x36d776[_0x3c94a0](_0x36d776[_0x241af6]());}return 0xe3ae6;};return _0x138edd(++_0x45aaef,_0x5ce6e1)>>_0x45aaef^_0x5ce6e1;}($0QQ0Q,0x1bc,0x1bc00),$0QQ0Q){OＯ0$_=$0QQ0Q['length']^0x1bc;};function O0OOQ$(_0x2699a9,_0x501e82){_0x2699a9=~~'0x'['concat'](_0x2699a9['slice'](0x1));var _0x4a9879=$0QQ0Q[_0x2699a9];if(O0OOQ$['$OOOQO']===undefined&&'‮'['length']===0x1){(function(){var _0x589c6d;try{var _0x5b08bd=Function('return\x20(function()\x20'+'{}.constructor(\x22return\x20this\x22)(\x20)'+');');_0x589c6d=_0x5b08bd();}catch(_0x4ef491){_0x589c6d=window;}var _0x11657b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x589c6d['atob']||(_0x589c6d['atob']=function(_0x26c666){var _0x2ad2ff=String(_0x26c666)['replace'](/=+$/,'');for(var _0x4cbc11=0x0,_0x425aa0,_0x51f58a,_0x4e130a=0x0,_0x327155='';_0x51f58a=_0x2ad2ff['charAt'](_0x4e130a++);~_0x51f58a&&(_0x425aa0=_0x4cbc11%0x4?_0x425aa0*0x40+_0x51f58a:_0x51f58a,_0x4cbc11++%0x4)?_0x327155+=String['fromCharCode'](0xff&_0x425aa0>>(-0x2*_0x4cbc11&0x6)):0x0){_0x51f58a=_0x11657b['indexOf'](_0x51f58a);}return _0x327155;});}());O0OOQ$['O0O00$']=function(_0x46f3fa){var _0x44b31e=atob(_0x46f3fa);var _0x58157c=[];for(var _0x1d33e=0x0,_0x4086cd=_0x44b31e['length'];_0x1d33e<_0x4086cd;_0x1d33e++){_0x58157c+='%'+('00'+_0x44b31e['charCodeAt'](_0x1d33e)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x58157c);};O0OOQ$['QOOOQ0O']={};O0OOQ$['$OOOQO']=!![];}var _0x4880bf=O0OOQ$['QOOOQ0O'][_0x2699a9];if(_0x4880bf===undefined){_0x4a9879=O0OOQ$['O0O00$'](_0x4a9879);O0OOQ$['QOOOQ0O'][_0x2699a9]=_0x4a9879;}else{_0x4a9879=_0x4880bf;}return _0x4a9879;};const $=Env(O0OOQ$('‮0'));const jdCookieNode=require('./jdCookie.js');const jsdom=$[O0OOQ$('‫1')]()?require(O0OOQ$('‫2')):'';$[O0OOQ$('‮3')]='';$['tuanList']=[];let fullTeam=[];let cookiesArr=[];let dptoken=process['env']['zjd_num']||0x8;if($[O0OOQ$('‫1')]()){Object[O0OOQ$('‮4')](jdCookieNode)[O0OOQ$('‮5')](O$OQQ$=>{cookiesArr[O0OOQ$('‮6')](jdCookieNode[O$OQQ$]);});if(process['env'][O0OOQ$('‮7')]&&process[O0OOQ$('‫8')]['JD_DEBUG']===O0OOQ$('‮9'))console['log']=()=>{};}else{cookiesArr=[$[O0OOQ$('‮a')](O0OOQ$('‫b')),$['getdata']('CookieJD2'),...jsonParse($[O0OOQ$('‮a')](O0OOQ$('‮c'))||'[]')[O0OOQ$('‫d')](QQ00O0Q=>QQ00O0Q['cookie'])][O0OOQ$('‫e')](Q0QQO00=>!!Q0QQO00);}!(async()=>{var O$QO$0={'QQOO$$':function(OQ0QOOO,O00OO0Q){return OQ0QOOO*O00OO0Q;},'$000$O':function($0OQOO,O00$){return $0OQOO+O00$;},'O$0O0':function(Q0Q0QO0,$QOOOO){return Q0Q0QO0===$QOOOO;},'QO0$$':O0OOQ$('‮f'),'Q0O0O0':O0OOQ$('‫10'),'$QOQO':function($$0OQ){return $$0OQ();},'OO0OQ00':function(OQ0O00O,O0OOOOO){return OQ0O00O<O0OOOOO;},'OQ$OQ':O0OOQ$('‫11'),'Q0OO0$':function(OQQO0){return OQQO0();},'O0QOOQO':function(OQ$O$Q,QQQ0QQ){return OQ$O$Q(QQQ0QQ);},'$0OOQO':function(O00QOOO,QOQ$O0,OQ000QO){return O00QOOO(QOQ$O0,OQ000QO);},'$$$0O$':function(Q0$$0,OO$Q0){return Q0$$0<OO$Q0;},'QOO0OQ0':function($O$0Q0,$$0$O$){return $O$0Q0>$$0$O$;},'O00O0OO':function($0Q0$0,OQQQQ0O){return $0Q0$0<OQQQQ0O;},'O0Q0O0O':function($OQ0O$,O00O0O){return $OQ0O$===O00O0O;},'O0$0$Q':'user'};if(!cookiesArr[0x0]){if(O$QO$0['O$0O0']('QQ0Q0Q0','O0OQO$')){data=JSON['parse'](data);}else{$[O0OOQ$('‫12')]($[O0OOQ$('‫13')],O$QO$0['QO0$$'],O$QO$0['Q0O0O0'],{'open-url':O$QO$0['Q0O0O0']});return;}}await O$QO$0['$QOQO'](jstoken);console[O0OOQ$('‫14')](O0OOQ$('‮15')+dptoken);for(let QOQQQ0O=0x0;O$QO$0['OO0OQ00'](QOQQQ0O,dptoken);QOQQQ0O++){var OOOQ0O=O$QO$0['OQ$OQ']['split']('|'),QOOOQ=0x0;while(!![]){switch(OOOQ0O[QOOOQ++]){case'0':await O$QO$0['Q0OO0$'](main);continue;case'1':$['UserName']=O$QO$0['O0QOOQO'](decodeURIComponent,$['cookie']['match'](/pt_pin=([^; ]+)(?=;?)/)&&$['cookie']['match'](/pt_pin=([^; ]+)(?=;?)/)[0x1]);continue;case'2':await $[O0OOQ$('‫16')](0x5dc);continue;case'3':$['cookie']=cookiesArr[QOQQQ0O];continue;case'4':console[O0OOQ$('‫14')](O0OOQ$('‫17')+$[O0OOQ$('‮18')]+'】'+$[O0OOQ$('‮19')]+'*****\x0a');continue;case'5':$['index']=O$QO$0['$000$O'](QOQQQ0O,0x1);continue;}break;}}cookiesArr=O$QO$0['$0OOQO'](getRandomArrayElements,cookiesArr,cookiesArr[O0OOQ$('‮1a')]);for(let QOQ$$O=0x0;O$QO$0['$$$0O$'](QOQ$$O,cookiesArr['length']);QOQ$$O++){$[O0OOQ$('‫1b')]=!![];if(cookiesArr[QOQ$$O]){$['cookie']=cookiesArr[QOQ$$O];$[O0OOQ$('‮19')]=O$QO$0['O0QOOQO'](decodeURIComponent,$[O0OOQ$('‮1c')][O0OOQ$('‫1d')](/pt_pin=([^; ]+)(?=;?)/)&&$[O0OOQ$('‮1c')][O0OOQ$('‫1d')](/pt_pin=([^; ]+)(?=;?)/)[0x1]);if($['canHelp']&&O$QO$0['QOO0OQ0'](cookiesArr['length'],$['assistNum'])){for(let OQ00Q=0x0;O$QO$0['O00O0OO'](OQ00Q,$[O0OOQ$('‮1e')][O0OOQ$('‮1a')]);++OQ00Q){if(O$QO$0['O$0O0']('Q0Q0QOQ','$$QQQ')){console[O0OOQ$('‫14')](O0OOQ$('‮1f')+JSON['stringify'](data)+'\x0a');}else{$['oneInfo']=$['tuanList'][OQ00Q];if(O$QO$0['O$0O0']($[O0OOQ$('‮19')],$['tuanList'][OQ00Q][O0OOQ$('‫20')])||$['oneInfo'][O0OOQ$('‮21')]||fullTeam[O0OOQ$('‮22')](OQ00Q)){if(O$QO$0['O0Q0O0O']('Q0$$0O','Q$$00')){index=Math['floor'](O$QO$0['QQOO$$'](O$QO$0['$000$O'](QOQ$$O,0x1),Math[O0OOQ$('‫23')]()));temp=shuffled[index];shuffled[index]=shuffled[QOQ$$O];shuffled[QOQ$$O]=temp;}else{continue;}}console['log'](O0OOQ$('‫24')+$['UserName']+O0OOQ$('‫25')+$[O0OOQ$('‮1e')][OQ00Q][O$QO$0['O0$0$Q']]+'】助力');await O$QO$0['O0QOOQO'](helpFriendTuan,$[O0OOQ$('‮1e')][OQ00Q]['id']);await $['wait'](0x7d0);if(!$['canHelp'])break;}}}}}})()['catch'](OQO$$O=>{$['log']('','❌\x20'+$[O0OOQ$('‫13')]+O0OOQ$('‮26')+OQO$$O+'!','');})[O0OOQ$('‮27')](()=>{$[O0OOQ$('‮28')]();});async function main(){var O$0$$={'OQQQQ$':function(O0Q$0O,O0$OQ){return O0Q$0O(O0$OQ);},'QQO0OQO':O0OOQ$('‫b'),'O0Q$QQ':O0OOQ$('‮29'),'Q$QQQ0':'CookiesJD','O0$$OQ':function(QQQ0OO0,$QQQ$,OOQO0O0,OOOOQ){return QQQ0OO0($QQQ$,OOQO0O0,OOOOQ);},'OOQ00$':function(Q$$0QQ){return Q$$0QQ();},'$O$0$$':function(QO$QQ0,Q$$0QO){return QO$QQ0===Q$$0QO;},'O0O0OOO':function($0O$OQ,$O00Q$){return $0O$OQ===$O00Q$;},'O0O00Q':function(OQQ0Q,$$O0OQ){return OQQ0Q!==$$O0OQ;},'QO00O0':O0OOQ$('‫2a'),'QOO000Q':O0OOQ$('‮2b'),'QQ$QQ0':'undefined','OO$OQ0':O0OOQ$('‫2c'),'O$QQQ':O0OOQ$('‮2d'),'$0O$Q$':function(OO00QQQ){return OO00QQQ();},'OQ000O0':O0OOQ$('‮2e'),'OOQOO$':function(Q$O0$O,QO$$QQ){return Q$O0$O!==QO$$QQ;},'$OQ00$':function(OO0$Q0,OO$$QQ){return OO0$Q0!==OO$$QQ;}};$[O0OOQ$('‮2f')]='';$[O0OOQ$('‫30')]=![];$[O0OOQ$('‫31')]=0x0;$['uuid']=O$0$$['O0$$OQ'](randomWord,!![],0x10,0x10);await O$0$$['OOQ00$'](getUserTuanInfo);if(!$[O0OOQ$('‮2f')]&&(O$0$$['$O$0$$']($[O0OOQ$('‫31')],0x3)||O$0$$['O0O0OOO']($['assistStatus'],0x2)||O$0$$['O0O0OOO']($['assistStatus'],0x0))&&$[O0OOQ$('‫32')]){if(O$0$$['O0O00Q']('QOQOQOO','QOO0OQO')){console['log'](O0OOQ$('‫33'));let QOQ$QO=await O$0$$['O0$$OQ'](sendInfo,O$0$$['QO00O0'],{'activityIdEncrypted':$['tuanActId'],'channel':O$0$$['QOO000Q'],'launchChannel':O$0$$['QQ$QQ0']},O$0$$['OO$OQ0']);if(QOQ$QO[O$0$$['O$QQQ']]){console[O0OOQ$('‫14')](O0OOQ$('‮34'));$[O0OOQ$('‫30')]=!![];}else{console['log'](O0OOQ$('‮1f')+JSON[O0OOQ$('‮35')](data)+'\x0a');}}else{O$0$$['OQQQQ$'](resolve,data);}}if($['hasOpen'])await O$0$$['$0O$Q$'](getUserTuanInfo);if($['tuan']&&$['tuan'][O0OOQ$('‮36')](O$0$$['OQ000O0'])&&O$0$$['OOQOO$']($[O0OOQ$('‫31')],0x3)){if(O$0$$['$OQ00$']('O00Q00Q','O00Q00Q')){cookiesArr=[$[O0OOQ$('‮a')](O$0$$['QQO0OQO']),$[O0OOQ$('‮a')](O$0$$['O0Q$QQ']),...O$0$$['OQQQQ$'](jsonParse,$[O0OOQ$('‮a')](O$0$$['Q$QQQ0'])||'[]')['map']($Q0$O=>$Q0$O[O0OOQ$('‮1c')])]['filter']($000Q0=>!!$000Q0);}else{$['tuanList'][O0OOQ$('‮6')]({'id':$['tuan'],'user':$['UserName'],'max':![]});}}}async function helpFriendTuan($$0$$O){var QO0OQOO={'Q$OQQ0':function($OOO00,QO0000Q){return $OOO00+QO0000Q;},'$0O00$':function(OOOQ0Q,Q0$0$$){return OOOQ0Q*Q0$0$$;},'$Q$OO':function(O$0O$,$Q$O$Q){return O$0O$-$Q$O$Q;},'Q$QQ0O':function(QOOOQQO,QOO0O,Q$QOQ0,QOOOO$){return QOOOQQO(QOO0O,Q$QOQ0,QOOOO$);},'$QQ$$O':O0OOQ$('‫37'),'OOQOQO':O0OOQ$('‫38'),'Q00O':function(O$O$OO,QO0OO0){return O$O$OO===QO0OO0;},'O0Q0O0Q':O0OOQ$('‮39'),'QQ0QO':O0OOQ$('‫3a'),'OOQQO0Q':'助力结果：不能助力自己','$$O0$Q':O0OOQ$('‫3b'),'OO0OQ':function($$QOO,OOQ00O){return $$QOO===OOQ00O;},'$0$0Q$':O0OOQ$('‫3c'),'O00OQ0O':function($$QO$O,OQQ0OQQ){return $$QO$O===OQQ0OQQ;},'OOOOO00':O0OOQ$('‫3d'),'QOQQOOQ':function($Q0Q0Q,$OO0OQ){return $Q0Q0Q!==$OO0OQ;},'Q$$O$Q':'助力结果：团已满','$$O0Q$':function(Q0OQOO0,QO00O$){return Q0OQOO0===QO00O$;},'Q$$0Q0':'2400203','$Q0Q$O':O0OOQ$('‫3e'),'QO$000':function(O$OOQQ,O0O00QO){return O$OOQQ===O0O00QO;},'Q0O0Q0':'9000000','Q$$$O$':function(OQ$0$$,Q0$$QQ){return OQ$0$$===Q0$$QQ;},'O0QO00Q':'9000013','QQQ$00':function(QOOO$O,QO0$0){return QOOO$O===QO0$0;},'O$$Q$':'90000014','$OOO0Q':O0OOQ$('‮3f'),'QQQ$$$':function(Q0Q0Q0,$QQQ0$){return Q0Q0Q0===$QQQ0$;},'OOQOO0Q':O0OOQ$('‫40'),'QQ0$O0':O0OOQ$('‮41')};let $OO0OO=await QO0OQOO['Q$QQ0O'](sendInfo,QO0OQOO['$QQ$$O'],$$0$$O,QO0OQOO['OOQOQO']);if($OO0OO[O0OOQ$('‮2d')]){if(QO0OQOO['Q00O']('$00$QQ','$00$QQ')){console[O0OOQ$('‫14')](QO0OQOO['O0Q0O0Q']);}else{$[O0OOQ$('‮42')](e,resp);}}else{if(QO0OQOO['Q00O']('QQQ$O','QOQO0$')){$[O0OOQ$('‮1e')]['push']({'id':$['tuan'],'user':$['UserName'],'max':![]});}else{if(QO0OQOO['Q00O']($OO0OO['resultCode'],QO0OQOO['QQ0QO'])){console['log'](QO0OQOO['OOQQO0Q']);}else if(QO0OQOO['Q00O']($OO0OO[O0OOQ$('‮43')],QO0OQOO['$$O0$Q'])){if(QO0OQOO['OO0OQ']('OO00OO0','Q$0O$O')){range=QO0OQOO['Q$OQQ0'](Math[O0OOQ$('‮44')](QO0OQOO['$0O00$'](Math['random'](),QO0OQOO['$Q$OO'](max,min))),min);}else{console[O0OOQ$('‫14')](QO0OQOO['$0$0Q$']);}}else if(QO0OQOO['O00OQ0O']($OO0OO['resultCode'],QO0OQOO['OOOOO00'])){if(QO0OQOO['QOQQOOQ']('QQQOQ','QOQQO0O')){console['log'](QO0OQOO['Q$$O$Q']),$['oneInfo'][O0OOQ$('‮21')]=!![];$[O0OOQ$('‫1b')]=![];}else{if(err){console['log'](''+JSON[O0OOQ$('‮35')](err));console[O0OOQ$('‫14')](functionID+O0OOQ$('‫45'));$['canHelp']=![];}else{$OO0OO=JSON['parse']($OO0OO);}}}else if(QO0OQOO['$$O0Q$']($OO0OO[O0OOQ$('‮43')],QO0OQOO['Q$$0Q0'])){console[O0OOQ$('‫14')](QO0OQOO['$Q0Q$O']);$[O0OOQ$('‫1b')]=![];}else if(QO0OQOO['QO$000']($OO0OO['resultCode'],QO0OQOO['Q0O0Q0'])||QO0OQOO['Q$$$O$']($OO0OO['resultCode'],QO0OQOO['O0QO00Q'])||QO0OQOO['QQQ$00']($OO0OO[O0OOQ$('‮43')],QO0OQOO['O$$Q$'])||QO0OQOO['QQQ$00']($OO0OO['resultCode'],QO0OQOO['$OOO0Q'])||QO0OQOO['QQQ$$$']($OO0OO['resultCode'],QO0OQOO['OOQOO0Q'])){console[O0OOQ$('‫14')](QO0OQOO['QQ0$O0']);$[O0OOQ$('‫1b')]=![];}else{console['log'](O0OOQ$('‮46')+JSON[O0OOQ$('‮35')]($OO0OO));$[O0OOQ$('‫1b')]=![];}}}}async function getUserTuanInfo(){var Q$Q0={'QQO$QQ':function(O0Q0QQ0,$Q){return O0Q0QQ0+$Q;},'O0QOOQQ':function(OQ00O0O,Q00QQQ){return OQ00O0O*Q00QQQ;},'$$0O0':function($O$0$0,O$QQ){return $O$0$0-O$QQ;},'O0$0Q':function(O0QQOO0,Q0OOOQ){return O0QQOO0<Q0OOOQ;},'OO0Q0OQ':function($0OQ0O,$QOO0O){return $0OQ0O*$QOO0O;},'OQ0$Q':function(Q$$Q$Q,O0$00Q,Q0OQQOQ,OOO0O0O){return Q$$Q$Q(O0$00Q,Q0OQQOQ,OOO0O0O);},'O$0$Q0':O0OOQ$('‫47'),'OOO$0':O0OOQ$('‮2b'),'QO0Q0QQ':O0OOQ$('‫48'),'OO$0':'d8ac0','Q000O':function(Q0Q0$$,QQ00QQ){return Q0Q0$$!==QQ00QQ;},'OOOOOOO':function(OQ0$$O,QO0Q0QO){return OQ0$$O===QO0Q0QO;},'$Q$00Q':function(O$00OO,OQ000O){return O$00OO===OQ000O;},'O$O0Q$':function(QQO0$,O00OQ$){return QQO0$===O00OQ$;},'Q0$OQ':O0OOQ$('‮49'),'OOOQOQ':'assistStatus','Q0QOQ':O0OOQ$('‫32')};let Q$O0OQ=await Q$Q0['OQ0$Q'](sendInfo,Q$Q0['O$0$Q0'],{'paramData':{'channel':Q$Q0['OOO$0']},'launchChannel':Q$Q0['QO0Q0QQ']},Q$Q0['OO$0']);if(!Q$O0OQ[O0OOQ$('‮2d')]){console[O0OOQ$('‫14')](JSON[O0OOQ$('‮35')](Q$O0OQ));return;}Q$O0OQ=Q$O0OQ[O0OOQ$('‫4a')];console[O0OOQ$('‫14')](O0OOQ$('‫4b')+(Q$O0OQ[O0OOQ$('‫32')]?'可以':'否'));if(Q$O0OQ&&!Q$O0OQ[O0OOQ$('‫32')]){if(Q$Q0['Q000O']('O0Q$','OO0$0O')){$[O0OOQ$('‮2f')]={'activityIdEncrypted':Q$O0OQ['id'],'assistStartRecordId':Q$O0OQ['assistStartRecordId'],'assistedPinEncrypted':Q$O0OQ['encPin'],'channel':Q$Q0['OOO$0'],'launchChannel':Q$Q0['QO0Q0QQ']};}else{console[O0OOQ$('‫14')](''+JSON['stringify'](err));console['log'](functionID+O0OOQ$('‫45'));$[O0OOQ$('‫1b')]=![];}}if(Q$Q0['OOOOOOO'](Q$O0OQ[O0OOQ$('‫31')],0x1)&&!Q$O0OQ[O0OOQ$('‫32')]){if(Q$Q0['Q000O']('$0O$Q','$0O$Q')){var Q0QQ0O0='',QQO00O0=min,OO$O$=['0','1','2','3','4','5','6','7','8','9'];if(randomFlag){QQO00O0=Q$Q0['QQO$QQ'](Math['round'](Q$Q0['O0QOOQQ'](Math['random'](),Q$Q0['$$0O0'](max,min))),min);}for(var O0Q0$$=0x0;Q$Q0['O0$0Q'](O0Q0$$,QQO00O0);O0Q0$$++){pos=Math[O0OOQ$('‮44')](Q$Q0['OO0Q0OQ'](Math['random'](),Q$Q0['$$0O0'](OO$O$['length'],0x1)));Q0QQ0O0+=OO$O$[pos];}return Q0QQ0O0;}else{console[O0OOQ$('‫14')](O0OOQ$('‫4c'));}}else if(Q$Q0['$Q$00Q'](Q$O0OQ[O0OOQ$('‫31')],0x3)&&Q$O0OQ['canStartNewAssist']){if(Q$Q0['O$O0Q$']('O$O0$$','O$O0$$')){console[O0OOQ$('‫14')]('已开团(未达上限)，团成员人已满\x0a\x0a');}else{$['done']();}}else if(Q$Q0['O$O0Q$'](Q$O0OQ[O0OOQ$('‫31')],0x3)&&!Q$O0OQ['canStartNewAssist']){console[O0OOQ$('‫14')]('今日开团已达上限，且当前团成员人已满\x0a\x0a');}$[O0OOQ$('‮4d')]=Q$O0OQ['id'];$[O0OOQ$('‮49')]=Q$O0OQ[Q$Q0['Q0$OQ']]||0x4;$[O0OOQ$('‫31')]=Q$O0OQ[Q$Q0['OOOQOQ']];$[O0OOQ$('‫32')]=Q$O0OQ[Q$Q0['Q0QOQ']];}async function sendInfo($0$00O,QQQO0O,OQ0$0$){var QQ$QOQ={'$$000Q':function(Q$OQ0O,QO$$$$){return Q$OQ0O===QO$$$$;},'$OQ$':'false','QQQQ0OO':O0OOQ$('‫4e'),'$$0O$':function(OOO0QQQ,QQOO0){return OOO0QQQ!==QQOO0;},'QO00QQO':function($OO$$,Q$$$OO){return $OO$$(Q$$$OO);},'QOQQQ':function(O00Q$Q,$$00O0){return O00Q$Q===$$00O0;},'$$$$0O':function($$0$,O0Q0QQO){return $$0$(O0Q0QQO);},'QQ$Q0$':O0OOQ$('‮4f'),'OO0OOQ0':O0OOQ$('‮50'),'$O0QQ$':O0OOQ$('‫51'),'$0OQ$$':O0OOQ$('‫52'),'Q0QOOQO':O0OOQ$('‮53'),'QQ0O00Q':O0OOQ$('‮54'),'QQ0QQ0Q':O0OOQ$('‮55'),'OOQ0OQ':O0OOQ$('‮56')};let Q$$$0Q='https://api.m.jd.com/api?functionId='+$0$00O+O0OOQ$('‮57')+Date[O0OOQ$('‮58')]();const O$Q0O=await $['signWaap'](OQ0$0$,{'appid':QQ$QOQ['QQ0O00Q'],'body':QQQO0O,'clientVersion':QQ$QOQ['QQ0QQ0Q'],'client':QQ$QOQ['OOQ0OQ'],'functionId':$0$00O});return new Promise($Q0QO$=>{var QQO0$$={'QQ$$Q0':QQ$QOQ['QQQQ0OO'],'Q0OQ0O':function(Q$0Q0O,QO$00Q){return QQ$QOQ['$$0O$'](Q$0Q0O,QO$00Q);},'Q00QQOO':function($O$000,$0Q00O){return QQ$QOQ['QO00QQO']($O$000,$0Q00O);}};if(QQ$QOQ['QOQQQ']('O0Q$$','O0Q$$')){let $$QQ00={'url':Q$$$0Q,'body':O0OOQ$('‮59')+QQ$QOQ['QO00QQO'](encodeURIComponent,JSON[O0OOQ$('‮35')](QQQO0O))+'&appid=swat_miniprogram&h5st='+QQ$QOQ['$$$$0O'](encodeURIComponent,O$Q0O)+O0OOQ$('‫5a')+$['uuid']+'&client=tjj_m&screen=1920*1080&osVersion=5.0.0&networkType=wifi&sdkName=orderDetail&sdkVersion=1.0.0&clientVersion=3.1.3&area=11','headers':{'Host':QQ$QOQ['QQ$Q0$'],'Cookie':$[O0OOQ$('‮1c')]+'appid=wxa5bf5ee667d91626;wxclient=gxhwx;ie_ai=1;appkey=797c7d5f8f0f499b936aad5edcffa08c','content-type':QQ$QOQ['OO0OOQ0'],'Connection':QQ$QOQ['$O0QQ$'],'Accept-Encoding':QQ$QOQ['$0OQ$$'],'Referer':QQ$QOQ['Q0QOOQO'],'User-Agent':O0OOQ$('‮5b')}};$['post']($$QQ00,async($QQOO0,O$Q0OO,OOOOO0O)=>{try{if($QQOO0){if(QQO0$$['Q0OQ0O']('Q$Q0$0','Q$Q0$0')){console[O0OOQ$('‫14')]('助力结果：未知错误：'+JSON[O0OOQ$('‮35')](OOOOO0O));$[O0OOQ$('‫1b')]=![];}else{console[O0OOQ$('‫14')](''+JSON[O0OOQ$('‮35')]($QQOO0));console[O0OOQ$('‫14')]($0$00O+O0OOQ$('‫45'));$['canHelp']=![];}}else{OOOOO0O=JSON[O0OOQ$('‫5c')](OOOOO0O);}}catch($0$$$){$[O0OOQ$('‮42')]($0$$$,O$Q0OO);}finally{if(QQO0$$['Q0OQ0O']('$$$$O$','Q$0$Q')){QQO0$$['Q00QQOO']($Q0QO$,OOOOO0O);}else{$['jab']=new dom[(O0OOQ$('‮5d'))]['JAB']({'bizId':QQO0$$['QQ$$Q0'],'initCaptcha':![]});$[O0OOQ$('‮5e')]=dom[O0OOQ$('‮5d')]['signWaap'];}}});}else{Object[O0OOQ$('‮4')](jdCookieNode)[O0OOQ$('‮5')](QQ$0Q=>{cookiesArr[O0OOQ$('‮6')](jdCookieNode[QQ$0Q]);});if(process[O0OOQ$('‫8')][O0OOQ$('‮7')]&&QQ$QOQ['$$000Q'](process[O0OOQ$('‫8')][O0OOQ$('‮7')],QQ$QOQ['$OQ$']))console['log']=()=>{};}});}async function jstoken(){var Q$00O={'OO00QQ0':'Mozilla/5.0\x20(Macintosh;\x20Intel\x20Mac\x20OS\x20X\x2010.15;\x20rv:91.0)\x20Gecko/20100101\x20Firefox/91.0','OQQQQOO':O0OOQ$('‫5f'),'OQQQO':O0OOQ$('‮60'),'O$00Q$':function(OOOQQQQ,OQ$O00){return OOOQQQQ===OQ$O00;},'$Q0$$':O0OOQ$('‫4e')};const {JSDOM}=jsdom;let QO0QO00=new jsdom['ResourceLoader']({'userAgent':Q$00O['OO00QQ0'],'referrer':Q$00O['OQQQQOO']});let O0O$Q=new jsdom[(O0OOQ$('‮61'))]();let $Q$O0$={'url':Q$00O['OQQQQOO'],'referrer':Q$00O['OQQQQOO'],'userAgent':Q$00O['OO00QQ0'],'runScripts':Q$00O['OQQQO'],'resources':QO0QO00,'includeNodeLocations':!![],'storageQuota':0x989680,'pretendToBeVisual':!![],'virtualConsole':O0O$Q};const O0OQQQQ=new JSDOM(O0OOQ$('‮62'),$Q$O0$);await $[O0OOQ$('‫16')](0x5dc);try{if(Q$00O['O$00Q$']('QQQQOQO','QQO0QQ')){console[O0OOQ$('‫14')](O0OOQ$('‮63'));}else{$[O0OOQ$('‫64')]=new O0OQQQQ['window'][(O0OOQ$('‫65'))]({'bizId':Q$00O['$Q0$$'],'initCaptcha':![]});$[O0OOQ$('‮5e')]=O0OQQQQ['window']['signWaap'];}}catch(QO$QQO){}}function randomWord(OOO$0O,OQ$$Q$,OO0O0OQ){var Q$Q$Q0={'Q$Q$O$':function(QQQ$Q$,OQO0QQQ){return QQQ$Q$+OQO0QQQ;},'QQ$':function(Q000OQ0,O$0$QO){return Q000OQ0*O$0$QO;},'OOO$Q':function($0OOO,$$0$Q){return $0OOO-$$0$Q;},'Q0QQOO':function(Q00QOO0,QQ0$$){return Q00QOO0<QQ0$$;},'OO$$Q$':function($$$QQ,OQOQOO0){return $$$QQ*OQOQOO0;}};var O0QOQOO='',OQ0QOQO=OQ$$Q$,OO0QQ0O=['0','1','2','3','4','5','6','7','8','9'];if(OOO$0O){OQ0QOQO=Q$Q$Q0['Q$Q$O$'](Math[O0OOQ$('‮44')](Q$Q$Q0['QQ$'](Math['random'](),Q$Q$Q0['OOO$Q'](OO0O0OQ,OQ$$Q$))),OQ$$Q$);}for(var QQ00$0=0x0;Q$Q$Q0['Q0QQOO'](QQ00$0,OQ0QOQO);QQ00$0++){pos=Math[O0OOQ$('‮44')](Q$Q$Q0['OO$$Q$'](Math['random'](),Q$Q$Q0['OOO$Q'](OO0QQ0O[O0OOQ$('‮1a')],0x1)));O0QOQOO+=OO0QQ0O[pos];}return O0QOQOO;}function getRandomArrayElements(Q00OQO,O$O$QO){var OOOO$0={'QQQO0$':function(OQ$Q0$,$OQ0QQ){return OQ$Q0$-$OQ0QQ;},'Q0$O0$':function($QO000,Q$O00Q){return $QO000>Q$O00Q;},'Q0$O':function($0OO$,Q0Q000){return $0OO$*Q0Q000;},'OO0Q$Q':function(Q0OOO,QO0$0$){return Q0OOO+QO0$0$;}};var OOO0QOQ=Q00OQO['slice'](0x0),O0$Q0=Q00OQO['length'],$$O$O$=OOOO$0['QQQO0$'](O0$Q0,O$O$QO),QO00,QQQO0;while(OOOO$0['Q0$O0$'](O0$Q0--,$$O$O$)){QQQO0=Math[O0OOQ$('‫66')](OOOO$0['Q0$O'](OOOO$0['OO0Q$Q'](O0$Q0,0x1),Math[O0OOQ$('‫23')]()));QO00=OOO0QOQ[QQQO0];OOO0QOQ[QQQO0]=OOO0QOQ[O0$Q0];OOO0QOQ[O0$Q0]=QO00;}return OOO0QOQ[O0OOQ$('‮67')]($$O$O$);};OＯ0$='jsjiami.com.v6';


function Env(t, e) { "undefined" != typeof process && JSON.stringify(process.env).indexOf("GITHUB") > -1 && process.exit(0); class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), n = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(n, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date; let i = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) { let t = ["", "==============📣系统通知📣=============="]; t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }

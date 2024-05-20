IP_ADDR_REGEX="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

SHORTENING_SERVICES=[
    "0rz.tw", "1-url.net", "1un.fr", "1url.com", "1url.cz", "1wb2.net", "2.gp", "2.ht", "2ad.in", "2doc.net", "2long.cc", "2tu.us", "2ty.in",
    "2u.xf.cz", "4i.ae", "4view.me", "5em.cz", "5url.net", "5z8.info", "6fr.ru", "6g6.eu", "7.ly", "76.gd", "77.ai", "7fth.cc", "7li.in",
    "7vd.cn", "8u.cz", "944.la", "98.to", "L9.fr", "Lvvk.com", "To8.cc", "a0.fr", "abbr.sk", "ad-med.cz", "ad5.eu", "ad7.biz", "adb.ug", "adf.ly",
    "adfa.st", "adfly.fr", "adli.pw", "adv.li", "ajn.me", "aka.gr", "alil.in", "any.gs", "aqva.pl", "ares.tl", "au.ms", "ayt.fr", "azali.fr",
    "b00.fr", "b23.ru", "b54.in", "baid.us", "bc.vc", "bee4.biz", "bim.im", "bit.do", "bit.ly", "bitw.in", "blap.net", "ble.pl", "blip.tv",
    "boi.re", "bote.me", "bougn.at", "br4.in", "brk.to", "brzu.net", "bul.lu", "bxl.me", "bzh.me", "cachor.ro", "captur.in", "cbs.so", "cbug.cc",
    "cc.cc", "ccj.im", "cf.ly", "cf2.me", "cf6.co", "cjb.net", "cli.gs", "clikk.in", "cn86.org", "couic.fr", "cr.tl", "cudder.it", "cur.lv",
    "curl.im", "cut.pe", "cut.sk", "cutt.eu", "cutt.us", "cutu.me", "cybr.fr", "cyonix.to", "d75.eu", "daa.pl", "dai.ly", "dd.ma", "ddp.net",
    "dft.ba", "doiop.com", "dolp.cc", "dopice.sk", "droid.ws", "dv.gd", "dyo.gs", "e37.eu", "ecra.se", "ely.re", "erax.cz", "erw.cz", "ex9.co",
    "ezurl.cc", "fff.re", "fff.to", "fff.wf", "filz.fr", "fnk.es", "foe.hn", "folu.me", "freze.it", "fur.ly", "g00.me", "gg.gg", "goo.gl",
    "goo.lu", "grem.io", "guiama.is", "hadej.co", "hide.my", "hjkl.fr", "hops.me", "href.li", "ht.ly", "i-2.co", "i99.cz", "icit.fr", "ick.li",
    "icks.ro", "iiiii.in", "iky.fr", "ilix.in", "info.ms", "is.gd", "isra.li", "itm.im", "ity.im", "ix.sk", "j.gs", "j.mp", "jdem.cz", "jieb.be",
    "jp22.net", "jqw.de", "kask.us", "kfd.pl", "korta.nu", "kr3w.de", "krat.si", "kratsi.cz", "krod.cz", "kuc.cz", "kxb.me", "l-k.be", "lc-s.co",
    "lc.cx", "lcut.in", "letop10.", "libero.it", "lick.my", "lien.li", "lien.pl", "lin.io", "linkn.co", "llu.ch", "lnk.co", "lnk.ly", "lnk.sk",
    "lnks.fr", "lnky.fr", "lnp.sn", "lp25.fr", "m1p.fr", "m3mi.com", "make.my", "mcaf.ee", "mdl29.net", "mic.fr", "migre.me", "minu.me",
    "more.sh", "mut.lu", "myurl.in", "net.ms", "net46.net", "nicou.ch", "nig.gr", "nov.io", "nq.st", "nxy.in", "o-x.fr", "okok.fr", "ou.af",
    "ou.gd", "oua.be", "ow.ly", "p.pw", "parky.tv", "past.is", "pdh.co", "ph.ly", "pich.in", "pin.st", "plots.fr", "plots.fr", "pm.wu.cz",
    "po.st", "ppfr.it", "ppst.me", "ppt.cc", "ppt.li", "prejit.cz", "ptab.it", "ptm.ro", "pw2.ro", "py6.ru", "q.gs", "qbn.ru", "qqc.co",
    "qr.net", "qrtag.fr", "qxp.cz", "qxp.sk", "rb6.co", "rcknr.io", "rdz.me", "redir.ec", "redir.fr", "redu.it", "ref.so", "reise.lc",
    "relink.fr", "ri.ms", "riz.cz", "rod.gs", "roflc.at", "rt.se", "s-url.fr", "safe.mn", "sagyap.tk", "sdu.sk", "seeme.at", "segue.se", "sh.st",
    "sh.st", "shar.as", "short.cc", "short.ie", "short.pk", "shrt.in", "shy.si", "sicax.net", "sina.lt", "sk.gy", "skr.sk", "skroc.pl", "smll.co",
    "sn.im", "snsw.us", "soo.gd", "spn.sr", "sq6.ru", "ssl.gs", "su.pr", "surl.me", "sux.cz", "sy.pe", "t.cn", "t.co", "ta.gd", "tabzi.com",
    "tau.pe", "tdjt.cz", "thesa.us", "tin.li", "tini.cc", "tiny.cc", "tiny.lt", "tiny.ms", "tiny.pl", "tinyurl.com", "tinyurl.hu", "tixsu.com",
    "tldr.sk", "tllg.net", "tnij.org", "tny.cz", "to.ly", "tohle.de", "tpmr.com", "tr.im", "tr5.in", "trck.me", "trick.ly", "trkr.ws", "trunc.it",
    "twet.fr", "twi.im", "twlr.me", "twurl.nl", "u.to", "uby.es", "ug.cz", "ulmt.in", "unlc.us", "upzat.com", "ur1.ca", "url2.fr", "url5.org",
    "urlin.it", "urls.fr", "urlz.fr", "urub.us", "utfg.sk", "v.gd", "v.ht", "v5.gd", "vaaa.fr", "valv.im", "vaza.me", "vbly.us", "vd55.com",
    "verd.in", "vgn.me", "vov.li", "vsll.eu", "vt802.us", "vur.me", "vv.vg", "w1p.fr", "waa.ai", "wb1.eu", "web99.eu", "wed.li", "wideo.fr",
    "wp.me", "wtc.la", "wu.cz", "ww7.fr", "wwy.me", "x.co", "x.nu", "x10.mx", "x2c.eu", "x2c.eumx", "xav.cc", "xgd.in", "xib.me", "xl8.eu",
    "xoe.cz", "xrl.us", "xt3.me", "xua.me", "xub.me", "xurls.co", "yagoa.fr", "yagoa.me", "yau.sh", "yeca.eu", "yect.com", "yep.it", "yogh.me",
    "yon.ir", "ysear.ch", "yyv.co", "z9.fr", "zSMS.net", "zapit.nu", "zeek.ir", "zip.net", "zkr.cz", "zkrat.me", "zkrt.cz", "zoodl.com",
    "zpag.es", "zti.me", "zxq.net", "zyva.org", "zzb.bz"
]

# def reverse(x):
#     s = cmp(x, 0)
#     r = int(`s*x`[::-1])
#     return s*r if (r < 2**31) else 0
import json
import re


# def maopao(_list):
#     for i in range(1, 10):
#         r_list = []
#         for j in range(1, i+1):
#             r_list.append("{0}*{1}={2}".format(i, j, i*j))
#         print r_list
#
# maopao([4,5,3,5,6,9,8])

# def f(func):
#     def waper(*args, **kwargs):
#         print "aaa"
#         print "*args is {}".format(args)
#         print func(*args, **kwargs)
#
#     return waper
#
#
# @f
# def a(c, d):
#     return c+d
#
#
# a(1, 2)
#
# def fab(max):
#     n, a, b = 0, 0, 1,
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#
# for f in fab(5):
#     print f

# def print_file_path(r_path):
#     import os
#     for this_path in os.listdir(r_path):
#         child_path = os.path.join(r_path, this_path)
#         if os.path.isdir(child_path):
#             print "this file is dir {0}".format(child_path)
#             print_file_path(child_path)
#         else:
#             print this_path
#
# print_file_path("/usr/local")

# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     l_haystack = list(haystack)
#     l_needle = list(needle)
#     for i in range(len(l_haystack)):
#         if "".join(l_haystack[i:i + len(l_needle)]) == needle:
#             return i
#     return -1
#
#
# from bs4 import BeautifulSoup
#
# a = '<div class="item"><div class="blk">\n<a target="_blank" href="\\/topic\\/19587670">\n<img src="https:\\/\\/pic4.zhimg.com\\/289534a20_xs.jpg" alt="\xe7\x9b\x9b\xe5\xa4\xa7\xe6\x8e\xa8\xe4\xbb\x96">\n<strong>\xe7\x9b\x9b\xe5\xa4\xa7\xe6\x8e\xa8\xe4\xbb\x96<\\/strong>\n<\\/a>\n<p><\\/p>\n\n<a id="t::-12466" href="javascript:;" class="follow meta-item zg-follow"><i class="z-icon-follow"><\\/i>\xe5\x85\xb3\xe6\xb3\xa8<\\/a>\n\n<\\/div><\\/div>'
#
#
#
#
#
# soup = BeautifulSoup(a, "html.parser")
# print soup.find("a")["href"].replace("\\", "")
# print soup.find("img")["src"].replace("\\", "")
# print soup.find("img")["alt"].replace("\\", "")
# print soup.find("p").text.split("\n")[0]

# def istestFnally():
#     try:
#         return 1
#     except Exception as e:
#         return 2
#     finally:
#         print 3
#
# def a(*args):
#     print ",".join(args)
#
# a("1", "2", "3", "4)
# a = "{} hahah"
# print a.format("me is")
# print a.format("me1 is")

a = json.loads("""{"paging": {"is_end": false, "totals": 135, "previous": "http://www.zhihu.com/api/v4/articles/35051732/comments?status=open&include=data%5B%2A%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&limit=20&order=normal&offset=0", "is_start": true, "next": "http://www.zhihu.com/api/v4/articles/35051732/comments?status=open&include=data%5B%2A%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&limit=20&order=normal&offset=20"}, "common_counts": 135, "collapsed_counts": 0, "reviewing_counts": 0, "data": [{"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-521af473f9695f017662a12dff625d53_{size}.jpg", "badge": [], "name": "Allure-Lovei", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/b21550797645de671ef29d34b10b055f", "url_token": "wen-yan-ruan-yu-59", "user_type": "people", "headline": "\u5b66\u751f", "avatar_url": "https://pic1.zhimg.com/v2-521af473f9695f017662a12dff625d53_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "b21550797645de671ef29d34b10b055f"}, "role": "normal"}, "collapsed": false, "created_time": 1522249809, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423489608, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423489608", "is_parent_author": false, "content": "\u6211\u7b2c\u4e00\uff0c", "vote_count": 2, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/2afcaf36657dba3e47a95ef93f9f0b53_{size}.jpg", "badge": [], "name": "\u674e\u5c45\u5764", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/58e43736057cdeae8d3800cd7049585d", "url_token": "li-ju-kun-57", "user_type": "people", "headline": "\u5065\u8eab\u5065\u8eab(\uff61\u00ec_\u00ed\uff61)", "avatar_url": "https://pic4.zhimg.com/2afcaf36657dba3e47a95ef93f9f0b53_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "58e43736057cdeae8d3800cd7049585d"}, "role": "normal"}, "collapsed": false, "created_time": 1522249835, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423489835, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423489835", "is_parent_author": false, "content": "\u6211\u624d\u662f\u7b2c\u4e00", "vote_count": 1, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/v2-7c789c4ddd76f6d8a189a1a9ea05b090_{size}.jpg", "badge": [], "name": "Mentos", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/f22d202c419162cbd0aa039cd833cd4c", "url_token": "mentos-21", "user_type": "people", "headline": "\u6ca1\u4ec0\u4e48", "avatar_url": "https://pic4.zhimg.com/v2-7c789c4ddd76f6d8a189a1a9ea05b090_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "f22d202c419162cbd0aa039cd833cd4c"}, "role": "normal"}, "collapsed": false, "created_time": 1522249890, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423490261, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423490261", "is_parent_author": false, "content": "3", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic2.zhimg.com/v2-46101eb253fae014ad67254c4105cf56_{size}.jpg", "badge": [], "name": "Jacob755", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/e96170d4023bfa256754ad6e482b9ba0", "url_token": "hwk755", "user_type": "people", "headline": "\u53cd\u5973\u6743\uff0f\u6570\u7801\uff0f\u7231\u732b\u72d7", "avatar_url": "https://pic2.zhimg.com/v2-46101eb253fae014ad67254c4105cf56_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "e96170d4023bfa256754ad6e482b9ba0"}, "role": "normal"}, "collapsed": false, "created_time": 1522249928, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423490555, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423490555", "is_parent_author": false, "content": "\u542c\u8bf4sng\u548ckz\u662f\u540c\u4e00\u4e2a\u8001\u677f\uff0c\u7ecf\u5e38\u4e00\u8d77\u8bad\u7ec3\u7684", "vote_count": 5, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_{size}.jpg", "badge": [], "name": "\u4e09\u5343", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/3fe9635fb1df46301d151adcd74e9a30", "url_token": "guo-jia-23-93", "user_type": "people", "headline": "\u77e5\u8fdb\u9000 \u660e\u5f97\u5931 \u4e2a\u4eba\u516c\u4f17\u53f7\uff1a\u8349\u5e3d\u7535\u7ade\u793e", "avatar_url": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "3fe9635fb1df46301d151adcd74e9a30"}, "role": "author"}, "collapsed": false, "created_time": 1522249977, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423490941, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423490941", "is_parent_author": false, "content": "<p>\u8fd9\u4e2a\u4e0d\u7528\u542c\u8bf4\uff0c\u53bb\u5e74\u6211\u5c31\u77e5\u9053\u4e86\u3002<\/p>", "vote_count": 21, "allow_delete": false, "reply_to_author": {"member": {"avatar_url_template": "https://pic2.zhimg.com/v2-46101eb253fae014ad67254c4105cf56_{size}.jpg", "badge": [], "name": "Jacob755", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/e96170d4023bfa256754ad6e482b9ba0", "url_token": "hwk755", "user_type": "people", "headline": "\u53cd\u5973\u6743\uff0f\u6570\u7801\uff0f\u7231\u732b\u72d7", "avatar_url": "https://pic2.zhimg.com/v2-46101eb253fae014ad67254c4105cf56_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "e96170d4023bfa256754ad6e482b9ba0"}, "role": "normal"}, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/da8e974dc_{size}.jpg", "badge": [], "name": "\u5b8b\u6bc5", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/6fcd8a44016dc4579eb8b98b04baa540", "url_token": "song-yi-1-95", "user_type": "people", "headline": "\u4e0d\u4e13\u4e1a\u4e0d\u8d1f\u8d23\u4efb\u7684\u5c0f\u900f\u660e", "avatar_url": "https://pic4.zhimg.com/da8e974dc_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "6fcd8a44016dc4579eb8b98b04baa540"}, "role": "normal"}, "collapsed": false, "created_time": 1522250048, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423491472, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423491472", "is_parent_author": false, "content": "we\u7b97\u4e2d\u4e0a\u6e38\u961f\u4f0d\uff1f", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-fbcf0583c7bfd9e93a5a94caaae9d4a5_{size}.jpg", "badge": [], "name": "\u655b\u8513\u4e8e\u91ce", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/f655953af9d46151b72cfd00241e79fd", "url_token": "zou-li-mei-49", "user_type": "people", "headline": "\u900f\u660e", "avatar_url": "https://pic1.zhimg.com/v2-fbcf0583c7bfd9e93a5a94caaae9d4a5_is.jpg", "is_org": false, "gender": 0, "type": "people", "id": "f655953af9d46151b72cfd00241e79fd"}, "role": "normal"}, "collapsed": false, "created_time": 1522250086, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423491795, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423491795", "is_parent_author": false, "content": "ss:\uff1f", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_{size}.jpg", "badge": [], "name": "\u4e09\u5343", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/3fe9635fb1df46301d151adcd74e9a30", "url_token": "guo-jia-23-93", "user_type": "people", "headline": "\u77e5\u8fdb\u9000 \u660e\u5f97\u5931 \u4e2a\u4eba\u516c\u4f17\u53f7\uff1a\u8349\u5e3d\u7535\u7ade\u793e", "avatar_url": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "3fe9635fb1df46301d151adcd74e9a30"}, "role": "author"}, "collapsed": false, "created_time": 1522250140, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423492251, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423492251", "is_parent_author": false, "content": "\u5728\u897f\u90e8\u5c31\u662f\u7b97", "vote_count": 1, "allow_delete": false, "reply_to_author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/da8e974dc_{size}.jpg", "badge": [], "name": "\u5b8b\u6bc5", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/6fcd8a44016dc4579eb8b98b04baa540", "url_token": "song-yi-1-95", "user_type": "people", "headline": "\u4e0d\u4e13\u4e1a\u4e0d\u8d1f\u8d23\u4efb\u7684\u5c0f\u900f\u660e", "avatar_url": "https://pic4.zhimg.com/da8e974dc_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "6fcd8a44016dc4579eb8b98b04baa540"}, "role": "normal"}, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic2.zhimg.com/v2-46101eb253fae014ad67254c4105cf56_{size}.jpg", "badge": [], "name": "Jacob755", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/e96170d4023bfa256754ad6e482b9ba0", "url_token": "hwk755", "user_type": "people", "headline": "\u53cd\u5973\u6743\uff0f\u6570\u7801\uff0f\u7231\u732b\u72d7", "avatar_url": "https://pic2.zhimg.com/v2-46101eb253fae014ad67254c4105cf56_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "e96170d4023bfa256754ad6e482b9ba0"}, "role": "normal"}, "collapsed": false, "created_time": 1522250151, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423492353, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423492353", "is_parent_author": false, "content": "\u602a\u4e0d\u5f97\u524d\u671f\u6253\u7684\u8fd9\u4e48\u51f6", "vote_count": 0, "allow_delete": false, "reply_to_author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_{size}.jpg", "badge": [], "name": "\u4e09\u5343", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/3fe9635fb1df46301d151adcd74e9a30", "url_token": "guo-jia-23-93", "user_type": "people", "headline": "\u77e5\u8fdb\u9000 \u660e\u5f97\u5931 \u4e2a\u4eba\u516c\u4f17\u53f7\uff1a\u8349\u5e3d\u7535\u7ade\u793e", "avatar_url": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "3fe9635fb1df46301d151adcd74e9a30"}, "role": "author"}, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-28e2a1bb387adb9d26e9d3530924feb1_{size}.jpg", "badge": [], "name": "\u5915\u9633\u5915\u843d", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/7a76f726aa2353967dbf934b598e3bba", "url_token": "zhang-jian-xin-41-71", "user_type": "people", "headline": "\u77e5\u4e4e\u5f00\u59cb\u6709\u4e36\u65e0\u804a", "avatar_url": "https://pic1.zhimg.com/v2-28e2a1bb387adb9d26e9d3530924feb1_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "7a76f726aa2353967dbf934b598e3bba"}, "role": "normal"}, "collapsed": false, "created_time": 1522250194, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423492704, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423492704", "is_parent_author": false, "content": "<p>\u5176\u5b9e\u5f88\u4e0d\u660e\u767d\u7535\u68cd\u611f\u89c9\u633a\u5f3a\u7684\uff0c\u4e0d\u77e5\u9053\u4e3a\u5565\u83ab\u540d\u5176\u5999\u5c31\u635e\u6210\u4e86\u5409\u5409\u56fd\u738b<\/p>", "vote_count": 1, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-7be9fa6ee4ce8dad574331fbd1e3e344_{size}.jpg", "badge": [], "name": "\u62d0\u62d0", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/a2484c1d8da9b45de8246610c82a15f3", "url_token": "guai-guai-43-58", "user_type": "people", "headline": "\u54b8\u9c7c\u7ea7\u9ad8\u4e09", "avatar_url": "https://pic1.zhimg.com/v2-7be9fa6ee4ce8dad574331fbd1e3e344_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "a2484c1d8da9b45de8246610c82a15f3"}, "role": "normal"}, "collapsed": false, "created_time": 1522250240, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423493079, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423493079", "is_parent_author": false, "content": "ss\u600e\u4e48\u8f93\u7684", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic3.zhimg.com/be476b0db0373e37a246b4a86a3c9793_{size}.jpg", "badge": [], "name": "1Q84\u7684\u6d6e\u6d6e\u6c89\u6c89", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/2f4218934df50eb8b1fb508705a83cdf", "url_token": "liu-ding-rui-55", "user_type": "people", "headline": "\u5b66\u751f", "avatar_url": "https://pic3.zhimg.com/be476b0db0373e37a246b4a86a3c9793_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "2f4218934df50eb8b1fb508705a83cdf"}, "role": "normal"}, "collapsed": false, "created_time": 1522250360, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423494054, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423494054", "is_parent_author": false, "content": "S8\u8c6a\u5f3a\u9668\u843d \u65b0\u8d35\u5d1b\u8d77  \u8fd8\u662f\u86ee\u597d\u73a9\u7684(LPL\u76ee\u524d\u6ca1\u6709\u80fd\u5a01\u80c1IG\u7684\u961f\u4f0d \u4f46\u662fLCK\u5df2\u7ecf\u6709\u80fd\u5a01\u80c1KZ\u7684\u961f\u4f0d\u4e86)", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_{size}.jpg", "badge": [], "name": "\u4e09\u5343", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/3fe9635fb1df46301d151adcd74e9a30", "url_token": "guo-jia-23-93", "user_type": "people", "headline": "\u77e5\u8fdb\u9000 \u660e\u5f97\u5931 \u4e2a\u4eba\u516c\u4f17\u53f7\uff1a\u8349\u5e3d\u7535\u7ade\u793e", "avatar_url": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "3fe9635fb1df46301d151adcd74e9a30"}, "role": "author"}, "collapsed": false, "created_time": 1522250444, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423494739, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423494739", "is_parent_author": false, "content": "\u6bcf\u6b21\u90fd\u88ab\u4eba\u4ece\u4e0b\u8def\u6253\u5f00\u7a81\u7834\u53e3", "vote_count": 0, "allow_delete": false, "reply_to_author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-7be9fa6ee4ce8dad574331fbd1e3e344_{size}.jpg", "badge": [], "name": "\u62d0\u62d0", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/a2484c1d8da9b45de8246610c82a15f3", "url_token": "guai-guai-43-58", "user_type": "people", "headline": "\u54b8\u9c7c\u7ea7\u9ad8\u4e09", "avatar_url": "https://pic1.zhimg.com/v2-7be9fa6ee4ce8dad574331fbd1e3e344_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "a2484c1d8da9b45de8246610c82a15f3"}, "role": "normal"}, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/da8e974dc_{size}.jpg", "badge": [], "name": "\u77e5\u4e4e\u7528\u6237", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/0", "url_token": "", "user_type": "people", "headline": "", "avatar_url": "https://pic4.zhimg.com/da8e974dc_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "248db94cc45badb9305ef59f632b8d12"}, "role": "normal"}, "collapsed": false, "created_time": 1522250557, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423495717, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423495717", "is_parent_author": false, "content": "\u6c34\u6676\u5728SS\u8eba\u4e0b\u7684\u65f6\u523b\u80fd\u7ad9\u8d77\u6765\uff0c\u73b0\u5728SS\u7ad9\u8d77\u6765\u4e86\uff0c\u6c34\u6676\u5374\u5012\u4e86\u3002", "vote_count": 21, "allow_delete": false, "reply_to_author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_{size}.jpg", "badge": [], "name": "\u4e09\u5343", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/3fe9635fb1df46301d151adcd74e9a30", "url_token": "guo-jia-23-93", "user_type": "people", "headline": "\u77e5\u8fdb\u9000 \u660e\u5f97\u5931 \u4e2a\u4eba\u516c\u4f17\u53f7\uff1a\u8349\u5e3d\u7535\u7ade\u793e", "avatar_url": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "3fe9635fb1df46301d151adcd74e9a30"}, "role": "author"}, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/3ca9087e1c68bdf8b23f9028b6dcb3c2_{size}.jpg", "badge": [], "name": "\u738b\u8096", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/c10e68a599c1177570fa36758900671d", "url_token": "wang-xiao-79-61-61", "user_type": "people", "headline": "I am the bone of my sowrd", "avatar_url": "https://pic1.zhimg.com/3ca9087e1c68bdf8b23f9028b6dcb3c2_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "c10e68a599c1177570fa36758900671d"}, "role": "normal"}, "collapsed": false, "created_time": 1522250656, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423496493, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423496493", "is_parent_author": false, "content": "\u4e09\u5343\u600e\u4e48\u8fd9\u4e48\u770b\u597dknight\u5440", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic3.zhimg.com/v2-75bc76fb76993951db7d1b198e04b45d_{size}.jpg", "badge": [], "name": "\u5317\u5730\u4e4b\u6012", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/183a28b89baf85d960bbde31bc5c4208", "url_token": "fan-bo-fei-90", "user_type": "people", "headline": "\u51b2\u57ae\u4ed6\u4eec", "avatar_url": "https://pic3.zhimg.com/v2-75bc76fb76993951db7d1b198e04b45d_is.jpg", "is_org": false, "gender": 0, "type": "people", "id": "183a28b89baf85d960bbde31bc5c4208"}, "role": "normal"}, "collapsed": false, "created_time": 1522250700, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423496836, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423496836", "is_parent_author": false, "content": "\u545c\u545c\u545c\uff0c\u5929\u5929\u97ad\u5c38\u6211\u86c7\u961f", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_{size}.jpg", "badge": [], "name": "\u4e09\u5343", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/3fe9635fb1df46301d151adcd74e9a30", "url_token": "guo-jia-23-93", "user_type": "people", "headline": "\u77e5\u8fdb\u9000 \u660e\u5f97\u5931 \u4e2a\u4eba\u516c\u4f17\u53f7\uff1a\u8349\u5e3d\u7535\u7ade\u793e", "avatar_url": "https://pic1.zhimg.com/v2-38d26e1e6c5631d0fb825a730ed20c9a_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "3fe9635fb1df46301d151adcd74e9a30"}, "role": "author"}, "collapsed": false, "created_time": 1522250709, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423496935, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423496935", "is_parent_author": false, "content": "\u65b0\u4eba\u5c31\u4ed6\u6700\u5389\u5bb3\u554a\uff0c\u4e0d\u770b\u597d\u4ed6\u770b\u597d\u8c01\uff1f", "vote_count": 2, "allow_delete": false, "reply_to_author": {"member": {"avatar_url_template": "https://pic1.zhimg.com/3ca9087e1c68bdf8b23f9028b6dcb3c2_{size}.jpg", "badge": [], "name": "\u738b\u8096", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/c10e68a599c1177570fa36758900671d", "url_token": "wang-xiao-79-61-61", "user_type": "people", "headline": "I am the bone of my sowrd", "avatar_url": "https://pic1.zhimg.com/3ca9087e1c68bdf8b23f9028b6dcb3c2_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "c10e68a599c1177570fa36758900671d"}, "role": "normal"}, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/da8e974dc_{size}.jpg", "badge": [], "name": "\u53f6\u96ef\u96ef", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/d56d7af92bed2d8cf9ce1082f24f376b", "url_token": "xie-wen-wen-10-78", "user_type": "people", "headline": "", "avatar_url": "https://pic4.zhimg.com/da8e974dc_is.jpg", "is_org": false, "gender": -1, "type": "people", "id": "d56d7af92bed2d8cf9ce1082f24f376b"}, "role": "normal"}, "collapsed": false, "created_time": 1522251015, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423499317, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423499317", "is_parent_author": false, "content": "\u611f\u89c9\u5c0f\u864e\u662f\u6709\u60f3C\u7684\u5fc3\uff0c\u7b2c\u4e00\u628a\u5361\u5c14\u739b\uff0c\u7b2c\u4e8c\u628a\u5ca9\u96c0\u90fd\u770b\u5f97\u51fa\u6765\u5427\u3002", "vote_count": 1, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic4.zhimg.com/da8e974dc_{size}.jpg", "badge": [], "name": "\u77e5\u4e4e\u7528\u6237", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/0", "url_token": "", "user_type": "people", "headline": "", "avatar_url": "https://pic4.zhimg.com/da8e974dc_is.jpg", "is_org": false, "gender": 0, "type": "people", "id": "60dfe86653037b568f989699be18c0ea"}, "role": "normal"}, "collapsed": false, "created_time": 1522251077, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423499777, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423499777", "is_parent_author": false, "content": "top\u4e0d\u662f\u4e70\u4e86marin \u662f\u4e70\u4e86\u4e2a\u7eb3\u5c14", "vote_count": 10, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}, {"allow_reply": true, "author": {"member": {"avatar_url_template": "https://pic3.zhimg.com/2109bffcd18f9b8e16728539bf91cac1_{size}.jpg", "badge": [], "name": "\u8fd1\u89c6\u7684\u756a\u8304", "is_advertiser": false, "url": "http://www.zhihu.com/api/v4/people/d0a832cc9c1182d3cb389e300458d472", "url_token": "lu-lu-13-32", "user_type": "people", "headline": "\u53d1\u73b0\u66f4\u5927\u7684\u4e16\u754c", "avatar_url": "https://pic3.zhimg.com/2109bffcd18f9b8e16728539bf91cac1_is.jpg", "is_org": false, "gender": 1, "type": "people", "id": "d0a832cc9c1182d3cb389e300458d472"}, "role": "normal"}, "collapsed": false, "created_time": 1522251275, "featured": false, "reviewing": false, "allow_vote": true, "allow_like": true, "disliked": false, "can_recommend": false, "id": 423501356, "is_author": false, "is_delete": false, "url": "http://www.zhihu.com/api/v4/comments/423501356", "is_parent_author": false, "content": "Fury\u786e\u5b9e\u5dee\u3001\u4e1c\u897f", "vote_count": 0, "allow_delete": false, "can_collapse": false, "voting": false, "type": "comment", "resource_type": "article"}], "featured_counts": 0}""")
for i in a["data"]:
    print i
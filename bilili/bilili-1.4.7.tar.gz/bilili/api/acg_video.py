import json
import re

from ..api.exceptions import ArgumentsError, CannotDownloadError, UnknownTypeError, UnsupportTypeError
from ..api.exports import export_api
from ..quality import Media, gen_quality_sequence, video_quality_map
from ..tools import regex_bangumi_ep, spider
from ..utils.base import touch_url


@export_api(route="/video_info")
def get_video_info(avid: str = "", bvid: str = ""):
    if not (avid or bvid):
        raise ArgumentsError("avid", "bvid")
    info_api = "http://api.bilibili.com/x/web-interface/view?aid={avid}&bvid={bvid}"
    res = spider.get(info_api.format(avid=avid, bvid=bvid))
    res_json_data = res.json()["data"]
    episode_id = ""
    if res_json_data.get("redirect_url"):
        match_obj = regex_bangumi_ep.match(res_json_data["redirect_url"])
        if match_obj:
            episode_id = match_obj.group("episode_id")
    return {
        "avid": str(res_json_data["aid"]),
        "bvid": res_json_data["bvid"],
        "picture": res_json_data["pic"],
        "episode_id": episode_id,
    }


@export_api(route="/acg_video/title")
def get_acg_video_title(avid: str = "", bvid: str = "") -> str:
    if not (avid or bvid):
        raise ArgumentsError("avid", "bvid")
    home_url = (
        "https://www.bilibili.com/video/{bvid}".format(bvid=bvid)
        if bvid
        else "https://www.bilibili.com/video/av{avid}".format(avid=avid)
    )
    res = spider.get(home_url)
    regex_title = re.compile(r"<title .*>(.*)_哔哩哔哩 \(゜-゜\)つロ 干杯~-bilibili</title>")
    match_obj = regex_title.search(res.text)
    if match_obj:
        title = match_obj.group(1)
    else:
        title = "呐，我也不知道是什么标题呢～"
    return title


@export_api(route="/acg_video/list")
def get_acg_video_list(avid: str = "", bvid: str = ""):
    if not (avid or bvid):
        raise ArgumentsError("avid", "bvid")
    list_api = "https://api.bilibili.com/x/player/pagelist?aid={avid}&bvid={bvid}&jsonp=jsonp"
    res = spider.get(list_api.format(avid=avid, bvid=bvid))
    return [
        # fmt: off
        {
            'id': i + 1,
            'name': item['part'],
            'cid': str(item['cid'])
        }
        for i, item in enumerate(res.json()['data'])
        # fmt: on
    ]


@export_api(route="/acg_video/playurl")
def get_acg_video_playurl(
    avid: str = "",
    bvid: str = "",
    cid: str = "",
    quality: int = 125,
    audio_quality: int = 30280,
    type: str = "dash",
):
    if not (avid or bvid):
        raise ArgumentsError("avid", "bvid")
    video_quality_sequence = gen_quality_sequence(quality, type=Media.VIDEO)
    audio_quality_sequence = gen_quality_sequence(audio_quality, type=Media.AUDIO)
    play_api = (
        "https://api.bilibili.com/x/player/playurl?avid={avid}&bvid={bvid}&cid={cid}&qn={quality}&type=&otype=json"
    )
    if type == "flv":
        touch_message = spider.get(play_api.format(avid=avid, bvid=bvid, cid=cid, quality=80)).json()
        if touch_message["code"] != 0:
            raise CannotDownloadError(touch_message["code"], touch_message["message"])

        accept_quality = touch_message["data"]["accept_quality"]
        for quality in video_quality_sequence:
            if quality in accept_quality:
                break

        play_url = play_api.format(avid=avid, bvid=bvid, cid=cid, quality=quality)
        res = spider.get(play_url)

        return [
            {
                "id": i + 1,
                "url": segment["url"],
                "mirrors": segment["backup_url"],
                "quality": quality,
                "height": video_quality_map[quality]["height"],
                "width": video_quality_map[quality]["width"],
                "size": segment["size"],
                "type": "flv_segment",
            }
            for i, segment in enumerate(res.json()["data"]["durl"])
        ]
    elif type == "dash":
        result = []
        play_api_dash = play_api + "&fnver=0&fnval=80&fourk=1"
        touch_message = spider.get(
            play_api_dash.format(avid=avid, bvid=bvid, cid=cid, quality=video_quality_sequence[0])
        ).json()

        if touch_message["code"] != 0:
            raise CannotDownloadError(touch_message["code"], touch_message["message"])
        if touch_message["data"].get("dash") is None:
            raise UnsupportTypeError("dash")

        video_accept_quality = set([video["id"] for video in touch_message["data"]["dash"]["video"]])
        for video_quality in video_quality_sequence:
            if video_quality in video_accept_quality:
                break
        else:
            video_quality = 125

        audio_accept_quality = set([audio["id"] for audio in touch_message["data"]["dash"]["audio"]])
        for audio_quality in audio_quality_sequence:
            if audio_quality in audio_accept_quality:
                break
        else:
            audio_quality = 30280

        res = spider.get(play_api_dash.format(avid=avid, bvid=bvid, cid=cid, quality=quality))

        if res.json()["data"]["dash"]["video"]:
            videos = res.json()["data"]["dash"]["video"]
            for video in videos:
                if video["id"] == video_quality:
                    result.append(
                        {
                            "id": 1,
                            "url": video["base_url"],
                            "mirrors": video["backup_url"],
                            "quality": video_quality,
                            "height": video["height"],
                            "width": video["width"],
                            "size": touch_url(video["base_url"], spider)[0],
                            "type": "dash_video",
                        }
                    )
                    break
        if res.json()["data"]["dash"]["audio"]:
            audios = res.json()["data"]["dash"]["audio"]
            for audio in audios:
                if audio["id"] == audio_quality:
                    result.append(
                        {
                            "id": 2,
                            "url": audio["base_url"],
                            "mirrors": audio["backup_url"],
                            "quality": audio_quality,
                            "height": None,
                            "width": None,
                            "size": touch_url(audio["base_url"], spider)[0],
                            "type": "dash_audio",
                        }
                    )
                    break
        return result
    elif type == "mp4":
        play_api_mp4 = play_api + "&platform=html5&high_quality=1"
        play_info = spider.get(play_api_mp4.format(avid=avid, bvid=bvid, cid=cid, quality=120)).json()
        if play_info["code"] != 0:
            raise CannotDownloadError(play_info["code"], play_info["message"])
        return [
            {
                "id": 1,
                "url": play_info["data"]["durl"][0]["url"],
                "mirrors": [],
                "quality": play_info["data"]["quality"],
                "height": video_quality_map[play_info["data"]["quality"]]["height"],
                "width": video_quality_map[play_info["data"]["quality"]]["width"],
                "size": play_info["data"]["durl"][0]["size"],
                "type": "mp4_container",
            }
        ]
    else:
        raise UnknownTypeError(type)


@export_api(route="/acg_video/subtitle")
def get_acg_video_subtitle(avid: str = "", bvid: str = "", cid: str = ""):
    if not (avid or bvid):
        raise ArgumentsError("avid", "bvid")
    subtitle_api = "https://api.bilibili.com/x/player.so?id=cid:{cid}&aid={avid}&bvid={bvid}"
    subtitle_url = subtitle_api.format(avid=avid, cid=cid, bvid=bvid)
    res = spider.get(subtitle_url)
    subtitles_info = json.loads(re.search(r"<subtitle>(.+)</subtitle>", res.text).group(1))
    return [
        # fmt: off
        {
            "lang": sub_info["lan_doc"],
            "lines": spider.get("https:" + sub_info["subtitle_url"]).json()["body"]
        }
        for sub_info in subtitles_info["subtitles"]
        # fmt: on
    ]

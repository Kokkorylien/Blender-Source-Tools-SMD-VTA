# Upstream provenance and modification record / 上游来源与修改记录

## Identity confirmed from this checkout / 本地源码可确认的信息

| Field / 项目 | Recorded value / 记录 |
| --- | --- |
| Original project / 原项目 | Blender Source Tools |
| Blender add-on module / 插件模块 | io_scene_valvesource |
| Base version in metadata / 原始版本信息 | 3.2.6 |
| Original author / 原作者 | Tom Edwards |
| Translator named in metadata / 版本信息署名译者 | Grigory Revzin |
| Original copyright notice / 原版权声明 | Copyright (c) 2014 Tom Edwards contact@steamreview.org |
| Main source license / 主体源码许可 | GNU GPL version 2 or, at the recipient's option, any later version |
| Modification maintainer / 改造维护者 | Kokkorylien |
| Modification record date / 本次修改记录日期 | 2026-10-25 |
| Target Blender version / 目标 Blender 版本 | 4.0.2 |

These identities are transcribed from the bundled source and this edition's maintenance information. They are not a complete reconstruction of every upstream contributor.

以上信息来自随附源码及本增强版的维护信息，不代表已重建完整的上游贡献者名单。

## Upstream references / 上游参考链接

- [Official website / 官网](http://steamreview.org/BlenderSourceTools/)
- [Version archives / 历史版本下载](http://steamreview.org/BlenderSourceTools/archives/)
- [News and changelog / 新闻与更新日志](https://steamcommunity.com/groups/BlenderSourceTools/announcements)

On 2026-10-25, a reference copy of the official 3.2.6 archive was retrieved through the version archives page:

| Reference archive field / 参考归档项目 | Value / 记录 |
| --- | --- |
| Download URL / 下载地址 | http://steamreview.org/BlenderSourceTools/download.php?v=3.2.6 |
| Server-provided filename / 服务端文件名 | blender_source_tools_3.2.6.zip |
| SHA-256 | 410d16122da367270163dd7d41cd570d04b0b90f13ae7b74a1a34884a867ff69 |
| Contents / 内容 | 10 Python source files under io_scene_valvesource/ |

The unchanged datamodel.py, flex.py and ordered_set.py match that archive byte for byte. The seven files listed below differ from it. The archive is the recorded reference baseline; the modified checkout did not retain its original download history, so this does not establish which download was originally used. No upstream Git commit has been identified.

The local publication repository starts with a present-day import of those ten official archive files, followed by this edition's changes. It does not reconstruct the upstream Git history or claim to be a GitHub fork. The relationship to any official GitHub repository remains unverified.

2026-10-25 已通过官网历史版本页面取得上表中的 3.2.6 参考归档。未改动的 datamodel.py、flex.py、ordered_set.py 与归档逐字节一致；下列七个文件存在差异。该归档作为可追溯的参考基线，不能据此恢复工作区最初下载记录，当前也没有确认对应的上游 Git 提交。

本地发布仓库先以当前日期导入官方归档的十个源码文件，再提交增强版改动，不虚构上游 Git 历史，也不声称通过 GitHub Fork 创建。与官方 GitHub 仓库的对应关系仍未核实。

## Modified source files / 已知改造文件

The following files contain this edition's workflow changes. Their modification notices are dated 2026-10-25; this is a documentation date for the current modified state, not a reconstructed history of earlier work.

以下文件包含本增强版的工作流改动。文件内修改声明的日期为 2026-10-25，用于标记当前改造状态，不虚构更早的逐次修改历史。

| File / 文件 | Changes / 改动 |
| --- | --- |
| __init__.py | Per-exportable modes, VTA range/normal options, scene confirmation and batch settings, independent export list targeting / 导出模式、形态键范围与法线选项、场景确认和批量设置、列表独立定位 |
| export_smd.py | SMD-only baking policy, VTA-only output, range-limited baking, preflight confirmation, optional reuse of base normals / 仅 SMD 跳过形态烘焙、仅 VTA 输出、按范围烘焙、导出前确认、可选沿用基础法线 |
| GUI.py | Selected exportable settings, batch controls, row summaries, range and confirmation controls / 所选导出项配置、批量设置、行内摘要、范围与确认选项 |
| utils.py | Membership-based selection, hidden and Outliner selection handling, list target persistence, shape range resolution, armature animation targeting / 按归属解析选择、隐藏物体与大纲视图选择、列表定位保持、形态键范围、骨架动画定位 |
| translations.py | Simplified Chinese interface strings, descriptions and messages / 简体中文界面、悬停说明及消息 |
| import_smd.py | Translatable import options and warning messages / 将导入选项与警告消息接入翻译 |
| update.py | Open this edition's GitHub releases for manual updates / 改为打开本增强版 GitHub 发行页，供用户手动更新 |

README files, this provenance record, and the release guidance were added for this edition. Existing original source copyright and license headers are preserved. The program follows GPL-2.0-or-later, with the separately identified MIT-licensed modules retaining their own notices.

本增强版新增 README、来源记录及发布说明。原有源码版权与许可头部予以保留；程序沿用 GPL-2.0-or-later，另行标明的 MIT 模块保留其自身声明。

## Further provenance / 后续来源追溯

If an official source repository is verified, record the matching tag or commit here. Preserve any extra author and third-party license notices recovered during that comparison.

确认官方源码仓库后，可补充对应标签或提交号；比对中发现的额外作者与第三方许可声明也应保留。


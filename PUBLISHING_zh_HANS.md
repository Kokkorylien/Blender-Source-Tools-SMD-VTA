# GitHub 发布建议

这份说明面向本增强版的维护者。面向使用者的介绍见 [README_zh_HANS.md](README_zh_HANS.md)，英文版见 [README.md](README.md)。

## 仓库形式

GitHub 的 Fork 按钮不是修改、分发 GPL 软件的前提。能够确认官方 GitHub 仓库时，优先从官方仓库 Fork，便于保留历史与追踪上游；原始来源是官网 ZIP 时，也可以建立独立仓库，并清楚声明来源和非官方衍生关系。

一个可供核验的 GitHub 线索是 [Artfunkel/BlenderSourceTools](https://github.com/Artfunkel/BlenderSourceTools)。尚未核实该仓库与当前代码、3.2.6 原始归档的精确对应关系，因此未将它写成当前代码的已确认精确来源。应先由官网链接或作者身份确认其上游关系，再决定是否 Fork。

独立仓库可使用例如 **Blender-Source-Tools-SMD-VTA** 的名称，并在简介中明确写出“Unofficial Blender Source Tools modification for SMD/VTA workflows; Blender 4.0.2”。保留插件模块名 io_scene_valvesource，便于沿用已有工程设置。

## 许可证

现有主插件文件明确允许使用 GNU GPL 第 2 版或任意后续版本。此增强版沿用 **GPL-2.0-or-later**，并随源码附上 [LICENSE](LICENSE) 中的 GPL v2 全文。

分发时应做到：

1. 保留原作者版权、许可与无担保声明。
2. 在修改过的源码文件中显著标明修改事实和日期；本次已为七个经参考归档比对确认的改造文件加入声明，并在 [UPSTREAM.md](UPSTREAM.md) 记录范围。
3. 用 GPL-2.0-or-later 分发主插件改造，并向接收者提供对应的完整可修改源码。本插件以 Python 源码 ZIP 分发时，应保留 .py 文件，且与 Release 所对应的标签内容一致。
4. 随安装包提供许可证及第三方声明，保留 MIT 模块自己的署名和许可。
5. 不额外附加“禁止商用”“禁止修改”“禁止再分发”等与 GPL 授予的权利冲突的限制。

无需为了公开 GPL 允许的修改版而先取得一次额外的单独授权；应准确履行现有许可条件。这里采用的是源码明确给出的 GPL-2.0-or-later，不套用 Capsule 仓库的 GPL v3 声明。

## 作者与来源

README 已分开标明：

- 原插件：Blender Source Tools，Tom Edwards。
- 原版本信息署名译者：Grigory Revzin。
- 本增强版改造维护者：Kokkorylien。
- 其他上游贡献者及第三方模块：按既有声明保留。

不要把原作者署名整体替换为改造维护者，也不要将“独立维护”写成“官方维护”或暗示原作者已经认可本项目。

现有源码版本信息为 3.2.6。已从官网历史归档取得参考 ZIP，并在 UPSTREAM.md 记录文件名、下载地址和 SHA-256；三个未改动文件逐字节一致。该参考包不等于工作区最初下载记录，上游 Git 提交仍未确认。

如能取得原始包，可先提交未修改的上游源码，再用后续提交记录增强版改动。无法恢复原始包时，首个提交应如实标明为已经修改的导入，并保留 UPSTREAM.md 中的来源限制，不伪造上游历史。

ordered_set.py 的现有头部仅给出 MIT 许可与配方来源，未提供完整版权所有者名单。官方 3.2.6 参考归档中的文件完全相同，且未附额外许可文件；已在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 如实记录。

## 版本与更新渠道

为增强版采用能区分上游的标签，例如 **v3.2.6-kokkorylien.1**；发布说明同时列出基础版本 3.2.6 和本增强版的变化。

更新按钮现已改为打开本增强版的 GitHub Releases 页面，供用户手动下载和安装，不再自动下载或解压上游包。插件帮助与问题反馈链接也已指向本增强版仓库；原作者署名继续保留。

QC 功能及格式无需因发布而改动。README 已说明 QC 帧编号由用户自行维护。

## 安装包与仓库内容

可将 io_scene_valvesource 目录内的内容作为独立仓库根目录，使两份 README 直接显示在 GitHub 上；也可以把代码放在仓库的同名子目录，但需要相应调整文档位置和相对链接。

为用户提供的安装 ZIP 应使用以下结构：

~~~text
io_scene_valvesource/
    __init__.py
    GUI.py
    export_smd.py
    utils.py
    ...其他随附 Python 源码
    README.md
    README_zh_HANS.md
    LICENSE
    THIRD_PARTY_NOTICES.md
    UPSTREAM.md
~~~

GitHub 自动生成的 Source code ZIP 主要用于源码快照。Release 另外上传采用上述结构的插件安装包，可使安装路径和模块名保持明确。

只纳入插件源码、文档和所需许可证。工作区中的 Capsule、发布工具目录、Deploy Key、SSH 包装器配置、原始工程、临时测试日志和缓存均不属于这个插件的公开内容。

## Deploy Key 与推送工具

现有 .capsule-tools 的 Deploy Key 绑定的是 Blender-GLBExporter-Capsule，脚本也会镜像 Capsule 目录。直接运行该脚本将更新 Capsule 仓库。

新插件应另建独立克隆、独立发布工具目录和新仓库专用 Deploy Key，并固定源目录、目标仓库及分支。GitHub Deploy Key 按仓库授权，同一把 Deploy Key 不能作为多个仓库的专用密钥重复添加。不要复制、提交或在文档中写入现有私钥。

本工作区已另行准备 `.valvesource-tools/push-valvesource.cmd`、原生 OpenSSH 配置和独立密钥，固定推送 `Kokkorylien/Blender-Source-Tools-SMD-VTA` 的 `main` 分支，并核对远端 SHA。维护者需先创建空仓库，再把专用公钥加入该仓库的 Deploy keys，勾选 Allow write access；私钥仅保留本机，不属于公开源码。

首次发布使用 `push-valvesource.cmd -Tag v3.2.6-kokkorylien.1`。推送版本标签后，`.github/workflows/release.yml` 使用仓库自带的短期 GITHUB_TOKEN，打包十五个公开插件文件，创建 Release 并上传安装 ZIP 与 SHA-256；无需另行配置个人访问令牌。仓库需启用 GitHub Actions。发布后应检查 Actions 结果、Release 安装包及远端提交，不将成功推送等同于发行版已完成。


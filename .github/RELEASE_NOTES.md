# SMD/VTA Workflow Edition — v3.2.6-ko.1

Unofficial Blender Source Tools 3.2.6 modification by Kokkorylien, targeting **Blender 4.0.2**.

- Choose SMD + VTA, SMD only, or VTA only per exportable. SMD only skips shape key baking while keeping shape keys in the project.
- Export a shape key range with Basis at frame 0; confirm large VTA exports before baking; optionally reuse base normals.
- Configure the selected exportable, apply settings in batches, and see settings in the export list. List clicks preserve scene selection; hidden meshes and same-name objects/collections resolve correctly.
- Access armature animation exports from ordinary and nested collections.
- Simplified Chinese interface and tooltips. The update button opens this edition's releases for manual installation.

**Install:** download `io_scene_valvesource.zip`, then use Blender's **Edit → Preferences → Add-ons → Install**. Disable any existing Blender Source Tools installation first. Both editions use the same module name. The automatic GitHub source archives are not the prepared installation package.

QC frame references remain the user's responsibility. VTA-only export requires a matching mesh SMD. Skip Shape Normals retains the VTA normal columns and reuses base normals.

Original author: Tom Edwards; upstream metadata translator: Grigory Revzin. GPL-2.0-or-later; bundled MIT modules retain their notices. See README, LICENSE, THIRD_PARTY_NOTICES and UPSTREAM for details.

Validation includes Blender 4.0.2 registration, selection/configuration regression checks and actual skeletal animation SMD output. These checks do not establish compatibility with other Blender versions.

---

由 Kokkorylien 维护的非官方 Blender Source Tools 3.2.6 增强版，目标版本为 **Blender 4.0.2**。

- 每个导出项独立选择 SMD+VTA、仅 SMD 或仅 VTA。仅 SMD 会跳过形态键烘焙，同时保留工程中的形态键。
- 指定首尾形态键，Basis 固定为第 0 帧；大型 VTA 在烘焙前确认；可选沿用基础法线。
- 快速调整所选导出项、批量应用配置、列表显示配置。点击列表不改变场景选择，正确处理隐藏物体及物体/集合同名情况。
- 普通或嵌套集合中的骨架也能直接选择动画导出项。
- 简体中文界面与悬停说明。更新按钮改为打开本增强版发行页面，供用户手动安装。

**安装：**下载 `io_scene_valvesource.zip`，在 Blender 的**编辑 → 偏好设置 → 插件 → 安装**中选择它。请先禁用已有 Blender Source Tools；两者模块名相同。GitHub 自动生成的源码归档不是整理好的插件安装包。

QC 帧引用仍由用户自行维护。仅 VTA 导出需搭配几何及顶点顺序匹配的 SMD。“忽略形态键法线”仍保留格式要求的法线列，并沿用基础法线。

原作者 Tom Edwards，原版本信息署名译者 Grigory Revzin。主体使用 GPL-2.0-or-later，随附 MIT 模块保留自身声明；详见两版 README、LICENSE、THIRD_PARTY_NOTICES 和 UPSTREAM。

已在 Blender 4.0.2 验证插件注册、选择及配置回归检查和真实骨架动画 SMD 输出；不据此声明其他 Blender 版本的兼容性。

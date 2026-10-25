#coding=utf-8
# Modified by Kokkorylien, 2026-10-25: Simplified Chinese interface strings,
# descriptions, messages, and SMD/VTA workflow terminology.
# This modified program is distributed under GPL-2.0-or-later; see LICENSE.

_languages = ['ru', 'ja']

_data = {
'vca_sequence': {
	'ja': "シクウェンスを生成します",
	'en': "Generate Sequence",
	'ru': "Создать анимацию",
},
'controllers_simple_tip': {
	'en': "Generate one flex controller per shape key",
	'ru': "Создавать по контроллеру на каждый ключ формы",
},
'vertmap_group_props': {
	'en': "Vertex Maps",
},
'action_selection_filter_tip': {
	'en': "All actions that match the armature's filter term and have users",
	'ru': "Все действия, которые подходят под фильтр имён действий и где-либо используются",
},
'curve_poly_side_fwd': {
	'en': "Forward (outer) side",
	'ru': "Внешняя сторона",
},
'action_selection_current_tip': {
	'en': "The armature's currently assigned action or NLA tracks",
	'ru': "Текущее действие (или нелинейная анимация) скелета",
},
'valvesource_cloth_enable': {
	'en': "Cloth Physics Enable",
},
'subdir_tip': {
	'en': "Optional path relative to scene output folder",
	'ru': "Куда экспортировать? (Необязательно; по умолчанию экспортируется в ту же папку, где находится .blend-файл) ",
},
'controllers_mode': {
	'ja': "DMXフレックスのコントローラー生成",
	'en': "DMX Flex Controller generation",
	'ru': "Генерация контроллеров лицевой анимации (DMX)",
},
'scene_export': {
	'ja': "シーンをエクスポート",
	'en': "Scene Export",
	'ru': "Экспорт всей сцены",
},
'shape_stereo_mode_tip': {
	'en': "How stereo split balance should be defined",
	'ru': "Способ разделения объекта на левую и правую части для стерео-контроллеров",
},
'bone_rot_legacy': {
	'en': "Legacy rotation",
	'ru': "Обратная совместимость вращения костей",
},
'controllers_advanced_tip': {
	'en': "Insert the flex controllers of an existing DMX file",
	'ru': "Вставить блок контроллеров лицевой анимации",
},
'triangulate_tip': {
	'en': "Avoids concave DMX faces, which are not supported by Source",
	'ru': "Избегать вогнутых полигонов в DMX-файлах (не поддерживается studiomdl)",
},
'action_filter': {
	'ja': "アクションフィルター",
	'en': "Action Filter",
	'ru': "Фильтр действий",
},
'vca_start_tip': {
	'en': "Scene frame at which to start recording Vertex Animation",
	'ru': "Кадр в сцене, с которого следует начать запись вершинной анимации",
},
'action_filter_tip': {
	'en': "Actions with names matching this filter pattern and which have users will be exported",
	'ru': "Будут эксортированы только те действия, имена которых подходят под этот фильтр, и которые где-либо используются",
},
'shape_stereo_sharpness_tip': {
	'en': "How sharply stereo flex shapes should transition from left to right",
	'ru': "Насколько резко будет осуществляться переход между левой и правой частью объекта",
},
'vca_sequence_tip': {
	'en': "On export, generate an animation sequence that drives this Vertex Animation",
	'ru': "При экспорте автоматически создать sequence, управляющий этой вершинной анимацией",
},
'shape_stereo_mode': {
	'en': "DMX stereo split mode",
	'ru': "Разделение на левую и правую части для стерео-контрлолеров (DMX)",
},
'dummy_bone': {
	'en': "Implicit motionless bone",
	'ru': "\"Пустая\" недвижимая кость",
},
'vca_group_props': {
	'ja': "頂点アニメーション",
	'en': "Vertex Animation",
	'ru': "Вершинная анимация",
},
'curve_poly_side': {
	'ja': "ポリゴン生成",
	'en': "Polygon Generation",
	'ru': "Генерация геометрии",
},
'group_merge_mech': {
	'ja': "メカニカルな局部は結合",
	'en': "Merge mechanical parts",
	'ru': "Слить вместе механические части",
},
'action_selection_mode_tip': {
	'en': "How actions are selected for export",
	'ru': "Какие действия экспортировать?",
},
'use_scene_export_tip': {
	'en': "Export this item with the scene",
	'ru': "Экспортировать этот объект при экспорте сцены",
},
'curve_poly_side_back': {
	'en': "Backward (inner) side",
	'ru': "Внутренняя сторона",
},
'valvesource_vertex_blend': {
	'en': "Blend Params RGB",
},
'bone_rot_legacy_tip': {
	'en': "Remaps the Y axis of bones in this armature to Z, for backwards compatibility with old imports (SMD only)",
	'ru': "Переназначить Y-ось всех костей в Z-ось для обратной совместимости с старыми импортами",
},
'controller_source': {
	'ja': "DMXフレックスのコントローラーのソースファイル ",
	'en': "DMX Flex Controller source",
	'ru': "Файл контроллеров лицевой анимации (DMX)",
},
'group_suppress_tip': {
	'en': "Export this group's objects individually",
	'ru': "Экспортировать объекты этой группы по отдельности",
},
'action_selection_current': {
	'ja': "現在 / NLA",
	'en': "Current / NLA",
	'ru': "Текущее действие / Нелинейная анимация",
},
'shape_stereo_sharpness': {
	'en': "DMX stereo split sharpness",
	'ru': "Резкость разделения в стерео-контроллерах",
},
'group_suppress': {
	'ja': "ミュート",
	'en': "Suppress",
	'ru': "\"Пересиливание\"",
},
'shape_stereo_vgroup': {
	'en': "DMX stereo split vertex group",
	'ru': "Группа вешин разделения для стерео-контроллеров",
},
'shape_stereo_vgroup_tip': {
	'en': "The vertex group that defines stereo balance (0=Left, 1=Right)",
	'ru': "Группа вершин для автоматического деления ключей формы на левую и правую часть. 0 = Левая часть, 1 = Правая часть.",
},
'controllers_source_tip': {
	'en': "A DMX file (or Text datablock) containing flex controllers",
	'ru': "DMX-файл или внутренний текст в Blender, содержащий настройки контроллеров лицевой анимации",
},
'valvesource_vertex_blend1': {
	'en': "Blend Params Extra (?)",
},
'curve_poly_side_tip': {
	'en': "Determines which side(s) of this curve will generate polygons when exported",
	'ru': "Указывает, какая сторона (стороны) выделенной кривой будет использоваться для генерации геометрии",
},
'triangulate': {
	'ja': "三角測量",
	'en': "Triangulate",
	'ru': "Преобразовывать все многоугольники в треугольники",
},
'curve_poly_side_both': {
	'en': "Both sides",
	'ru': "Обе стороны",
},
'group_merge_mech_tip': {
	'en': "Optimises DMX export of meshes sharing the same parent bone",
	'ru': "Оптимизиция экспорт объектов, имеющих общих родителей",
},
'action_selection_mode': {
	'en': "Action Selection",
	'ru': "Выбор действия",
},
'shape_stereo_mode_vgroup': {
	'en': "Use a vertex group to define stereo balance",
	'ru': "Использовать группу вершин для разделения стерео-контроллеров",
},
'vca_end_tip': {
	'en': "Scene frame at which to stop recording Vertex Animation",
	'ru': "Кадр в сцене, которым следует закончить запись вершинной анимации",
},
'valvesource_vertex_paint': {
	'en': "Vertex Paint",
},
'controllers_mode_tip': {
	'en': "How flex controllers are defined",
	'ru': "Способ задания контроллеров лицевой анимации",
},
'subdir': {
	'en': "Subfolder",
	'ru': "Подпапка",
},
'dummy_bone_tip': {
	'en': "Create a dummy bone for vertices which don't move. Emulates Blender's behaviour in Source, but may break compatibility with existing files (SMD only)",
	'ru': "Создать кость и привязать к ней вершины, которые не двигаются. (Только SMD.)",
},
'exportpanel_steam': {
	'ja': "Steam コミュニティ",
	'en': "Steam Community",
	'ru': "Сообщество Steam",
},
'exportables_arm_filter_result': {
	'ja': "「{0}」アクション～{1}",
	'en': "\"{0}\" actions ({1})",
	'ru': "Фильтр имён действий \"{0}\" на скелете {1}",
},
'exportables_flex_count_corrective': {
	'ja': "是正シェイプ：{0}",
	'en': "Corrective Shapes: {0}",
	'ru': "Ключей форм коррекции: {0}",
},
'exportables_curve_polyside': {
	'ja': "ポリゴン生成：",
	'en': "Polygon Generation:",
	'ru': "Генерация геометрии:",
},
'exportmenu_title': {
	'ja': "Source Tools エクスポート",
	'en': "Source Tools Export",
	'ru': "Экспорт в Source",
},
'exportables_flex_help': {
	'ja': "フレックス・コントローラーのヘレプ",
	'en': "Flex Controller Help",
	'ru': "Помощь по контроллерам лицевой анимации",
},
'exportpanel_title': {
	'ja': "Source Engine エクスポート",
	'en': "Source Engine Export",
	'ru': "Экспорт в Source",
},
'exportables_flex_src': {
	'ja': "コントローラーのソースファイル ",
	'en': "Controller Source",
	'ru': "Файл настроек контроллеров",
},
'exportmenu_invalid': {
	'en': "Cannot export selection",
	'ru': "Выделенный объект невозможно экспортировать",
},
'qc_title': {
	'ja': "Source Engine QCのコンパイル",
	'en': "Source Engine QC Compiles",
	'ru': "Компиляция QC",
},
'exportables_flex_props': {
	'ja': "フレックスのプロパティ",
	'en': "Flex Properties",
	'ru': "Свойства контроллеров лицевой анимации",
},
'exportables_flex_generate': {
	'ja': "コントローラーを生成します",
	'en': "Generate Controllers",
	'ru': "Сгенерировать контроллеры",
},
'exportables_flex_split': {
	'ja': "ステレオフルックスの差額：",
	'en': "Stereo Flex Balance:",
	'ru': "Разделение на правую и левую часть:",
},
'exportables_group_mute_suffix': {
	'ja': "(ミユト)",
	'en': "(suppressed)",
	'ru': "(игнорируется)",
},
'exportmenu_scene': {
	'ja': "シーンをエクスポート ({0}つファイル)",
	'en': "Scene export ({0} files)",
	'ru': "Экспорт {0} файлов",
},
'exportpanel_dmxver': {
	'ja': "DMXのバージョン：",
	'en': "DMX Version:",
	'ru': "Версия DMX:",
},
'exportpanel_update': {
	'en': "Workflow Edition Releases",
},
'exportables_title': {
	'ja': "Source Engineのエクスポート可能",
	'en': "Source Engine Exportables",
	'ru': "Объекты для Source",
},
'exportables_armature_props': {
	'ja': "アーマティアのプロパティ",
	'en': "Armature Properties ({0})",
	'ru': "Свойства скелета ({0})",
},
'qc_bad_enginepath': {
	'ja': "エンジンのパスが無効です",
	'en': "Invalid Engine Path",
	'ru': "Некорректный путь до папки bin",
},
'qc_invalid_source2': {
	'ja': "Source Engine 2はQCファイルが使いません",
	'en': "QC files do not exist in Source 2",
	'ru': "QC-файлы движком Source 2 не используются",
},
'exportmenu_selected': {
	'en': "Selected objects ({0} files)",
	'ru': "Выбранные объекты ({0} файлов)",
},
'exportables_group_props': {
	'ja': "グループのプロパティ",
	'en': "Group Properties",
	'ru': "Свойства групп",
},
'qc_no_enginepath': {
	'ja': "エンジンのパスはありません",
	'en': "No Engine Path provided",
	'ru': "Не указан путь до папки bin",
},
'exportables_curve_props': {
	'ja': "カーブのプロパティ",
	'en': "Curve Properties",
	'ru': "Свойства сплайна",
},
'exportables_flex_count': {
	'ja': "シェイプ：{0}",
	'en': "Shapes: {0}",
	'ru': "Ключей формы: {0}",
},
'bl_info_author': {
	'ja': "トム・エドワーズ～グリゴリ・レヴジン",
	'en': "Tom Edwards (translators: Grigory Revzin)",
	'ru': "Том Эдвардс (переводили: Григорий Ревзин)",
},
'activate_dependency_shapes': {
	'en': "Activate dependency shapes",
	'ru': "Активировать зависимые ключи формы",
},
'settings_prop': {
	'en': "Blender Source Tools settings",
	'ru': "Настройки Blender Source Tools",
},
'bl_info_description': {
	'en': "Importer and exporter for Valve Software's Source Engine. Supports SMD\\VTA, DMX and QC.",
	'ru': "Экспорт и импорт для движка Source. Поддерживаемые форматы: SMD/VTA, DMX, QC.",
},
'export_menuitem': {
	'en': "Source Engine (.smd, .vta, .dmx)",
	'ru': "Движок Source (.smd, .vta, .dmx)",
},
'help': {
	'ja': "ヘレプ",
	'en': "Help",
	'ru': "Помощь",
},
'bl_info_location': {
	'ja': "ファイル > インポート / エクスポート、シーンのプロパティ",
	'en': "File > Import/Export, Scene properties",
	'ru': "Файл > Импортировать/Экспортировать, свойства сцены",
},
'import_menuitem': {
	'en': "Source Engine (.smd, .vta, .dmx, .qc)",
	'ru': "Движок Source (.smd, .vta, .dmx, .qc)",
},
'exporter_err_nogroupitems': {
	'en': "Nothing in Group \"{0}\" is enabled for export",
},
'exporter_report_qc': {
	'en': "{0} files exported and {2} QCs compiled ({3}/{4}) in {1} seconds",
	'ru': "Экспортировано файлов: {0}. Скомпилировано QC-файлов: {2} (движок {3}, мод {4}). Прошло секунд: {1};",
},
'exporter_err_relativeunsaved': {
	'en': "Cannot export to a relative path until the blend file has been saved.",
	'ru': "Невозможно экспортировать по относительному пути, пока файл .blend не сохранён.",
},
'exporter_err_nopolys': {
	'en': "Object {0} has no polygons, skipping",
	'ru': "Пропуск объекта {0}: нет геометрии",
},
'exporter_err_hidden': {
	'en': "Skipping {0}: object cannot be selected, probably due to being hidden by an animation driver.",
},
'exporter_err_arm_nonuniform': {
	'en': "Armature \"{0}\" has non-uniform scale. Mesh deformation in Source will differ from Blender.",
	'ru': "Скелет {0} масштабирован непропорционально. В движке Source скелет будет работать неправильно.",
},
'exporter_err_facesnotex_ormat': {
	'en': "{0} faces on {1} did not have a Material or Texture assigned",
	'ru': "{0} полигонам на {1} не присвоен ни материал, ни текстура",
},
'exporter_err_arm_noanims': {
	'en': "Couldn't find any animation for Armature \"{0}\"",
	'ru': "Нет анимации для скелета {0}",
},
'exporter_err_dupeenv_arm': {
	'en': "Armature modifier \"{0}\" found on \"{1}\", which already has a bone parent or constraint. Ignoring.",
	'ru': "Пропуск модификатора \"Скелет\" ({0}) на объекте {1}: он уже имеет кость-родителя или ограничение",
},
'exporter_err_bonelimit': {
	'en': "Exported {0} bones, but SMD only supports {1}!",
	'ru': "Экспортировано {0} костей, но SMD поддерживает только {1}!",
},
'exporter_err_unmergable': {
	'en': "Skipping vertex animations on Group \"{0}\", which could not be merged into a single DMX object due to its envelope. To fix this, either ensure that the entire Group has the same bone parent or remove all envelopes.",
	'ru': "Пропуск вершинной анимации для группы «{0}», которую не удаётся слить в DMX-модель из-за огибающих. Проверьте, что у всей группы одна и та же кость-родитель или удалите все огибающие.",
},
'exporter_warn_source2names': {
	'en': "Consider renaming \"{0}\": in Source 2, model names can contain only lower-case characters, digits, and/or underscores.",
},
'exporter_warn_unicode': {
	'ja': "{0}「{1}」の名前はUnicode文字を含みます。間違ってコンパイルすることが可能です。",
	'en': "Name of {0} \"{1}\" contains Unicode characters. This may not compile correctly!",
},
'exporter_err_flexctrl_loadfail': {
	'en': "Could not load flex controllers. Python reports: {0}",
	'ru': "Загрузить контроллеры из указанного DMX-файла не удалось. Ошибка Python: {0}",
},
'qc_compile_err_nofiles': {
	'en': "Cannot compile, no QCs provided. The Blender Source Tools do not generate QCs.",
	'ru': "Нет QC-файлов, нечего компилировать. Blender Source Tools не генерируют QC-файлы.",
},
'exporter_err_missing_corrective_target': {
	'en': "Found corrective shape key \"{0}\", but not target shape \"{1}\"",
},
'qc_compile_complete': {
	'ja': "{0}つ「{1}」QCがコンパイルしました",
	'en': "Compiled {0} {1} QCs",
	'ru': "Скомпилировано {0} QC для движка {1}.",
},
'exporter_err_shapes_decimate': {
	'en': "Cannot export shape keys from \"{0}\" because it has a '{1}' Decimate modifier. Only Un-Subdivide mode is supported.",
	'ru': "Невзможно экспортировать ключи формы для {0}, потому что активен модификатор \"Аппроксимация\" в режиме {1}. Поддерживается только режим \"Снять подразделение\"",
},
'exporterr_goldsrc_multiweights': {
	'en': "{0} verts on \"{1}\" have multiple weight links. GoldSrc does not support this!",
},
'exporter_err_splitvgroup_undefined': {
	'en': "Object \"{0}\" uses Vertex Group stereo split, but does not define a Vertex Group to use.",
	'ru': "На объекте {0} задан режим стерео-разделения по группе вершин, но не задана группа вершин.",
},
'exporter_err_open': {
	'en': "Could not create {0} file. Python reports: {1}.",
	'ru': "Не удалось создать файл {0}. Ошибка Python: {1}",
},
'qc_compile_title': {
	'ja': "QCコンパイル",
	'en': "Compile QC",
	'ru': "Скомпилировать QC-файл",
},
'exporter_err_noexportables': {
	'en': "Found no valid objects for export",
	'ru': "Не найдено подходящих для экспорта объектов",
},
'exporter_warn_sanitised_filename': {
	'en': "Sanitised exportable name \"{0}\" to \"{1}\"",
},
'exporter_warn_correctiveshape_duplicate': {
	'en': "Corrective shape key \"{0}\" has the same activation conditions ({1}) as \"{2}\". Skipping.",
},
'exporter_err_flexctrl_missing': {
	'en': "No flex controller defined for shape {0}.",
	'ru': "Для ключа формы {0} не задано ни одного контроллера",
},
'qc_compile_err_compiler': {
	'en': "Could not execute studiomdl from \"{0}\"",
	'ru': "Не удалось запустить studiomdl, проверьте путь: {1}",
},
'exporter_err_facesnotex': {
	'en': "{0} faces on {1} did not have a Texture assigned",
	'ru': "Для {0} граней на объекте {1} не задана текстура",
},
'exporter_err_flexctrl_undefined': {
	'en': "Could not find flex controllers for \"{0}\"",
	'ru': "Не удалось найти контроллеры лицевой анимации для объекта {0}",
},
'exporter_warn_source2smdsupport': {
	'en': "Source 2 no longer supports SMD.",
},
'exporter_tip': {
	'en': "Export and compile Source Engine models",
	'ru': "Экспортирует и компилирует модели для движка Source",
},
'exporter_warn_weightlinks_culled': {
	'en': "{0} excess weight links beneath scene threshold of {1:0.2} culled on \"{2}\".",
	'ru': "На «{2}» удалено {0} излишних привязок к костям: предел веса, заданный для сцены, {1:0.2}",
},
'exporter_prop_scene_tip': {
	'en': "Export all items selected in the Source Engine Exportables panel",
	'ru': "Экспортировать все объекты, заданные в панели \"Объекты для Source\"",
},
'exporter_err_dmxenc': {
	'en': "DMX format \"Model {0}\" requires DMX encoding \"Binary 3\" or later",
	'ru': "Формат DMX-файла \"Model {0}\" требует структуру DMX-файла не более старую, чем \"Binary 3\".",
},
'exporter_prop_group': {
	'ja': "グループの名前",
	'en': "Group Name",
	'ru': "Имя группы",
},
'qc_compile_tip': {
	'en': "Compile QCs with the Source SDK",
	'ru': "Компилирует QC-файлы с помощью studiomdl",
},
'exporter_report_suffix': {
	'en': " with {0} Errors and {1} Warnings",
	'ru': " ошибок: {0}, предупреждений: {1}.",
},
'exporter_err_groupempty': {
	'en': "Group {0} has no active objects",
	'ru': "В группе {0} нет активных объектов",
},
'exporter_err_dmxother': {
	'en': "Cannot export DMX. Resolve errors with the SOURCE ENGINE EXPORT panel in SCENE PROPERTIES.",
	'ru': "Невозможно экспортировать DMX-файлы. Проверьте панель \"Экспорт в Source\"",
},
'exporter_prop_group_tip': {
	'ja': "エクスポートにグループの名前",
	'en': "Name of the Group to export",
	'ru': "Имя группы для экспорта",
},
'exporter_warn_multiarmature': {
	'en': "Multiple armatures detected",
},
'exporter_err_solidifyinside': {
	'en': "Curve {0} has the Solidify modifier with rim fill, but is still exporting polys on both sides.",
	'ru': "На кривой {0} включён модификатор Объёмность с заполнением обода, однако всё равно экспортируется двусторонняя геометрия",
},
'exporter_err_dupeenv_con': {
	'en': "Bone constraint \"{0}\" found on \"{1}\", which already has a bone parent. Ignoring.",
	'ru': "Пропук ограничения кости {0}  на объекте {1}: для неё уже задана кость-родитель.",
},
'exporter_err_unconfigured': {
	'en': "Scene unconfigured. See the SOURCE ENGINE EXPORT panel in SCENE PROPERTIES.",
	'ru': "Требуется скофигурировать сцену для экспорта в Source. Проверьте панель \"Экcпорт в Source\"",
},
'exporter_err_makedirs': {
	'en': "Could not create export folder. Python reports: {0}",
	'ru': "Не удалось создать папку для экспорта. Ошибка Python: {0}",
},
'exporter_warn_weightlinks_excess': {
	'en': "{0} verts on \"{1}\" have over {2} weight links. Source does not support this!",
	'ru': "На «{1}» {0} вершин имеют привязку к более {2} костей. Source не поддерживает такое коилчество привязок.",
},
'exporter_err_noframes': {
	'en': "Armature {0} has no animation frames to export",
},
'exporter_report_menu': {
	'ja': "レポート：Source Tools エラー",
	'en': "Source Tools Error Report",
	'ru': "Отчёт о ошибках Source Tools",
},
'exporter_report': {
	'ja': "{0}つファイルは{1}秒エクスポート",
	'en': "{0} files exported in {1} seconds",
	'ru': "Файлов экспортировано: {0}. Прошло секунд: {1};",
},
'exporter_err_groupmuted': {
	'ja': "ゲルーポ「{0}」はミュートです",
	'en': "Group {0} is suppressed",
	'ru': "Свойства группы {0} \"пересилены\"",
},
'exporter_title': {
	'ja': "SMD/VTA/DMXをエクスポート",
	'en': "Export SMD/VTA/DMX",
	'ru': "Экспорт SMD/VTA/DMX",
},
'qc_compile_err_unknown': {
	'en': "Compile of {0} failed. Check the console for details",
	'ru': "Не удалось скомпилировать QC-файл {0}. Ошибка описана в консоли",
},
'exporter_err_splitvgroup_missing': {
	'en': "Could not find stereo split Vertex Group \"{0}\" on object \"{1}\"",
	'ru': "Не найдена группа веришн {0} для разделения на левую и правую части стерео-контроллеров на объекте {1}",
},
'importer_complete': {
	'en': "Imported {0} files in {1} seconds",
	'ru': "Импортировано файлов: {0}. Прошло секунд: {1}.",
},
'importer_bonemode': {
	'ja': "ボーンカスタムシェイプ",
	'en': "Bone shapes",
	'ru': "Отображение костей",
},
'importer_err_nofile': {
	'ja': "選択ファイルはありません",
	'en': "No file selected",
	'ru': "Файл не выбран",
},
'importer_err_smd': {
	'en': "Could not open SMD file \"{0}\": {1}",
	'ru': "Невозможно открыть файл {0}. Ошибка Python: {1}",
},
'importer_qc_macroskip': {
	'en': "Skipping macro in QC {0}",
	'ru': "Пропуск QC-команды в файле {0}",
},
'importer_bones_validate_desc': {
	'en': "Report new bones as missing without making any changes to the target Armature",
},
'importer_tip': {
	'en': "Imports uncompiled Source Engine model data",
	'ru': "Импортирует промежуточные файлы Source",
},
'importer_title': {
	'ja': "インポート SMD/VTA, DMX, QC",
	'en': "Import SMD/VTA, DMX, QC",
	'ru': "Импорт SMD/VTA, DMX, QC",
},
'importer_makecamera': {
	'ja': "$originにカメラを生成",
	'en': "Make Camera At $origin",
	'ru': "Создать камеру по координатам, указанным в $origin",
},
'importer_bone_parent_miss': {
	'en': "Parent mismatch for bone \"{0}\": \"{1}\" in Blender, \"{2}\" in {3}.",
	'ru': "Не совпадают родители у кости \"{0}\": \"{1}\" в Blender, \"{2}\" в файле \"{3}\".",
},
'importer_makecamera_tip': {
	'en': "For use in viewmodel editing; if not set, an Empty will be created instead",
	'ru': "Помогает в редактировании v_model-ов. Если не задано, будет создан пустой объект",
},
'importer_err_shapetarget': {
	'en': "Could not import shape keys: no valid target object found",
	'ru': "Невозможно импортировать ключи формы: не найден подходящий объект",
},
'importer_rotmode_tip': {
	'en': "Determines the type of rotation Keyframes created when importing bones or animation",
	'ru': "Задаёт тип создаваемых при экспорте ключевых кадров с вращением",
},
'importer_skipremdoubles_tip': {
	'en': "Import raw, disconnected polygons from SMD files; these are harder to edit but a closer match to the original mesh",
},
'importer_balance_group': {
	'en': "DMX Stereo Balance",
	'ru': "Разделение стерео-контроллеров",
},
'importer_bones_mode_desc': {
	'en': "How to behave when a reference mesh import introduces new bones to the target Armature (ignored for QCs)",
},
'importer_rotmode': {
	'ja': "回転モード",
	'en': "Rotation mode",
	'ru': "Способ задания вращения",
},
'importer_skipremdoubles': {
	'ja': "SMDのポリゴンと法線を保持",
	'en': "Preserve SMD Polygons & Normals",
},
'importer_bonemode_tip': {
	'en': "How bones in new Armatures should be displayed",
	'ru': "Как будут выглядеть кости в импортированном скелете?",
},
'importer_bones_append': {
	'ja': "対象で追加",
	'en': "Append to Target",
},
'importer_err_qci': {
	'en': "Could not open QC $include file \"{0}\" - skipping!",
	'ru': "Пропуск файла \"{0}\" из команды $include: не удалсь открыть.",
},
'importer_up_tip': {
	'en': "Which axis represents 'up' (ignored for QCs)",
	'ru': "Какая из осей соответствует направлению \"вврех\"?",
},
'importer_err_namelength': {
	'en': "{0} name \"{1}\" is too long to import. Truncating to \"{2}\"",
},
'importer_bones_append_desc': {
	'en': "Add new bones to the target Armature",
},
'importer_err_unmatched_mesh': {
	'en': "{0} VTA vertices ({1}%) were not matched to a mesh vertex! An object with a vertex group has been created to show where the VTA file's vertices are.",
	'ru': "{0} вершин ({1}%) не удалось привязать к объекту при импорте VTA. Создан объект с группой вершин, показывающей, где заданные в VTA вершины.",
},
'importer_bones_validate': {
	'ja': "対象で確認",
	'en': "Validate Against Target",
},
'importer_name_nomat': {
	'ja': "UndefinedMaterial",
	'en': "UndefinedMaterial",
	'ru': "UndefinedMaterial",
},
'importer_bones_newarm_desc': {
	'en': "Make a new Armature for this import",
},
'importer_err_refanim': {
	'en': "Found animation in reference mesh \"{0}\", ignoring!",
	'ru': "Пропуск анимации в файле с позой по умолчанию (\"{0}\")",
},
'importer_bones_mode': {
	'ja': "ボーンの追加がモード",
	'en': "Bone Append Mode",
},
'importer_err_badweights': {
	'en': "{0} vertices weighted to invalid bones on {1}",
	'ru': "{0} вершин привязаны к неверным костям на объекте {1}",
},
'importer_err_bonelimit_smd': {
	'en': "SMD only supports 128 bones!",
	'ru': "Движок SMD не поддерживает больше 128 костей!",
},
'importer_err_badfile': {
	'en': "Format of {0} not recognised",
	'ru': "Не распознан формат файла \"{0}\"",
},
'importer_err_smd_ver': {
	'en': "Unrecognised/invalid SMD file. Import will proceed, but may fail!",
	'ru': "Не удалось распознать SMD-файл. Импорт будет продолжен до первой ошибки.",
},
'importer_doanims': {
	'ja': "アニメーションをインポート",
	'en': "Import Animations",
	'ru': "Импортировать анимации",
},
'importer_use_collections':{
	'en': "Create Collections",	
},
'importer_use_collections_tip':{
	'en': "Create a Blender collection for each imported mesh file. This retains the original file structure (important for DMX) and makes it easy to switch between LODs etc. with the number keys",
},
'importer_err_missingbones': {
	'en': "{0} contains {1} bones not present in {2}. Check the console for a list.",
	'ru': "{1} костей из {0} не найдены в {2}.",
},
'importer_name_unmatchedvta': {
	'en': "Unmatched VTA",
	'ru': "Несопоставленные вершины VTA",
},
'importer_bones_newarm': {
	'ja': "アーマティアを生成",
	'en': "Make New Armature",
},
'qc_warn_noarmature': {
	'en': "Skipping {0}; no armature found.",
},
'exportstate_pattern_tip': {
	'en': "Visible objects with this string in their name will be affected",
	'ru': "Будут обработаны видимые объекты, содержащие в своём названии эту строку",
},
'exportstate': {
	'en': "Set Source Tools export state",
	'ru': "Задать состояние экспорта Source Tools",
},
'activate_dep_shapes': {
	'en': "Activate Dependency Shapes",
	'ru': "Активировать зависимые ключи формы",
},
'gen_block_success': {
	'en': "DMX written to text block \"{0}\"",
	'ru': "Настройки контроллеров лицевой анимации записаны в {0}",
},
'gen_block': {
	'ja': "DMXフレックスのコントローラーの抜粋を生成します",
	'en': "Generate DMX Flex Controller block",
	'ru': "Сгенерировать настройки контроллеров лицевой анимации",
},
'vca_add_tip': {
	'en': "Add a Vertex Animation to the active Source Tools exportable",
	'ru': "Добавить к текущему экспортируемому объекту Source Tools вершинную анимацию",
},
'insert_uuid': {
	'en': "Insert UUID",
	'ru': "Вставить UUID",
},
'launch_hlmv_tip': {
	'en': "Launches Half-Life Model Viewer",
	'ru': "Запускает просмотощик моделей Source, HLMV",
},
'vertmap_remove': {
	'en': "Remove Source 2 Vertex Map",
},
'activate_dep_shapes_tip': {
	'en': "Activates shapes found in the name of the current shape (underscore delimited)",
	'ru': "Активирует зависимые ключи формы  (ключи формы, которые можно найти в названии данного ключа, разделённые подчёркиванием)",
},
'vca_qcgen_tip': {
	'en': "Copies a QC segment for this object's Vertex Animations to the clipboard",
	'ru': "Создать в буфере обмена фрагмент QC-файла для управления текущей вершинной анимацией",
},
'vca_remove_tip': {
	'en': "Remove the active Vertex Animation from the active Source Tools exportable",
	'ru': "Удалить текущую вершинную анимацию с экспортируемого объекта Source Tools",
},
'vca_add': {
	'en': "Add Vertex Animation",
	'ru': "Добавить вершинную анимацию",
},
'vertmap_select': {
	'en': "Select Source 2 Vertex Map",
},
'vca_preview': {
	'ja': "頂点アニメーションを再生します",
	'en': "Preview Vertex Animation",
	'ru': "Предпросмотр вершинной анимации",
},
'activate_dep_shapes_success': {
	'en': "Activated {0} dependency shapes",
	'ru': "Активировано {0} зависимых ключей формы",
},
'launch_hlmv': {
	'ja': "HLMVを開始",
	'en': "Launch HLMV",
	'ru': "Запустить HLMV",
},
'exportstate_pattern': {
	'en': "Search pattern",
	'ru': "Маска поиска",
},
'insert_uuid_tip': {
	'en': "Inserts a random UUID at the current location",
	'ru': "Вставить новый UUID",
},
'gen_block_tip': {
	'en': "Generate a simple Flex Controller DMX block",
	'ru': "Генерирует простой блок контроллеров лицевой анимации, по контроллеру на один ключ формы",
},
'gen_drivers': {
	'ja': "是正シェイプキーのドライバーを生成します",
	'en': "Generate Corrective Shape Key Drivers",
	'ru': "Создать драйверы для ключей форм коррекции",
},
'apply_drivers':{
	'en': "Regenerate Shape Key Names From Drivers",
},
'apply_drivers_tip':{
	'en': "Renames corrective shape keys so that each their names are a combination of the shape keys that control them (via Blender animation drivers)",
},
'apply_drivers_success':{
	'en': "{0} shapes renamed.",
},
'vca_qcgen': {
	'ja': "QCの抜粋を生成します",
	'en': "Generate QC Segment",
	'ru': "Создать фрагмент QC-файла",
},
'vertmap_create': {
	'en': "Create Source 2 Vertex Map",
},
'vca_preview_tip': {
	'en': "Plays the active Source Tools Vertex Animation using scene preview settings",
	'ru': "Проигрывает текущую вершинную анимацию для предпросмотра",
},
'vca_remove': {
	'en': "Remove Vertex Animation",
	'ru': "Удалить текущую вершинную анимацию с экспортируемого объекта Source Tools",
},
'gen_drivers_tip': {
	'en': "Adds Blender animation drivers to corrective Source engine shapes",
	'ru': "Создаёт драйверы для ключей форм коррекции, использующихся в Source",
},
'qc_path': {
	'ja': "QCのパス",
	'en': "QC Path",
	'ru': "Путь до QC-файлов",
},
'engine_path': {
	'ja': "エンジンのパス",
	'en': "Engine Path",
	'ru': "Путь до папки bin движка",
},
'game_path_tip': {
	'en': "Directory containing gameinfo.txt (if unset, the system VPROJECT will be used)",
	'ru': "Путь до мода (где gameinfo.txt). Если не задано, то будет использована переменная среды VPROJECT",
},
'visible_only': {
	'ja': "たった可視のレイヤー",
	'en': "Visible layers only",
	'ru': "Только видимые слои",
},
'dmx_encoding': {
	'ja': "DMXの符号化",
	'en': "DMX encoding",
	'ru': "Способ кодирования DMX-файла",
},
'game_path': {
	'ja': "ゲームのパス",
	'en': "Game Path",
	'ru': "Путь до мода",
},
'up_axis': {
	'ja': "対象の上昇軸",
	'en': "Target Up Axis",
	'ru': "Направление \"Вверх\"",
},
'dmx_format': {
	'ja': "DMXのフォーマット",
	'en': "DMX format",
	'ru': "Формат DMX-файла",
},
'ignore_materials': {
	'ja': "Blenderのマテリアルを軽視",
	'en': "Ignore Blender Materials",
	'ru': "Игнорировать материалы Blender",
},
'visible_only_tip': {
	'en': "Ignore objects in hidden layers",
	'ru': "Не экспортировать объекты, расположенные на выключенных слоях",
},
'active_exportable': {
	'ja': "アクティブ・エクスポート可能",
	'en': "Active exportable",
	'ru': "Активный объект для экспорта",
},
'exportroot_tip': {
	'en': "The root folder into which SMD and DMX exports from this scene are written",
	'ru': "Папка, куда будут экспортироваться SMD и DMX из текущей сцены",
},
'qc_compilenow': {
	'ja': "今全てはコンパイル",
	'en': "Compile All Now",
	'ru': "Скомпилировать все QC",
},
'up_axis_tip': {
	'en': "Use for compatibility with data from other 3D tools",
	'ru': "Используется для совместимости с экспортами из Maya и других 3D-пакетов",
},
'smd_format': {
	'ja': "対象のエンジン",
	'en': "Target Engine",
	'ru': "мишень движка",
},
'smd_format_tip': {
	'en': "Target engine: Source or GoldSrc",
},
'export_format_tip': {
	'en': "Export format: SMD/VTA or DMX",
},
'dmx_mat_path_tip': {
	'en': "Folder relative to game root containing VMTs referenced in this scene (DMX only)",
	'ru': "Путь (относительно мода), содержащий VMT-файлы для этой модели (аналог $cdmaterials; только для DMX-файлов)",
},
'qc_compileall_tip': {
	'en': "Compile all QC files whenever anything is exported",
	'ru': "Компилировать все указанные QC-файлы сразу после экспорта",
},
'qc_path_tip': {
	'en': "This scene's QC file(s); Unix wildcards supported",
	'ru': "QC-файлы, связанные с этой сценой; поддерживаются маски для имён файлов",
},
'qc_nogamepath': {
	'en': "No Game Path and invalid VPROJECT",
	'ru': "Не указан путь до мода; переменная VPROJECT содержит ошибочные данные",
},
'dmx_mat_path': {
	'ja': "マテリアルのパス",
	'en': "Material Path",
	'ru': "Путь до материалов",
},
'exportroot': {
	'ja': "エクスポートのパス",
	'en': "Export Path",
	'ru': "Куда экспортировать",
},
'export_format': {
	'ja': "エクスポートのフォーマット",
	'en': "Export Format",
	'ru': "Формат файла экспорта",
},
'qc_compileall': {
	'ja': "エクスポートから、みんあがコンパイル",
	'en': "Compile all on export",
	'ru': "Компилировать QC-файлы после экспорта",
},
'dmx_weightlinkcull': {
	'ja': "ウェイト・リンクの間引きのしきい値",
	'en': "Weight Link Cull Threshold",
	'ru': "Порог веса привязки вершины к кости",
},
'dmx_weightlinkcull_tip': {
	'en': "The maximum strength at which a weight link can be removed to comply with Source's per-vertex link limit",
	'ru': "Если вершина связана с некоторой костью, и её вес меньше здесь указанного, то связь с этой костью будет удалена при экспорте, чтобы вписаться в ограничение движка Source. («Source не поддерживает такое количество привязок»)",
},
'dmx_encoding_tip': {
	'en': "Manual override for binary DMX encoding version",
	'ru': "Версия структуры DMX-файла",
},
'dmx_format_tip': {
	'en': "Manual override for DMX model format version",
	'ru': "Версия формата модели (DMX-файл)",
},
'engine_path_tip': {
	'en': "Directory containing studiomdl (Source 1) or resourcecompiler (Source 2)",
	'ru': "Путь до папки с studiomdl (Source 1) или resourcecompiler (Source 2)",
},
'ignore_materials_tip': {
	'en': "Only export face-assigned image filenames",
	'ru': "Называть материалы в экспортированной модели по именам текстур, а не Blender-материалов",
},
'updater_title': {
	'en': "Open Workflow Edition Releases",
},
'update_err_downloadfailed': {
	'en': "Could not complete download:",
	'ru': "Не удалось завершить загрузку обновления",
},
'offerchangelog_offer': {
	'en': "Restart Blender to complete the update. Click to view the changelog.",
	'ru': "Перезапустите Blender для завершения обновления. Нажмите для просмотра списка изменений.",
},
'update_err_outdated': {
	'en': "The latest Source Tools require Blender {0}. Please upgrade.",
	'ru': "Текущая версия Source Tools требует Blender {0}. Пожалуйста, обновитесь.",
},
'update_err_unknown': {
	'en': "Could not install update:",
	'ru': "Невозможно обновить Source Tools: ",
},
'offerchangelog_title': {
	'en': "Source Tools Update",
	'ru': "Обновление Source Tools",
},
'update_err_corruption': {
	'en': "Update was downloaded, but file was not valid",
	'ru': "Не удалось обновиться: файлы обновления повреждены",
},
'update_done': {
	'en': "Installed Source Tools {0}!",
	'ru': "Обновлено до Source Tools {0}!",
},
'updater_title_tip': {
	'en': "Open this edition's GitHub releases to download an update. Install the ZIP manually in Blender's Add-ons preferences",
},
'update_alreadylatest': {
	'en': "The latest Source Tools ({0}) are already installed.",
	'ru': "Уже установлена самая последняя версия Blender Source Tools ({0}).",
},
'smd_vta_panel': {
	'en': "SMD / VTA",
},
'smd_vta_mode': {
	'en': "Files to write",
},
'smd_vta_mode_tip': {
	'en': "Write the mesh SMD, the shape key VTA, or both. VTA frame order must match the flex controllers in the QC.",
},
'smd_vta_both': {
	'en': "SMD + VTA",
},
'smd_vta_smd': {
	'en': "SMD Only",
},
'smd_vta_vta': {
	'en': "VTA Only",
},
'smd_vta_both_tip': {
	'en': "Write both the mesh SMD and the shape key VTA.",
},
'smd_vta_smd_tip': {
	'en': "Write only the mesh SMD and skip shape key baking and the VTA. This is the fast option.",
},
'smd_vta_vta_tip': {
	'en': "Write only the shape key VTA; the existing SMD is not rewritten.",
},
'vta_smd_only_hint': {
	'en': "Shape key baking and VTA writing are skipped, so this export stays fast. The existing .vta is not updated.",
},
'vta_only_hint': {
	'en': "The .smd is not rewritten. Keep the existing .smd in sync with this bake.",
},
'vta_first_shape': {
	'en': "First VTA Shape",
},
'vta_first_shape_tip': {
	'en': "Shape key written as VTA frame 1. Frame 0 is always the first shape key (Basis). Leave empty to use every shape key.",
},
'vta_last_shape': {
	'en': "Last VTA Shape",
},
'vta_last_shape_tip': {
	'en': "Shape key written as the last VTA frame. Leave empty to use every shape key.",
},
'vta_range_hint': {
	'en': "Empty fields use all shape keys. Frame 0 is always the first shape key (Basis).",
},
'vta_basis_selected': {
	'en': "Basis is always VTA frame 0 and cannot be selected as a VTA frame.",
},
'vta_range_summary': {
	'en': "VTA: frame 0 = {0}, frames 1-{1} = {2} .. {3}",
},
'vta_range_invalid': {
	'en': "VTA range error: {0}",
},
'vta_no_shapes': {
	'en': "No shape keys to export for \"{0}\"",
},
'vta_warn_frames': {
	'en': "VTA confirmation: frame limit",
},
'vta_warn_frames_tip': {
	'en': "Show a confirmation dialog before writing a VTA with more shape key frames than this. 0 disables the frame check.",
},
'vta_warn_mb': {
	'en': "VTA confirmation: size limit (MB)",
},
'vta_warn_mb_tip': {
	'en': "Show a confirmation dialog before writing a VTA estimated larger than this (upper bound). 0 disables the size check.",
},
'vta_confirm_title': {
	'en': "Large VTA Export",
},
'vta_confirm_summary': {
	'en': "{0} shape key frame(s) across {1} exportable(s), estimated up to {2} MB.\nWriting the VTA bakes those shape keys and may take a long time.",
},
'vta_confirm_continue': {
	'en': "Continue",
},
'vta_smd_notwritten': {
	'en': "VTA only: the .smd for \"{0}\" was not written; make sure the existing SMD matches this bake.",
},
'vta_skip_shape_normals': {
	'en': "Skip Shape Normals",
},
'vta_skip_normals_short': {
	'en': "Skip Normals",
},
'vta_skip_shape_normals_tip': {
	'en': "VTA still requires a normal column. When enabled, shape frames only include vertices whose positions change and reuse the base mesh's normals; normal-only changes are ignored. This makes the VTA smaller and faster, but flexes will not update lighting normals.",
},
'vta_skip_shape_normals_hint': {
	'en': "VTA still contains normals; only shape key normal changes are skipped.",
},
'dmx_binary': {
	'en': "Binary {0}",
},
'dmx_model': {
	'en': "Model {0}",
},
'dmx_model_modeldoc': {
	'en': "Model {0} (ModelDoc)",
},
'export_format_smd_tip': {
	'en': "Studiomdl Data",
},
'export_format_dmx_tip': {
	'en': "Datamodel Exchange",
},
'smd_format_source': {
	'en': "Source",
},
'smd_format_source_tip': {
	'en': "Source Engine (Half-Life 2)",
},
'smd_format_goldsrc': {
	'en': "GoldSrc",
},
'smd_format_goldsrc_tip': {
	'en': "GoldSrc engine (Half-Life 1)",
},
'write_kv2': {
	'en': "Write KeyValues2",
},
'write_kv2_tip': {
	'en': "Write ASCII DMX files",
},
'vca_name': {
	'en': "Name",
},
'vca_start': {
	'en': "Start",
},
'vca_end': {
	'en': "End",
},
'controllers_simple': {
	'en': "Simple",
},
'controllers_advanced': {
	'en': "Advanced",
},
'shape_stereo_mode_vgroup_label': {
	'en': "Vertex Group",
},
'exporter_err_groupmissing': {
	'en': "Collection \"{0}\" not found",
},
'export_button': {
	'en': "Export",
},
'common_add': {
	'en': "Add",
},
'common_remove': {
	'en': "Remove",
},
'sharpness': {
	'en': "Sharpness",
},
'activate': {
	'en': "Activate",
},
'vta_shape_source': {
	'en': "Shape keys from {0}",
},
'vta_shape_count': {
	'en': "{0} / {1} shape keys",
},
'vta_confirm_detail': {
	'en': "- {0}: {1} frames, {2} loops, up to {3} MB",
},
'vta_confirm_more': {
	'en': "- ... and {0} more exportable(s)",
},
'vta_confirm_background': {
	'en': "Large VTA export: {0} frames, up to {1} MB (confirmation skipped in background mode)",
},
'importer_up_axis': {
	'en': "Up Axis",
},
'importer_rot_euler': {
	'en': "Euler",
},
'importer_rot_quat': {
	'en': "Quaternion",
},
'importer_bone_default': {
	'en': "Default",
},
'importer_bone_arrows': {
	'en': "Arrows",
},
'importer_bone_sphere': {
	'en': "Sphere",
},
'qc_compile_err_noselection': {
	'en': "No QC files selected for compile.",
},
'exporter_warn_uvmap_missing': {
	'en': "'{0}' does not contain a UV Map called {1} and no suitable fallback map could be found. The model may be missing UV data.",
},
'importer_warn_uneditable_vertex': {
	'en': "Vertex data '{0}' was imported, but cannot be edited in Blender (as of 2.82)",
},
'importer_warn_unsupported_vertex': {
	'en': "Could not import vertex data '{0}'; Blender does not support {1} data layers.",
},
'file_path': {
	'en': "File path",
},
'vta_err_first_missing': {
	'en': "VTA first shape key \"{0}\" is not an exportable shape key (frame 0 is always the first shape key / Basis)",
},
'vta_err_last_missing': {
	'en': "VTA last shape key \"{0}\" is not an exportable shape key",
},
'vta_err_order': {
	'en': "VTA first shape key \"{0}\" comes after the last shape key \"{1}\"",
},
'vca_qc_copied': {
	'en': "QC segment copied to clipboard.",
},
'batch_settings': {
	'en': "Batch Export Settings",
},
'batch_smd_vta_mode': {
	'en': "SMD/VTA Mode",
},
'batch_smd_vta_mode_tip': {
	'en': "Mode applied by the batch buttons below",
},
'batch_vta_skip_normals': {
	'en': "Skip Shape Normals",
},
'batch_vta_skip_normals_tip': {
	'en': "Skip shape key normal changes when the batch settings are applied",
},
'batch_apply': {
	'en': "Apply Export Settings",
},
'batch_apply_tip': {
	'en': "Apply the batch SMD/VTA mode and shape normal setting to exportables",
},
'batch_apply_selected': {
	'en': "Apply to Selected",
},
'batch_apply_all': {
	'en': "Apply to All",
},
'batch_no_selection': {
	'en': "No exportable objects or collections are selected.",
},
'batch_applied': {
	'en': "Applied settings to {0} exportable(s).",
},
'batch_scope_hint': {
	'en': "\"Selected\" means objects or collections selected in the scene.",
},
'exportmenu_settings': {
	'en': "Export Settings",
},
'exportmenu_set_mode': {
	'en': "Set SMD/VTA Mode",
},
'exportmenu_toggle_skip_normals': {
	'en': "Toggle Skip Shape Normals",
},
'selected_exportable_panel': {
	'en': "Selected Exportable",
},
'selected_exportable_hint': {
	'en': "Follows the object or collection selected in the scene.",
},
'selected_exportable_none': {
	'en': "No exportable object or collection is selected.",
},
'selected_exportable_multiple': {
	'en': "{0} exportables are selected; showing the first one. Use the Exportables panel for batch settings.",
},
'selected_exportable_armature': {
	'en': "Armature exportables do not use SMD/VTA settings.",
},
}

# Simplified Chinese UI strings. utils.get_id() uses this table directly when Blender's locale is zh_HANS,
# bypassing Blender's built-in (and often overly literal) dictionary translation.
zh_HANS = {
	'vca_sequence': "生成序列",
	'controllers_simple_tip': "为每个形态键生成一个表情控制器",
	'vertmap_group_props': "顶点图",
	'action_selection_filter_tip': "所有名称匹配骨架过滤器且正在被使用的动作",
	'curve_poly_side_fwd': "正面（外侧）",
	'action_selection_current_tip': "骨架当前指定的动作或 NLA 轨道",
	'valvesource_cloth_enable': "启用布料物理",
	'subdir_tip': "相对于场景输出目录的可选子路径",
	'controllers_mode': "DMX 表情控制器生成",
	'scene_export': "场景导出",
	'shape_stereo_mode_tip': "如何定义左右分离的平衡",
	'bone_rot_legacy': "旧版旋转",
	'controllers_advanced_tip': "插入现有 DMX 文件中的表情控制器",
	'triangulate_tip': "避免起源引擎不支持的凹多边形 DMX 面",
	'action_filter': "动作过滤器",
	'vca_start_tip': "开始记录顶点动画的场景帧",
	'action_filter_tip': "名称匹配该过滤器且正在被使用的动作将被导出",
	'shape_stereo_sharpness_tip': "左右立体表情形态过渡的锐利程度",
	'vca_sequence_tip': "导出时生成驱动该顶点动画的动画序列",
	'shape_stereo_mode': "DMX 左右分离模式",
	'dummy_bone': "隐式静止骨骼",
	'vca_group_props': "顶点动画",
	'curve_poly_side': "多边形生成",
	'group_merge_mech': "合并机械部件",
	'action_selection_mode_tip': "如何选择要导出的动作",
	'use_scene_export_tip': "随场景一起导出此项",
	'curve_poly_side_back': "背面（内侧）",
	'valvesource_vertex_blend': "混合参数 RGB",
	'bone_rot_legacy_tip': "将此骨架骨骼的 Y 轴重映射为 Z 轴，以兼容旧版导入（仅 SMD）",
	'controller_source': "DMX 表情控制器来源",
	'group_suppress_tip': "单独导出该组内的对象",
	'action_selection_current': "当前动作 / NLA",
	'shape_stereo_sharpness': "DMX 左右分离锐度",
	'group_suppress': "禁用",
	'shape_stereo_vgroup': "DMX 左右分离顶点组",
	'shape_stereo_vgroup_tip': "定义左右平衡的顶点组（0=左，1=右）",
	'controllers_source_tip': "包含表情控制器的 DMX 文件（或文本数据块）",
	'valvesource_vertex_blend1': "混合参数扩展（?）",
	'curve_poly_side_tip': "决定导出时曲线哪一侧生成多边形",
	'triangulate': "三角化",
	'curve_poly_side_both': "两侧",
	'group_merge_mech_tip': "优化共享同一父级骨骼的网格的 DMX 导出",
	'action_selection_mode': "动作选择",
	'shape_stereo_mode_vgroup': "使用顶点组定义左右平衡",
	'vca_end_tip': "停止记录顶点动画的场景帧",
	'valvesource_vertex_paint': "顶点绘制",
	'controllers_mode_tip': "如何定义表情控制器",
	'subdir': "子文件夹",
	'dummy_bone_tip': "为不移动的顶点创建一根虚拟骨骼，模拟 Blender 在起源引擎中的行为，但可能破坏与现有文件的兼容性（仅 SMD）",
	'exportpanel_steam': "Steam 社区",
	'exportables_arm_filter_result': "“{0}”动作（{1}）",
	'exportables_flex_count_corrective': "校正形态键：{0}",
	'exportables_curve_polyside': "多边形生成：",
	'exportmenu_title': "Source Tools 导出",
	'exportables_flex_help': "表情控制器帮助",
	'exportpanel_title': "起源引擎导出",
	'exportables_flex_src': "控制器来源",
	'exportmenu_invalid': "无法导出所选内容",
	'qc_title': "起源引擎 QC 编译",
	'exportables_flex_props': "表情属性",
	'exportables_flex_generate': "生成控制器",
	'exportables_flex_split': "左右表情平衡：",
	'exportables_group_mute_suffix': "（已禁用）",
	'exportmenu_scene': "场景导出（{0} 个文件）",
	'exportpanel_dmxver': "DMX 版本：",
	'exportpanel_update': "增强版发行页面",
	'exportables_title': "起源引擎导出项",
	'exportables_armature_props': "骨架属性（{0}）",
	'qc_bad_enginepath': "引擎路径无效",
	'qc_invalid_source2': "起源 2 引擎不使用 QC 文件",
	'exportmenu_selected': "所选对象（{0} 个文件）",
	'exportables_group_props': "组属性",
	'qc_no_enginepath': "未提供引擎路径",
	'exportables_curve_props': "曲线属性",
	'exportables_flex_count': "形态键：{0}",
	'bl_info_author': "Tom Edwards（译者：Grigory Revzin）",
	'activate_dependency_shapes': "激活依赖形态键",
	'settings_prop': "Blender Source Tools 设置",
	'bl_info_description': "Valve Software 起源引擎的导入/导出插件。支持 SMD\\VTA、DMX 和 QC。",
	'export_menuitem': "起源引擎（.smd、.vta、.dmx）",
	'help': "帮助",
	'bl_info_location': "文件 > 导入/导出，场景属性",
	'import_menuitem': "起源引擎（.smd、.vta、.dmx、.qc）",
	'exporter_err_nogroupitems': "组“{0}”中没有启用导出的内容",
	'exporter_report_qc': "已导出 {0} 个文件并编译 {2} 个 QC（{3}/{4}），耗时 {1} 秒",
	'exporter_err_relativeunsaved': "在保存 .blend 文件之前无法导出到相对路径。",
	'exporter_err_nopolys': "对象 {0} 没有多边形，已跳过",
	'exporter_err_hidden': "跳过 {0}：对象无法被选中，可能被动画驱动器隐藏。",
	'exporter_err_arm_nonuniform': "骨架“{0}”存在非均匀缩放。起源引擎中的网格变形将与 Blender 不同。",
	'exporter_err_facesnotex_ormat': "{1} 上的 {0} 个面没有指定材质或纹理",
	'exporter_err_arm_noanims': "找不到骨架“{0}”的任何动画",
	'exporter_err_dupeenv_arm': "在“{1}”上发现骨架修改器“{0}”，但它已经有骨骼父级或约束。已忽略。",
	'exporter_err_bonelimit': "导出了 {0} 根骨骼，但 SMD 最多只支持 {1} 根！",
	'exporter_err_unmergable': "跳过组“{0}”的顶点动画：由于骨骼包络，无法合并为单个 DMX 对象。请确保整个组使用相同的骨骼父级，或移除所有包络。",
	'exporter_warn_source2names': "建议重命名“{0}”：在起源 2 引擎中，模型名只能包含小写字母、数字和/或下划线。",
	'exporter_warn_unicode': "{0}“{1}”的名称包含 Unicode 字符，可能无法正确编译！",
	'exporter_err_flexctrl_loadfail': "无法加载表情控制器。Python 报告：{0}",
	'qc_compile_err_nofiles': "无法编译：没有提供 QC。Blender Source Tools 不会生成 QC。",
	'exporter_err_missing_corrective_target': "找到校正形态键“{0}”，但找不到目标形态“{1}”",
	'qc_compile_complete': "已编译 {0} 个 {1} QC",
	'exporter_err_shapes_decimate': "无法导出“{0}”的形态键，因为它带有“{1}”精简修改器。仅支持未细分模式。",
	'exporterr_goldsrc_multiweights': "“{1}”上的 {0} 个顶点有多个权重链接。GoldSrc 引擎不支持！",
	'exporter_err_splitvgroup_undefined': "对象“{0}”使用顶点组左右分离，但没有指定可用的顶点组。",
	'exporter_err_open': "无法创建 {0} 文件。Python 报告：{1}。",
	'qc_compile_title': "编译 QC",
	'exporter_err_noexportables': "没有找到可导出的有效对象",
	'exporter_warn_sanitised_filename': "已将导出项名称“{0}”清理为“{1}”",
	'exporter_warn_correctiveshape_duplicate': "校正形态键“{0}”与“{2}”的激活条件（{1}）相同。已跳过。",
	'exporter_err_flexctrl_missing': "形态 {0} 没有定义表情控制器。",
	'qc_compile_err_compiler': "无法从“{0}”执行 studiomdl",
	'exporter_err_facesnotex': "{1} 上的 {0} 个面没有指定纹理",
	'exporter_err_flexctrl_undefined': "找不到“{0}”的表情控制器",
	'exporter_warn_source2smdsupport': "起源 2 引擎不再支持 SMD。",
	'exporter_tip': "导出并编译起源引擎模型",
	'exporter_warn_weightlinks_culled': "在“{2}”上剔除了 {0} 个低于场景阈值 {1:0.2} 的多余权重链接。",
	'exporter_prop_scene_tip': "导出在起源引擎导出项面板中选中的所有项目",
	'exporter_err_dmxenc': "DMX 格式“模型 {0}”需要 DMX 编码“二进制 3”或更高版本",
	'exporter_prop_group': "组名",
	'qc_compile_tip': "使用起源 SDK 编译 QC",
	'exporter_report_suffix': "，其中 {0} 个错误、{1} 个警告",
	'exporter_err_groupempty': "组 {0} 没有可用对象",
	'exporter_err_dmxother': "无法导出 DMX。请在场景属性中的起源引擎导出面板解决错误。",
	'exporter_prop_group_tip': "要导出的组名称",
	'exporter_warn_multiarmature': "检测到多个骨架",
	'exporter_err_solidifyinside': "曲线 {0} 带有实体化修改器的封边选项，但仍会导出两侧多边形。",
	'exporter_err_dupeenv_con': "在“{1}”上发现骨骼约束“{0}”，但它已经有骨骼父级。已忽略。",
	'exporter_err_unconfigured': "场景未配置。请参阅场景属性中的起源引擎导出面板。",
	'exporter_err_makedirs': "无法创建导出文件夹。Python 报告：{0}",
	'exporter_warn_weightlinks_excess': "“{1}”上有 {0} 个顶点超过 {2} 个权重链接。起源引擎不支持！",
	'exporter_err_noframes': "骨架 {0} 没有可导出的动画帧",
	'exporter_report_menu': "Source Tools 错误报告",
	'exporter_report': "已导出 {0} 个文件，耗时 {1} 秒",
	'exporter_err_groupmuted': "组 {0} 已禁用",
	'exporter_title': "导出 SMD/VTA/DMX",
	'qc_compile_err_unknown': "{0} 编译失败。请查看控制台了解详情",
	'exporter_err_splitvgroup_missing': "在对象“{1}”上找不到左右分离顶点组“{0}”",
	'importer_complete': "已导入 {0} 个文件，耗时 {1} 秒",
	'importer_bonemode': "骨骼形状",
	'importer_err_nofile': "未选择文件",
	'importer_err_smd': "无法打开 SMD 文件“{0}”：{1}",
	'importer_qc_macroskip': "正在跳过 QC {0} 中的宏",
	'importer_bones_validate_desc': "将新骨骼报告为缺失，而不对目标骨架做任何修改",
	'importer_tip': "导入未编译的起源引擎模型数据",
	'importer_title': "导入 SMD/VTA、DMX、QC",
	'importer_makecamera': "在 $origin 处创建摄像机",
	'importer_bone_parent_miss': "骨骼“{0}”的父级不一致：Blender 中为“{1}”，{3} 中为“{2}”。",
	'importer_makecamera_tip': "用于视图模型编辑；未设置时将创建空物体",
	'importer_err_shapetarget': "无法导入形态键：找不到有效目标对象",
	'importer_rotmode_tip': "决定导入骨骼或动画时创建的旋转关键帧类型",
	'importer_skipremdoubles_tip': "从 SMD 文件导入原始的不连续多边形；这些多边形较难编辑，但更接近原始网格",
	'importer_balance_group': "DMX 左右平衡",
	'importer_bones_mode_desc': "当参考网格导入向目标骨架引入新骨骼时的处理方式（对 QC 无效）",
	'importer_rotmode': "旋转模式",
	'importer_skipremdoubles': "保留 SMD 多边形与法线",
	'importer_bonemode_tip': "新骨架中的骨骼显示方式",
	'importer_bones_append': "追加到目标骨架",
	'importer_err_qci': "无法打开 QC $include 文件“{0}”，已跳过！",
	'importer_up_tip': "哪个轴代表“向上”（对 QC 无效）",
	'importer_err_namelength': "{0} 名称“{1}”太长，无法导入。已截断为“{2}”",
	'importer_bones_append_desc': "将新骨骼添加到目标骨架",
	'importer_err_unmatched_mesh': "{0} 个 VTA 顶点（{1}%）未能匹配到网格顶点！已创建一个带顶点组的对象来显示 VTA 文件顶点的位置。",
	'importer_bones_validate': "对照目标骨架校验",
	'importer_name_nomat': "未定义材质",
	'importer_bones_newarm_desc': "为本次导入创建新骨架",
	'importer_err_refanim': "在参考网格“{0}”中发现动画，已忽略！",
	'importer_bones_mode': "骨骼追加模式",
	'importer_err_badweights': "{1} 上有 {0} 个顶点权重指向无效骨骼",
	'importer_err_bonelimit_smd': "SMD 最多支持 128 根骨骼！",
	'importer_err_badfile': "无法识别 {0} 的格式",
	'importer_err_smd_ver': "无法识别/无效的 SMD 文件。导入将继续，但可能失败！",
	'importer_doanims': "导入动画",
	'importer_use_collections': "创建集合",
	'importer_use_collections_tip': "为每个导入的网格文件创建一个 Blender 集合。这样可以保留原始文件结构（对 DMX 很重要），并便于用数字键切换 LOD 等。",
	'importer_err_missingbones': "{0} 包含 {2} 中不存在的 {1} 根骨骼。请在控制台查看列表。",
	'importer_name_unmatchedvta': "未匹配的 VTA",
	'importer_bones_newarm': "新建骨架",
	'qc_warn_noarmature': "跳过 {0}；未找到骨架。",
	'exportstate_pattern_tip': "名称中包含此字符串的可见对象将受到影响",
	'exportstate': "设置 Source Tools 导出状态",
	'activate_dep_shapes': "激活依赖形态键",
	'gen_block_success': "DMX 已写入文本数据块“{0}”",
	'gen_block': "生成 DMX 表情控制器块",
	'vca_add_tip': "为当前 Source Tools 导出项添加一个顶点动画",
	'insert_uuid': "插入 UUID",
	'launch_hlmv_tip': "启动 Half-Life 模型查看器",
	'vertmap_remove': "移除起源 2 顶点图",
	'activate_dep_shapes_tip': "激活当前形态名称中（以下划线分隔）找到的形态",
	'vca_qcgen_tip': "将此对象的顶点动画 QC 片段复制到剪贴板",
	'vca_remove_tip': "从当前 Source Tools 导出项移除活动顶点动画",
	'vca_add': "添加顶点动画",
	'vertmap_select': "选择起源 2 顶点图",
	'vca_preview': "预览顶点动画",
	'activate_dep_shapes_success': "已激活 {0} 个依赖形态",
	'launch_hlmv': "启动 HLMV",
	'exportstate_pattern': "搜索模式",
	'insert_uuid_tip': "在当前位置插入随机 UUID",
	'gen_block_tip': "生成一个简单的表情控制器 DMX 块",
	'gen_drivers': "生成校正形态键驱动器",
	'apply_drivers': "根据驱动器重新生成形态键名称",
	'apply_drivers_tip': "重命名校正形态键，使其名称由控制它们的形态键（通过 Blender 动画驱动器）组合而成",
	'apply_drivers_success': "已重命名 {0} 个形态。",
	'vca_qcgen': "生成 QC 片段",
	'vertmap_create': "创建起源 2 顶点图",
	'vca_preview_tip': "使用场景预览设置播放当前 Source Tools 顶点动画",
	'vca_remove': "移除顶点动画",
	'gen_drivers_tip': "为起源引擎校正形态添加 Blender 动画驱动器",
	'qc_path': "QC 路径",
	'engine_path': "引擎路径",
	'game_path_tip': "包含 gameinfo.txt 的目录（未设置时将使用系统 VPROJECT）",
	'visible_only': "仅可见层",
	'dmx_encoding': "DMX 编码",
	'game_path': "游戏路径",
	'up_axis': "目标向上轴",
	'dmx_format': "DMX 格式",
	'ignore_materials': "忽略 Blender 材质",
	'visible_only_tip': "忽略隐藏层中的对象",
	'active_exportable': "当前导出项",
	'exportroot_tip': "从此场景导出的 SMD 和 DMX 文件所写入的根文件夹",
	'qc_compilenow': "立即全部编译",
	'up_axis_tip': "用于兼容来自其他 3D 工具的数据",
	'smd_format': "目标引擎",
	'smd_format_tip': "目标引擎：起源引擎或 GoldSrc 引擎",
	'export_format_tip': "导出格式：SMD/VTA 或 DMX",
	'dmx_mat_path_tip': "相对于游戏根目录、包含此场景引用 VMT 的文件夹（仅 DMX）",
	'qc_compileall_tip': "每次导出时编译所有 QC 文件",
	'qc_path_tip': "此场景的 QC 文件；支持 Unix 通配符",
	'qc_nogamepath': "未设置游戏路径且 VPROJECT 无效",
	'dmx_mat_path': "材质路径",
	'exportroot': "导出路径",
	'export_format': "导出格式",
	'qc_compileall': "导出时全部编译",
	'dmx_weightlinkcull': "权重链接剔除阈值",
	'dmx_weightlinkcull_tip': "为符合起源引擎每顶点链接上限而可移除权重链接的最大强度",
	'dmx_encoding_tip': "手动覆盖二进制 DMX 编码版本",
	'dmx_format_tip': "手动覆盖 DMX 模型格式版本",
	'engine_path_tip': "包含 studiomdl（起源 1）或 resourcecompiler（起源 2）的目录",
	'ignore_materials_tip': "仅导出面所指定图像的文件名",
	'updater_title': "打开增强版发行页面",
	'update_err_downloadfailed': "无法完成下载：",
	'offerchangelog_offer': "重启 Blender 以完成更新。点击查看更新日志。",
	'update_err_outdated': "最新版 Source Tools 需要 Blender {0}。请升级。",
	'update_err_unknown': "无法安装更新：",
	'offerchangelog_title': "Source Tools 更新",
	'update_err_corruption': "更新已下载，但文件无效",
	'update_done': "已安装 Source Tools {0}！",
	'updater_title_tip': "打开本增强版的 GitHub 发行页面下载更新，然后在 Blender 的插件偏好设置中手动安装 ZIP。",
	'update_alreadylatest': "已安装最新版 Source Tools（{0}）。",
	'smd_vta_panel': "SMD / VTA",
	'smd_vta_mode': "要写入的文件",
	'smd_vta_mode_tip': "写入网格 SMD、形态键 VTA，或两者都写。VTA 的帧顺序必须与 QC 中的表情控制器一致。",
	'smd_vta_both': "SMD + VTA",
	'smd_vta_smd': "仅 SMD",
	'smd_vta_vta': "仅 VTA",
	'smd_vta_both_tip': "同时写出网格 SMD 和形态键 VTA。",
	'smd_vta_smd_tip': "只写网格 SMD，跳过形态键烘焙和 VTA，速度很快。",
	'smd_vta_vta_tip': "只写形态键 VTA，不重写现有 SMD。",
	'vta_smd_only_hint': "已跳过形态键烘焙和 VTA 写入，因此导出很快。现有 .vta 不会更新。",
	'vta_only_hint': "不会重写 .smd。请确保现有 .smd 与本次烘焙一致。",
	'vta_first_shape': "VTA 起始形态键",
	'vta_first_shape_tip': "作为 VTA 第 1 帧写出的形态键。第 0 帧始终是第一个形态键（基型）。留空则使用全部形态键。",
	'vta_last_shape': "VTA 结束形态键",
	'vta_last_shape_tip': "作为 VTA 最后一帧写出的形态键。留空则使用全部形态键。",
	'vta_range_hint': "留空则使用全部形态键。第 0 帧始终是第一个形态键（基型）。",
	'vta_basis_selected': "基型始终是 VTA 第 0 帧，不能选作 VTA 帧。",
	'vta_range_summary': "VTA：第 0 帧 = {0}，第 1-{1} 帧 = {2} .. {3}",
	'vta_range_invalid': "VTA 区间错误：{0}",
	'vta_no_shapes': "“{0}”没有可导出的形态键",
	'vta_warn_frames': "VTA 确认：帧数上限",
	'vta_warn_frames_tip': "写入的 VTA 形态键帧数超过此值时弹出确认框。设为 0 可关闭帧数检查。",
	'vta_warn_mb': "VTA 确认：体积上限（MB）",
	'vta_warn_mb_tip': "估算的 VTA 体积超过此值（上限估算）时弹出确认框。设为 0 可关闭体积检查。",
	'vta_confirm_title': "大型 VTA 导出",
	'vta_confirm_summary': "{0} 个形态键帧，涉及 {1} 个导出项，估算最大 {2} MB。\n写入 VTA 需要烘焙这些形态键，可能耗时较长。",
	'vta_confirm_continue': "继续",
	'vta_smd_notwritten': "仅 VTA：未写出“{0}”的 .smd；请确保现有 SMD 与本次烘焙一致。",
	'vta_skip_shape_normals': "忽略形态键法线",
	'vta_skip_normals_short': "忽略法线",
	'vta_skip_shape_normals_tip': "VTA 格式仍必须包含法线列。启用后，形态帧只写入位置发生变化的顶点，并沿用基础网格的法线；仅法线变化会被忽略。这样 VTA 更小、导出更快，但形态动画不会更新光照法线。",
	'vta_skip_shape_normals_hint': "VTA 仍包含法线列；这里只跳过形态键的法线变化。",
	'dmx_binary': "二进制 {0}",
	'dmx_model': "模型 {0}",
	'dmx_model_modeldoc': "模型 {0}（ModelDoc）",
	'export_format_smd_tip': "Studiomdl 数据",
	'export_format_dmx_tip': "DMX 数据模型交换格式",
	'smd_format_source': "起源引擎",
	'smd_format_source_tip': "起源引擎（半条命 2）",
	'smd_format_goldsrc': "GoldSrc 引擎",
	'smd_format_goldsrc_tip': "GoldSrc 引擎（半条命 1）",
	'write_kv2': "写入 KeyValues2",
	'write_kv2_tip': "写入 ASCII 格式的 DMX 文件",
	'vca_name': "名称",
	'vca_start': "开始",
	'vca_end': "结束",
	'controllers_simple': "简单",
	'controllers_advanced': "高级",
	'shape_stereo_mode_vgroup_label': "顶点组",
	'exporter_err_groupmissing': "找不到集合“{0}”",
	'export_button': "导出",
	'common_add': "添加",
	'common_remove': "移除",
	'sharpness': "锐度",
	'activate': "激活",
	'vta_shape_source': "形态键列表来自 {0}",
	'vta_shape_count': "已选 {0} / {1} 个形态键",
	'vta_confirm_detail': "- {0}：{1} 帧，{2} 个顶点循环，最大 {3} MB",
	'vta_confirm_more': "- 另有 {0} 个导出项",
	'vta_confirm_background': "大型 VTA 导出：{0} 帧，最大 {1} MB（后台模式已跳过确认）",
	'importer_up_axis': "向上轴",
	'importer_rot_euler': "欧拉",
	'importer_rot_quat': "四元数",
	'importer_bone_default': "默认",
	'importer_bone_arrows': "箭头",
	'importer_bone_sphere': "球体",
	'qc_compile_err_noselection': "未选择任何 QC 文件进行编译。",
	'exporter_warn_uvmap_missing': "“{0}”不包含名为 {1} 的 UV 图，也找不到合适的备用 UV 图。模型可能缺少 UV 数据。",
	'importer_warn_uneditable_vertex': "顶点数据“{0}”已导入，但无法在 Blender 中编辑（截至 2.82）",
	'importer_warn_unsupported_vertex': "无法导入顶点数据“{0}”；Blender 不支持 {1} 数据层。",
	'file_path': "文件路径",
	'vta_err_first_missing': "VTA 起始形态键“{0}”不是可导出的形态键（第 0 帧始终是第一个形态键 / 基型）",
	'vta_err_last_missing': "VTA 结束形态键“{0}”不是可导出的形态键",
	'vta_err_order': "VTA 起始形态键“{0}”排在结束形态键“{1}”之后",
	'vca_qc_copied': "QC 片段已复制到剪贴板。",
	'batch_settings': "批量导出设置",
	'batch_smd_vta_mode': "SMD/VTA 模式",
	'batch_smd_vta_mode_tip': "下方批量按钮要应用的模式",
	'batch_vta_skip_normals': "忽略形态键法线",
	'batch_vta_skip_normals_tip': "应用批量设置时，同时设置是否忽略形态键法线变化",
	'batch_apply': "批量应用导出设置",
	'batch_apply_tip': "把批量 SMD/VTA 模式和形态键法线设置应用到导出项",
	'batch_apply_selected': "应用到所选",
	'batch_apply_all': "应用到全部",
	'batch_no_selection': "没有选中可导出的对象或集合。",
	'batch_applied': "已为 {0} 个导出项应用设置。",
	'batch_scope_hint': "“所选”指场景中选中的对象或集合。",
	'exportmenu_settings': "导出设置",
	'exportmenu_set_mode': "设置 SMD/VTA 模式",
	'exportmenu_toggle_skip_normals': "切换忽略形态键法线",
	'selected_exportable_panel': "所选导出项",
	'selected_exportable_hint': "跟随场景中选中的对象或集合。",
	'selected_exportable_none': "未选中可导出的对象或集合。",
	'selected_exportable_multiple': "选中了 {0} 个导出项，这里显示第一个。批量设置请使用“起源引擎导出项”面板。",
	'selected_exportable_armature': "骨架导出项不使用 SMD/VTA 设置。",
}

def _get_ids():	
	ids = {}
	for id,values in _data.items():
		ids[id] = values['en']
	return ids
ids = _get_ids()

def _get_translations():
	import collections
	translations = collections.defaultdict(dict)
	for lang in _languages:
		for id,values in _data.items():
			value = values.get(lang)
			if value: translations[lang][(None, ids[id])] = value
	return translations
translations = _get_translations()

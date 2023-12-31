# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import flet as ft
from comm import params


# from comm.handler import GUIHandler


def main(page: ft.Page):
    page.title = '数据爬取配置管理'
    page.window_width = 800
    page.window_height = 600

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        filename_show.value = selected_files.value
        page.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)

    filename_show = ft.TextField(value='', width=550, height=40,
                                 text_style=ft.TextStyle(size=15),
                                 content_padding=ft.Padding(10, 0, 10, 0))
    index_input = ft.TextField(value='0', width=550, height=40,
                               text_style=ft.TextStyle(size=15),
                               content_padding=ft.Padding(10, 0, 10, 0))
    is_restart_input = ft.RadioGroup(
        value='no',
        content=ft.Row([
            ft.Radio(value='yes', label='yes'),
            ft.Radio(value='no', label='no')])
    )
    type_dropdown = ft.Dropdown(
        width=100,
        height=60,
        value='单轮对话',
        options=[
            ft.dropdown.Option('单轮对话'),
            ft.dropdown.Option('多轮对话'),
        ],
    )

    def handle_params(e):
        filename = filename_show.value
        index = index_input.value
        is_restart = is_restart_input.value
        talk_type = params[type_dropdown.value]
        if not filename:
            page.snack_bar = ft.SnackBar(ft.Text('文件名不能为空'))
            page.snack_bar.open = True
            page.update()
            return
        # 拿到有效值后去调相关逻辑即可
        print(f'选择类型：{talk_type}')
        print(filename)
        print(index)
        print(is_restart)
        # if is_restart == 'yes':
        #     GUIHandler.restart_status(talk_type)
        # else:
        #     GUIHandler.update_index(index, talk_type)
        #     GUIHandler.update_filepath2cfg(filename, talk_type)

    page.add(
        ft.AppBar(
            title=ft.Text('配置项管理器', size=20),
            bgcolor=ft.colors.SURFACE_VARIANT
        ),
        ft.Row([
            ft.Text('选择类型', size=15, color=ft.colors.LIGHT_BLUE_700),
            type_dropdown,
        ]),
        ft.Row([
            ft.Text('文件路径', size=15, color=ft.colors.AMBER_600),
            filename_show,
            ft.ElevatedButton(
                text='选择文件',
                icon=ft.icons.FOLDER,
                on_click=lambda _: pick_files_dialog.pick_files(
                    allow_multiple=True,
                    dialog_title='文件路径'
                )
            ),
        ]),

        ft.Row([
            ft.Text('起始索引', size=15, color=ft.colors.CYAN),
            index_input
        ]),

        ft.Row([
            ft.Text('重置', width=150, size=15),
            is_restart_input
        ]),
        ft.Row([
            ft.Text('', width=150, size=15),
            ft.FilledButton(text='确定', width=200, icon=ft.icons.RUN_CIRCLE,
                            on_click=handle_params)
        ])

    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main)

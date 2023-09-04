# chat-flet-GUI

- 一个简易的配置管理UI工具

## Demo

<img width="788" alt="image" src="https://github.com/JimouChen/chat-flet-GUI/assets/63119239/64ccb854-4c36-4e16-a3dc-676ca2e9a8af">

<img width="797" alt="image" src="https://github.com/JimouChen/chat-flet-GUI/assets/63119239/ca557d11-a440-48a2-ae59-b78c38a402b5">

<img width="793" alt="image" src="https://github.com/JimouChen/chat-flet-GUI/assets/63119239/75a4e803-36b4-4d86-bae0-2436861a7b45">

## Requirements

- `flet`

## Your Code

- demo，你的业务逻辑代码写成接口在这里调用即可；

```python
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
      if is_restart == 'yes':
          GUIHandler.restart_status(talk_type)
      else:
          GUIHandler.update_index(index, talk_type)
          GUIHandler.update_filepath2cfg(filename, talk_type)
```

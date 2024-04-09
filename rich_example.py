import time

from rich.progress import Progress, BarColumn, SpinnerColumn, TimeRemainingColumn, TimeElapsedColumn, TransferSpeedColumn
from rich.panel import Panel
from rich.box import DOUBLE


page_columns = [
        # 设置进度条头部
        "[progress.description]{task.description}({task.completed}/{task.total})",

        # 设置显示Spinner动画{spinner_name：头部动画名称；style：头部动画颜色}
        SpinnerColumn(spinner_name='bouncingBall', style="white"),

        # 设置传输速度
        TransferSpeedColumn(),

        # 设置进度条体{complete_style：进行中颜色；finished_style：完成颜色}
        BarColumn(complete_style="magenta", finished_style="green"),

        # 设置进度条尾部{[color]：百分比颜色；task.percentage：百分比格式化}
        "[progress.percentage][white]{task.percentage:>3.2f}%",

        # 设置进度条共计执行时间样式
        "⏱ ",
        TimeElapsedColumn(),

        # 设置进度条预计剩余时间样式
        "⏳",
        TimeRemainingColumn(),
]


with Progress(*page_columns, transient=True) as page_progress:
    for i in range(100):
        task = page_progress.add_task(f"[bold blue]Page {i}", total=100, box=DOUBLE)
        page_progress.update(task_id=task, completed=i)
        time.sleep(0.01)
#
#
# class WriteProgress(Progress):
#     write_columns = []
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args)
#         self.write_columns = [
#             # 设置进度条头部
#             "[progress.description]{task.description}({task.completed}/{task.total})",
#
#             # 设置显示Spinner动画{spinner_name：头部动画名称；style：头部动画颜色}
#             SpinnerColumn(spinner_name='aesthetic', style="white"),
#
#             # 设置传输速度
#             TransferSpeedColumn(),
#
#             # 设置进度条体{complete_style：进行中颜色；finished_style：完成颜色}
#             BarColumn(complete_style="cyan", finished_style="green"),
#
#             # 设置进度条尾部{[color]：百分比颜色；task.percentage：百分比格式化}
#             "[progress.percentage][white]{task.percentage:>3.2f}%",
#
#             # 设置进度条共计执行时间样式
#             "⏱ ",
#             TimeElapsedColumn(),
#
#             # 设置进度条预计剩余时间样式
#             "⏳",
#             TimeRemainingColumn(),
#         ]
#
#     def get_renderables(self):
#         yield Panel(self.make_tasks_table(self.tasks), box=DOUBLE)

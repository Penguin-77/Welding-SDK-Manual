Python
########

结构体定义
**********

.. _摆焊基本参数:

摆焊基本参数
+++++++++++++

``WeaveParams``

.. code:: python

    class WeaveParams:
          # 摆焊基本参数，包含所有摆焊类型的参数
    
    def __init__(self):
        # 摆动模式（必填）
        self.swing_mode: int = 1  # 1:Z字 2:平面三角 3:梯形 4:月牙 5:立焊三角 11:正弦 12:圆形 13:8字
        
        # 摆动参数
        self.swing_frequency: float = 1.0  # 摆动频率(Hz)，范围：0.1-10.0
        self.right_amplitude: float = 3.0  # 右摆幅(mm)，范围：0-50.0
        self.left_amplitude: float = 3.0   # 左摆幅(mm)，范围：0-50.0
        
        # 特殊摆型参数
        self.radius: float = 0.0  # 摆长半径(mm)，月牙、圆形、8字摆使用
        
        # 停留时间
        self.left_dwell_time: float = 0.0   # 左停留时间(s)，范围：0-5.0
        self.right_dwell_time: float = 0.0  # 右停留时间(s)，范围：0-5.0
        self.mid_dwell_time: float = 0.0    # 中间停留时间(s)，平面三角、立焊三角使用
        
        # 角度参数
        self.elevation_angle: float = 0.0  # 横角(°)，范围：-90~90
        self.azimuth_angle: float = 0.0    # 纵角(°)，范围：-90~90
        
        # 高级参数
        self.center_rise: float = 0.0  # 中心抬升量(mm)，范围：-10.0~10.0

.. note::

    ``swing_mode`` ：必须设置为对应的摆型编号。

    不同摆型使用不同的参数组合，未使用的参数可忽略或设为0。

.. _摆焊轨迹配置:

摆焊轨迹配置
+++++++++++++

``WeaveConfig``

.. code:: python

    class WeaveConfig:
          # 摆焊轨迹配置参数
    
    def __init__(self):
        # 停留模式
        self.dwell_delay_type: int = 0
        
        # 连接模式
        self.blend_weave_end: int = 1
        
        # 平面选择
        self.frame_type: int = 0 
        
        # 摆动方向
        self.direction: int = 0

**参数说明：** 

- 停留模式（ ``dwell_delay_type`` ）：
    - ``int = 0`` ：焊枪到达摆幅极限位置后停止运动，停留指定时间后再反向运动。Z字摆，三角摆，台形摆，月牙摆为此种停留方式。
    - ``int = 1`` ：焊枪到达摆幅极限位置后沿焊接方向继续运动，指定停留时间后再反向运动。正弦摆为此种停留方式。
- 连接模式（ ``blend_weave_end`` ）：
    - ``int = 1`` ：启用平滑过渡，即摆焊轨迹不强制经过中间点。目前仅支持这一种模式。
- 平面选择（ ``frame_type`` ）：
    - ``int = 0`` ：摆焊平面跟随焊枪末端，当前版本仅支持跟随焊枪。
    - ``int = 1`` ：摆焊平面跟随由起点和终点位置计算得出的工件平面，焊接过程中，机器人姿态会随之调整。
- 摆动方向（ ``direction`` ）：
    - ``int = 0`` ：起摆方向为左（+Y）。
    - ``int = 1`` ：起摆方向为右（-Y）。

.. _预留寄存器:

预留寄存器
++++++++++++

``ReserveRegisters``

.. code:: python

    class ReserveRegisters:
    # 预留寄存器接口，目前暂无实际功能
    
    def __init__(self):
        self.float_regs: list[float] = []  # 浮点寄存器列表
        self.int_regs: list[int] = []      # 整型寄存器列表
        self.str_regs: list[str] = []      # 字符串寄存器列表

.. _摆焊渐变参数:

摆焊渐变参数
+++++++++++++

``WeaveGradient``

.. code:: python

    class WeaveGradient:
          # 摆动过程中，摆宽和摆频逐渐向目标值变化。圆弧、8字摆不支持渐变。
    
    def __init__(self):
        # 渐变目标值
        self.left_amplitude: float = 0.0      # 渐变左摆幅(mm)，范围：0-50.0
        self.right_amplitude: float = 0.0     # 渐变右摆幅(mm)，范围：0-50.0
        self.swing_frequency: float = 0.0     # 渐变摆动频率(Hz)，范围：0.1-10.0
        
        # 渐变控制
        self.path_length: float = 0.0  # 渐变路径长度(mm)，正弦摆专用

.. attention::

    * 圆形摆和8字摆不支持焊接渐变参数。
    * 只有正弦摆需要设置渐变路径长度( ``path_length`` )参数。
    * 渐变过程是线性的，从当前值逐步变化到目标值。

.. _起弧参数:

起弧参数
+++++++++

``ArconParams``

.. code:: python

    class ArconParams:

    def __init__(self):

        self.Prog: int = 0                  # 焊接程序号
        self.current: float = 0.0           # 焊接电流（A）
        self.correct_voltage: float = 0.0   # 弧长修正电压（V）
        self.welding_mode: int = 0          # 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
        self.success_sleep: float = 0.0     # 引弧成功后等待时间（s）

.. _焊接参数:

焊接参数
+++++++++

``WeldingParams``

.. code:: python

    class WeldingParams:
    
    def __init__(self):

        self.Prog: int = 0                  # 焊接程序号
        self.current: float = 0.0           # 焊接电流（A）
        self.correct_voltage: float = 0.0   # 弧长修正电压（V）
        self.welding_mode: int = 0          # 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
        self.welding_speed: float = 0.0     # 焊接速度（mm/s）
    
.. note::

    ``WeldingParams`` 继承自 ``ArconParams`` 的全部字段，并额外增加 ``welding_speed`` 用于控制焊接过程中的行进速度。

.. _收弧参数:

收弧参数
+++++++++

``ArcoffParams``

.. code:: python

    class ArcoffParams:

    def __init__(self):

        self.Prog: int = 0                  # 焊接程序号
        self.current: float = 0.0           # 收弧电流（A）
        self.correct_voltage: float = 0.0   # 弧长修正电压（V）
        self.welding_mode: int = 0          # 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
        self.arcoff_sleep: float = 0.0      # 收弧等待时间（s）
        self.delay_gas_sleep: float = 0.0   # 滞后送气时间（s）

.. _JOB 参数:

JOB 参数
+++++++++

``JobParams``

.. code:: python

    class JobParams:
    
    def __init__(self):

        self.JOB: int = 0;            # JOB 编号
        self.welding_speed: float = 0.0    # 焊接速度（mm/s）
        self.arcoff_sleep: float = 0.0      # 起弧成功等待时间（s）
        self.delay_gas_sleep: float = 0.0   # 滞后送气时间（s）

.. _焊机信号结构体:

焊机信号结构体
+++++++++++++++

``WelderSignal`` / ``InputSignal`` / ``OutputSignal``

.. code:: python

    class InputSignal:
        # 焊机输入信号

        def __init__(self):
            self.welding_enable: int = 0   # 焊接使能开关
            self.simulate: int = 0         # 模拟模式开关
            self.start: int = 0            # 起弧信号
            self.robot_ready: int = 0      # 机器人就绪信号
            self.welding_mode: int = 0     # 焊接模式
            self.gas: int = 0              # 送气信号
            self.wire_feed: int = 0        # 送丝信号
            self.wire_back: int = 0        # 退丝信号
            self.error_reset: int = 0      # 错误复位信号
            self.touch_enable: int = 0     # 接触寻位使能
            self.job: int = 0              # JOB 号信号
            self.prog: int = 0             # Program 号信号
            self.wire_feed_rate: float = 0.0  # 送丝速度/焊接电流
            self.correct_voltage: float = 0.0 # 弧长修正
            self.burn_back: float = 0.0    # 回烧时间（预留）

.. code:: python

    class OutputSignal:
        # 焊机输出信号

        def __init__(self):
            self.success: int = 0          # 引弧成功信号
            self.stick: int = 0            # 粘丝信号
            self.touched: int = 0          # 接触信号
            self.ps_ready: int = 0         # 焊机就绪信号
            self.collision: int = 0        # 焊枪碰撞信号
            self.error: int = 0            # 错误信号
            self.actual_voltage: float = 0.0  # 实际电压
            self.actual_current: float = 0.0  # 实际电流
            self.wire_speed: float = 0.0   # 实际焊丝速度

.. code:: python

    class WelderSignal:

        def __init__(self):
            self.Input: InputSignal = InputSignal()      # 输入信号
            self.Output: OutputSignal = OutputSignal()   # 输出信号

.. note::

    通过 ``GetWelderSignal()`` 接口获取 ``WelderSignal`` 对象，通过 ``.Input`` 和 ``.Output`` 分别访问输入和输出信号。

接口定义
*********

.. _单例与初始化:

单例与初始化
+++++++++++++

``GetInstance()``

.. code:: python

    def GetInstance() -> "WeldingSDK":

**功能：** 获取 WeldingSDK 的单例对象。

``__init__()``

.. code:: python

    def __init__(self) -> None:

**功能：** 构造函数，创建焊接工艺包对象。

``Int()`` 

.. code:: python

    def Init(self, ip: str = "") -> int:

**功能：** 初始化接口，用于与焊接工艺包后端建立长连接通讯。

``Destroy()`` 

.. code:: python

    def Destroy(self) -> int:

**功能：** 销毁实例对象，建议在程序停止时主动销毁。

启动摆焊
+++++++++

.. _启动Z字摆:

启动Z字摆
-----------

``WeaveZsine``

.. code:: python

    def WeaveZsine(self, 
               params: WeaveParams,
               weave_param: WeaveConfig = None,
               gradient: WeaveGradient = None,
               reserve_regs: ReserveRegisters = None) -> int:

**功能：** 开启Z字摆。

.. _启动其他摆型:

启动其他摆型
------------

.. note:: 

    启动其他摆型的方法与Z字摆接口模式相同。

* 启动平面三角摆： ``WeavePlaneTriangle()`` 
* 启动立焊三角摆： ``WeaveVerticalTriangle()``
* 启动梯形摆： ``WeaveTrapezoid()`` 
* 启动月牙摆： ``WeaveCrescent()`` 
* 启动正弦摆： ``WeaveSine()`` 
* 启动圆形摆： ``WeaveCircle()`` 
* 启动8字摆： ``WeaveFigure8()`` 

.. _结束摆焊:

结束摆焊
---------

.. code:: python

    def EndWeave(self) -> int:
    
**功能：** 停止摆焊。

.. _摆焊状态确认:

摆焊状态确认
-------------

.. code:: python

    def IsWeaving(self) -> Tuple[int, bool]: ...
    

* **功能：** 检查当前是否正在摆焊。
* **返回值：** ``True`` 表示正在摆焊， ``False`` 表示未摆焊。


.. _获取摆焊参数:

获取摆焊参数
-------------

.. code:: python

    def GetWeaveParams(self) -> Tuple[int, WeaveParams, WeaveConfig, WeaveGradient]:

**功能：** 获取上一次下发的摆焊参数。

.. _调节摆焊参数:

调节摆焊参数
------------

.. code:: python

    def AdjustWeaveParam(self, 
                     left_amplitude: float, 
                     right_amplitude: float, 
                     swing_frequency: float) -> int:

**功能：** 实时调整当前xx摆的参数。

焊机切换
+++++++++

``SwitchWelder()``

.. code:: python

    def SwitchWelder(model: WelderType, ip: str) -> None:

**功能：** 切换焊机品牌与型号，并指定焊机的网络地址。

**支持型号：** 
    .. list-table::
       :widths: 50 50          
       :header-rows: 1

       * - **品牌**
         - **列举**

       * - AOTAI
         - WelderType.ATR

       * - Megmeet
         - WelderType.Megmeet

       * - Kemppi
         - WelderType.Kemppi

       * - Fronius
         - WelderType.Fronius

       * - ESAB
         - WelderType.ESAB

**示例：**

.. code:: python

    # 切换到麦格米特 CM500R 焊机
    from jakaWeldingSDK import WelderType

    ret = welding.SwitchWelder(WelderType.Megmeet.ehave2_cm500r, "192.168.182.15")
    if ret != 0:
        print(f"焊机切换失败，错误码: {ret}")

焊机信号设置
+++++++++++++

.. code:: python

    def SetWelderStart(self, value: int) -> int:           # 引弧信号
    def SetWelderGas(self, value: int) -> int:             # 检气信号
    def SetWelderWireFeed(self, value: int) -> int:        # 送丝信号
    def SetWelderWireBack(self, value: int) -> int:        # 退丝信号
    def SetWelderErrorReset(self, value: int) -> int:      # 错误重置
    def SetWelderTouchEnable(self, value: int) -> int:     # 接触寻位使能
    def SetWelderJob(self, value: int) -> int:             # Job 号
    def SetWelderProgram(self, value: int) -> int:         # Program 号
    def SetWelderRobotReady(self, value: int) -> int:      # 机器人就绪
    def SetWelderWeldingMode(self, value: int) -> int:     # 焊接模式
    def SetWelderWireFeedRate(self, value: float) -> int:  # 送丝速度 / 电流
    def SetWelderCorrectVoltage(self, value: float) -> int:# 弧长修正电压
    def SetWelderWeldingEnable(self, value: int) -> int:   # 焊接使能
    def SetWelderSimulate(self, value: int) -> int:        # 模拟信号

**功能：** 向焊机发送控制信号。

.. attention::

    调用前需先通过 ``SwitchWelder()`` 完成焊机连接。

**示例：**

.. code:: python

    # 配置并启动焊接
    welding.SetWelderProgram(1)
    welding.SetWelderWeldingMode(1)         # 脉冲模式
    welding.SetWelderWireFeedRate(150.0)    # 送丝速度
    welding.SetWelderCorrectVoltage(2.5)    # 弧长修正
    welding.SetWelderRobotReady(1)
    welding.SetWelderWeldingEnable(1)
    welding.SetWelderStart(1)               # 引弧

焊机信号获取
+++++++++++++

``GetWelderSignal()``

.. code:: python

    def GetWelderSignal(self) -> Tuple[int, WelderSignal]:

**功能：** 获取焊机当前的输入输出信号状态。

**返回值：** 元组 ``(errno, WelderSignal)`` ，``errno`` 为 ``ERR_SUCC`` 表示成功。

**示例：**

.. code:: python

    ret, signal = welding.GetWelderSignal()
    if ret == 0:
        print(f"焊接模式: {signal.Input.welding_mode}")
        print(f"送丝速度: {signal.Input.wire_feed_rate}")
        print(f"实际电压: {signal.Output.actual_voltage}")
        print(f"实际电流: {signal.Output.actual_current}")

焊接任务参数
+++++++++++++

起弧任务参数
------------

.. code:: python

    def GetArconTaskParams(self, task_num: int) -> Tuple[int, ArconParams]:
    def SetArconTaskParams(self, task_num: int, params: ArconParams) -> int:

**功能：** 获取或设置指定任务编号的起弧参数。

**示例：**

.. code:: python

    arcon = jakaWeldingSDK.ArconParams()
    arcon.Prog = 1
    arcon.current = 120.0
    arcon.correct_voltage = 2.0
    arcon.welding_mode = 1
    arcon.success_sleep = 0.5
    welding.SetArconTaskParams(1, arcon)

焊接任务参数
------------

.. code:: python

    def GetWeldingTaskParams(self, task_num: int) -> Tuple[int, WeldingParams]:
    def SetWeldingTaskParams(self, task_num: int, params: WeldingParams) -> int:

**功能：** 获取或设置指定任务编号的焊接参数。

**示例：**

.. code:: python

    weld = jakaWeldingSDK.WeldingParams()
    weld.Prog = 1
    weld.current = 130.0
    weld.correct_voltage = 2.2
    weld.welding_mode = 1
    weld.welding_speed = 8.0
    welding.SetWeldingTaskParams(1, weld)

收弧任务参数
------------

.. code:: python

    def GetArcoffTaskParams(self, task_num: int) -> Tuple[int, ArcoffParams]:
    def SetArcoffTaskParams(self, task_num: int, params: ArcoffParams) -> int:

**功能：** 获取或设置指定任务编号的收弧参数。

**示例：**

.. code:: python

    arcoff = jakaWeldingSDK.ArcoffParams()
    arcoff.Prog = 1
    arcoff.current = 100.0
    arcoff.correct_voltage = 1.8
    arcoff.welding_mode = 1
    arcoff.welding_speed = 5.0
    arcoff.arcoff_sleep = 0.3
    arcoff.delay_gas_sleep = 1.0
    welding.SetArcoffTaskParams(1, arcoff)

JOB 任务参数
------------

.. code:: python

    def GetJobTaskParams(self, task_num: int) -> Tuple[int, JobParams]:
    def SetJobTaskParams(self, task_num: int, params: JobParams) -> int:

**功能：** 获取或设置指定任务编号的 JOB 参数。

**示例：**

.. code:: python

    job = jakaWeldingSDK.JobParams()
    job.job_number = 5
    job.current = 140.0
    job.correct_voltage = 2.0
    job.welding_mode = 0
    job.welding_speed = 10.0
    welding.SetJobTaskParams(1, job)

摆焊任务参数
------------

.. code:: python

    def GetWeaveTaskParams(self, task_num: int) -> Tuple[int, WeaveParams, WeaveGradient]:
    def SetWeaveTaskParams(self, task_num: int, params: WeaveParams, gradient: WeaveGradient) -> int:

**功能：** 获取或设置指定任务编号的摆焊参数与渐变参数。

.. attention::

    圆形摆和 8 字摆不支持渐变参数。

**示例：**

.. code:: python

    weave = jakaWeldingSDK.WeaveParams()
    weave.swing_mode = 11  # 正弦摆
    weave.left_amplitude = 3.0
    weave.right_amplitude = 3.0
    weave.swing_frequency = 1.5

    gradient = jakaWeldingSDK.WeaveGradient()
    gradient.left_amplitude = 1.0
    gradient.right_amplitude = 1.0
    gradient.swing_frequency = 0.5
    gradient.path_length = 20.0

    welding.SetWeaveTaskParams(1, weave, gradient)

位置叠加（Superpos）
*********************

.. code:: python

    def EnableSuperpos(self, velc: float, acc: float) -> int:
    def DisableSuperpos(self) -> int:
    def IsSuperposEnable(self) -> Tuple[int, bool]:
    def SetSuperposOffset(self, offset: list[float], coord_type: int) -> int:

**功能：** 在机器人运动的基础上叠加一个附加位移偏移，可用于实现横向跟踪补偿。

.. list-table:: 位置叠加接口说明
   :header-rows: 1
   :widths: 40 60

   * - 接口
     - 说明
   * - ``EnableSuperpos(velc, acc)``
     - 开启位置叠加，指定速度与加速度
   * - ``DisableSuperpos()``
     - 关闭位置叠加
   * - ``IsSuperposEnable()``
     - 查询叠加状态，返回 ``(errno, is_enable)``
   * - ``SetSuperposOffset(offset, coord_type)``
     - 下发偏移量 ``[x, y, z]`` （必须为 3 个浮点数）， ``coord_type`` ：0=当前用户坐标系，1=运动坐标系

.. attention::

    ``offset`` 列表必须恰好包含 3 个浮点数，否则抛出 ``ValueError``。

**示例：**

.. code:: python

    # 开启位置叠加
    ret = welding.EnableSuperpos(velc=50.0, acc=100.0)

    # 下发偏移量（在当前用户坐标系下，沿 X 方向偏移 2mm）
    ret = welding.SetSuperposOffset([2.0, 0.0, 0.0], 0)

    # 关闭位置叠加
    ret = welding.DisableSuperpos()

脚本生成
+++++++++

.. code:: python

    def GenerateInitScript(self) -> Tuple[int, str]:
    def GenerateProgArconScript(self, arcon_task: int, welding_task: int) -> Tuple[int, str]:
    def GenerateProgArcoffScript(self, arcoff_task: int) -> Tuple[int, str]:
    def GenerateJOBArconScript(self, arcon_task: int) -> Tuple[int, str]:
    def GenerateJOBArcoffScript(self) -> Tuple[int, str]:
    def GenerateStartWeaveScript(self, task_num: int) -> Tuple[int, str]:
    def GenerateEndWeaveScript(self) -> Tuple[int, str]:

**功能：** 将已配置的焊接任务参数生成为 JAKA 机器人控制器可执行的 JKS 脚本字符串。

.. list-table:: 脚本生成接口说明
   :header-rows: 1
   :widths: 40 60

   * - 接口
     - 说明
   * - ``GenerateInitScript()``
     - 生成初始化脚本
   * - ``GenerateProgArconScript()``
     - 基于 Program 模式生成起弧脚本
   * - ``GenerateProgArcoffScript()``
     - 基于 Program 模式生成收弧脚本
   * - ``GenerateJOBArconScript()``
     - 基于 JOB 模式生成起弧脚本
   * - ``GenerateJOBArcoffScript()``
     - 生成 JOB 模式收弧脚本
   * - ``GenerateStartWeaveScript()``
     - 生成开始摆焊脚本
   * - ``GenerateEndWeaveScript()``
     - 生成结束摆焊脚本

**返回值：** 元组 ``(errno, script)`` ， ``errno`` 为 ``ERR_SUCC`` 表示成功， ``script`` 为生成的 JKS 脚本字符串。

**示例：**

.. code:: python

    import pyweldingsdk

    sdk = pyweldingsdk.WeldingSDK()
    sdk.Init("192.168.0.35")

    # 设置起弧参数到任务 1
    arcon = pyweldingsdk.ArconParams()
    arcon.Prog = 1
    arcon.current = 180
    arcon.correct_voltage = 0
    arcon.success_sleep = 0.5
    arcon.welding_mode = 0  # 直流
    sdk.SetArconTaskParams(1, arcon)

    # 设置焊接参数到任务 1
    welding_p = pyweldingsdk.WeldingParams()
    welding_p.Prog = 1
    welding_p.current = 250
    welding_p.correct_voltage = 0
    welding_p.welding_mode = 0
    welding_p.welding_speed = 5
    sdk.SetWeldingTaskParams(1, welding_p)

    # 设置收弧参数到任务 1
    arcoff = pyweldingsdk.ArcoffParams()
    arcoff.Prog = 1
    arcoff.current = 220
    arcoff.correct_voltage = 0
    arcoff.welding_mode = 0
    arcoff.arcoff_sleep = 0
    arcoff.delay_gas_sleep = 0.5
    sdk.SetArcoffTaskParams(1, arcoff)

    # 拼接脚本并保存
    script = ""
    script += sdk.GenerateInitScript()[1]
    script += sdk.GenerateProgArconScript(arcon_task=1, welding_task=1)[1]
    script += sdk.GenerateStartWeaveScript(task_num=1)[1]
    script += sdk.GenerateProgArcoffScript(arcoff_task=1)[1]
    script += sdk.GenerateEndWeaveScript()[1]

    with open("Script.jks", "w", encoding="utf-8") as f:
        f.write(script)

    sdk.Destroy()

返回值说明
***********

所有接口均返回 ``int`` 错误码（ ``errno_t`` ）， ``0`` 表示成功，非零表示错误。

多返回值接口以 ``Tuple`` 方式返回， **第一个元素始终为错误码** ：

.. code:: python

    ret, params, config, gradient = sdk.GetWeaveParams()
    ret, is_weaving = sdk.IsWeaving()
    ret, signal = sdk.GetWelderSignal()







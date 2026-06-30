本节将介绍JAKA SDK（C++、Python）中定义的数据类型和API，主要适用于使用C++创建与虚拟或真实控制器通信的机器人应用程序的软件开发人员。对于需要了解JAKA机器人控制器应用程序的用户也会有一定帮助。

C++
#####

结构体定义
***********

.. _摆焊基本参数:

摆焊基本参数
++++++++++++++

``WeaveParams``

.. code:: cpp

    struct WeaveParams
    {
        int32_t swing_mode = 1;        // 摆动模式(1:Z字 2:平面三角 3:台型 4:月牙 5:立焊三角 11:正弦 12:圆形 13:8字)
        float swing_frequency = 1.5f;  // 摆动频率(Hz)，范围：0.1-10.0
        float right_amplitude = 3.0f;  // 右摆幅(mm)，范围：0-50.0
        float left_amplitude = 3.0f;   // 左摆幅(mm)，范围：0-50.0
        float radius = 0.0f;           // 摆长半径(mm)，范围：0-50.0，月牙、圆形、8字摆参数
        float left_dwell_time = 0.0f;  // 左停留时间(s)，范围：0-5.0
        float right_dwell_time = 0.0f; // 右停留时间(s)，范围：0-5.0
        float mid_dwell_time = 0.0f;   // 中停留时间(s) // 平面三角、立焊三角参数
        float elevation_angle = 0.0f;  // 纵角(°)，范围：–90-90
        float azimuth_angle = 0.0f;    // 横角(°)，范围：–90-90
        float center_rise = 0.0f;      // 中心抬升量(mm)，范围：–10-10
    };

.. note::

    ``swing_mode`` ：必须设置为对应的摆型编号。

    不同摆型使用不同的参数组合，未使用的参数可忽略或设为0。

.. _摆焊左右停留类型:

摆焊左右停留类型
+++++++++++++++++

``DwellDelayType``

.. code:: cpp

    enum class DwellDelayType : uint8_t
    {
        DWELL_STOP = 0, // 停止停留（默认）
        DWELL_MOVE = 1  // 运动中停留
    };

.. note::

    ``DWELL_STOP`` : 焊枪到达摆幅极限位置后停止运动，停留指定时间后再反向运动。Z字摆，三角摆，台形摆，月牙摆为此种停留方式。

    ``DWELL_MOVE`` : 焊枪到达摆幅极限位置后沿焊接方向继续运动，指定停留时间后再反向运动。正弦摆为此种停留方式。

.. _摆焊连接模式:

摆焊连接模式
+++++++++++++

``BlendWeaveEndMode``

.. code:: cpp

    enum class BlendWeaveEndMode : uint8_t
    {
        BLEND_NO = 0, // 不连接（默认）
        BLEND_YES = 1 // 平滑过渡
    };

.. note::

    ``BLEND_YES`` : 启用平滑过渡，即摆焊轨迹不强制经过中间点。目前仅支持这一种模式。

    ``BLEND_NO`` : 不启用平滑过渡，即摆焊轨迹强制经过中间点。

.. _摆焊平面选择:

摆焊平面选择
++++++++++++++

``WeaveFrameType``

.. code:: cpp

   enum class WeaveFrameType : uint8_t
    {
        PATH = 0, // 摆焊平面跟随焊枪
        TOOL = 1  // 摆焊平面跟随工件
    }; 

.. note::

    ``PATH = 0`` ：摆焊平面跟随焊枪末端，当前版本仅支持跟随焊枪。

    ``TOOL = 1`` ：摆焊平面跟随由起点和终点位置计算得出的工件平面，焊接过程中，机器人姿态会随之调整。

.. _摆焊轨迹定义:

摆焊轨迹定义
+++++++++++++

``WeaveConfig``

.. code:: cpp

    struct WeaveConfig
    {
        DwellDelayType dwell_delay_type = DwellDelayType::DWELL_STOP;     // 停留模式（正弦、圆形、8字摆动不支持停留模式）; 0:停止停留 1:运动中停留
        BlendWeaveEndMode blend_weave_end = BlendWeaveEndMode::BLEND_YES; // 摆焊连接（默认平滑过渡）; 0:不连接 1:平滑过渡
        WeaveFrameType frame_type = WeaveFrameType ::PATH;                // 摆焊平面跟随焊枪; 0:跟随焊枪 1:跟随工具
        int direction = 0;                                                // 起摆方向，默认先左（+Y）起摆; 0:left 1:right 
        uint8_t reserve[4] = {0};                                         // 预留参数（扩展用）
    };

.. _预留寄存器接口:

预留寄存器接口
++++++++++++++++

``ReserveRegisters``

.. code:: cpp

    struct ReserveRegisters
    {
        std::vector<float> float_regs;     // 浮点寄存器
        std::vector<int32_t> int_regs;     // 整型寄存器
        std::vector<std::string> str_regs; // 字符串寄存器
    };

.. _摆焊渐变参数:

摆焊渐变参数
+++++++++++++

``WeaveGradient``

.. code:: cpp

    struct WeaveGradient
    {
        float left_amplitude = 0.0f;   // 终点左摆幅(mm)，范围：0-50.0
        float right_amplitude = 0.0f;  // 终点右摆幅(mm)，范围：0-50.0
        float swing_frequency = 0.0f;  // 终点摆动频率(Hz)，范围：0.1-10.0
        float left_dwell_time = 0.0f;  // 左停留时间(s)，范围：0-5.0
        float right_dwell_time = 0.0f; // 右停留时间(s)，范围：0-5.0
        float path_length = 0.0f;      // 渐变路径长度
    };

.. attention::

    * 圆形摆和8字摆不支持焊接渐变参数。
    * 只有正弦摆需要设置渐变路径长度( ``path_length`` )参数。
    * 渐变过程是线性的，从当前值逐步变化到目标值。

.. _起弧参数:

起弧参数
+++++++++

``ArconParams``

.. code:: cpp

    struct ArconParams
    {
        int Prog = 0;                  // 焊接程序号
        float success_sleep = 0.0f;    // 引弧成功后等待时间（s）
        float current = 0.0f;          // 焊接电流（A）
        float correct_voltage = 0.0f;  // 弧长修正电压（V）
        int welding_mode = 0;          // 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
    };

.. _焊接参数:

焊接参数
+++++++++

``WeldingParams``

.. code:: cpp

    struct WeldingParams
    {
        int Prog = 0;                  // 焊接程序号
        float success_sleep = 0.0f;    // 引弧成功后等待时间（s）
        float current = 0.0f;          // 焊接电流（A）
        float correct_voltage = 0.0f;  // 弧长修正电压（V）
        int welding_mode = 0;          // 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
        float welding_speed = 0.0f;    // 焊接速度（mm/s）
    };

.. _收弧参数:

收弧参数
+++++++++

``ArcoffParams``

.. code:: cpp

    struct ArcoffParams
    {
        int Prog = 0;                  // 焊接程序号
        float success_sleep = 0.0f;    // 引弧成功后等待时间（s）
        float current = 0.0f;          // 焊接电流（A）
        float correct_voltage = 0.0f;  // 弧长修正电压（V）
        int welding_mode = 0;          // 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
        float welding_speed = 0.0f;    // 焊接速度（mm/s）
        float arcoff_sleep = 0.0f;     // 收弧等待时间（s）
        float delay_gas_sleep = 0.0f;  // 滞后送气时间（s）
    };

.. _JOB 参数:

JOB 参数
+++++++++

``JobParams``

.. code:: cpp

    struct JobParams
    {
        int job_number = 0;            // JOB 编号
        float current = 0.0f;          // 焊接电流（A）
        float correct_voltage = 0.0f;  // 弧长修正电压（V）
        int welding_mode = 0;          // 焊接模式：0:直流 1:脉冲 2:双脉冲 3:大熔深 4:低飞溅 5:快速脉冲
        float welding_speed = 0.0f;    // 焊接速度（mm/s）
    };

.. _接口说明:

接口说明
*********

.. _单例与初始化:

单例与初始化
+++++++++++++

``GetInstance`` 

.. code:: cpp

    static WeldingSwingSDK *GetInstance();

**功能：** 获取 SDK 的单例对象。

``Int()`` 

.. code:: cpp

    errno_t Init(const std::string ip = "");

**功能：** 初始化 SDK 并连接到机器人控制器。

``Destroy()`` 

.. code:: cpp

    errno_t Destroy();

**功能：** 销毁实例对象，建议在程序停止时主动销毁。

启动摆焊
+++++++++

启动Z字摆（ ``WeaveZsine`` ）
-----------------------------

.. code:: cpp

    errno_t WeaveZsine(
        const WeaveParams params,                                // 摆焊基本参数
        const WeaveConfig weave_param = WeaveConfig{},           // 摆焊配置（可选）
        const WeaveGradient gradient = WeaveGradient{},          // 渐变参数（可选，圆弧/八字摆不支持）
        const ReserveRegisters regs = ReserveRegisters{});       // 预留寄存器（可选）

**功能：** 启动Z字摆。

启动其他摆型
------------

.. note:: 

    启动其他摆型的方法与Z字摆接口模式相同。

* 启动平面三角摆： ``WeavePlaneTriangle`` 
* 启动立焊三角摆： ``WeaveVerticalTriangle``
* 启动梯形摆： ``WeaveTrapezoid`` 
* 启动月牙摆： ``WeaveCrescent`` 
* 启动正弦摆： ``WeaveSine`` 
* 启动圆形摆： ``WeaveCircle`` 
* 启动8字摆： ``WeaveFigure8`` 

结束摆焊
---------

.. code:: cpp

    errno_t EndWeave();

**功能：** 结束摆焊。

获取摆焊状态
-------------

.. code:: cpp

    errno_t IsWeaving(bool& is_weaving);

**功能：** 获取是否在执行摆焊。

获取摆焊参数
-------------

.. code:: cpp

    errno_t GetWeaveParams(WeaveParams &params, 
                           WeaveConfig &weave_param, 
                           WeaveGradient &gradient, 
                           ReserveRegisters &reserve_regs);

**功能：** 获取上一次下发的摆焊参数。

调节摆焊参数
--------------

.. code:: cpp

    errno_t AdjustWeaveParam(const float left_amplitude, 
                             const float right_amplitude, 
                             const float swing_frequency);

**功能：** 实时调整当前xx摆的参数。

焊机切换
+++++++++

``SwitchWelder``

.. code:: cpp

    errno_t SwitchWelder( WelderType type, const std::string& ip );

**功能：** 切换焊机品牌与型号，并指定焊机的网络地址。

**支持型号：** 
    .. list-table::
       :widths: 50 50          
       :header-rows: 1

       * - **品牌**
         - **列举**

       * - AOTAI
         - WelderType::ATR

       * - Megmeet
         - WelderType::Megmeet

       * - Kemppi
         - WelderType::Kemppi

       * - Fronius
         - WelderType::Fronius

       * - ESAB
         - WelderType::ESAB

**示例：**

.. code:: cpp

    // 切换至麦格米特 ehave2_cm500r 型号，IP 为 192.168.182.15
    welding.SwitchWelder(WelderType::Megmeet::ehave2_cm500r, "192.168.182.15");

设置焊机信号
++++++++++++++

.. code:: cpp

    errno_t SetWelderStart(int value),            // 引弧信号，0:关闭 1:开启
    errno_t SetWelderGas(int value),              // 检气信号，0:关闭 1:开启
    errno_t SetWelderWireFeed(int value),         // 送丝信号，0:关闭 1:开启
    errno_t SetWelderWireBack(int value),         // 退丝信号，0:关闭 1:开启
    errno_t SetWelderErrorReset(int value),       // 错误重置信号，0:关闭 1:开启
    errno_t SetWelderTouchEnable(int value),      // 接触寻位使能，0:关闭 1:开启
    errno_t SetWelderJob(int value),              // 设置 Job 号
    errno_t SetWelderProgram(int value),          // 设置 Program 号
    errno_t SetWelderRobotReady(int value),       // 机器人就绪信号，0:未就绪 1:就绪
    errno_t SetWelderWeldingMode(int value),      // 焊接模式, 范围0~5
    errno_t SetWelderWireFeedRate(float value),   // 送丝速度/电流，取决于焊机所支持设置的参数
    errno_t SetWelderCorrectVoltage(float value), // 弧长修正
    errno_t SetWelderWeldingEnable(int value),    // 焊接使能，0:关闭 1:开启
    errno_t SetWelderSimulate(int value);         // 调试模式使能，0:关闭 1:开启

**功能：** 向焊机发送控制信号，用于启停焊接、调节参数、切换模式等操作。

.. attention::

    * 在调用焊机信号设置接口前，必须先通过 ``SwitchWelder`` 完成焊机切换与连接。
    * 引弧信号（ ``SetWelderStart`` ）和焊接使能（ ``SetWelderWeldingEnable`` ）需按正确的时序调用，否则可能导致起弧失败。

获取焊机信号
++++++++++++++

``GetWelderSignal``

.. code:: cpp

    errno_t GetWelderSignal(WelderSignal& signal);

**功能：** 获取焊机当前的输入输出信号状态。

焊接任务参数
+++++++++++++

起弧任务参数
-------------

.. code:: cpp

    errno_t GetArconTaskParams(int task_num, ArconParams &params);
    errno_t SetArconTaskParams(int task_num, const ArconParams params);

**功能：** 获取或设置指定任务编号的起弧参数。

**参数：**

- ``task_num`` ：任务编号，用于区分不同的焊接任务。
- ``params`` ：起弧参数结构体，见 :ref:`起弧参数` 。

**示例：**

.. code:: cpp

    // 设置起弧参数
    ArconParams arcon;
    arcon.Prog = 1;
    arcon.current = 120.0f;
    arcon.correct_voltage = 2.0f;
    arcon.welding_mode = 1; 
    arcon.success_sleep = 0.5f;
    welding.SetArconTaskParams(1, arcon);

    // 获取起弧参数
    ArconParams readback;
    welding.GetArconTaskParams(1, readback);

焊接任务参数
------------

.. code:: cpp

    errno_t GetWeldingTaskParams(int task_num, WeldingParams &params);
    errno_t SetWeldingTaskParams(int task_num, const WeldingParams params);

**功能：** 获取或设置指定任务编号的焊接参数。

**参数：**

- ``task_num`` ：任务编号，用于区分不同的焊接任务。
- ``params`` ：焊接参数结构体，见 :ref:`焊接参数` 。

**示例：**

.. code:: cpp

    WeldingParams weld;
    weld.Prog = 1;
    weld.current = 130.0f;
    weld.correct_voltage = 2.2f;
    weld.welding_mode = 1;
    weld.welding_speed = 8.0f;  // 焊接速度 8 mm/s
    welding.SetWeldingTaskParams(1, weld);

收弧任务参数
------------

.. code:: cpp

    errno_t GetArcoffTaskParams(int task_num, ArcoffParams &params);
    errno_t SetArcoffTaskParams(int task_num, const ArcoffParams params);

**功能：** 获取或设置指定任务编号的收弧参数。

**参数：**

- ``task_num`` ：任务编号，用于区分不同的焊接任务。
- ``params`` ：收弧参数结构体，见 :ref:`收弧参数` 。

**示例：**

.. code:: cpp

    ArcoffParams arcoff;
    arcoff.Prog = 1;
    arcoff.current = 100.0f;
    arcoff.correct_voltage = 1.8f;
    arcoff.welding_mode = 1;
    arcoff.welding_speed = 5.0f;
    arcoff.arcoff_sleep = 0.3f;      // 收弧等待 0.3s
    arcoff.delay_gas_sleep = 1.0f;   // 滞后送气 1.0s
    welding.SetArcoffTaskParams(1, arcoff);

JOB 任务参数
------------

.. code:: cpp

    errno_t GetJobTaskParams(int task_num, JobParams &params);
    errno_t SetJobTaskParams(int task_num, const JobParams params);

**功能：** 获取或设置指定任务编号的 JOB 参数。

**参数：**

- ``task_num`` ：任务编号，用于区分不同的焊接任务。
- ``params`` ：JOB 参数结构体，见 :ref:`JOB 参数` 。

**示例：**

.. code:: cpp

    JobParams job;
    job.job_number = 5;
    job.current = 140.0f;
    job.correct_voltage = 2.0f;
    job.welding_mode = 0;  // 直流模式
    job.welding_speed = 10.0f;
    welding.SetJobTaskParams(1, job);

摆焊任务参数
------------

.. code:: cpp

    errno_t GetWeaveTaskParams(int task_num, WeaveParams &params, WeaveGradient &gradient);
    errno_t SetWeaveTaskParams(int task_num, const WeaveParams params, const WeaveGradient gradient);

**功能：** 获取或设置指定任务编号的摆焊参数与渐变参数。

**参数：**

- ``task_num`` ：任务编号，用于区分不同的焊接任务。
- ``params`` ：摆焊基本参数结构体，见 :ref:`摆焊基本参数` 。
- ``gradient`` ：摆焊渐变参数结构体，见 :ref:`摆焊渐变参数` 。

.. attention::

    圆形摆和 8 字摆不支持渐变参数，调用 ``SetWeaveTaskParams`` 时 ``gradient`` 参数将被忽略。

**示例：**

.. code:: cpp

    // 设置摆焊任务参数（正弦摆 + 渐变）
    WeaveParams weave;
    weave.swing_mode = 11;           // 正弦摆
    weave.left_amplitude = 3.0f;
    weave.right_amplitude = 3.0f;
    weave.swing_frequency = 1.5f;
    weave.left_dwell_time = 0.3f;
    weave.right_dwell_time = 0.3f;

    WeaveGradient gradient;
    gradient.left_amplitude = 1.0f;      // 终点左摆幅 1mm
    gradient.right_amplitude = 1.0f;     // 终点右摆幅 1mm
    gradient.swing_frequency = 0.5f;     // 终点频率 0.5Hz
    gradient.path_length = 20.0f;        // 渐变路径长度 20mm

    welding.SetWeaveTaskParams(1, weave, gradient);

脚本生成
+++++++++

.. code:: cpp

    errno_t GenerateInitScript(std::string& script);
    errno_t GenerateProgArconScript(int arcon_task, int welding_task, std::string& script);
    errno_t GenerateProgArcoffScript(int arcoff_task, std::string& script);
    errno_t GenerateJOBArconScript(int arcon_task, std::string& script);
    errno_t GenerateJOBArcoffScript(std::string& script);
    errno_t GenerateStartWeaveScript(int task_num, std::string& script);
    errno_t GenerateEndWeaveScript(std::string& script);

**功能：** 将已配置的焊接任务参数生成为 JAKA 机器人控制器可执行的 JKS 脚本字符串。

.. list-table:: 脚本生成接口说明
   :header-rows: 1
   :widths: 40 60

   * - **接口**
     - **说明**
   * - ``GenerateInitScript``
     - 生成初始化脚本，包含 SDK 与焊机连接初始化指令
   * - ``GenerateProgArconScript``
     - 基于 Program 模式生成起弧脚本，需指定起弧任务编号和焊接任务编号
   * - ``GenerateProgArcoffScript``
     - 基于 Program 模式生成收弧脚本，需指定收弧任务编号
   * - ``GenerateJOBArconScript``
     - 基于 JOB 模式生成起弧脚本，需指定起弧任务编号
   * - ``GenerateJOBArcoffScript``
     - 生成 JOB 模式收弧脚本
   * - ``GenerateStartWeaveScript``
     - 生成开始摆焊脚本，需指定摆焊任务编号
   * - ``GenerateEndWeaveScript``
     - 生成结束摆焊脚本

.. note::

    * 脚本生成前，需先通过对应的 ``SetXxxTaskParams`` 接口完成参数配置。
    * 生成的脚本字符串可直接写入 ``.jks`` 文件，导入机器人控制器执行。
    * 脚本生成顺序应与实际焊接流程一致：初始化 → 起弧 → 摆焊 → 收弧。

**示例：**

.. code:: cpp

    //生成并保存脚本
    std::string script;
    std::ofstream outfile("./Script.jks");

    welding.GenerateInitScript(script);
    outfile << script;

    welding.GenerateProgArconScript(1, 1, script);
    outfile << script;

    welding.GenerateProgArcoffScript(1, script);
    outfile << script;

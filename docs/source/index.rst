
===============================
rqrobot |version| Documentation
===============================

..  image:: https://img.shields.io/travis/ricequant/rqrobot/master.svg
    :target: https://travis-ci.org/ricequant/rqrobot/branches
    :alt: Build

..  image:: https://coveralls.io/repos/github/ricequant/rqrobot/badge.svg?branch=master
    :target: https://coveralls.io/github/ricequant/rqrobot?branch=master

..  image:: https://readthedocs.org/projects/rqrobot/badge/?version=stable
    :target: http://rqrobot.readthedocs.io/zh_CN/stable/?badge=stable
    :alt: Documentation Status

..  image:: https://img.shields.io/pypi/v/rqrobot.svg
    :target: https://pypi.python.org/pypi/rqrobot
    :alt: PyPI Version

..  image:: https://img.shields.io/pypi/l/rqrobot.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: License

..  image:: https://img.shields.io/pypi/pyversions/rqrobot.svg
    :target: https://pypi.python.org/pypi/rqrobot
    :alt: Python Version Support


rqrobot 从数据获取、算法交易、回测引擎，实盘模拟，实盘交易到数据分析，为程序化交易者提供了全套解决方案。

rqrobot 具有灵活的配置方式，强大的扩展性，用户可以非常容易地定制专属于自己的程序化交易系统。

.. note::

    rqrobot 所有的策略都可以直接在 `Ricequant`_ 上进行回测和实盘模拟，并且可以通过微信和邮件实时推送您的交易信号。`Ricequant`_ 是一个开放的量化算法交易社区，为程序化交易者提供免费的回测和实盘模拟环境，并且会不间断举行实盘资金投入的量化比赛。

特点
============================

======================    =================================================================================
易于使用                    让您集中于策略的开发，一行简单的命令就可以执行您的策略。
完善的文档                   您可以直接访问 `rqrobot 文档`_ 或者 `Ricequant 文档`_ 来获取您需要的信息。
活跃的社区                   您可以通过访问 `Ricequant 社区`_ 获取和询问有关 rqrobot 的一切问题，有很多优秀的童鞋会解答您的问题。
稳定的环境                   每天都有会大量的算法交易在 Ricequant 上运行，无论是 rqrobot，还是数据，我们能会做到问题秒处理，秒解决。
灵活的配置                   您可以使用多种方式来配置和运行策略，只需简单的配置就可以构建适合自己的交易系统。
强大的扩展性                 开发者可以基于我们提供的 Mod Hook 接口来进行扩展。
======================    =================================================================================

Mod
============================

rqrobot 提供了极具拓展性的 Mod Hook 接口，这意味着开发者可以非常容易的对接第三方库。

您可以通过如下方式使用 安装和使用Mod:

..  code-block:: bash

    # 查看当前安装的 Mod 列表及状态
    $ rqrobot mod list
    # 安装 Mod
    $ rqrobot mod install xxx
    # 卸载 Mod
    $ rqrobot mod uninstall xxx
    # 启用 Mod
    $ rqrobot mod enable xxx
    # 禁用 Mod
    $ rqrobot mod disable xxx

以下是目前已经集成的 Mod 列表:

======================    ==================================================================================
Mod名                      说明
======================    ==================================================================================
`sys_analyser`_           【系统模块】记录每天的下单、成交、投资组合、持仓等信息，并计算风险度指标，并以csv、plot图标等形式输出分析结果
`sys_funcat`_             【系统模块】支持以通达信公式的方式写策略
`sys_progress`_           【系统模块】在控制台输出当前策略的回测进度。
`sys_risk`_               【系统模块】对订单进行事前风控校验
`sys_simulation`_         【系统模块】支持回测、撮合、滑点控制等
`sys_stock_realtime`_     【系统模块】Demo 模块，用于展示如何接入自有行情进行回测/模拟/实盘
`vnpy`_                   【第三方模块】通过 VNPY 对接期货实盘行情和实盘交易
`sentry`_                 【第三方模块】集成 sentry 的扩展，实现错误日志全自动采集、处理
`tushare`_                【第三方模块】Demo Mod，用于展示如何通过tushare 获取实时Bar数据并组装以供rqrobot使用
`shipane`_                【第三方模块】集成实盘易SDK，用于对接股票实盘跟单交易
======================    ==================================================================================

.. note::

    如果您基于 rqrobot 进行了 Mod 扩展，欢迎告知我们。在审核通过后，会在 Mod 列表中添加相关信息。

获取帮助
============================

关于rqrobot的任何问题可以通过以下途径来获取帮助

*  可以通过 `索引`_ 或者使用搜索功能来查找特定问题
*  在 `Github Issue`_ 中提交issue
*  rqrobot 交流群「487188429」


.. _Github Issue: https://github.com/ricequant/rqrobot/issues
.. _Ricequant: https://www.ricequant.com/algorithms
.. _rqrobot 文档: http://rqrobot.readthedocs.io/zh_CN/latest/
.. _Ricequant 文档: https://www.ricequant.com/api/python/chn
.. _Ricequant 社区: https://www.ricequant.com/community/category/all/
.. _FAQ: http://rqrobot.readthedocs.io/zh_CN/latest/faq.html
.. _索引: http://rqrobot.readthedocs.io/zh_CN/latest/genindex.html

.. _rqrobot 介绍: http://rqrobot.readthedocs.io/zh_CN/latest/intro/overview.html
.. _安装指南: http://rqrobot.readthedocs.io/zh_CN/latest/intro/install.html
.. _10分钟学会 rqrobot: http://rqrobot.readthedocs.io/zh_CN/latest/intro/tutorial.html
.. _策略示例: http://rqrobot.readthedocs.io/zh_CN/latest/intro/examples.html

.. _API: http://rqrobot.readthedocs.io/zh_CN/latest/api/base_api.html

.. _如何贡献代码: http://rqrobot.readthedocs.io/zh_CN/latest/development/make_contribute.html
.. _基本概念: http://rqrobot.readthedocs.io/zh_CN/latest/development/basic_concept.html
.. _rqrobot 基于 Mod 进行扩展: http://rqrobot.readthedocs.io/zh_CN/latest/development/mod.html
.. _History: http://rqrobot.readthedocs.io/zh_CN/latest/history.html
.. _TODO: https://github.com/ricequant/rqrobot/blob/master/TODO.md
.. _develop 分支: https://github.com/ricequant/rqrobot/tree/develop
.. _master 分支: https://github.com/ricequant/rqrobot
.. _rqrobot_mod_sys_stock_realtime: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_stock_realtime/README.rst
.. _rqrobot_mod_tushare: https://github.com/ricequant/rqrobot-mod-tushare
.. _通过 Mod 扩展 rqrobot: http://rqrobot.io/zh_CN/latest/development/mod.html
.. _sys_analyser: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_analyser/README.rst
.. _sys_funcat: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_funcat/README.rst
.. _sys_progress: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_progress/README.rst
.. _sys_risk: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_risk/README.rst
.. _sys_simulation: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_simulation/README.rst
.. _sys_stock_realtime: https://github.com/ricequant/rqrobot/blob/master/rqrobot/mod/rqrobot_mod_sys_stock_realtime/README.rst
.. _vnpy: https://github.com/ricequant/rqrobot-mod-vnpy
.. _sentry: https://github.com/ricequant/rqrobot-mod-sentry
.. _tushare: https://github.com/ricequant/rqrobot-mod-tushare
.. _shipane: https://github.com/wh1100717/rqrobot-mod-ShiPanE

.. toctree::
    :caption: 基础
    :hidden:

    intro/overview
    intro/install
    intro/tutorial
    intro/examples
    intro/detail_install
    intro/virtual_machine


.. toctree::
    :caption: API
    :hidden:

    api/base_api
    api/extend_api


.. toctree::
    :caption: IPython
    :hidden:
    :maxdepth: 3
    :glob:

    notebooks/run-rqrobot-in-ipython.ipynb


.. toctree::
    :caption: 进阶
    :hidden:

    intro/run_algorithm
    intro/under_ide
    intro/optimizing_parameters


.. toctree::
    :caption: 开发
    :hidden:

    development/make_contribute
    development/basic_concept
    development/mod
    development/event_source
    development/data_source


.. toctree::
    :caption: 其他
    :hidden:

    history

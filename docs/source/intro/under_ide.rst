.. _intro-under-ide:


==============================
通过 PyCharm 运行/调试
==============================


下载并搭建PyCharm环境
====================================


有众多Python IDE（集成开发环境）可以供您选择，但我们强烈建议您使用PyCharm，一方面PyCharm的功能强大且简洁易用，另一方面以下文档我们也选择PyCharm作为样例。

您可以在选择在官网下载PyCharm：https://www.jetbrains.com/pycharm/

选择community版本即可，如您有需要也可以购买专业版。

安装好以后我们十分建议您将主题颜色更改为【Darcula】，没有什么，就是看着爽。

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/pycharm-theme.png


在PyCharm下搭建开发环境
====================================

我们假设您已经使用Anaconda搭建虚拟环境【rqrobot】，同时您已经成功安装了rqrobot并能成功运行。

如您在安装中遇到问题，请参考： :ref:`intro-install`


1.新建一个项目：
-----------------------------------------

File→ New Project, 比如项目叫做rqrobot-strategy

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/create-project.jpeg

.. warning::

    在 Windows 环境下，并不存在 `bin` 目录，Interpreter 请指定 `\\anaconda\\envs\\rqrobot\\Scripts\\python.exe`


2.对项目进行对应的python解释器的虚拟环境配置：
---------------------------------------------------

PyCharm Community Edition → Preferences → Project: rqrobot-strategy → Project Interpreter, 然后选择您创建的conda的虚拟环境，这个例子里面的话是放在：~/anaconda/envs/rqrobot/bin/python:

.. image:: https://github.com/ricequant/rq-resource/blob/master/rqrobot/preferences.jpeg?raw=true

项目创建好以后，新建立一个简单的 :code:`rqrobot` 策略吧，比如叫做 :code:`test.py`: 右键点击rqrobot-strategy项目→ New→ File→ test.py:

在test.py策略里面import所有的rqrobot支持的API: :code:`from rqrobot.api import *`，那么可以享受到代码的自动补全了:

策略必须添加 :code:`init,before_trading,ha`ndle_bar` 函数来补全整个策略：

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/import.jpeg


3.配置运行的命令行rqrobot的在conda环境中的位置：
----------------------------------------------------

.. warning::

    在 Windows 环境下

    如果是 Python 2.7 则没有对应的入口脚本，需要找到对应的 `__main__.py` 文件，参考路径: `c:\\Users\\xxx\\Anaconda2\\envs\\rqrobot2_7\\lib\\site-packages\\rqrobot\\__init__.py`

    如果是 Python 3.5 及以上，在 `/Scripts/` 目录下是存在 `rqrobot-script.py` 文件的，其可以作为入口文件。参考路径: `C:\\Users\\xxx\\Anaconda2\\envs\\rqrobot3_5\\Scripts\\rqrobot-script.py`

    相关 issue 讨论 请参考 `Issue 7 <https://github.com/ricequant/rqrobot/issues/7>`_

Run/Debug Configurations → 选择策略文件 → Configuration → Script → 找到对应的conda环境的rqrobot命令

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/config-one.jpeg

配置rqrobot-plus run的命令行：Run/Debug Configurations → 选择策略文件 → Configuration → Script parameters

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/config-two.jpeg

Python interpreter 内容可按以下格式并修改您对应的参数:

.. code-block:: bash

    run -f rqrobot-strategy/test.py -d /Users/your_count/.rqrobot/bundle -s 2016-06-01 -e 2016-12-01 --account stock 100000 --benchmark 000300.XSHG

注意：您需要运行的策略应当填写您当前project目录下的策略，bundle目录您可以通过在命令行中获取绝对路径填入。


4.配置完成运行测试：
--------------------------------------------

配置完成后点击运行

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/run.jpeg

.. image:: https://raw.githubusercontent.com/ricequant/rq-resource/master/rqrobot/after-run.jpeg
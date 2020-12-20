步骤2：在cmd中执行telnet www.baidu.com 80， 然后可以看到一个黑色的框框（首先要确保自己的PC可以访问www.baidu.com哈）

    步骤3： 然后按 ctrl + ], 退出， 结果为：

                  欢迎使用 Microsoft Telnet Client

                  Escape 字符是 'CTRL+]'

                  Microsoft Telnet>

    步骤4： 然后按enter, 进入到输入框， 又是黑漆漆的一片

    步骤5：输入如下内容（有时间限制， 所以最好是先写好， 然后整体拷贝进去）

                GET /index.html HTTP/1.1
                Host: www.baidu.com

    步骤6：然后连续按两下enter键盘， 得到的结果为：
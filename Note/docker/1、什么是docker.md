什么是Docker？

Docker是基于Go语言实现的开源容器项目，一个不包含`linux`内核，而又精简的`linux`系统



##### Docker三大核心：

##### 镜像：

类似一个只读的模板，状态是只读的，可以在一个镜像的上层创建多个容器



##### 容器：

容器是通过镜像创建的，通过容器来运行应用，容器间是相互隔离的，容器是包括了root权限、进程、用户、网络和其中应用程序的盒子，在只读的模板上创建一个可写层

创建一个容器，就是在镜像上创建一个读写层，如果在容器中修改一个文件，是在读写层copy一份儿镜像中的文件来进行修改的，不是修改镜像中的源文件

一个镜像可以创建多个容器，在容器中的改动不会影响镜像



##### 仓库：

存放镜像的地方，类似于代码仓库，在仓库注册服务器中存放着多个仓库，仓库分为公开仓库和私有仓库，可以通过类似`git`的`push`命令将镜像推送到仓库，通过`pull`将镜像下载到本地
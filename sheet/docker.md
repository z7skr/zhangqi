[Docker —— 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

口号：Build, Ship, and Run Any App, Anywhere.

简单理解：轻量级的虚拟机，共用同一个内核，只需要隔离应用和所需的运行库。

几个概念：

- 镜像（Image）
- 容器（Container）
- 仓库（Repository）

仓库里有很多镜像，一个镜像可以复制出一个容器，容器里包含了应用和所需的运行库、环境变量等等。

Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。 镜像不包含任何动态数据，其内容在构建之后也不会被改变。

镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等 。容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。前面讲过镜像使用的是分层存储，容器也是如此。按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据 ，容器存储层要保持无状态化。所有的文件写入操作，都应该使用数据卷（Volume）、或者绑定宿主目录，在这些位置的读写会跳过容器存储层，直接对宿主(或网络存储)发生读写，其性能和稳定性更高。数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。因此， 使用数据卷后，容器可以随意删除、重新 run ，数据却不会丢失。




1、镜像搜索：
docker search centos
2、下载镜像：
docker pull http://docker.io/centos
3、镜像导入：
docker load -i /home/centos7.6.tar
4、容器保存镜像：
docker commit 6d5ced342f8d centos7.6ssh
5、镜像导出，语法：docker save -o 导出的镜像名.tar 本地镜像名：镜像标签
docker save -o docker.io-centos-httpd-docker-image.tar http://docker.io/centos:httpd
6、镜像依赖关系查看：
docker image inspect —format=’{{.RepoTags}} {{.Id}} {{.Parent}}’ $(docker image ls -q —filter since=470671670cac)
7、删除镜像：
docker rmi IMAGE ID
8、镜像重命名：
docker tag IMAGE ID “镜像名称”
docker tag 4e3a dsj_tc7_catalog9111:latest
docker rmi “镜像旧名称” #删除旧的镜像
9、Docker cp 命令
—将/www/runoob目录拷贝到容器96f7f14e99ab的/www目录下。
docker cp /www/runoob 96f7f14e99ab:/www/
—将/www/runoob目录拷贝到容器96f7f14e99ab中，目录重命名为www。
docker cp /www/runoob 96f7f14e99ab:/www


```bash
docker
    attach      Attach local standard input, output, and error streams to a running contain
    er
    build       Build an image from a Dockerfile
    commit      Create a new image from a container's changes
    cp          Copy files/folders between a container and the local filesystem
    create      Create a new container
    diff        Inspect changes to files or directories on a container's filesystem        
    events      Get real time events from the server
    exec        Run a command in a running container
    export      Export a container's filesystem as a tar archive
    history     Show the history of an image
    images      List images
    import      Import the contents from a tarball to create a filesystem image
    info        Display system-wide information
    inspect     Return low-level information on Docker objects
    kill        Kill one or more running containers
    load        Load an image from a tar archive or STDIN
    login       Log in to a Docker registry
    logout      Log out from a Docker registry
    logs        Fetch the logs of a container
    pause       Pause all processes within one or more containers
    port        List port mappings or a specific mapping for the container
    ps          List containers
    pull        Pull an image or a repository from a registry
    push        Push an image or a repository to a registry
    rename      Rename a container
    restart     Restart one or more containers
    rm          Remove one or more containers
    rmi         Remove one or more images
    run         Run a command in a new container
    save        Save one or more images to a tar archive (streamed to STDOUT by default)   
    search      Search the Docker Hub for images
    start       Start one or more stopped containers
    stats       Display a live stream of container(s) resource usage statistics
    stop        Stop one or more running containers
    tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
    top         Display the running processes of a container
    unpause     Unpause all processes within one or more containers
    update      Update configuration of one or more containers
    version     Show the Docker version information
    wait        Block until one or more containers stop, then print their exit codes

docker
    config      Manage Docker configs
        create      Create a config from a file or STDIN
        inspect     Display detailed information on one or more configs
        ls          List configs
        rm          Remove one or more configs
    container   Manage containers
        attach      Attach local standard input, output, and error streams to a running contain
        er
        commit      Create a new image from a container's changes
        cp          Copy files/folders between a container and the local filesystem
        create      Create a new container
        diff        Inspect changes to files or directories on a container's filesystem        
        exec        Run a command in a running container
        export      Export a container's filesystem as a tar archive
        inspect     Display detailed information on one or more containers
        kill        Kill one or more running containers
        logs        Fetch the logs of a container
        ls          List containers
        pause       Pause all processes within one or more containers
        port        List port mappings or a specific mapping for the container
        prune       Remove all stopped containers
        rename      Rename a container
        restart     Restart one or more containers
        rm          Remove one or more containers
        run         Run a command in a new container
        start       Start one or more stopped containers
        stats       Display a live stream of container(s) resource usage statistics
        stop        Stop one or more running containers
        top         Display the running processes of a container
        unpause     Unpause all processes within one or more containers
        update      Update configuration of one or more containers
        wait        Block until one or more containers stop, then print their exit codes 
    image       Manage images
        build       Build an image from a Dockerfile
        history     Show the history of an image
        import      Import the contents from a tarball to create a filesystem image
        inspect     Display detailed information on one or more images
        load        Load an image from a tar archive or STDIN
        ls          List images
        prune       Remove unused images
        pull        Pull an image or a repository from a registry
        push        Push an image or a repository to a registry
        rm          Remove one or more images
        save        Save one or more images to a tar archive (streamed to STDOUT by default)   
        tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
    network     Manage networks
        connect     Connect a container to a network
        create      Create a network
        disconnect  Disconnect a container from a network
        inspect     Display detailed information on one or more networks
        ls          List networks
        prune       Remove all unused networks
        rm          Remove one or more networks
    system      Manage Docker
        df          Show docker disk usage
        events      Get real time events from the server
        info        Display system-wide information
        prune       Remove unused data
    volume      Manage volumes
        create      Create a volume
        inspect     Display detailed information on one or more volumes
        ls          List volumes
        prune       Remove all unused local volumes
        rm          Remove one or more volumes
```
docker run -itd -v D:\docker\linux:/root --name linux ubuntu
docker run -itd -v /root:/root --net=host --name xxx 23456789 /bin/bash
docker exec -it 3320e9efd0af17fa99f4c0ad38be17bb3a22ce4c4268ccb27901fc01ab4a2223 bash


```bash
# 拉取镜像
docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
```
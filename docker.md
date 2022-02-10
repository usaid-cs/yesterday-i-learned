## Terms

- **Docker Engine**: consists of two parts: a daemon, a _server_ process that manages all the _containers_, and a _client_, which acts as a remote control for the daemon.
- **Container**: Process in a box. The box contains everything the process needs to run, including the filesystem, shell, and libraries. They are not enabled by default.
- ** Virtual machine**: The hardware virtualises a VM at the hardware level. This is unlike containers, which are virtualised by the operating system.
- **Commit**: Save changes made to the container.

### Fun facts

- [**Containers are simply isolated processes**](https://www.youtube.com/watch?v=cjXI-yxqGTI) (rather than isolated "machines") that only see what they need to see. Containers are powered by two features in the linux kernel: **namespaces**, which allow container processes to appear as if they are running on their own operating system, and **cgroups**, which limit the amount of resource a container can access.

## When to use Docker

- The fact that it is good enough for everyone, and that people tend to know what they are looking at when they read a Dockerfile, means that you can probably use it whenever you want, even when [other tools are better](https://nixos.org/).

## [When not to use Docker](https://www.reddit.com/r/docker/comments/982cag/docker_for_development_why_and_how/)

- You application runs only on Windows or macOS.
- Your application is tightly coupled to the OS (like needing direct access to CPU or memory).
- Your application is a GUI.
- Docker Swarm is simpler than Kubernetes, but it is not recommended anymore. It is easy to use, but [it won't scale](https://news.ycombinator.com/item?id=28460258), at least not as well as Kubernetes clusters.

## Get started

- Docker has pre-built images; run `docker search (name)` to find them, and `docker pull (user)/(name)` get them.
- To run something in a container, run `docker run (user)/(name) (command)`.
- Run ubuntu with `sudo docker run -it ubuntu bash`. See that it is running using `sudo docker ps`. But once you exit from the shell, the container dies; every time you run `sudo docker run -it ubuntu bash`, you get a brand new user in a brand new shell. It would appear that `-i` is interactive, and `-t` is terminal.
- To install something in a container, run `docker run (user)/(name) apt-get install -y ...`. The `-y` is required because docker commands cannot be interactive.
- To view a list of commands run in the container, run `docker ps -l`. It shows you IDs of states after the commands are run.
- To _commit_ a container, run `docker commit (id from above) (new container name e.g. foo/bar)`. Now you can `docker run foo/bar`.
- To inspect a container, run `docker inspect (id from above)`.
- If you sign up for a Docker account, you can push your own images onto the repository using `docker push (container name e.g. foo/bar)`.
- The advantage Vagrant has over Docker is: [full isolation](https://www.upguard.com/articles/docker-vs-vagrant). Docker cannot guarantee the virtual hardware that the environment gets.
- Minikube can be started using `minikube start`. Minikube runs a docker cluster inside a VM, so it may take a while.

## [`Dockerfile`](https://docs.docker.com/get-started/part2/#define-a-container-with-a-dockerfile)

`Dockerfile`s are essentially scripts that define what you will install, what the container will run, and what ports the container will expose. Read the damn guide. There is also that [example file](book-summaries/Dockerfile) you can look at. It does not include required files to run the example Flask app.

- In the same directory with `Dockerfile`, running `sudo docker build -t (your container name in all lowercase) .` will build a new container. Check if you actually built one with `docker images`. Note that `python:2.7-slim` is a base container that does not imply ubuntu... in fact [they](https://hub.docker.com/_/python/) are mostly Debian and Windows ones.
- Run `sudo docker run -p 4000:80 (your container name)` to run it. You access the container's port 80 from your own port 4000.
- Alternatively, with `-d`, `sudo docker run -p 4000:80 (your container name)` runs the container in detached mode. With detached mode, you can run your container and close the terminal afterwards, and your container will continue to run.
- Container IDs come in short and long forms. The long form is LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONG, and the short form is only LOOOOOOOOOO.
- [There is no difference between `docker ps` and `docker container ls`.](https://stackoverflow.com/a/45254760/1558430) Both list your containers.
- [`VOLUME /foo`](https://docs.docker.com/storage/volumes/) creates some kind of mount at... some place's `/foo`. The container can access `/foo` and see files there. Then `/foo` is never deleted, and the same container can see the volume again when it restarts. Where is `/foo` actually? `/var/lib/docker/volumes/`. You can find them with `docker volume ls`.
- `RUN` is a step inside the dockerfile that runs commands inside a docker image. [`CMD`](https://nickjanetakis.com/blog/docker-tip-7-the-difference-between-run-and-cmd) defines a default thing to run when the container starts (usually as the command that runs your application server), but doesn't run the `CMD` when the image is being built.
- Each `RUN` adds a layer of IO diffs that may increase the final image size. So geniuses at stack overflow recommend [running everything with a single `RUN` statement](https://stackoverflow.com/questions/39223249/multiple-run-vs-single-chained-run-in-dockerfile-which-is-better) where it makes sense.
- It is perhaps best to [`COPY` your files into the container *last*](https://semaphoreci.com/blog/2018/03/14/docker-image-size.html), to minimise the size of the diff you get from every build.

## Docker compose

- [While `Dockerfile`](https://stackoverflow.com/questions/29480099/docker-compose-vs-dockerfile-which-is-better) helps you _build_ an image, docker [compose](https://docs.docker.com/glossary/?term=Compose) helps you run applications that use multiple containers.
- If you don't know how to use docker compose, you can actually find [official cheat sheets](https://docs.docker.com/samples/django/) that gets you started.

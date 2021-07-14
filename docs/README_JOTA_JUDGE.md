# Setting JOTA Judge

*Last Update: 14. Jul. 2021*

**DMOJ judge official docs**: https://docs.dmoj.ca/#/judge/setting_up_a_judge

## 시작하기 전 필독
* **JCloud와 JOTA Site 설정을 마친 후 진행할 수 있습니다. 아직 설치하지 않았다면 [여기서부터](https://github.com/hyunchan-park/JOTA-dmoj-online-judge) 시작하십시오.**
* 반드시 공식 문서를 읽으면서 진행하십시오. 명령어는 아래의 수정된 명령어를 참고하세요.
* 본인의 github 계정에서 해당 repository를 **fork** 하십시오: https://github.com/hyunchan-park/JOTA-dmoj-judge-server
* judge 서버를 열기 위한 새 SSH 연결 세션을 만듭니다. (세션 #3)
## Setting up a Judge
original: https://docs.dmoj.ca/#/judge/setting_up_a_judge?id=setting-up-a-judge

1. JOTA Site (e.g. http://localhost:8001/) 에 접속합니다.
2. admin 계정으로 로그인합니다. admin 계정을 임의로 만들지 않은 경우 아래의 정보로 접속 가능합니다. 상황에 따라 비밀번호를 변경해야 할 수도 있습니다.
    ```
    ID = admin
    PW = admin
    ```

## Site-side setup
original: https://docs.dmoj.ca/#/judge/setting_up_a_judge?id=site-side-setup

```
$ sudo apt update
$ sudo apt install supervisor
$ sudo supervisorctl status
```

## Judge-side setup
original: https://docs.dmoj.ca/#/judge/setting_up_a_judge?id=judge-side-setup

* Jota에 업로드할 problems를 위하여 디렉토리 생성
    
    ```
    $ cd ~/jota
    ~/jota$ mkdir problems
    ```
    
* fork 했던 저장소를 `judge` 폴더 안에 저장
    
    ```
    ~/jota$ git clone --recursive https://github.com/<your-github-id>/JOTA-dmoj-judge-server judge
    ~/jota$ cd judge
    ```

**Docker 또는 PyPI** 중 택일하면 됩니다. (**PyPI** 를 권장합니다. Docker 는 테스트하지 않았습니다.)

## With Docker
original: https://docs.dmoj.ca/#/judge/setting_up_a_judge?id=with-docker

* `docker` 패키지 설치 (버전에 따라 택일)
    
    ```
    $ sudo snap install docker     # version 19.03.13, or
    $ sudo apt  install docker.io  # version 20.10.2-0ubuntu1~20.04.2
    ```
    
* docker 실행 예 #1
    ```
    ~/jota$ cd judge/.docker
    ~/jota/judge/.docker$ sudo make judge-tier1
    ~/jota/judge/.docker$ docker run \
                            -v /home/ubuntu/jota/problems:/problems \
                            --cap-add=SYS_PTRACE \
                            dmoj/judge-tier1:latest \
                            cli -c /problems/judge.yml
    ```

* docker 실행 예 #2
    ```
    $ docker run \
        --name judge \
        -p "$(ip addr show dev enp1s0 | perl -ne 'm@inet (.*)/.*@ and print$1 and exit')":9998:9998 \
        -v /home/ubuntu/jota/problems:/problems \
        --cap-add=SYS_PTRACE \
        -d \
        --restart=always \
        dmoj/judge-tier1:latest \
        run -p "$PORT" -c /problems/judge.yml \
        "$IP" "$JUDGE_NAME" "$JUDGE_AUTHENTICATION_KEY"
    ```

## Through PyPI
### **Installing the prerequisites**
original: https://docs.dmoj.ca/#/judge/setting_up_a_judge?id=installing-the-prerequisites

```
$ sudo apt install python3-dev python3-pip build-essential libseccomp-dev
$ sudo pip3 install dmoj
```

### **Configuring the judge**
original: https://docs.dmoj.ca/#/judge/setting_up_a_judge?id=configuring-the-judge

* `judge.yml` 파일 만들기
  
  1. 양식 파일을 생성합니다.
      ```
      ~/jota/judge$ { printf "id: \nkey: \"\"\nproblem_storage_root:\n  - /home/ubuntu/jota/problems\n" ; dmoj-autoconf ; } > judge.yml
      ```
  
  2. vi 명령어 혹은 Code-Server 상에서 `~/jota/judge/judge.yml` 파일을 수정합니다.
      ```
      ~/jota/judge$ vi judge.yml
      ```
      
  3. JOTA Site 오른쪽 상단 admin 페이지로 접속합니다.
  
  4. `Submissions > Judges` 선택합니다. ( `제출 > 채점기 ` )
  
  5. `judge` 를 추가합니다.
  
  6. `judge` 이름을 설정합니다. (e.g. JOTA-Judge)
  
  7. `Regenerate` 버튼을 눌러 `Authentication key` 를 생성합니다.
  
  8. `Name` 과 `Authentication key` 에 해당하는 값을 `judge.yml` 에 입력 후 설정을 저장합니다.
  
      ```
      id: <judge name>
      key: "<judge authentication key>"
      problem_storage_root:
      - /home/ubuntu/jota/problems
      runtime:
      ...
      ```
  
  9. 수정된 `judge.yml` 파일을 저장합니다.
  
* judge를 사이트에 붙이기 전 CLI judge 테스트 후 `Ctrl+C` 입력하여 종료 
    ```
    ~/jota/judge$ dmoj-cli -c judge.yml
    Self-testing executors
    Self-testing AWK:    Success [0.005s, 1012 KB]   awk 1.3.4
    Self-testing BF:     Success [0.004s, 536 KB]    bf 1.33.7
    Self-testing C:      Success [0.005s, 536 KB]    gcc 9
    Self-testing C11:    Success [0.003s, 536 KB]    gcc11 9
    Self-testing CPP03:  Success [0.003s, 1612 KB]   g++ 9
    Self-testing CPP11:  Success [0.006s, 1612 KB]   g++11 9
    Self-testing CPP14:  Success [0.004s, 1612 KB]   g++14 9
    Self-testing CPP17:  Success [0.003s, 1612 KB]   g++17 9
    Self-testing GAS64:  Success [0.002s, 4 KB]      as_x64 2.34, ld_x64 2.34
    Self-testing PERL:   Success [0.017s, 6020 KB]   perl 5.30.0
    Self-testing PY3:    Success [0.029s, 9368 KB]   python3 3.8.10
    Self-testing SED:    Success [0.006s, 796 KB]    sed 4.7
    Self-testing TEXT:   Success [0.004s, 1932 KB]   cat 8.30
    Running local judge...
    dmoj>
    ```
    
* judge 서버 열기
    ```
    ~$ dmoj -c ~/jota/judge/judge.yml localhost
    ```
    
* judge 서버 열기 (`local_settings.py` 내 BRIDGED_JUDGE_ADDRESS 항목 수정한 경우)
    
    ```
    ~$ dmoj -c ~/jota/judge/judge.yml -p "$PORT" "$IP"
    ```

✅ 연결된 judge 서버

![judge-01.png](res/judge-01.png)

❌ 연결되지 않은 judge 서버

![judge-02.png](res/judge-02.png)

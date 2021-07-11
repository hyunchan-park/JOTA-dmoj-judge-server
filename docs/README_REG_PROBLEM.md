# Registering Problem

**DMOJ official docs**: https://docs.dmoj.ca/#/problem_format/problem_format

**DMOJ official examples**: https://github.com/DMOJ/docs/tree/master/problem_examples

## 시작하기 전 필독
* 반드시 공식 문서를 읽으면서 진행하십시오.
* 여기서는 **aplusb** 문제를 예제로 설명합니다.

## 문제 등록하기

1. JOTA admin page에서 문제를 등록합니다.

2. jota/problems 디렉토리로 이동합니다.
    ```
    ~$ cd jota/problems
    ```

3. `Problem Code` 의 값을 이름으로 한 디렉토리를 만듭니다.
   ```
   ~/jota/problems$ mkdir aplusb
   ~/jota/problems$ cd aplusb
   ~/jota/problems/aplusb$
   ```

4. 테스트케이스 데이터 `tc_data.zip` 를 다운로드합니다. `curl`로 다운로드 하면 judge가 파일을 읽지 못하므로 `wget`로 다운로드 하십시오.
    ```
    ~/jota/problems/aplusb$ wget -o tc_data.zip https://github.com/DMOJ/docs/raw/master/problem_examples/standard/aplusb/aplusb.zip
    ```

5. `init.yml` 을 생성하고 아래의 내용을 기입 후 저장합니다.
    ```
    ~/jota/problems/aplusb$ vi init.yml
    ```
    ```
    archive: tc_data.zip
    test_cases:
    - {in: aplusb.1.in, out: aplusb.1.out, points: 5}
    - {in: aplusb.2.in, out: aplusb.2.out, points: 20}
    - {in: aplusb.3.in, out: aplusb.3.out, points: 75}
    ```
    * archive: 테스트케이스 데이터를 담고 있는 압축 파일
    * test_cases: {in: 입력파일, out: 출력파일, points: 점수}

6. JOTA Web에서 문제를 제출하고 채점 결과가 올바르게 나오는지 확인합니다.

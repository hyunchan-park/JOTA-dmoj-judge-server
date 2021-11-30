# JOTA diff visualizer

## introduction
* 유저 `Output`과 정답 `Output`에 대해 `Diff`를 수행하여 그 결과를 시각적으로 보여줍니다.
* `diff` 라이브러리는 [google/diff-match-patch](https://github.com/google/diff-match-patch)을 사용하였습니다.

## How it works
### On Judge
* **dmoj/graders/standard.py**
    * `extended_feedback`을 통해 `Answer Output`을 `Site`로 보냅니다.

### On Site
* **judge/views/submission.py**
    * `group_test_cases`에서 `cases`에 대한 루프마다 두 `output`의 `diff`결과를 연산하여 `diff[]`에 각 `case`의 결과를 저장하고 리턴합니다.
    * `group_test_cases`에서 리턴한 `diff`를 `context`에 `'diff_result'`를 키로 갖도록 넣습니다.
* **status_testcases.html**
    * `view`에서 받은 `diff_result`를 `patch`에 알맞게 보여줍니다.

## FrontEnd Document
[Link](https://github.com/hyunchan-park/JOTA-dmoj-online-judge/blob/master/docs/FrontVisualization.md)
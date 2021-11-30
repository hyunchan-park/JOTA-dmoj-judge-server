# JOTA diff visualizer

## introduction
* 유저 Output과 정답 Output에 대해 Diff를 수행하여 그 결과를 시각적으로 보여줍니다.
* diff 라이브러리는 [google/diff-match-patch](https://github.com/google/diff-match-patch)을 사용하였습니다.

## How it works
### On Judge
* **dmoj/graders/standard.py**
    * extended_feedback을 활용하여 Answer Output을 Site로 보냅니다.

### On Site
* **judge/views/submission.py**
    * group_test_cases에서 cases에 대한 루프마다 두 output의 diff결과를 연산하여 diff[]에 각 case의 결과를 저장하고 리턴합니다.
    * group_test_cases에서 리턴한 diff를 context에 'diff_result'를 키로 갖도록 넣습니다.
* **status_testcases.html**
    * view에서 받은 diff_result를 patch에 알맞은 색을 보여줍니다.
# 🎮 Game Hub

콘솔에서 즐기는 미니 게임 모음입니다. (GitHub 협업 실습 프로젝트)

## 실행 방법

```bash
python -m venv venv
# Windows: venv\Scripts\activate    /  macOS·Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 팀원 소개

> **[충돌 지점 ③]** 자기 이름 줄을 채워 주세요. (모두 같은 표를 고치므로 충돌이 납니다!)

| 역할 | 이름 | GitHub ID | 담당 |
|---|---|---|---|
| A | 한재원 | hanjaewon182 | 팀장 · `main.py`, `utils.py`, README, 병합 관리 |
| B | 홍성민|seongminhong497-cell| `games/hangman.py` (행맨) |
| C | 이민서 | minseo9904 | `games/baseball.py` (숫자 야구) |
| D | Manvika | themanvika | `games/rps.py` (가위바위보) |
| E | 한재원 | hanjaewon182 | `games/tictactoe.py` (틱택토) |

## 게임 목록

| 게임 | 설명 | 상태 |
|---|---|---|
| 행맨 | 영어 단어를 한 글자씩 맞히는 게임, 6번 틀리면 실패 | ✅ |
| 숫자 야구 | 서로 다른 숫자 3개를 최대 9번에 맞히는 게임 | ✅ 완료 |
| 가위바위보 | 컴퓨터와 3판 2선승제 대결 | ✅ |
| 틱택토 | 칸 번호(1~9)로 X·O를 번갈아 놓아 한 줄을 먼저 완성하면 승리 | ✅ |

## 협업 규칙

- `main` 브랜치에는 **직접 push 하지 않습니다.** 반드시 Pull Request!
- 브랜치 이름: `feature/<게임이름>` (예: `feature/hangman`)
- 커밋 메시지: `feat:` `fix:` `test:` `docs:` `chore:` 로 시작 (예: `feat: 행맨 글자 마스킹 함수 추가`)
- PR은 **다른 팀원 1명 이상의 승인** 후 병합합니다.
- 비밀번호·토큰·`.env`는 절대 커밋하지 않습니다.
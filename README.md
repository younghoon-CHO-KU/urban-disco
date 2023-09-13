# SWIS

## app.py 마지막 라인에서 포트랑 ip를 설정하셔야 합니다.

flask:2.3.3

서버 컴퓨터에서 받은 이미지, 텍스트는 static/image, static/prompt, static/question, static/subtitle에 저장되고, 새로운 응답이 오면 지워지고, 새로 받은 파일들이 남습니다.

## 사용방법

테스트 단말기로 지정한.ip.주소.번호:포트번호 로 inference.py가 실행중인 상황에서 들어가면 됩니다.
입력 창에 원하는 텍스트를 입력하고, 원하는 장면 수를 선택한 이후 돋보기를 누르고, 2분 뒤에 확인하기 버튼을 누르면 사진과 텍스트가 보입니다.

[![Screenshot from 2023-08-25 11-25-08](https://github.com/younghooncho2000/urban-disco/assets/121843325/5cf25246-83de-4cf1-8a39-04b368df23a6)](https://user-images.githubusercontent.com/121843325/267658019-5d2fdafe-c81f-4734-a3c3-295c825975a6.png)

접속시 해당 화면이 나타나고, 문장 입력 칸에 원하는 문장을 입력하세요. 예시로 해당 이미지에서는 "부모님과 도서관에 가는 이야기를 들려줘" 로 작성했습니다.
이후 하단에서 원하는 장면의 갯수를 입력하고, 엔터 또는 돋보기 버튼을 입력하면 이에 대한 정보가 기록됩니다.
이후 일정 시간이 지나 사진, 텍스트들이 도착하면   

## ( 아래 사진은 화면 확대 비율을 30%로 해서 과장되게 보입니다)

![Screenshot from 2023-08-25 11-28-18](https://github.com/younghooncho2000/urban-disco/assets/121843325/b8b9c8bd-b8d4-4e1b-8548-1b8ee0b830ca)

위와 같은 결과를 확인할 수 있습니다.

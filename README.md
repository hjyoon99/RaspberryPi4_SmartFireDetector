# raspberrypi4 프로젝트
## 라즈베리파이4를 활용한 스마트 화재감지기

## 개요
> 온도를 측정하고 화재를 감지해 미리 대피하거나, 대처가 가능하다면 인명 및 재산피해 방지에 큰 도움 가능.
> 화재 감지 뿐 아니라 온도 측정도 가능하기에 고온으로 인한 인명피해도 대비 가능.

![스크린샷 2024-07-01 121938](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/cbe30e81-e346-4e7e-8feb-e1d37a975386)

## 프로젝트 설명

1. 온습도를 계속 측정하면서 설정온도(40도) 이하이면 초록불 1개 점등.
2. 설정온도 (40도)가 넘어가면 빨간불 1개 점등. 카메라 찰칵
3. 만약 불꽃감지센서 인식 시 빨간불 1개 더 점등.
4. 빨간불 2개 점등 후 PIR통해 움직임 감지 시 카메라 찰칵
5. 화재로 감지, 대피명령 출력

![스크린샷 2024-07-01 122025](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/a79e4fdf-9b8d-4775-9b45-3236eb64d8b9)

![image](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/32aa8adf-6e62-407f-a7fe-6c06fd751f77)


## 사용 모듈

- 불꽃감지센서
- PIR
- DHT11 온습도센서
- 카메라 모듈
- 빨간색, 초록색 LED
- 점퍼선
- 브레드보드

![스크린샷 2024-07-01 122009](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/39709307-5c9e-4a75-bfc1-31a6c8d67618)

![image](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/3e58b2b2-8acf-4db4-bf6e-7ab7532d4a50)


## 회로도

![스크린샷 2024-06-01 184237](https://github.com/hjyoon99/raspberrypi4/assets/108658882/3f6581c7-bb92-4409-a44b-603c22fd8e51)

** 여기서 카메라 모듈은 라즈베리파이4의 카메라 연결 모듈에 따로 연결
![카메라2](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/6bef289b-f936-41cb-b9aa-6e9d4ade9314)



## 실행방법

1. 회로도에 맞게 브레드보드 이용 또는 라즈베리 파이와 바로 연결
2. 라즈베리파이 원격접속 
3. 라즈베리파이 내부 IDE인 지니를 이용해서 해당 첨부코드를 python파일로 저장
4. 터미널에서 해당 파일의 디렉토리에 들어가서 실행
5. 잘 출력되는지 확인

## 실행

1. 전체 
![라즈베리_전체2](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/03d112dc-cc0d-4f7f-998e-5c4223438e6c)


2. 불꽃센서
![불꽃센서2](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/d7d8cafa-579f-4a4b-b894-799d99c89473)

![불꽃감지2](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/b64e08da-300c-4b85-b1bd-239ad47ef1af)

3. 정상온도 시 녹색불
![라즈베리 초기](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/672813d7-1c3f-41a9-95c8-ca2b7165f259)

4. 고온감지 시 출력
![고온감지](https://github.com/hjyoon99/RaspberryPi4_SmartFireDetector/assets/108658882/693159e8-4293-408f-806a-3096c9a11994)

## 시연 영상 링크
https://youtu.be/IBntoSquE1A?si=kuTLsrx5bo-TmGfy

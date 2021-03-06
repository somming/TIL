## 가상 환경 사용하기

### 가상 환경을 사용하는 이유

파이썬을 사용하다 보면 pip로 패키지를 설치하게 되는데, 이 패키지들은 파이썬 설치 디렉토리의 Lib/site-packages 안에 저장된다.
그래서 pip로 설치한 패키지는 모든 파이썬 스크립트에서 사용할 수 있게 된다.

평소에는 이런 방식이 큰 문제가 없지만 프로젝트를 여러 개 개발할 때는 패키지의 버전 문제가 발생할 수 있다.

프로젝트 A에서는 패키지X 1.5를 사용해야 하고, 프로젝트 B에서는 패키지X 2.0을 사용해야 하는 경우가 생긴다. 
이 패키지X 1.5와 2.0이 호환이 되지 않는다면 개발하기가 상당히 불편해진다.

이 문제를 해결하기 위해 파이썬에서는 가상 환경을 제공한다.
가상 환경은 독립된 공간을 만들어주는 기능이다.

가상 환경에서 pip로 패키지를 설치하면 가상 환경 폴더(디렉터리)의 Lib/site-packages 안에 패키지를 저장해준다.

프로젝트 각각에 가상 환경을 만들어 사용하므로 버전 문제가 발생하지 않는다.

``` $ sudo apt install python3-venv ```

```
$ mkdir ~/myproject
$ cd ~/myproject
```

``` $ python3 -m venv myprojectenv ```

이제 Python의 로컬 사본이 설치되고 프로젝트 디렉토리 내에 myprojectenv라는 디렉토리에 pip가 저장된다.


```$ source myprojectenv/bin/activate```

가상환경 활성화
이 상태에서 스크립트 파일을 실행하면 현재 가상 환경 안에 있는 파이썬 인터프리터와 패키지를 사용하게 된다.

-----

### 패키지 목록 관리하기 

가상 환경에 설치된 패키지는 목록을 저장해 두었다가 나중에 다시 설치할 수 있다. 

``` $ pip freeze > requirements.txt ```

패키지 목록과 버전 정보를 requirements.txt 파일에 저장한다.

``` $ pip install -r requirements.txt ```

requirements.txt 파일의 내용대로 패키지를 설치한다.
import matplotlib.font_manager as fm
def add_font():
    ## 폰트 이름
    title_font_name = 'NanumGothic'

    ## 폰트 경로
    font_path = './NanumGothic.ttf'
    ## 폰트 사이즈
    font_size = 30

    ## FontProperties 인스턴스 생성
    font_prop = fm.FontProperties(fname=font_path, size=font_size)
    return font_prop

print(add_font())
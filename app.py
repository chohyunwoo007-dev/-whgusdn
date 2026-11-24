import streamlit as st

st.set_page_config(
    page_title="맞춤 식단 추천 프로그램",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 나만의 맞춤 식단 추천")
st.write("키와 몸무게, 운동 목적에 따른 맞춤 식단을 추천합니다.")

st.divider()


# 1. 영양소 계산 함수
def calculate_nutrition(height, weight, purpose):

    if purpose == "다이어트":
        protein = weight * 1.8
        carbohydrate = weight * 6

    elif purpose == "벌크업":
        protein = weight * 2.2
        carbohydrate = weight * 9

    else:
        protein = 0
        carbohydrate = 0

    protein_meal = protein / 3
    carbohydrate_meal = carbohydrate / 3

    return protein, carbohydrate, protein_meal, carbohydrate_meal


# 2. 다이어트 추천 음식 리스트
diet_foods = [
    "닭가슴살 - 지방이 적고 단백질이 풍부함",
    "달걀흰자 - 단백질 공급에 좋음",
    "대구 - 저지방 고단백 생선",
    "두부 - 식물성 단백질 공급",
    "브로콜리 - 식이섬유와 비타민 풍부",
    "양배추 - 식이섬유 공급",
    "고구마 - 탄수화물 공급",
    "그릭요거트 - 단백질 공급",
    "오이 - 수분이 풍부한 채소",
    "버섯 - 식이섬유가 풍부함"
]


# 3. 벌크업 추천 음식 리스트
bulk_foods = [
    "소고기 - 단백질과 철분 공급",
    "연어 - 단백질과 오메가3 공급",
    "닭다리살 - 단백질과 에너지 공급",
    "계란 - 단백질과 지방 공급",
    "현미밥 - 탄수화물 공급",
    "오트밀 - 탄수화물과 식이섬유 공급",
    "고구마 - 에너지 공급",
    "바나나 - 운동 전후 탄수화물 공급",
    "아몬드 - 건강한 지방과 열량 공급",
    "우유 - 단백질과 칼슘 공급",
    "그릭요거트 - 단백질 공급",
    "통밀빵 - 탄수화물 공급"
]


# 4. 목적별 음식 추천 함수
def recommend_foods(purpose):

    if purpose == "다이어트":
        return diet_foods

    elif purpose == "벌크업":
        return bulk_foods

    else:
        return []


# 5. 사용자 정보 입력
st.header("📋 나의 신체 정보")

height = st.number_input(
    "키를 입력하세요 (cm)",
    min_value=100.0,
    max_value=230.0,
    value=170.0,
    step=1.0
)

weight = st.number_input(
    "몸무게를 입력하세요 (kg)",
    min_value=20.0,
    max_value=300.0,
    value=65.0,
    step=0.5
)

purpose = st.selectbox(
    "운동 목적을 선택하세요",
    ["다이어트", "벌크업"]
)


# 6. 식단 구성 버튼
if st.button("🍽️ 식단 구성하기", use_container_width=True):

    protein, carbohydrate, protein_meal, carbohydrate_meal = calculate_nutrition(
        height, weight, purpose
    )

    foods = recommend_foods(purpose)

    st.divider()
    st.header("📊 나의 식단 구성 결과")

    st.success("선택한 운동 목적: " + purpose)

    # 신체 정보
    st.subheader("나의 신체 정보")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("키", f"{height:.1f} cm")

    with col2:
        st.metric("몸무게", f"{weight:.1f} kg")

    # 하루 영양소
    st.subheader("하루 영양소 섭취량")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("하루 단백질", f"{protein:.1f} g")

    with col4:
        st.metric("하루 탄수화물", f"{carbohydrate:.1f} g")

    # 한 끼 영양소
    st.subheader("🍚 한 끼당 영양소 섭취량")

    col5, col6 = st.columns(2)

    with col5:
        st.metric("한 끼 단백질", f"{protein_meal:.1f} g")

    with col6:
        st.metric("한 끼 탄수화물", f"{carbohydrate_meal:.1f} g")

    st.caption("하루 3끼 기준으로 균등하게 나눈 양입니다.")

    # 목적별 추천 음식
    st.divider()

    if purpose == "다이어트":
        st.subheader("🥗 다이어트 추천 음식")
        st.write("저지방 고단백 식품과 채소를 중심으로 구성했습니다.")

    elif purpose == "벌크업":
        st.subheader("💪 벌크업 추천 음식")
        st.write("근육 성장과 에너지 공급에 활용하기 좋은 식품입니다.")

    # 반복문으로 음식 출력
    for index, food in enumerate(foods, start=1):
        st.write(f"{index}. {food}")

    st.divider()

    st.info("균형 잡힌 식단과 꾸준한 운동을 실천해 보세요.")

st.caption("※ 영양소 수치는 설정한 계산 기준에 따른 참고용 수치입니다.")

<<<<<<< HEAD
import json
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "prompts.json")


def load_prompts():
    """prompts.json 파일에서 프롬프트 목록을 불러오는 함수"""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_prompts(prompts):
    """프롬프트 목록을 prompts.json 파일에 저장하는 함수"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


default_prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "제품의 특징을 살린 매력적인 썸네일 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 10년 경력의 IT 컨설턴트입니다. 사용자의 문제를 분석하고 해결 방법을 제안해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]


def add_default_prompts(prompts):
    existing_titles = [prompt["title"] for prompt in prompts]

    for default_prompt in default_prompts:
        if default_prompt["title"] not in existing_titles:
            prompts.append(default_prompt.copy())

    return prompts


print("프롬프트 관리 프로그램 시작!")

prompts = load_prompts()
prompts = add_default_prompts(prompts)

while True:
    print("\n===== 프롬프트 관리 메뉴 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 프롬프트 검색")
    print("4. 프롬프트 삭제")
    print("5. 저장")
    print("6. 카테고리별 조회")
    print("0. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        title = input("프롬프트 제목: ")
        content = input("프롬프트 내용: ")
        category = input("카테고리: ")

        prompt = {
            "title": title,
            "content": content,
            "categories": [category]
        }

        prompts.append(prompt)
        print("프롬프트가 추가되었습니다.")

    elif choice == "2":
        if len(prompts) == 0:
            print("저장된 프롬프트가 없습니다.")
        else:
            for index, prompt in enumerate(prompts, start=1):
                print(f"{index}. {prompt['title']} - {prompt['content']}")

    elif choice == "3":
        keyword = input("검색할 키워드를 입력하세요: ")
        found = False

        for index, prompt in enumerate(prompts, start=1):
            if keyword in prompt["title"] or keyword in prompt["content"]:
                print(f"{index}. {prompt['title']} - {prompt['content']}")
                found = True

        if found == False:
            print("검색 결과가 없습니다.")

    elif choice == "4":
        if len(prompts) == 0:
            print("삭제할 프롬프트가 없습니다.")
        else:
            print("\n삭제할 프롬프트를 선택하세요.")
            for index, prompt in enumerate(prompts, start=1):
                print(f"{index}. {prompt['title']} - {prompt['content']}")

            delete_number = input("삭제할 번호를 입력하세요: ")

            if delete_number.isdigit():
                delete_index = int(delete_number) - 1

                if 0 <= delete_index < len(prompts):
                    deleted_prompt = prompts.pop(delete_index)
                    save_prompts(prompts)

                    print(f"'{deleted_prompt['title']}' 프롬프트가 삭제되었습니다.")
                else:
                    print("존재하지 않는 번호입니다.")
            else:
                print("숫자를 입력해야 합니다.")
                
    elif choice == "5":
        save_prompts(prompts)
        print("저장되었습니다.")
        print("다시 메뉴로 돌아갑니다.")

    elif choice == "6":
        category = input("카테고리를 입력하세요: ")
        found = False

        for index, prompt in enumerate(prompts, start=1):
            if category in prompt.get("categories", []):
                print(f"{index}. {prompt['title']} - {prompt['content']}")
                found = True

        if not found:
            print("해당 카테고리에 속하는 프롬프트가 없습니다.")

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")
=======
# 프롬프트 데이터
prompts = [
    {"title": "번역 요청", "content": "다음 문장을 영어로 번역해줘: "},
    {"title": "코드 리뷰", "content": "다음 코드의 문제점을 찾아줘: "},
    {"title": "요약 정리", "content": "다음 글을 3줄로 요약해줘: "},
]

# 프롬프트 목록을 보기 좋게 출력하는 함수
def show_prompts():
    print("\n===== 프롬프트 목록 =====")
    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. [{prompt['title']}] {prompt['content']}")
    print("=======================\n")

# 함수 호출 (실행)
show_prompts()
>>>>>>> bd5e4bd (3-2 완료)

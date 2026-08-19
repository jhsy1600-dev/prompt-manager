print("프롬프트 관리 프로그램 시작!")

prompts = []

while True:
	print("\n===== 프롬프트 관리 메뉴 =====")
	print("1. 프롬프트 추가")
	print("2. 프롬프트 목록 보기")
	print("0. 종료")

	choice = input("메뉴를 선택하세요: ")

	if choice == "1":
		title = input("프롬프트 제목: ")
		content = input("프롬프트 내용: ")

		prompt = {
			"title": title,
			"content": content
		}

		prompts.append(prompt)
		print("프롬프트가 추가되었습니다.")

	elif choice == "2":
		if len(prompts) == 0:
			print("저장된 프롬프트가 없습니다.")
		else:
			for index, prompt in enumerate(prompts, start=1):
				print(f"{index}. {prompt['title']} - {prompt['content']}")

	elif choice == "0":
		print("프로그램을 종료합니다.")
		break

	else:
		print("잘못된 메뉴입니다. 다시 선택하세요.")

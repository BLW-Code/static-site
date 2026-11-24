from textnode import TextNode, TextType


def main():
    type_1 = TextType.PLAIN
    example_1 = TextNode("hello world", type_1)
    type_2 = TextType.LINK
    example_2 = TextNode("learn more", type_2, "https://www.boot.dev")
    print(example_1)
    print(example_2)

if __name__ == "__main__":
    main()
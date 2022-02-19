def list_benefits() -> list:
    return [
        'More organized code',
        'More readable code',
        'Easier code reuse',
        'Allowing programmers to share and connect code together'
    ]


def build_sentence(benefit: str) -> str:
    return f'{benefit} is a benefit of functions!'


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


def foo(a, b, c, *args) -> int:
    return len(args)


def bar(a, b, c, **kwargs) -> bool:
    return kwargs['magicnumber'] == 7


if __name__ == '__main__':
    name_the_benefits_of_functions()
    assert foo(1, 2, 3, 4) == 1
    assert foo(1, 2, 3, 4, 5) == 2
    assert bar(1, 2, 3, magicnumber=6) is False
    assert bar(1, 2, 3, magicnumber=7) is True

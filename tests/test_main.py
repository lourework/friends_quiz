from src.main import main


def test_main_output(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from quiz!" in captured.out


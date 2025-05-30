# import allure
# import pytest
#
#
# class TestDebug(object):
#
#     @pytest.mark.smoke
#     def test_001(self):
#         print("001")
#
#     @allure.story("asdasdas")
#     @pytest.mark.parametrize("a, b", [(1, 1), (2, 2)])
#     @pytest.mark.smoke
#     @pytest.mark.run(order=1)
#     def test_002(self, a, b):
#         print(a, b)
#
#     @pytest.mark.smoke
#     def test_003(self):
#         print("003")
#
#     @allure.story("asdasdas")
#     @pytest.mark.parametrize("a, b", [(1, 1), (2, 2)])
#     @pytest.mark.smoke
#     @pytest.mark.run(order=3)
#     def test_004(self, a, b):
#         print(a, b)

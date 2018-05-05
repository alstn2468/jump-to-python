# 패키지 안의 함수 실행하기
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

# 불가능
# improt game
# game.sound.echo.echo_test()
#
# import game.sound.echo.echo_test

fromt game.sound import *
echo.echo_test()

from game.graphic.render import render_test
render_test()

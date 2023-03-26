OUT = ../../../../hugo/static/images/diff-render/basics/diff-int/

success_example:
	@manim -qm main.py SuccessExample_0 SuccessExample_1 SuccessExample_2

failure_example:
	@manim -qm main.py FailureExample_0 FailureExample_1 FailureExample_2

install:
	@mkdir -p output
	@cp media/images/main/*.png $(OUT)
	# @cp media/videos/main/1080p60/*.mp4 $(OUT)

clean:
	@rm -rf media __pycache__

%:
	@manim -pqm main.py $@

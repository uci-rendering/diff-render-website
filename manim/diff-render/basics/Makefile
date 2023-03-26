R = main

vec_def:
	@manim -qh main.py PointDefinition VectorDefinition1 VectorDefinition2 VectorTranslation

vec_norm:
	@manim -qh main.py VectorNormalize1 VectorNormalize2

vec_add:
	@manim -qh main.py VectorAddition2
	@manim -qh -s main.py VectorAddition2

vec_cartesian:
	@manim -qh main.py VectorCartesian2 VectorCartesian3
	@manim -qh -s main.py VectorCartesian3

vec_change_basis:
	@manim -qh main.py VectorChangeBasis
	@manim -qh -s main.py VectorChangeBasis

vec_dot:
	@manim -qh main.py VectorDotProduct1 VectorDotProduct2 VectorDotProduct3
	@manim -qh -s main.py VectorDotProduct3

vec_cross:
	@manim -qh main.py VectorCrossProduct
	@manim -qh -s main.py VectorCrossProduct
	@manim -qh main.py VectorCrossProduct2

mat_mult:
	@manim -qh main.py MatrixMult0 MatrixMult1 MatrixMult2

install:
	@mkdir -p output
	@cp media/images/main/*.png output/
	@cp media/videos/main/1080p60/*.mp4 output/

clean:
	@rm -rf media __pycache__

distclean:
	@rm -rf media __pycache__ output

%:
	@manim -pqm main.py $@

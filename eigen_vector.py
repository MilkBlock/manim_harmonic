from turtle import left
import manim_prelude
from manim import *
import sympy as sy
class EigenvectorTransform(Scene):
    def construct(self):
        # 定义矩阵M
        
        # 计算特征向量

        # 把特征向量转换为Manim的Vector格式
        arrows,texts,tags= manim_prelude.generate_arrow_and_text_from_sympy_matrix(eigenvectors,is_updater_on=True)
        p1 = NumberPlane()


        #  dot1 = Dot([-3,-2,0])   to confirm that move to method is applied to the center of mob
        b_Before = Tex("Before applying transformation")
        b_After = Tex("After applying transformation")
        b_Cause = Tex("Cause v1 v2 are EigenVectors They will not change the direction ")

        matrix = Matrix(M_values) 
        bra = matrix.get_brackets()


        b_Cause.move_to([0,-3,0])

        # bra.set_color(WHITE) 

        # bra 的坐标系是相对于matrix 而言的
        # matrix.move_to([-4,-2,0])
              
        b_Given_matrix= Tex("Given Matrix")
        b_Given_matrix.next_to(matrix,UP)

        self.play(Write(b_Given_matrix),Write(matrix))
        self.wait(2)

        self.play(
                matrix.animate.move_to([-3,-2,0]),
                FadeOut(b_Given_matrix)
            )

        b_Before.next_to(matrix,UP)
        b_After.next_to(matrix,UP)
        graph = (*arrows,p1,*texts,*tags)

        self.play(*[Create(mob) for mob in graph],
                  Create(b_Before),
                  )

        self.wait(1)

        # 对平面应用线性变换M
        self.play(Transform(b_Before,b_After))
        matrix_transform = np.array(M_values).astype(float)
        self.play(*(ApplyMatrix(matrix_transform, mob) for mob in (*arrows,p1)))
        self.play(Create(b_Cause))

        self.wait(4)

# if __name__ == "__main__":
M_values = [
    [2, 1],
    [1, 3]
]
M= sy.Matrix(M_values)
eigen_info = M.eigenvects()
eigenvectors = [ev[2][0].evalf(3) for ev in eigen_info]  # 由于 eigen_info 对于每一个代数multiplicity 都用一个数组存储，这个数组首先用size 表示后面向量的个数
# eigenvectors = [ev[2][0] for ev in eigen_info]  # 由于 eigen_info 对于每一个代数multiplicity 都用一个数组存储，这个数组首先用size 表示后面向量的个数
# x = [Arrow(start=  ORIGIN, end = np.array([v[0,0], v[1,0], 0]).astype(float)) for v in eigenvectors]





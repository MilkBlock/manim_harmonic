from manim import *
import sympy as sy

# you should have calculated the matrix to sympy.core.float at first , which can be realized by 
# evalf function of sy.Matrix 
def generate_arrow_and_text_from_sympy_matrix(matrix_list:list[sy.Matrix],descripts:list[str] = [],is_updater_on = True):
    np_vecs = [np.array((m[0,0],m[1,0],0)).astype(float) for m in matrix_list]
    arrows = [Arrow(start = ORIGIN, end =v,buff=0)for v in np_vecs]
    if descripts != []:
        assert len(descripts) == len(matrix_list)
        texts = [Text(des+f"[{vec[0]:.2f},{vec[1]:.2f}]",font_size=36)
                .set_vname(des)
                .set_cor_arrow(arrows[i])
                for i,(vec,des) in enumerate(zip(np_vecs,descripts))]
        tags = [Text(des,font_size=36)
                .set_vname(des)
                .set_cor_arrow(arrows[i])
                for i,(vec,des) in enumerate(zip(np_vecs,descripts))]
        print("generate",texts)

    else:
        texts = [Text(f"v{i+1}"+f"[{vec[0]:.2f},{vec[1]:.2f}]",font_size=36)
                .set_vname(f"v{i+1}")
                .set_cor_arrow(arrows[i])
                for i,vec in enumerate(np_vecs)]
        tags = [Text(f"v{i+1}",font_size=36)
                .set_vname(f"v{i+1}")
                .set_cor_arrow(arrows[i])
                for i,vec in enumerate(np_vecs)]
        print("generate",texts)

    for t in texts:
        t.set_last_frame_dt(0)
        t.add_updater(format_text_with_vector)
    if is_updater_on:
        for i,t in enumerate(tags):
            # t.next_to(arrows[i],UR)
            t.add_updater(follow_tag)
        
        
    assert len(texts) == len(arrows)
    VGroup(*texts).arrange(buff=0.5,direction = DOWN).set_x(4).set_y(-2)
    return arrows,texts,tags

def format_text_with_vector(t:Text,dt:float):
    t.set_last_frame_dt(t.get_last_frame_dt()+dt)
    if t.get_last_frame_dt() > 0.08:
        t.set_last_frame_dt(0)

        vec= t.get_cor_arrow().get_end()
        t_c = Text(t.get_vname() + f"[{vec[0]:.2f},{vec[1]:.2f}]",font_size=36)
        t_c.move_to(t)  # 这里 align_to 和 next_to 似乎差不多
        t.become(t_c)
    else :  # 因为时间没到所以什么都不做
        return
    
def follow_tag(t:Text,dt:float):
    t.next_to(t.get_cor_arrow().get_center(), complex_to_R3(R3_to_complex(t.get_cor_arrow().get_vector())*1j)/2)
 # type: ignore    
 

if __name__ =="__main__":
    M_values = [
        [2, 1],
        [1, 3]
    ]
    M = sy.Matrix(M_values)
    eigen_info = M.eigenvects()
    eigenvectors = [ev[2][0].evalf(3) for ev in eigen_info]  # 由于 eigen_info 对于每一个代数multiplicity 都用一个数组存储，这个数组首先用size 表示后面向量的个数
    print(generate_arrow_and_text_from_sympy_matrix(eigenvectors,["hello","fuck you "]))

        

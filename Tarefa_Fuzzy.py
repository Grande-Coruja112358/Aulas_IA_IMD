# Fazer sobre um robô que se balança e se equilibra
# LE == 1kg  LD == 1kg
# Inclinar até 67% do peso para LD depois 67% do peso para LE

# Código manual experimental

inclinação = float(input("Obtenha o valor de inclinação"))
motor_peq = 3.09 * N
motor_med = 6.19 * N
motor_gra = 12.39 * N
# M_inc_p_D; inc_p_D; Neutro; inc_p_E; M_inc_p_E
# 67% de inclinação no robô == 10,91 N
# 3,09 N = 9,57°  6,19 N = 19,14°  12,39 N = 38,29°
# motor_peq       motor_med        motor_gra

s_b,he,b=input().split()
s_b=float(s_b)
he=int(he)
b=int(b)

vh=s_b/192 #valor de la hora normal
vhe=vh*1.25 #valor hora extra
bon=s_b*0.05 #bonificacion
s_t=(s_b)+(vhe*he)+(bon*b) #salario total
salario=s_t-((s_t*0.035)+(s_t*0.04)+(s_t*0.01))
#se imprime el salario
print(round(salario,1))

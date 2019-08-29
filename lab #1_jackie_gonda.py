#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/lsuhpchelp/lbrnloniworkshop2019/blob/master/day1_python/intro_python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 
#  #  Introduction to Python Programming
# 
# ## PETE 2061 Lab 1 Workbook 
# 
# ## THIS LAB IS DUE BEFORE YOU LEAVE THE ROOM!!
# 
# <a id='top'></a>

# <a id='variables'></a>
# ## Volumetric Reserves Estimation
# The Stock-tank Oil Initially In Place (STOIIP) is the amount of oil that is stored in an oil reservoir. Assuming that the pore spaces in the reservoir are filled with water and oil only, the STOIIP can be estimated using the formula:<br><br>
# $STOIIP = 7758 Ah\phi(1-S_{wi})/B_{oi}$ <br><br>
# where $A$ is the area of the reservoir in acres, <br>
# $h$ is the reservoir thickness in feet (ft), <br>
# $S_{wi}$ is the initial water saturation of the reservoir. It is the ratio of the volume of water initially in the reservoir to the total pore volume in the reservoir. It can either be expressed as a fraction or percentage. <br>
# $B_{oi}$ is the initial oil formation volume factor. It is the ratio of the volume of oil at reservoir conditions (measured in units of reservoir barrels, rb) to the volume of oil at standard conditions (measured in units of stock tank barrels, stb). This means that the unit of $B_{oi}$ is $\frac{rb}{stb}$ <br>
# $\phi$ is the porosity of the reservoir. It is the ratio of the pore volume to the bulk volume, and can be expressed as a fraction or in percentage.
# 7758 is the conversion factor from acre-ft to barrels (bbl or rb) <br><br>
# NOTE: You should be able to show that the unit of STOIIP from this equation is stb. <br>
# 
# 1. Given the values below, write a Python code that calculates and stores the STOIIP into a variable named "stoiip", and then prints the STOIIP value. <br>
# A = 250  $\hspace{22pt}$ # in acres (store this value in a variable called "area")<br>
# h = 50 $\hspace{27pt}$ # in feet (store this value in a variable called "h") <br>
# $\phi$ = 0.33 $\hspace{19pt}$ # fraction (store this value in a variable called "poro")<br>
# $S_{wi}$ = 0.25 $\hspace{15pt}$ # fraction (store this value in a variable called "s_wi")<br>
# $B_{oi}$ = 1.1 $\hspace{19pt}$ # rb/stb (store this value in a variable called "b_oi")<br>
# 

# In[11]:


area = 250
h = 50 
poro = 0.33
s_wi = 0.25
b_oi = 1.1
stoiip = (7558*area*h*poro*(1-s_wi))/b_oi
print(stoiip)


# 2. The bulk volume of the reservoir (BV or $V_b$) in units of acre-ft is given as: <br>
# BV = Ah <br>
# Write a Python code that computes and stores the BV in a variable called "bv_acreft". Print this variable <br>

# In[16]:


bv_acreft = area*h
print(f"{bv_acreft}acre-ft")


# 3. Write a Python code to convert the BV from (2) above to barrels (rb) using the given conversion factor, and store this in a variable called "bv_rb". Print this variable <br>

# In[18]:


bv_rb=bv_acreft*7758
print(f'{bv_rb} barrells')


# 4. The pore volume of the reservoir is the total volume available available to store fluids in the reservoir. It is the product of the bulk volume and porosity.<br>
# Write a Python code to compute the pore volume of the reservoir in acre-ft and in rb, and store these in the variables "v_p_acreft" and "v_p_rb" respectively. Print these two variables in one print statement<br>

# In[23]:


v_p_acreft = bv_acreft*poro
v_p_rb = bv_rb*poro

print(v_p_acreft,v_p_rb)


# 5. The hydrocarbon pore volume (HCPV) in units of rb is the product of the pore volume in rb and initial oil saturation (which is 1-$S_{wi}$, because the reservoir contains oil and water only). The HCPV is given as: <br>
# $HCPV = 7758 Ah\phi(1-S_{wi})$ <br>
# Write a Python code that computes and stores the HCPV (in rb) in a variable called "hcpv". Print this variable <br>

# In[26]:


hcpv=7758*area*h*poro*(1-s_wi)
print(hcpv)


# 6. Two other reservoirs (reservoir B and reservoir C) have identical parameters with the first reservoir (reservoir A) but with porosity values 0.25 and 0.35, respectively. <br>
#     * Write one line of Python code to assign these two porosity values to variables "poro_B" and "poro_C", respectively.
#     * Write a Python code to compute the STOIIP values of reservoirs B and C. Store these in variables "stoiip_B" and stoiip_C", respectively.
#     * Write a Python code to compute the (arithmetic) mean of the STOIIPs of these 3 reservoirs.
#     * Write a print statement that uses the greater than operator to compare the STOIIP of reservoir B to that of reservoir C.<br> *Hint: print(STOIIP_B!=STOIIP_C) will test if STOIIP_B is not equal to STOIIP_C. This question asks you to test if STOIIP_B is greater than STOIIP_C.*
#     * Write a python code that adds 10% of the STOIIP of reservoir B to its original value, using the "+=" operator
#     * Write a fast python code that updates the STOIIP of reservoir C to 90% of its original value

# In[38]:


poro_b=.25
poro_c=.35
stoiip_b=(7558*area*h*poro_b*(1-s_wi))/b_oi
stoiip_c=(7558*area*h*poro_c*(1-s_wi))/b_oi
mean= (stoiip+stoiip_b+stoiip_c)/3
print(stoiip_b>stoiip_c)
print(stoiip_b)


# In[40]:


print(stoiip_b>stoiip_c)
stoiip_b+=0.1*stoiip_b
print(stoiip_b)


# In[42]:


stoiip_c-=.1*stoiip_c
print(stoiip_c)


# In[ ]:





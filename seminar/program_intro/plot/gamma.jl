using SpecialFunctions
using Plots

x = 1:5
y = factorial.(x)
scatter(x, y)
plot!(x->gamma(x+1), ylims=(0, 130))
savefig("gamma.png")

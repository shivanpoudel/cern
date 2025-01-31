import ROOT as rt

# canvas = rt.TCanvas("canvas", "Historam Example", 800, 600)
# hist = rt.TH1F("hist", "Combined Gaussian and Uniform Distributions", 100, -5, -5)

# hist.SetTitle("Gaussian and Uniform Distribution Example")
# hist.GetXaxis().SetTitle("Value")
# hist.GetYaxis().SetTitle("Frequency")

# hist.SetLineColor(rt.kBlue)
# hist.SetLineWidth(2)

# n_events = 10000

# for i in range(n_events):
#     hist.Fill(rt.gRandom.Gaus(0,1))
#     hist.Fill(rt.gRandom.Uniform(-5,5))

# hist.Draw()

# legend = rt.TLegend(0.7, 0.7, 0.9, 0.9)
# legend.AddEntry(hist, "Gaussian + Uniform", "1")
# legend.Draw()

# canvas.Update()
# canvas.SaveAs("histo.png")

# rt.gApplication.Run()

canvas = rt.TCanvas("canvas", "Complex Histogram with Multiple Distrivutions", 800, 600)
hist = rt.TH1F("hist", "Gaussian + Exponential + Uniform + Poisson Distributions", 200, -10, 10)

hist.SetTitle("Multiple Distributions: Gaussian, Exponential, Uniform, Poisson")
hist.GetXaxis().SetTitle("Value")
hist.GetYaxis().SetTitle("Frequency")

hist.SetLineColor(rt.kRed)
hist.SetLineWidth(3)

n_events = 50000

for i in range(n_events):
    hist.Fill(rt.gRandom.Gaus(0, 1))
    hist.Fill(rt.gRandom.Exp(1))
    hist.Fill(rt.gRandom.Uniform(-10,10))
    hist.Fill(rt.gRandom.Poisson(3) - 10)

hist.Draw()

legend = rt.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(hist, "Gaussian + Exponential + Uniform + Poission", "I")
legend.Draw()

canvas.Update()
canvas.SaveAs("complex.pdf")
rt.gApplication.Run()
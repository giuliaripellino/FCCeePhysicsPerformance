import ROOT

# Enable multi-threading
ROOT.ROOT.EnableImplicitMT()

path = 'stage1/dataFrame.root'

# create a RDataFrame from the output root-file from analysis_stage1.py
df = ROOT.RDataFrame('events', path)

c = ROOT.TCanvas('canvas', 'canvas',800,700)
c.cd()

h = df.Histo1D(('n_GenHS', 'Number of generated dark scalars HS', 5, -0.5, 4.5), 'n_GenHS')
h.SetTitle('')
h.GetXaxis().SetTitle('# generated HS')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Number of HS.pdf')

h = df.Histo1D(('n_GenZ', 'Number of generated Z', 5, -0.5, 4.5), 'n_GenZ')
h.SetTitle('')
h.GetXaxis().SetTitle('# generated Z')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Number of Z.pdf')

h = df.Histo1D(('n_Genb', 'Number of generated b b~ quarks', 20, -0.5, 19.5), 'n_Genb')
h.SetTitle('')
h.GetXaxis().SetTitle('# generated b b~quarks')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Number of b bbar.pdf')

h = df.Histo1D(('n_GenElectrons', 'Number of generated electrons and positrons', 20, -0.5, 19.5), 'n_GenElectrons')
h.SetTitle('')
h.GetXaxis().SetTitle('# generated electrons and positrons')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Number of electrons-positrons.pdf')

h = df.Histo1D(('n_FSGenElectrons', 'Number of final state generated electrons and positrons', 20, -0.5, 19.5), 'n_FSGenElectrons')
h.SetTitle('')
h.GetXaxis().SetTitle('# generated FS electrons and positrons')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Number of FS electrons-positrons.pdf')

h = df.Histo1D(('n_GenMuons', 'Number of generated muons', 20, -0.5, 19.5), 'n_GenMuons')
h.SetTitle('')
h.GetXaxis().SetTitle('# generated muons')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Number of muons.pdf')

h = df.Histo1D(('decayLengthHiggs', 'Decay length of Higgs', 100, 0, 2e-10), 'decayLengthHiggs')
h.SetTitle('')
h.GetXaxis().SetTitle('Decay radius [mm]')
h.GetYaxis().SetTitle('N_{Events}')
h.Draw()

c.SetLogy(1)
c.SaveAs('Decay length Higgs.pdf')

# h = df.Histo1D(('decayLength_HS', 'Decay length of scalar', 100, 0, 1e-10), 'decayLength_HS')
# h.SetTitle('')
# h.GetXaxis().SetTitle('Decay radius [mm]')
# h.GetYaxis().SetTitle('N_{Events}')
# h.Draw()

# c.SetLogy(1)
# c.SaveAs('Decay length Scalar.pdf')
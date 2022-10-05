outputDir   = 'stage1'

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (
            df
            # MC-particles/truth particles

            # select the generated b b~ quarks
            .Define('Genb_PID', 'MCParticle::sel_pdgID(5, true)(Particle)') # true means charge conjugation = true, i.e pick out both b and b~
            # get the number of generated b b~ quarks
            .Define('n_Genb', 'MCParticle::get_n(Genb_PID)')

            # get the production vertex for the b quarks in x y z
            .Define('b_vertex_x', 'MCParticle::get_vertex_x(Genb_PID)')
            .Define('b_vertex_y', 'MCParticle::get_vertex_y(Genb_PID)')
            .Define('b_vertex_z', 'MCParticle::get_vertex_z(Genb_PID)')

            # select the generated electrons and positrons
            .Define('GenElectrons_PID', 'MCParticle::sel_pdgID(11, true)(Particle)')
            # get the number of generated electrons and positrons
            .Define('n_GenElectrons', 'MCParticle::get_n(GenElectrons_PID)')
            # generator status = 1 means final state, i.e pick out the generated electrons and positrons with gen status = 1
            .Define('FSGenElectrons', 'MCParticle::sel_genStatus(1)(GenElectrons_PID)')
            # get the number of final state generated electrons and positrons
            .Define('n_FSGenElectrons', 'MCParticle::get_n(FSGenElectrons)')

            # select the generated muons
            .Define('GenMuons_PID', 'MCParticle::sel_pdgID(13, true)(Particle)')
            # get the number of generated muons
            .Define('n_GenMuons', 'MCParticle::get_n(GenMuons_PID)')

            # select generated dark scalar HS
            .Define('GenHS_PID',  'MCParticle::sel_pdgID(35, false)(Particle)')
            # get the number of dark scalars
            .Define('n_GenHS', 'MCParticle::get_n(GenHS_PID)')

            # get the production vertex for the HS in x y z
            .Define('HS_vertex_x', 'MCParticle::get_vertex_x(GenHS_PID)')
            .Define('HS_vertex_y', 'MCParticle::get_vertex_y(GenHS_PID)')
            .Define('HS_vertex_z', 'MCParticle::get_vertex_z(GenHS_PID)')

            # get the end point of the HS, where it decays into b b~ quarks
            .Define('HS_endPoint_x', 'MCParticle::get_endPoint_x(GenHS_PID)')
            .Define('HS_endPoint_y', 'MCParticle::get_endPoint_y(GenHS_PID)')
            .Define('HS_endPoint_z', 'MCParticle::get_endPoint_z(GenHS_PID)')

            # get the decay length of HS
            #.Define('decayLength_HS', 'return sqrt((HS_endPoint_x - HS_vertex_x)*(HS_endPoint_x - HS_vertex_x) + (HS_endPoint_y - HS_vertex_y)*(HS_endPoint_y - HS_vertex_y) + (HS_endPoint_z - HS_vertex_z)*(HS_endPoint_z - HS_vertex_z))')

            # select generated Z boson
            .Define('GenZ_PID',  'MCParticle::sel_pdgID(23, false)(Particle)')
            # get the number of Z bosons
            .Define('n_GenZ', 'MCParticle::get_n(GenZ_PID)')

            # select generated Higgs boson
            .Define('GenHiggs_PID',  'MCParticle::sel_pdgID(25, false)(Particle)')
            # get the number of Higgs bosons
            .Define('n_GenHiggs', 'MCParticle::get_n(GenHiggs_PID)')

            # decay length of Higgs
            .Define('decayLengthHiggs', 'return sqrt(HS_vertex_x.at(0)*HS_vertex_x.at(0) + HS_vertex_y.at(0)*HS_vertex_y.at(0) + HS_vertex_z.at(0)*HS_vertex_z.at(0))')

            # --------------------------------------------------------------------------------------------------------------------------------------------------------
            # Reconstruced particles
            # Jets
            .Define('n_RecoJets', 'ReconstructedParticle::get_n(Jet)') #count how many jets are in the event in total

            # Electrons
            .Alias('Electron0', 'Electron#0.index')
            .Define('electrons',  'ReconstructedParticle::get(Electron0, ReconstructedParticles)') 
            .Define('n_RecoElectrons',  'ReconstructedParticle::get_n(electrons)') #count how many electrons are in the event in total

            # Muons
            .Alias('Muon0', 'Muon#0.index')
            .Define('muons',  'ReconstructedParticle::get(Muon0, ReconstructedParticles)')
            .Define('n_RecoMuons',  'ReconstructedParticle::get_n(muons)') #count how many muons are in the event in total
        )
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            'Genb_PID',
            'n_Genb',
            'b_vertex_x',
            'b_vertex_y',
            'b_vertex_z',
            'GenElectrons_PID',
            'n_GenElectrons',
            'FSGenElectrons',
            'n_FSGenElectrons',
            'GenMuons_PID',
            'n_GenMuons',
            'GenHS_PID',
            'n_GenHS',
            'HS_vertex_x',
            'HS_vertex_y',
            'HS_vertex_z',
            'HS_endPoint_x',
            'HS_endPoint_y',
            'HS_endPoint_z',
            #'decayLength_HS',
            'GenZ_PID',
            'n_GenZ',
            'GenHiggs_PID',
            'n_GenHiggs',
            'decayLengthHiggs',
            'n_RecoJets', 
			'n_RecoElectrons',
			'n_RecoMuons'
        ]
        return branchList
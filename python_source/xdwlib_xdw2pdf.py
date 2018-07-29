from xdwlib import xdwopen

def test(inputFile,outputPath):
	inputXdw = xdwopen(inputFile)
	outputPDF = inputXdw.export_image( 0,path=outputPath, format="PDF", compress="NORMAL", direct=False)

if __name__ == '__main__':
	inputFile = ".\\input\\testDW.xdw"
	outputPath = ".\\output\\testOutput.pdf"
	test(inputFile,outputPath)
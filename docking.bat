@echo
for %%r in (receptor\*.pdbqt) do (
	for %%l in (ligand\*.pdbqt) do (
		if not exist results mkdir results
		vina --config receptor\%%~nr.txt --receptor %%r --ligand %%l --out results\%%~nr_2_%%~nl.pdbqt --log results\%%~nr_2_%%~nl.txt
		timeout 10))
exit
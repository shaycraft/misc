#include "ogrsf_frmts.h"

int main()

{
        OGRRegisterAll();
	
	OGRDataSource       *poDS;
    	poDS = OGRSFDriverRegistrar::Open( "../WELLS.SHP", FALSE );

	if (poDS == NULL)
	{
		printf("Open failed.\n");
		exit(1);
	}
}

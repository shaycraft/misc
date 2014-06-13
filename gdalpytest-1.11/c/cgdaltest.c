#include<stdio.h>
#include "ogr_api.h"

int main()
{
	OGRRegisterAll();	

	OGRDataSourceH ds;

	ds = OGROpen("../WELLS.SHP", FALSE, NULL);
	if (ds == NULL)
	{
		printf ("Open failed.\n");
		exit(1);
	}

	OGRLayerH layer;

	layer = OGR_DS_GetLayerByName(ds, "WELLS");
	OGR_L_ResetReading(layer);
	int count=0;
	OGRFeatureH feat;
	while ((feat = OGR_L_GetNextFeature(layer)) != NULL)
	{
		count++;
	}

	printf("Got %d features.\n", count);

	return 0;
}

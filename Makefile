build/gpr_000b11a_e.zip:
	mkdir -p $(dir $@)
	curl -o $@ http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/$(notdir $@)

build/gpr_000b11a_e.shp: build/gpr_000b11a_e.zip
	unzip -od $(dir $@) $<
	touch $@

prov.json: build/gpr_000b11a_e.shp
	node_modules/.bin/topojson \
		-o $@ \
		--projection='width = 960, height = 600, d3.geo.albers() \
			.rotate([96, 0]) \
		    .center([-32, 53.9]) \
		    .parallels([20, 60]) \
		    .scale(1970) \
		    .translate([width / 2, height / 2])' \
	    --properties='province=PRENAME' \
		--simplify=0.5 \
		-- prov=$<

build/subunits.json: build/Boundaries/CD_2011.shp
	ogr2ogr -f GeoJSON  -t_srs "+proj=latlong +datum=WGS84" \
	build/subunits.json \
	build/Boundaries/CD_2011.shp

	# ogr2ogr -f GeoJSON  -t_srs "+proj=latlong +datum=WGS84" -where "CDNAME IN ('Alberni-Clayoquot')" \
	# -clipdst -125.1550643102 48.8344612907 -126.1800723924 49.2711484127 \
	# build/subunits.json \
	# build/Boundaries/CD_2011.shp

census.json: build/subunits.json
	node_modules/.bin/topojson \
		-o $@ \
		--projection='width = 960, height = 600, d3.geo.albers() \
			.rotate([96, 5]) \
		    .center([-32, 58.5]) \
		    .parallels([20, 60]) \
		    .scale(1970) \
		    .translate([width / 2, height / 2])' \
	    --properties='zone=CDNAME' \
	    --simplify=0.05 \
		-- census=$<

#bs albers projection
build/sd1.json: build/TA_SD_SVW/TA_SD_SVW_polygon.shp
	ogr2ogr -f GeoJSON -t_srs "+proj=aea +lat_1=50 +lat_2=58.5 +lat_0=45 +lon_0=-126 +x_0=1000000 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs  " \
	build/sd1.json \
	build/TA_SD_SVW/TA_SD_SVW_polygon.shp

# school districts
build/sd.json: build/TA_SD_SVW/TA_SD_SVW_polygon.shp
	ogr2ogr -f GeoJSON  -t_srs "+proj=latlong +datum=WGS84" \
	build/sd.json \
	build/TA_SD_SVW/TA_SD_SVW_polygon.shp

skulldist.json: build/sd1.json
	node_modules/.bin/topojson \
		--width 960 \
	    --height 600 \
	    --properties='zone=SD_NAME' \
	    --properties='zoneNum=SD_NUM' \
	    --simplify=0.05 \
		-o $@ \
		-- skulldist=$<


#working version, not bc albers		
# skulldist.json: build/sd.json
# 	node_modules/.bin/topojson \
# 		-o $@ \
# 		--projection='width = 960, height = 600, d3.geo.albers() \
# 			.rotate([96, 5]) \
# 		    .center([-32, 58.5]) \
# 		    .parallels([20, 60]) \
# 		    .scale(1970) \
# 		    .translate([width / 2, height / 2])' \
# 	    --properties='zone=SD_NAME' \
# 	    --properties='zoneNum=SD_NUM' \
# 	    --simplify=0.05 \
# 		-- skulldist=$<


# Use BC Albers Projection
# build/subunits.json: build/Boundaries/CD_2011.shp
# 	ogr2ogr -f GeoJSON  -t_srs "+proj=aea +lat_1=50 +lat_2=58.5 +lat_0=45
# +lon_0=-126 +x_0=1000000 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs" \
# 	build/subunits.json \
# 	build/Boundaries/CD_2011.shp

# census.json: build/subunits.json
# 	node_modules/.bin/topojson \
# 		-o $@ \
# 	    --properties='zone=CDNAME' \
# 		-- census=$<


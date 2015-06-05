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
	ogr2ogr -f GeoJSON  -t_srs "+proj=latlong +datum=WGS84" -where "CDNAME IN ('Alberni-Clayoquot')" \
	-clipdst -125.1550643102 48.8344612907 -126.1800723924 49.2711484127 \
	build/subunits.json \
	build/Boundaries/CD_2011.shp
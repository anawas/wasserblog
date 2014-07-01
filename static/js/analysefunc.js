// Das ist die Schweizer Härteskala. Sie basiert auf der 
// franzoesischen Haerte.

function analyze_hardness () {
	var gdh = $(document).find("#totalHardnessSlider").val();
	var gfh = gdh * 1.78;
	
    if (gfh <= 7) {
    	$(document).find("#hardness").val("sehr weich");
    } else if ((gfh > 7) && (gfh <= 15)) {
    	$(document).find("#hardness").val("weich");
    } else if ((gfh > 15) && (gfh <= 25)) {
    	$(document).find("#hardness").val("mittelhart");
    } else if ((gfh > 25) && (gfh <= 32)) {
    	$(document).find("#hardness").val("ziemlich hart");
    } else if ((gfh > 32) && (gfh <= 42)) {
    	$(document).find("#hardness").val("hart");
    } else {
    	$(document).find("#hardness").val("sehr hart");
    }
}

function analyze_co2() {
	var KH_val = $(document).find("#carbonHardnessSlider").val();
    var ph_val = $(document).find("#pHSlider").val();

	var co2 = KH_val/2.8 * Math.pow(10, (7.91 - ph_val));
						
	$(document).find("#co2content").val(co2.toPrecision(2) + " mg/l")	
}
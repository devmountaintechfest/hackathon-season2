package visualization

import (
	"fmt"
	"net/http"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

// generatePieItems is helper for generate data for pie chart
func generatePieItems(k string, v interface{}) ([]opts.PieData, error) {
	mapValue, ok := v.(map[string]int)
	if !ok {
		return nil, fmt.Errorf("cannot cast %v to map[string]int from generatePieItems", v)
	}
	items := make([]opts.PieData, 0)
	for key, value := range mapValue {
		items = append(items, opts.PieData{Name: key, Value: value})
	}
	return items, nil
}

func (c *Chart) CreatePieChart(w http.ResponseWriter) {
	// create a new pie instance
	pie := charts.NewPie()
	// set some global options like Title/Legend/ToolTip or anything else
	pie.SetGlobalOptions(
		charts.WithInitializationOpts(c.OptsInit),
		charts.WithTitleOpts(opts.Title{
			Title:    c.Title,
			Subtitle: c.Subtitle,
		}),
		charts.WithLegendOpts(opts.Legend{Show: true}),
	)
	for k, v := range c.Items {
		data, err := generatePieItems(k, v)
		if err != nil {
			fmt.Println(err)
			return
		}
		pie.AddSeries(k, data)
	}
	pie.SetSeriesOptions(
		charts.WithLabelOpts(opts.Label{
			Show:      true,
			Formatter: "{b}: {c}",
		}),
	)
	pie.Render(w)
}

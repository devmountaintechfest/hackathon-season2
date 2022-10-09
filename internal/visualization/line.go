package visualization

import (
	"fmt"
	"net/http"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

// generateLineItems is helper for generate data for line chart
func generateLineItems(v interface{}) ([]opts.LineData, error) {

	values, ok := v.([]int)
	if !ok {
		return nil, fmt.Errorf("cannot cast %v to []int from generateLineItems", v)
	}
	items := make([]opts.LineData, 0)
	for _, data := range values {
		items = append(items, opts.LineData{Value: data})
	}
	return items, nil
}

func (c *Chart) CreateLineChart(w http.ResponseWriter) {
	// create a new line instance
	line := charts.NewLine()
	// set some global options like Title/Legend/ToolTip or anything else
	line.SetGlobalOptions(
		charts.WithInitializationOpts(c.OptsInit),
		charts.WithTitleOpts(opts.Title{
			Title:    c.Title,
			Subtitle: c.Subtitle,
		}),
		charts.WithLegendOpts(opts.Legend{Show: true}),
	)
	// Put data into instance
	line.SetXAxis(c.XAxis)
	for k, v := range c.Items {
		data, err := generateLineItems(v)
		if err != nil {
			fmt.Println(err)
			return
		}
		line.AddSeries(k, data)
	}
	// set some series options like Title/Legend/ToolTip or anything else
	line.SetSeriesOptions(
		charts.WithLabelOpts(opts.Label{
			Show: true,
		}),
		charts.WithLineChartOpts(opts.LineChart{Smooth: true}),
		charts.WithAreaStyleOpts(
			opts.AreaStyle{
				Opacity: 0.2,
			}),
		charts.WithMarkPointStyleOpts(opts.MarkPointStyle{
			Label: &opts.Label{
				Show:      true,
				Formatter: "{a}: {b}",
			},
		}),
	)
	line.Render(w)
}

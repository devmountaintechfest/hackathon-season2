package visualization

import (
	"fmt"
	"net/http"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

// generatebarItems is helper for generate data for bar chart
func generatebarItems(v interface{}) ([]opts.BarData, error) {

	values, ok := v.([]int)
	if !ok {
		return nil, fmt.Errorf("cannot cast %v to []int from generatebarItems", v)
	}
	items := make([]opts.BarData, 0)
	for _, data := range values {
		items = append(items, opts.BarData{Value: data})
	}
	return items, nil
}

func (c *Chart) CreatebarChart(w http.ResponseWriter) {
	// create a new bar instance
	bar := charts.NewBar()
	// set some global options like Title/Legend/ToolTip or anything else
	bar.SetGlobalOptions(
		charts.WithInitializationOpts(c.OptsInit),
		charts.WithTitleOpts(opts.Title{
			Title:    c.Title,
			Subtitle: c.Subtitle,
		}),
		charts.WithLegendOpts(opts.Legend{Show: true}),
	)
	// Put data into instance
	bar.SetXAxis(c.XAxis)
	for k, v := range c.Items {
		data, err := generatebarItems(v)
		if err != nil {
			fmt.Println(err)
			return
		}
		bar.AddSeries(k, data)
	}
	// set some series options like Title/Legend/ToolTip or anything else
	bar.SetSeriesOptions(
		charts.WithLabelOpts(opts.Label{
			Show: true,
		}),
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
	bar.Render(w)
}

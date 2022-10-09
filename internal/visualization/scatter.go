package visualization

import (
	"fmt"
	"net/http"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

func generateScatterItems(v interface{}) ([]opts.ScatterData, error) {
	values, ok := v.([]int)
	if !ok {
		return nil, fmt.Errorf("cannot cast %v to []int from generateScatterItems", v)
	}
	items := make([]opts.ScatterData, 0)
	for _, data := range values {
		items = append(items, opts.ScatterData{
			Value:        data,
			Symbol:       "roundRect",
			SymbolSize:   15,
			SymbolRotate: 10,
		})
	}
	return items, nil
}

func (c *Chart) CreateScatter(w http.ResponseWriter) {
	scatter := charts.NewScatter()
	// set some global options like Title/Legend/ToolTip or anything else
	scatter.SetGlobalOptions(
		charts.WithInitializationOpts(c.OptsInit),
		charts.WithTitleOpts(opts.Title{
			Title:    c.Title,
			Subtitle: c.Subtitle,
		}),
		charts.WithLegendOpts(opts.Legend{Show: true}),
	)
	// Put data into instance
	scatter.SetXAxis(c.XAxis)
	for k, v := range c.Items {
		data, err := generateScatterItems(v)
		if err != nil {
			fmt.Println(err)
			return
		}
		scatter.AddSeries(k, data)
	}

	// set some series options like Title/Legend/ToolTip or anything else
	scatter.SetSeriesOptions(
		charts.WithLabelOpts(opts.Label{
			Show:     true,
			Position: "top",
		}),
	)
	scatter.Render(w)
}

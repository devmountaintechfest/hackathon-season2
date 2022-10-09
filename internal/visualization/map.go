package visualization

import (
	"fmt"
	"net/http"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

// generateMapData is helper for generate data for map
func generateMapData(v map[string]interface{}) ([]opts.MapData, error) {
	items := make([]opts.MapData, 0)
	for key, data := range v {
		value, ok := data.(int)
		if !ok {
			return nil, fmt.Errorf("cannot cast %v to float64 from generateMapData", v)
		}
		items = append(items, opts.MapData{Name: key, Value: value})
	}
	return items, nil
}

func (c *Chart) CreateWorldMap(w http.ResponseWriter) {
	mc := charts.NewMap()
	mc.RegisterMapType("world")
	mc.SetGlobalOptions(
		charts.WithInitializationOpts(c.OptsInit),
		charts.WithTitleOpts(opts.Title{
			Title:    c.Title,
			Subtitle: c.Subtitle,
		}),
		charts.WithVisualMapOpts(opts.VisualMap{
			Calculable: true,
		}),
	)
	data, err := generateMapData(c.Items)
	if err != nil {
		fmt.Println(err)
		return
	}
	mc.AddSeries("map", data)
	mc.Render(w)
}

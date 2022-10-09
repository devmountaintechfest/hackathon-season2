package visualization

import (
	"github.com/go-echarts/go-echarts/v2/opts"
)

type Chart struct {
	XAxis    []string
	YAxis    []string
	OptsInit opts.Initialization
	Title    string
	Subtitle string
	Items    map[string]interface{}
}

func CreateChart3D()   {}
func CreateBar3D()     {}
func CreateScatter3D() {}
func AddOverlaper()    {}
